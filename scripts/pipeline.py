#!/usr/bin/env python3
"""
UAKS Pipeline Manager
====================
Manages the atomic knowledge pipeline for Unified Atomic Knowledge Substrate.

Usage:
    python pipeline.py status                    # Show pipeline status
    python pipeline.py ingest <source>           # Ingest atoms from source
    python pipeline.py refine <atom_id>          # Run atom through refinery
    python pipeline.py deduplicate                # Run deduplication check
    python pipeline.py integrity                  # Verify integrity
    python pipeline.py assemble <query>          # Assemble atoms for query
    python pipeline.py find-paper <topic>         # Find academic papers
    python pipeline.py add-atom <type> <content> # Add new atom manually
    python pipeline.py list-atoms                 # List all atoms
"""

import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).parent.parent
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = REPO_ROOT / "data"
MANIFESTS_DIR = REPO_ROOT / "manifests"
DOCS_DIR = REPO_ROOT / "docs"

STAGES = ["source", "intake", "refinery", "dedup", "storage", "assembly", "output"]
STAGE_NAMES = {
    "source": "Source Collection",
    "intake": "Intake Processing",
    "refinery": "Refinement Pipeline",
    "dedup": "Deduplication",
    "storage": "Graph Storage",
    "assembly": "Assembly Engine",
    "output": "Output Generation",
}

sys.path.insert(0, str(SCRIPT_DIR))


def get_state_file():
    return DATA_DIR / "pipeline_state.json"


def load_state():
    state_file = get_state_file()
    if state_file.exists():
        with open(state_file, "r") as f:
            return json.load(f)
    return {
        "version": "1.0",
        "initialized": datetime.now().isoformat(),
        "atoms": {
            "text": [],
            "code": [],
            "total": 0,
        },
        "pipeline": {stage: {"status": "idle", "processed": 0} for stage in STAGES},
        "dedup": {"duplicates_found": 0, "last_run": None},
        "integrity": {"verified": False, "last_check": None},
    }


def save_state(data):
    state_file = get_state_file()
    data["last_updated"] = datetime.now().isoformat()
    with open(state_file, "w") as f:
        json.dump(data, f, indent=2)


def compute_atom_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:16]


def cmd_status(args):
    data = load_state()
    print("\n" + "=" * 50)
    print("UAKS PIPELINE STATUS")
    print("=" * 50)
    print(f"\nAtoms: {data['atoms']['total']}")
    print(f"  - TextAtoms: {len(data['atoms']['text'])}")
    print(f"  - CodeAtoms: {len(data['atoms']['code'])}")
    print(f"\nPipeline:")
    for stage, info in data["pipeline"].items():
        status = (
            "🔴"
            if info["status"] == "idle"
            else "🟡"
            if info["status"] == "running"
            else "✅"
        )
        print(f"  {status} {stage}: {info['processed']} processed")
    print(f"\nDeduplication: {data['dedup']['duplicates_found']} duplicates")
    print(
        f"Integrity: {'✅ Verified' if data['integrity']['verified'] else '⚠️ Not verified'}"
    )
    print()


def cmd_ingest(args):
    if not args:
        print("Usage: pipeline.py ingest <source_path>")
        return

    source_path = args[0]
    data = load_state()
    data["pipeline"]["intake"]["status"] = "running"
    save_state(data)

    source_file = Path(source_path)
    if not source_file.exists():
        print(f"Source not found: {source_path}")
        return

    content = source_file.read_text()
    atom_hash = compute_atom_hash(content)
    atom_id = f"atom_{atom_hash}"

    atom_type = (
        "code"
        if source_file.suffix in [".py", ".js", ".ts", ".go", ".rs", ".java"]
        else "text"
    )

    atom = {
        "id": atom_id,
        "type": atom_type,
        "source": str(source_file),
        "hash": atom_hash,
        "size": len(content),
        "ingested": datetime.now().isoformat(),
        "status": "raw",
    }

    if atom_type == "text":
        data["atoms"]["text"].append(atom)
    else:
        data["atoms"]["code"].append(atom)
    data["atoms"]["total"] += 1

    data["pipeline"]["intake"]["status"] = "completed"
    data["pipeline"]["intake"]["processed"] += 1
    save_state(data)

    print(f"Ingested: {atom_id} ({atom_type}) from {source_file.name}")


def cmd_refine(args):
    if not args:
        print("Usage: pipeline.py refine <atom_id>")
        return

    atom_id = args[0]
    data = load_state()

    atom = None
    for a in data["atoms"]["text"]:
        if a["id"] == atom_id:
            atom = a
            break
    for a in data["atoms"]["code"]:
        if a["id"] == atom_id:
            atom = a
            break

    if not atom:
        print(f"Atom not found: {atom_id}")
        return

    data["pipeline"]["refinery"]["status"] = "running"
    save_state(data)

    atom["status"] = "refined"
    atom["refined"] = datetime.now().isoformat()

    data["pipeline"]["refinery"]["status"] = "completed"
    data["pipeline"]["refinery"]["processed"] += 1
    save_state(data)

    print(f"Refined: {atom_id}")


def cmd_deduplicate(args):
    data = load_state()
    data["pipeline"]["dedup"]["status"] = "running"
    save_state(data)

    all_atoms = data["atoms"]["text"] + data["atoms"]["code"]
    hashes = {}
    duplicates = []

    for atom in all_atoms:
        h = atom.get("hash")
        if h in hashes:
            duplicates.append((atom["id"], hashes[h]))
        else:
            hashes[h] = atom["id"]

    data["dedup"]["duplicates_found"] = len(duplicates)
    data["dedup"]["last_run"] = datetime.now().isoformat()
    data["pipeline"]["dedup"]["status"] = "completed"
    data["pipeline"]["dedup"]["processed"] = len(all_atoms)
    save_state(data)

    if duplicates:
        print(f"Found {len(duplicates)} duplicates:")
        for dup in duplicates:
            print(f"  {dup[0]} = {dup[1]}")
    else:
        print("No duplicates found")


def cmd_integrity(args):
    data = load_state()
    data["pipeline"]["storage"]["status"] = "running"
    save_state(data)

    all_atoms = data["atoms"]["text"] + data["atoms"]["code"]
    verified = 0
    failed = []

    for atom in all_atoms:
        source_file = Path(atom.get("source", ""))
        if source_file.exists():
            content = source_file.read_text()
            current_hash = compute_atom_hash(content)
            if current_hash[:16] == atom.get("hash"):
                verified += 1
            else:
                failed.append(atom["id"])
        else:
            failed.append(atom["id"])

    data["integrity"]["verified"] = len(failed) == 0
    data["integrity"]["last_check"] = datetime.now().isoformat()
    data["integrity"]["verified_count"] = verified
    data["integrity"]["failed_count"] = len(failed)
    data["pipeline"]["storage"]["status"] = "completed"
    data["pipeline"]["storage"]["processed"] = len(all_atoms)
    save_state(data)

    if failed:
        print(f"Integrity check: {verified} OK, {len(failed)} FAILED")
    else:
        print(f"Integrity verified: {verified} atoms")


def cmd_assemble(args):
    if not args:
        print("Usage: pipeline.py assemble <query>")
        return

    query = " ".join(args)
    data = load_state()

    print(f"\nAssembling atoms for query: {query}")
    print("-" * 40)

    all_atoms = data["atoms"]["text"] + data["atoms"]["code"]
    if not all_atoms:
        print("No atoms available")
        return

    print(f"Searching {len(all_atoms)} atoms...")
    relevant = all_atoms[:5]

    print(f"\nRetrieved {len(relevant)} atoms:")
    for atom in relevant:
        print(f"  - {atom['id']} ({atom['type']}, {atom.get('status', 'unknown')})")

    data["pipeline"]["assembly"]["status"] = "completed"
    data["pipeline"]["assembly"]["processed"] += len(relevant)
    save_state(data)

    print("\nAssembly complete - ready for output generation")


def cmd_list_atoms(args):
    data = load_state()
    print("\nAtoms in UAKS:")
    print("=" * 50)

    print(f"\nTextAtoms ({len(data['atoms']['text'])}):")
    for atom in data["atoms"]["text"]:
        print(
            f"  {atom['id']} - {atom.get('status', 'unknown')} - {atom.get('source', 'unknown')}"
        )

    print(f"\nCodeAtoms ({len(data['atoms']['code'])}):")
    for atom in data["atoms"]["code"]:
        print(
            f"  {atom['id']} - {atom.get('status', 'unknown')} - {atom.get('source', 'unknown')}"
        )


def cmd_add_atom(args):
    if len(args) < 2:
        print("Usage: pipeline.py add-atom <type> <content>")
        return

    atom_type = args[0]
    content = " ".join(args[1:])

    if atom_type not in ["text", "code"]:
        print("Type must be 'text' or 'code'")
        return

    data = load_state()
    atom_hash = compute_atom_hash(content)
    atom_id = f"atom_{atom_hash}"

    atom = {
        "id": atom_id,
        "type": atom_type,
        "content": content[:100] + "..." if len(content) > 100 else content,
        "hash": atom_hash,
        "size": len(content),
        "ingested": datetime.now().isoformat(),
        "status": "raw",
    }

    if atom_type == "text":
        data["atoms"]["text"].append(atom)
    else:
        data["atoms"]["code"].append(atom)
    data["atoms"]["total"] += 1

    save_state(data)
    print(f"Added: {atom_id}")


try:
    from academic import AcademicClient

    HAS_ACADEMIC = True
except ImportError:
    HAS_ACADEMIC = False


def cmd_find_paper(args):
    if not HAS_ACADEMIC:
        print("Error: academic module not installed")
        print("Run: pip install requests")
        return

    if not args:
        print("Usage: pipeline.py find-paper <topic>")
        return

    topic = " ".join(args)
    client = AcademicClient()
    results = client.search(topic, limit=10)

    print(f"\nSearch: {topic}")
    print("=" * 50)

    all_papers = []
    for source, papers in results.items():
        for paper in papers:
            paper.source = source
            all_papers.append(paper)

    all_papers.sort(key=lambda p: p.citation_count, reverse=True)

    for i, paper in enumerate(all_papers[:10], 1):
        print(f"{i}. {paper.title}")
        print(f"   {', '.join(paper.authors[:2])} ({paper.year or 'N/A'})")
        print(f"   Citations: {paper.citation_count}")
        print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "status": cmd_status,
        "ingest": cmd_ingest,
        "refine": cmd_refine,
        "deduplicate": cmd_deduplicate,
        "integrity": cmd_integrity,
        "assemble": cmd_assemble,
        "list-atoms": cmd_list_atoms,
        "add-atom": cmd_add_atom,
        "find-paper": cmd_find_paper,
    }

    if cmd in commands:
        commands[cmd](args)
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
