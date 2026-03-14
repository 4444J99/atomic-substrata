#!/usr/bin/env python3
"""
UAKS Graph Storage
=================
Graph-based atomic storage with relationships between atoms.

Features:
- Nodes = atoms
- Edges = relationships
- Content-addressable storage
- Graph queries
"""

import hashlib
import json
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class GraphNode:
    """Represents an atom node in the graph."""

    id: str
    type: str  # text, code, concept
    hash: str
    content: str
    source: str
    created_at: str
    metadata: dict = field(default_factory=dict)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "hash": self.hash,
            "content": self.content,
            "source": self.source,
            "created_at": self.created_at,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "GraphNode":
        return cls(
            id=data["id"],
            type=data["type"],
            hash=data["hash"],
            content=data["content"],
            source=data["source"],
            created_at=data["created_at"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class GraphEdge:
    """Represents a relationship between atoms."""

    id: str
    source_id: str
    target_id: str
    relationship: str  # references, similar_to, part_of, derives_from, etc.
    weight: float = 1.0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: dict = field(default_factory=dict)

    def to_dict(self):
        return {
            "id": self.id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relationship": self.relationship,
            "weight": self.weight,
            "created_at": self.created_at,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "GraphEdge":
        return cls(
            id=data["id"],
            source_id=data["source_id"],
            target_id=data["target_id"],
            relationship=data["relationship"],
            weight=data.get("weight", 1.0),
            created_at=data.get("created_at", datetime.now().isoformat()),
            metadata=data.get("metadata", {}),
        )


class GraphStorage:
    """Graph-based storage for atoms."""

    def __init__(self, storage_file: Optional[Path] = None):
        self.storage_file = storage_file or Path("data/graph_storage.json")
        self.nodes: dict[str, GraphNode] = {}
        self.edges: dict[str, GraphEdge] = {}
        self.adjacency: dict[str, list[str]] = defaultdict(list)
        self.reverse_adjacency: dict[str, list[str]] = defaultdict(list)

        self.load()

    def load(self):
        """Load graph from file."""
        if not self.storage_file.exists():
            return

        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)

            self.nodes = {
                k: GraphNode.from_dict(v) for k, v in data.get("nodes", {}).items()
            }
            self.edges = {
                k: GraphEdge.from_dict(v) for k, v in data.get("edges", {}).items()
            }

            # Rebuild adjacency lists
            self._rebuild_adjacency()
        except Exception as e:
            print(f"Error loading graph: {e}")

    def save(self):
        """Save graph to file."""
        data = {
            "nodes": {k: v.to_dict() for k, v in self.nodes.items()},
            "edges": {k: v.to_dict() for k, v in self.edges.items()},
            "last_updated": datetime.now().isoformat(),
        }

        self.storage_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=2)

    def _rebuild_adjacency(self):
        """Rebuild adjacency lists from edges."""
        self.adjacency = defaultdict(list)
        self.reverse_adjacency = defaultdict(list)

        for edge in self.edges.values():
            self.adjacency[edge.source_id].append(edge.id)
            self.reverse_adjacency[edge.target_id].append(edge.id)

    def add_node(self, node: GraphNode) -> GraphNode:
        """Add a node to the graph."""
        self.nodes[node.id] = node
        self.save()
        return node

    def add_edge(self, edge: GraphEdge) -> GraphEdge:
        """Add an edge to the graph."""
        # Verify nodes exist
        if edge.source_id not in self.nodes:
            raise ValueError(f"Source node not found: {edge.source_id}")
        if edge.target_id not in self.nodes:
            raise ValueError(f"Target node not found: {edge.target_id}")

        self.edges[edge.id] = edge
        self.adjacency[edge.source_id].append(edge.id)
        self.reverse_adjacency[edge.target_id].append(edge.id)
        self.save()
        return edge

    def get_node(self, node_id: str) -> Optional[GraphNode]:
        """Get a node by ID."""
        return self.nodes.get(node_id)

    def get_edges_from(self, node_id: str) -> list[GraphEdge]:
        """Get all edges from a node."""
        edge_ids = self.adjacency.get(node_id, [])
        return [self.edges[eid] for eid in edge_ids if eid in self.edges]

    def get_edges_to(self, node_id: str) -> list[GraphEdge]:
        """Get all edges to a node."""
        edge_ids = self.reverse_adjacency.get(node_id, [])
        return [self.edges[eid] for eid in edge_ids if eid in self.edges]

    def find_by_hash(self, atom_hash: str) -> list[GraphNode]:
        """Find nodes by hash (for deduplication)."""
        return [n for n in self.nodes.values() if n.hash == atom_hash]

    def find_by_type(self, node_type: str) -> list[GraphNode]:
        """Find all nodes of a given type."""
        return [n for n in self.nodes.values() if n.type == node_type]

    def find_by_relationship(self, relationship: str) -> list[GraphEdge]:
        """Find all edges of a given relationship type."""
        return [e for e in self.edges.values() if e.relationship == relationship]

    def traverse(self, start_id: str, max_depth: int = 2) -> dict[str, list[GraphNode]]:
        """
        Traverse graph from a starting node.

        Returns dict mapping depth to list of nodes found.
        """
        visited = set()
        results = {0: [self.nodes[start_id]]} if start_id in self.nodes else {}

        current_level = [start_id]

        for depth in range(1, max_depth + 1):
            next_level = []
            level_nodes = []

            for node_id in current_level:
                if node_id in visited:
                    continue
                visited.add(node_id)

                # Get connected nodes
                edges = self.get_edges_from(node_id)
                for edge in edges:
                    if edge.target_id in self.nodes:
                        next_level.append(edge.target_id)
                        level_nodes.append(self.nodes[edge.target_id])

            if level_nodes:
                results[depth] = level_nodes

            current_level = next_level
            if not current_level:
                break

        return results

    def get_stats(self) -> dict:
        """Get graph statistics."""
        type_counts = defaultdict(int)
        rel_counts = defaultdict(int)

        for node in self.nodes.values():
            type_counts[node.type] += 1

        for edge in self.edges.values():
            rel_counts[edge.relationship] += 1

        return {
            "total_nodes": len(self.nodes),
            "total_edges": len(self.edges),
            "node_types": dict(type_counts),
            "relationship_types": dict(rel_counts),
        }

    def export_json(self) -> str:
        """Export graph as JSON string."""
        data = {
            "nodes": {k: v.to_dict() for k, v in self.nodes.items()},
            "edges": {k: v.to_dict() for k, v in self.edges.items()},
            "stats": self.get_stats(),
            "exported_at": datetime.now().isoformat(),
        }
        return json.dumps(data, indent=2)


def create_from_pipeline_state(pipeline_state_file: Path, graph_storage_file: Path):
    """Create graph storage from pipeline state."""
    with open(pipeline_state_file, "r") as f:
        state = json.load(f)

    graph = GraphStorage(graph_storage_file)

    # Add atoms as nodes
    for atom_data in state.get("atoms", {}).get("text", []):
        node = GraphNode(
            id=atom_data["id"],
            type="text",
            hash=atom_data["hash"],
            content=atom_data.get("content", ""),
            source=atom_data.get("source", ""),
            created_at=atom_data.get("ingested", datetime.now().isoformat()),
        )
        graph.add_node(node)

    for atom_data in state.get("atoms", {}).get("code", []):
        node = GraphNode(
            id=atom_data["id"],
            type="code",
            hash=atom_data["hash"],
            content=atom_data.get("content", ""),
            source=atom_data.get("source", ""),
            created_at=atom_data.get("ingested", datetime.now().isoformat()),
        )
        graph.add_node(node)

    # Create "same_hash" edges for deduplication candidates
    hash_groups = defaultdict(list)
    for node in graph.nodes.values():
        hash_groups[node.hash].append(node.id)

    for hash_val, node_ids in hash_groups.items():
        if len(node_ids) > 1:
            # Create similarity edges between nodes with same hash
            for i in range(len(node_ids)):
                for j in range(i + 1, len(node_ids)):
                    edge_id = hashlib.sha256(
                        f"{node_ids[i]}:{node_ids[j]}".encode()
                    ).hexdigest()[:16]

                    edge = GraphEdge(
                        id=edge_id,
                        source_id=node_ids[i],
                        target_id=node_ids[j],
                        relationship="same_hash",
                        weight=1.0,
                    )
                    try:
                        graph.add_edge(edge)
                    except ValueError:
                        pass  # Edge might already exist

    print(f"Created graph with {len(graph.nodes)} nodes and {len(graph.edges)} edges")
    return graph


def main():
    """CLI for graph storage."""
    import sys

    graph = GraphStorage()

    if len(sys.argv) < 2:
        print("Usage: graph_storage.py <command>")
        print("  Commands:")
        print("    stats              - Show graph statistics")
        print("    list               - List all nodes")
        print("    import             - Import from pipeline state")
        print("    export             - Export to JSON")
        print("    find <type>        - Find nodes by type")
        print("    traverse <node_id> - Traverse from node")
        return

    cmd = sys.argv[1]

    if cmd == "stats":
        stats = graph.get_stats()
        print("=== Graph Statistics ===")
        print(f"Nodes: {stats['total_nodes']}")
        print(f"Edges: {stats['total_edges']}")
        print("\nNode types:")
        for t, c in stats["node_types"].items():
            print(f"  {t}: {c}")
        print("\nRelationship types:")
        for r, c in stats["relationship_types"].items():
            print(f"  {r}: {c}")

    elif cmd == "list":
        print(f"=== Nodes ({len(graph.nodes)}) ===")
        for node in list(graph.nodes.values())[:20]:
            print(f"  {node.id} ({node.type}): {node.content[:50]}...")

        print(f"\n=== Edges ({len(graph.edges)}) ===")
        for edge in list(graph.edges.values())[:20]:
            print(f"  {edge.source_id} --[{edge.relationship}]--> {edge.target_id}")

    elif cmd == "import":
        pipeline_file = Path("data/pipeline_state.json")
        graph_file = Path("data/graph_storage.json")
        graph = create_from_pipeline_state(pipeline_file, graph_file)
        print("Import complete")

    elif cmd == "export":
        print(graph.export_json())

    elif cmd == "find":
        if len(sys.argv) < 3:
            print("Usage: graph_storage.py find <type>")
            return
        node_type = sys.argv[2]
        nodes = graph.find_by_type(node_type)
        print(f"Found {len(nodes)} nodes of type '{node_type}':")
        for node in nodes:
            print(f"  {node.id}: {node.content[:50]}...")

    elif cmd == "traverse":
        if len(sys.argv) < 3:
            print("Usage: graph_storage.py traverse <node_id>")
            return
        node_id = sys.argv[2]
        results = graph.traverse(node_id, max_depth=2)
        for depth, nodes in results.items():
            print(f"\nDepth {depth}:")
            for node in nodes:
                print(f"  {node.id}: {node.content[:50]}...")

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
