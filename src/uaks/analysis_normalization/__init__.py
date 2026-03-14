#!/usr/bin/env python3
"""
Analysis Normalization Module
============================
Normalizes and analyzes atom data.

Features:
- Statistical analysis
- Pattern detection
- Anomaly detection
- Aggregation
"""

import json
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class AnalysisResult:
    """Result of analysis."""

    metric: str
    value: Any
    details: dict


class AnalysisNormalizer:
    """Normalizes and analyzes atom data."""

    def __init__(self):
        pass

    def analyze_atoms(self, state_file: str = "data/pipeline_state.json") -> dict:
        """
        Analyze atoms in pipeline state.

        Args:
            state_file: Path to pipeline state

        Returns:
            Analysis results
        """
        path = Path(state_file)

        if not path.exists():
            return {"error": "State file not found"}

        with open(path) as f:
            state = json.load(f)

        atoms = state.get("atoms", {})

        results = {
            "total_atoms": atoms.get("total", 0),
            "text_atoms": len(atoms.get("text", [])),
            "code_atoms": len(atoms.get("code", [])),
            "by_status": self._analyze_by_status(atoms),
            "size_distribution": self._analyze_sizes(atoms),
        }

        return results

    def _analyze_by_status(self, atoms: dict) -> dict:
        """Analyze atoms by status."""
        text_atoms = atoms.get("text", [])
        code_atoms = atoms.get("code", [])

        text_status = Counter(a.get("status", "unknown") for a in text_atoms)
        code_status = Counter(a.get("status", "unknown") for a in code_atoms)

        return {
            "text": dict(text_status),
            "code": dict(code_status),
        }

    def _analyze_sizes(self, atoms: dict) -> dict:
        """Analyze atom sizes."""
        all_sizes = []

        for atom in atoms.get("text", []):
            all_sizes.append(atom.get("size", 0))

        for atom in atoms.get("code", []):
            all_sizes.append(atom.get("size", 0))

        if not all_sizes:
            return {}

        return {
            "mean": statistics.mean(all_sizes),
            "median": statistics.median(all_sizes),
            "stdev": statistics.stdev(all_sizes) if len(all_sizes) > 1 else 0,
            "min": min(all_sizes),
            "max": max(all_sizes),
        }

    def detect_anomalies(
        self, state_file: str = "data/pipeline_state.json", threshold: float = 2.0
    ) -> dict:
        """
        Detect anomalies in atom data.

        Args:
            state_file: Path to pipeline state
            threshold: Standard deviation threshold

        Returns:
            List of anomalies
        """
        path = Path(state_file)

        if not path.exists():
            return {"error": "State file not found"}

        with open(path) as f:
            state = json.load(f)

        atoms = state.get("atoms", {})
        all_sizes = []

        for atom in atoms.get("text", []) + atoms.get("code", []):
            all_sizes.append(
                {
                    "id": atom.get("id"),
                    "size": atom.get("size", 0),
                }
            )

        if len(all_sizes) < 3:
            return {"anomalies": [], "message": "Not enough data for anomaly detection"}

        sizes = [a["size"] for a in all_sizes]
        mean = statistics.mean(sizes)
        stdev = statistics.stdev(sizes) if len(sizes) > 1 else 0

        anomalies = []
        for item in all_sizes:
            z_score = abs((item["size"] - mean) / stdev) if stdev > 0 else 0
            if z_score > threshold:
                anomalies.append(
                    {
                        "id": item["id"],
                        "size": item["size"],
                        "z_score": z_score,
                    }
                )

        return {
            "anomalies": anomalies,
            "threshold": threshold,
            "mean": mean,
            "stdev": stdev,
        }

    def aggregate_by_source(self, state_file: str = "data/pipeline_state.json") -> dict:
        """Aggregate atoms by source."""
        path = Path(state_file)

        if not path.exists():
            return {"error": "State file not found"}

        with open(path) as f:
            state = json.load(f)

        atoms = state.get("atoms", {})
        source_counts = defaultdict(int)

        for atom in atoms.get("text", []) + atoms.get("code", []):
            source = atom.get("source", "unknown")
            source_counts[source] += 1

        return dict(source_counts)


def main():
    """CLI for analysis."""
    import sys

    analyzer = AnalysisNormalizer()

    if len(sys.argv) < 2:
        print("Usage: analysis_normalization.py <command>")
        print("  analyze           - Analyze atoms")
        print("  anomalies          - Detect anomalies")
        print("  by-source          - Aggregate by source")
        return

    cmd = sys.argv[1]

    if cmd == "analyze":
        result = analyzer.analyze_atoms()
        print(json.dumps(result, indent=2))

    elif cmd == "anomalies":
        result = analyzer.detect_anomalies()
        print(json.dumps(result, indent=2))

    elif cmd == "by-source":
        result = analyzer.aggregate_by_source()
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
