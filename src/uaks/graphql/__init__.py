#!/usr/bin/env python3
"""
GraphQL API
===========
GraphQL schema and resolvers for UAKS.

Features:
- Atom queries
- Assembly queries
- Graph traversal
- Search functionality
"""

import json
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Atom:
    """Represents an atom in GraphQL."""

    id: str
    type: str
    content: str
    hash: str
    source: str
    metadata: dict = field(default_factory=dict)


@dataclass
class Query:
    """GraphQL-style query parser."""

    operation: str
    args: dict
    fields: list


class GraphQLSchema:
    """GraphQL schema for UAKS."""

    def __init__(self):
        self.atoms: dict[str, Atom] = {}
        self.resolvers = {
            "atoms": self.resolve_atoms,
            "atom": self.resolve_atom,
            "search": self.resolve_search,
            "assembly": self.resolve_assembly,
        }

    def add_atom(self, atom: Atom):
        """Add an atom to the schema."""
        self.atoms[atom.id] = atom

    def query(self, query_str: str) -> dict:
        """
        Execute a GraphQL-style query.

        Args:
            query_str: GraphQL query string

        Returns:
            Query result
        """
        query = self._parse_query(query_str)

        if query.operation == "atoms":
            return self.resolve_atoms(query.args, query.fields)
        elif query.operation == "atom":
            return self.resolve_atom(query.args, query.fields)
        elif query.operation == "search":
            return self.resolve_search(query.args, query.fields)
        elif query.operation == "assembly":
            return self.resolve_assembly(query.args, query.fields)

        return {"error": f"Unknown operation: {query.operation}"}

    def _parse_query(self, query_str: str) -> Query:
        """Parse a simple GraphQL-style query."""
        lines = [l.strip() for l in query_str.split("\n") if l.strip()]

        operation = ""
        args = {}
        fields = []

        for line in lines:
            if line.startswith("{"):
                continue

            if "(" in line:
                # Has arguments
                op_part, arg_part = line.split("(")
                operation = op_part.strip()
                arg_part = arg_part.rstrip(")").strip()

                # Parse arguments
                for arg in arg_part.split(","):
                    if ":" in arg:
                        key, val = arg.split(":")
                        args[key.strip()] = val.strip().strip('"')
            elif line.startswith("}"):
                continue
            else:
                fields.append(line.strip())

        return Query(operation=operation, args=args, fields=fields)

    def resolve_atoms(self, args: dict, fields: list) -> dict:
        """Resolve atoms query."""
        atom_type = args.get("type", "all")

        results = []
        for atom in self.atoms.values():
            if atom_type == "all" or atom.type == atom_type:
                results.append(self._filter_fields(atom, fields))

        return {"atoms": results}

    def resolve_atom(self, args: dict, fields: list) -> dict:
        """Resolve single atom query."""
        atom_id = args.get("id")

        if not atom_id or atom_id not in self.atoms:
            return {"error": f"Atom not found: {atom_id}"}

        atom = self.atoms[atom_id]
        return {"atom": self._filter_fields(atom, fields)}

    def resolve_search(self, args: dict, fields: list) -> dict:
        """Resolve search query."""
        query = args.get("query", "")
        limit = int(args.get("limit", 10))

        if not query:
            return {"error": "Search query required"}

        # Simple text search
        results = []
        query_lower = query.lower()

        for atom in self.atoms.values():
            if query_lower in atom.content.lower():
                results.append(self._filter_fields(atom, fields))
                if len(results) >= limit:
                    break

        return {"results": results}

    def resolve_assembly(self, args: dict, fields: list) -> dict:
        """Resolve assembly query."""
        query = args.get("query", "")

        if not query:
            return {"error": "Assembly query required"}

        # For now, return matching atoms as assembly
        results = self.resolve_search({"query": query, "limit": 5}, fields)

        return {
            "query": query,
            "assembled": results.get("results", []),
            "confidence": 0.85,
        }

    def _filter_fields(self, atom: Atom, fields: list) -> dict:
        """Filter fields for output."""
        if not fields:
            # Return all fields
            return {
                "id": atom.id,
                "type": atom.type,
                "content": atom.content,
                "hash": atom.hash,
                "source": atom.source,
                "metadata": atom.metadata,
            }

        result = {}
        for field in fields:
            if hasattr(atom, field):
                result[field] = getattr(atom, field)

        return result

    def schema(self) -> str:
        """Return GraphQL schema definition."""
        return """
type Atom {
    id: ID!
    type: String!
    content: String!
    hash: String!
    source: String!
    metadata: JSON
}

type Query {
    atoms(type: String): [Atom!]!
    atom(id: ID!): Atom
    search(query: String!, limit: Int): [Atom!]!
    assembly(query: String!): AssemblyResult
}

type AssemblyResult {
    query: String!
    assembled: [Atom!]!
    confidence: Float!
}
"""


class GraphQLExecutor:
    """Executes GraphQL queries against UAKS data."""

    def __init__(self):
        self.schema = GraphQLSchema()

    def execute(self, query: str) -> dict:
        """Execute a GraphQL query."""
        return self.schema.query(query)

    def load_from_state(self, state_file: str):
        """Load atoms from pipeline state."""
        import pathlib

        path = pathlib.Path(state_file)
        if not path.exists():
            return

        with open(path) as f:
            state = json.load(f)

        for atom_data in state.get("atoms", {}).get("text", []):
            atom = Atom(
                id=atom_data.get("id", ""),
                type="text",
                content=atom_data.get("content", ""),
                hash=atom_data.get("hash", ""),
                source=atom_data.get("source", ""),
                metadata={},
            )
            self.schema.add_atom(atom)

        for atom_data in state.get("atoms", {}).get("code", []):
            atom = Atom(
                id=atom_data.get("id", ""),
                type="code",
                content=atom_data.get("content", ""),
                hash=atom_data.get("hash", ""),
                source=atom_data.get("source", ""),
                metadata={},
            )
            self.schema.add_atom(atom)


def main():
    """CLI for GraphQL."""
    import sys

    executor = GraphQLExecutor()

    # Load from state if available
    executor.load_from_state("data/pipeline_state.json")

    if len(sys.argv) < 2:
        print("Usage: graphql.py <query_file>")
        print("")
        print("Example query:")
        print("""
{
  atoms(type: "text") {
    id
    content
  }
}
""")
        return

    query_file = sys.argv[1]

    with open(query_file) as f:
        query = f.read()

    result = executor.execute(query)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
