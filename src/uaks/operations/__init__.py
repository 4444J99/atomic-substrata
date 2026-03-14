#!/usr/bin/env python3
"""
Operations Module
=================
Operational utilities for UAKS.

Features:
- Health checks
- Monitoring
- Logging
- Error handling
"""

import json
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class HealthStatus:
    """Health check result."""

    component: str
    status: str  # healthy, degraded, unhealthy
    message: str = ""
    details: dict = field(default_factory=dict)


class Operations:
    """Operations utilities for UAKS."""

    def __init__(self):
        self.start_time = time.time()
        self.health_checks = []

    def health_check(self) -> list[HealthStatus]:
        """
        Run all health checks.

        Returns:
            List of health check results
        """
        checks = [
            self._check_pipeline_state(),
            self._check_data_directory(),
            self._check_graph_storage(),
        ]

        return checks

    def _check_pipeline_state(self) -> HealthStatus:
        """Check pipeline state file."""
        state_file = Path("data/pipeline_state.json")

        if not state_file.exists():
            return HealthStatus(
                component="pipeline_state",
                status="unhealthy",
                message="Pipeline state file not found",
            )

        try:
            with open(state_file) as f:
                state = json.load(f)

            atoms = state.get("atoms", {}).get("total", 0)

            return HealthStatus(
                component="pipeline_state",
                status="healthy",
                message=f"Pipeline state OK ({atoms} atoms)",
                details={"atom_count": atoms},
            )
        except Exception as e:
            return HealthStatus(
                component="pipeline_state",
                status="unhealthy",
                message=f"Error: {str(e)}",
            )

    def _check_data_directory(self) -> HealthStatus:
        """Check data directory."""
        data_dir = Path("data")

        if not data_dir.exists():
            return HealthStatus(
                component="data_directory",
                status="unhealthy",
                message="Data directory not found",
            )

        files = list(data_dir.glob("*.json"))

        return HealthStatus(
            component="data_directory",
            status="healthy",
            message=f"Data directory OK ({len(files)} files)",
            details={"file_count": len(files)},
        )

    def _check_graph_storage(self) -> HealthStatus:
        """Check graph storage."""
        graph_file = Path("data/graph_storage.json")

        if not graph_file.exists():
            return HealthStatus(
                component="graph_storage",
                status="degraded",
                message="Graph storage not initialized",
            )

        try:
            with open(graph_file) as f:
                data = json.load(f)

            nodes = len(data.get("nodes", {}))
            edges = len(data.get("edges", {}))

            return HealthStatus(
                component="graph_storage",
                status="healthy",
                message=f"Graph storage OK ({nodes} nodes, {edges} edges)",
                details={"nodes": nodes, "edges": edges},
            )
        except Exception as e:
            return HealthStatus(
                component="graph_storage",
                status="unhealthy",
                message=f"Error: {str(e)}",
            )

    def uptime(self) -> float:
        """Get uptime in seconds."""
        return time.time() - self.start_time

    def get_stats(self) -> dict:
        """Get operational statistics."""
        checks = self.health_check()

        return {
            "uptime_seconds": self.uptime(),
            "health_checks": [
                {
                    "component": c.component,
                    "status": c.status,
                    "message": c.message,
                }
                for c in checks
            ],
            "overall_status": "healthy"
            if all(c.status == "healthy" for c in checks)
            else "degraded",
        }


def main():
    """CLI for operations."""
    import sys

    ops = Operations()

    if len(sys.argv) < 2:
        print("Usage: operations.py <command>")
        print("  health   - Run health checks")
        print("  stats    - Get statistics")
        return

    cmd = sys.argv[1]

    if cmd == "health":
        checks = ops.health_check()
        print("=== Health Checks ===")
        for check in checks:
            status_icon = (
                "✅"
                if check.status == "healthy"
                else "🟡"
                if check.status == "degraded"
                else "❌"
            )
            print(f"{status_icon} {check.component}: {check.message}")

    elif cmd == "stats":
        stats = ops.get_stats()
        print("=== Operations Stats ===")
        print(f"Uptime: {stats['uptime_seconds']:.1f}s")
        print(f"Status: {stats['overall_status']}")


if __name__ == "__main__":
    main()
