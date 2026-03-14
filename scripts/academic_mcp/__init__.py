#!/usr/bin/env python3
"""
UAKS MCP Server
===============
Exposes UAKS pipeline operations as MCP tools.

Usage:
    python -m academic_mcp.server
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from mcp.server.fastmcp import FastMCP

    HAS_MCP = True
except ImportError:
    HAS_MCP = False
    FastMcp = object

from academic import AcademicClient, Paper

mcp = FastMCP("uaks") if HAS_MCP else None

_client = None


def get_client() -> AcademicClient:
    global _client
    if _client is None:
        env_key = "SEMANTIC_SCHOLAR_API_KEY"  # allow-secret
        api_key = os.environ.get(env_key)  # allow-secret
        _client = AcademicClient(api_key)
    return _client


def get_pipeline_state():
    state_file = Path(__file__).parent.parent / "data" / "pipeline_state.json"
    if state_file.exists():
        with open(state_file, "r") as f:
            return json.load(f)
    return {
        "version": "1.0",
        "initialized": datetime.now().isoformat(),
        "atoms": {"text": [], "code": [], "total": 0},
        "pipeline": {
            "source": {"status": "idle", "processed": 0},
            "intake": {"status": "idle", "processed": 0},
            "refinery": {"status": "idle", "processed": 0},
            "dedup": {"status": "idle", "processed": 0},
            "storage": {"status": "idle", "processed": 0},
            "assembly": {"status": "idle", "processed": 0},
            "output": {"status": "idle", "processed": 0},
        },
    }


if HAS_MCP:

    @mcp.tool()
    def uaks_status() -> str:
        """Get current UAKS pipeline status."""
        data = get_pipeline_state()

        lines = [
            "=== UAKS PIPELINE STATUS ===",
            f"Total Atoms: {data['atoms']['total']}",
            f"  TextAtoms: {len(data['atoms']['text'])}",
            f"  CodeAtoms: {len(data['atoms']['code'])}",
            "",
            "Pipeline Stages:",
        ]

        for stage, info in data["pipeline"].items():
            status_icon = (
                "🔴"
                if info["status"] == "idle"
                else "🟡"
                if info["status"] == "running"
                else "✅"
            )
            lines.append(f"  {status_icon} {stage}: {info['processed']} processed")

        lines.append("")
        lines.append(
            f"Deduplication: {data.get('dedup', {}).get('duplicates_found', 0)} duplicates"
        )
        lines.append(
            f"Integrity: {'✅ Verified' if data.get('integrity', {}).get('verified') else '⚠️ Not verified'}"
        )

        return "\n".join(lines)

    @mcp.tool()
    def uaks_list_atoms(atom_type: str = "all") -> str:
        """
        List atoms in the UAKS.

        Args:
            atom_type: Type to list (all, text, code)
        """
        data = get_pipeline_state()

        if atom_type == "text":
            atoms = data["atoms"]["text"]
        elif atom_type == "code":
            atoms = data["atoms"]["code"]
        else:
            atoms = data["atoms"]["text"] + data["atoms"]["code"]

        if not atoms:
            return "No atoms found in UAKS."

        lines = [f"=== {len(atoms)} Atoms ({atom_type}) ==="]

        for atom in atoms[:20]:
            lines.append(f"- {atom['id']} ({atom.get('type', 'unknown')})")
            lines.append(f"  Status: {atom.get('status', 'unknown')}")
            lines.append(f"  Source: {atom.get('source', 'unknown')}")

        if len(atoms) > 20:
            lines.append(f"... and {len(atoms) - 20} more")

        return "\n".join(lines)

    @mcp.tool()
    def academic_search(
        query: str, sources: str = "semantic_scholar,arxiv,pubmed", limit: int = 10
    ) -> str:
        """
        Search for academic papers across multiple sources.

        Args:
            query: Search query string
            sources: Comma-separated sources to search
            limit: Maximum results per source
        """
        source_list = [s.strip() for s in sources.split(",")]
        client = get_client()
        results = client.search(query, sources=source_list, limit=limit)

        output = []
        for source, papers in results.items():
            output.append(f"=== {source.upper()} ({len(papers)} results) ===")
            for i, paper in enumerate(papers, 1):
                output.append(f"{i}. {paper.title}")
                output.append(
                    f"   Authors: {', '.join(paper.authors[:3])}"
                    + ("..." if len(paper.authors) > 3 else "")
                )
                output.append(f"   Year: {paper.year or 'N/A'}")
                output.append(f"   Citations: {paper.citation_count}")
                output.append(f"   DOI: {paper.doi or 'N/A'}")
                output.append(f"   PDF: {paper.pdf_url or 'N/A'}")
                output.append("")

        return "\n".join(output)

    @mcp.tool()
    def academic_get_paper(identifier: str) -> str:
        """Get paper metadata by identifier."""
        client = get_client()
        paper = client.get_paper(identifier)

        if paper is None:
            return f"Paper not found: {identifier}"

        lines = [
            f"Title: {paper.title}",
            f"Authors: {', '.join(paper.authors)}",
            f"Year: {paper.year or 'N/A'}",
            f"DOI: {paper.doi or 'N/A'}",
            f"arXiv: {paper.arxiv_id or 'N/A'}",
            f"Venue: {paper.venue or 'N/A'}",
            f"Citations: {paper.citation_count}",
            f"PDF URL: {paper.pdf_url or 'N/A'}",
            "",
            f"Abstract: {paper.abstract[:500] + '...' if paper.abstract and len(paper.abstract) > 500 else paper.abstract or 'N/A'}",
        ]

        return "\n".join(lines)

    @mcp.tool()
    def academic_find_reading(topic: str, limit: int = 10) -> str:
        """Find relevant academic papers for a topic."""
        client = get_client()
        results = client.search(topic, limit=limit)

        output = [f"Search: {topic}", ""]

        all_papers = []
        for source, papers in results.items():
            all_papers.extend(papers)

        all_papers.sort(key=lambda p: p.citation_count, reverse=True)

        for i, paper in enumerate(all_papers[:10], 1):
            output.append(f"{i}. {paper.title}")
            output.append(f"   {', '.join(paper.authors[:2])} ({paper.year or 'N/A'})")
            output.append(f"   Citations: {paper.citation_count}")
            output.append(f"   PDF: {paper.pdf_url or 'N/A'}")
            output.append("")

        return "\n".join(output)


if __name__ == "__main__":
    if not HAS_MCP:
        print("Error: mcp package not installed")
        print("Run: pip install mcp")
        sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()
    else:
        mcp.run(transport="stdio")
