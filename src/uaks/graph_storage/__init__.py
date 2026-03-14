#!/usr/bin/env python3
"""
Graph Storage
=============
Graph-based atomic storage with relationships between atoms.

Features:
- Nodes = atoms
- Edges = relationships
- Content-addressable storage
- Graph queries

This module re-exports the implementation from scripts/graph_storage.py.
"""

import sys
from pathlib import Path

_script_path = (
    Path(__file__).parent.parent.parent.parent / "scripts" / "graph_storage.py"
)

if _script_path.exists():
    _module_name = _script_path.stem
    if str(_script_path.parent) not in sys.path:
        sys.path.insert(0, str(_script_path.parent))
    from graph_storage import GraphNode, GraphEdge, GraphStorage

    __all__ = ["GraphNode", "GraphEdge", "GraphStorage"]
else:
    raise ImportError(f"graph_storage.py not found at {_script_path}")
