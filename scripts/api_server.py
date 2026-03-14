#!/usr/bin/env python3
"""
UAKS REST API Server
====================
Simple REST API for UAKS operations.

Usage:
    python api_server.py [--port 8080]
"""

import json
import sys
from datetime import datetime
from pathlib import Path

try:
    from flask import Flask, jsonify, request

    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from assembly import AssemblyEngine
from graph_storage import GraphStorage

app = Flask(__name__)

# Initialize components
pipeline_state_file = Path("data/pipeline_state.json")
graph_storage_file = Path("data/graph_storage.json")

assembly_engine = None
graph_storage = None


def get_assembly():
    global assembly_engine
    if assembly_engine is None:
        assembly_engine = AssemblyEngine(pipeline_state_file)
        assembly_engine.load_atoms()
        assembly_engine.build_index()
    return assembly_engine


def get_graph():
    global graph_storage
    if graph_storage is None:
        graph_storage = GraphStorage(graph_storage_file)
    return graph_storage


def load_pipeline_state():
    if pipeline_state_file.exists():
        with open(pipeline_state_file, "r") as f:
            return json.load(f)
    return None


@app.route("/")
def index():
    return jsonify(
        {
            "name": "UAKS API",
            "version": "1.0.0",
            "endpoints": [
                "/status",
                "/atoms",
                "/atoms/<atom_id>",
                "/assemble",
                "/graph",
                "/graph/<node_id>",
                "/search",
            ],
        }
    )


@app.route("/status")
def status():
    """Get pipeline status."""
    state = load_pipeline_state()
    if state:
        return jsonify(
            {
                "atoms": state.get("atoms", {}),
                "pipeline": state.get("pipeline", {}),
                "dedup": state.get("dedup", {}),
                "integrity": state.get("integrity", {}),
                "last_updated": state.get("last_updated"),
            }
        )
    return jsonify({"error": "No state found"}), 404


@app.route("/atoms")
def list_atoms():
    """List all atoms."""
    state = load_pipeline_state()
    if not state:
        return jsonify({"error": "No state found"}), 404

    atom_type = request.args.get("type", "all")

    atoms = []
    if atom_type in ["all", "text"]:
        atoms.extend(state.get("atoms", {}).get("text", []))
    if atom_type in ["all", "code"]:
        atoms.extend(state.get("atoms", {}).get("code", []))

    return jsonify(
        {
            "count": len(atoms),
            "atoms": atoms,
        }
    )


@app.route("/atoms/<atom_id>")
def get_atom(atom_id):
    """Get a specific atom."""
    state = load_pipeline_state()
    if not state:
        return jsonify({"error": "No state found"}), 404

    # Search in text atoms
    for atom in state.get("atoms", {}).get("text", []):
        if atom["id"] == atom_id:
            return jsonify(atom)

    # Search in code atoms
    for atom in state.get("atoms", {}).get("code", []):
        if atom["id"] == atom_id:
            return jsonify(atom)

    return jsonify({"error": "Atom not found"}), 404


@app.route("/assemble", methods=["POST"])
def assemble():
    """Assemble atoms for a query."""
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Query required"}), 400

    query = data["query"]
    top_k = data.get("top_k", 5)

    engine = get_assembly()
    result = engine.assemble(query, top_k=top_k)

    return jsonify(
        {
            "query": result.query,
            "confidence": result.confidence,
            "atom_count": len(result.atoms),
            "atoms": [
                {
                    "id": a.id,
                    "type": a.type,
                    "content": a.content[:200] + "..."
                    if len(a.content) > 200
                    else a.content,
                    "source": a.source,
                }
                for a in result.atoms
            ],
            "assembled_text": result.assembled_text,
            "assembled_at": result.assembled_at,
        }
    )


@app.route("/graph")
def graph_stats():
    """Get graph statistics."""
    graph = get_graph()
    stats = graph.get_stats()
    return jsonify(stats)


@app.route("/graph/<node_id>")
def get_node(node_id):
    """Get a node and its connections."""
    graph = get_graph()
    node = graph.get_node(node_id)

    if not node:
        return jsonify({"error": "Node not found"}), 404

    edges_from = graph.get_edges_from(node_id)
    edges_to = graph.get_edges_to(node_id)

    return jsonify(
        {
            "node": node.to_dict(),
            "edges_from": [e.to_dict() for e in edges_from],
            "edges_to": [e.to_dict() for e in edges_to],
        }
    )


@app.route("/search")
def search():
    """Search atoms by query."""
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Query parameter 'q' required"}), 400

    engine = get_assembly()
    results = engine.search(query, top_k=10)

    return jsonify(
        {
            "query": query,
            "results": [
                {
                    "id": atom.id,
                    "type": atom.type,
                    "content": atom.content[:100] + "..."
                    if len(atom.content) > 100
                    else atom.content,
                    "similarity": sim,
                }
                for atom, sim in results
            ],
        }
    )


def main():
    """Run the API server."""
    if not HAS_FLASK:
        print("Error: Flask not installed")
        print("Run: pip install flask")
        sys.exit(1)

    port = 8080
    if len(sys.argv) > 1 and sys.argv[1] == "--port":
        port = int(sys.argv[2])

    print(f"Starting UAKS API server on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)


if __name__ == "__main__":
    main()
