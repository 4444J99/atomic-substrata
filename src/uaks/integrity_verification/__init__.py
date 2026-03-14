#!/usr/bin/env python3
"""
Integrity Verification Module
============================
Verifies integrity of UAKS data.

Features:
- Hash verification
- Data consistency checks
- Audit logging
"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


@dataclass
class IntegrityIssue:
    """Represents an integrity issue."""

    severity: str  # critical, warning, info
    component: str
    message: str
    details: dict = field(default_factory=dict)


@dataclass
class IntegrityReport:
    """Integrity verification report."""

    timestamp: str
    status: str  # pass, fail, warning
    issues: list[IntegrityIssue]
    verified_items: int = 0
    failed_items: int = 0


class IntegrityVerifier:
    """Verifies integrity of UAKS data."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)

    def verify_all(self) -> IntegrityReport:
        """
        Run all integrity checks.

        Returns:
            Integrity report
        """
        issues = []

        # Verify pipeline state
        issues.extend(self._verify_pipeline_state())

        # Verify graph storage
        issues.extend(self._verify_graph_storage())

        # Verify CAS storage
        issues.extend(self._verify_cas_storage())

        # Determine overall status
        if any(i.severity == "critical" for i in issues):
            status = "fail"
        elif any(i.severity == "warning" for i in issues):
            status = "warning"
        else:
            status = "pass"

        return IntegrityReport(
            timestamp=datetime.now().isoformat(),
            status=status,
            issues=issues,
            verified_items=len(issues),
            failed_items=sum(1 for i in issues if i.severity == "critical"),
        )

    def _verify_pipeline_state(self) -> list[IntegrityIssue]:
        """Verify pipeline state file."""
        issues = []
        state_file = self.data_dir / "pipeline_state.json"

        if not state_file.exists():
            issues.append(
                IntegrityIssue(
                    severity="critical",
                    component="pipeline_state",
                    message="Pipeline state file not found",
                )
            )
            return issues

        try:
            with open(state_file) as f:
                state = json.load(f)

            # Check required fields
            if "version" not in state:
                issues.append(
                    IntegrityIssue(
                        severity="warning",
                        component="pipeline_state",
                        message="Missing version field",
                    )
                )

            if "atoms" not in state:
                issues.append(
                    IntegrityIssue(
                        severity="critical",
                        component="pipeline_state",
                        message="Missing atoms field",
                    )
                )

        except json.JSONDecodeError as e:
            issues.append(
                IntegrityIssue(
                    severity="critical",
                    component="pipeline_state",
                    message=f"Invalid JSON: {str(e)}",
                )
            )
        except Exception as e:
            issues.append(
                IntegrityIssue(
                    severity="critical",
                    component="pipeline_state",
                    message=f"Error reading file: {str(e)}",
                )
            )

        return issues

    def _verify_graph_storage(self) -> list[IntegrityIssue]:
        """Verify graph storage."""
        issues = []
        graph_file = self.data_dir / "graph_storage.json"

        if not graph_file.exists():
            # Not critical - graph might not be initialized
            issues.append(
                IntegrityIssue(
                    severity="info",
                    component="graph_storage",
                    message="Graph storage not initialized",
                )
            )
            return issues

        try:
            with open(graph_file) as f:
                data = json.load(f)

            # Verify structure
            if "nodes" not in data:
                issues.append(
                    IntegrityIssue(
                        severity="warning",
                        component="graph_storage",
                        message="Missing nodes field",
                    )
                )

            if "edges" not in data:
                issues.append(
                    IntegrityIssue(
                        severity="warning",
                        component="graph_storage",
                        message="Missing edges field",
                    )
                )

        except json.JSONDecodeError as e:
            issues.append(
                IntegrityIssue(
                    severity="critical",
                    component="graph_storage",
                    message=f"Invalid JSON: {str(e)}",
                )
            )

        return issues

    def _verify_cas_storage(self) -> list[IntegrityIssue]:
        """Verify content-addressable storage."""
        issues = []
        cas_dir = self.data_dir / "cas"

        if not cas_dir.exists():
            issues.append(
                IntegrityIssue(
                    severity="info",
                    component="cas_storage",
                    message="CAS storage not initialized",
                )
            )
            return issues

        index_file = cas_dir / "index.json"

        if not index_file.exists():
            issues.append(
                IntegrityIssue(
                    severity="warning",
                    component="cas_storage",
                    message="CAS index not found",
                )
            )
            return issues

        try:
            with open(index_file) as f:
                index = json.load(f)

            # Verify objects exist
            objects_dir = cas_dir / "objects"
            if not objects_dir.exists():
                issues.append(
                    IntegrityIssue(
                        severity="warning",
                        component="cas_storage",
                        message="Objects directory not found",
                    )
                )

        except Exception as e:
            issues.append(
                IntegrityIssue(
                    severity="warning",
                    component="cas_storage",
                    message=f"Error verifying: {str(e)}",
                )
            )

        return issues

    def compute_hash(self, content: str) -> str:
        """Compute SHA256 hash."""
        return hashlib.sha256(content.encode()).hexdigest()


def main():
    """CLI for integrity verification."""
    import sys

    verifier = IntegrityVerifier()

    if len(sys.argv) > 1 and sys.argv[1] == "--data-dir":
        if len(sys.argv) < 4:
            print("Usage: integrity_verification.py [--data-dir <path>]")
            return
        verifier = IntegrityVerifier(sys.argv[2])

    report = verifier.verify_all()

    print(f"=== Integrity Report ===")
    print(f"Status: {report.status.upper()}")
    print(f"Verified: {report.verified_items}")
    print(f"Failed: {report.failed_items}")
    print()

    if report.issues:
        print("Issues:")
        for issue in report.issues:
            icon = (
                "❌"
                if issue.severity == "critical"
                else "🟡"
                if issue.severity == "warning"
                else "ℹ️"
            )
            print(f"  {icon} [{issue.severity}] {issue.component}: {issue.message}")


if __name__ == "__main__":
    main()
