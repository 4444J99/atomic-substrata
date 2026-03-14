#!/usr/bin/env python3
"""
Portal Projection Module
=======================
Projects UAKS data to different formats.

Features:
- Export to various formats
- API generation
- Visualization data
- Report generation
"""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


@dataclass
class ProjectionConfig:
    """Configuration for projection."""

    format: str  # json, markdown, html, api
    include_metadata: bool = True
    include_graph: bool = False
    max_items: int = 1000


class PortalProjection:
    """Projects UAKS data to various formats."""

    def __init__(self):
        self.formatters = {
            "json": self._format_json,
            "markdown": self._format_markdown,
            "html": self._format_html,
            "api": self._format_api,
        }

    def project(
        self,
        state_file: str = "data/pipeline_state.json",
        config: Optional[ProjectionConfig] = None,
    ) -> str:
        """
        Project UAKS data to specified format.

        Args:
            state_file: Path to pipeline state
            config: Projection configuration

        Returns:
            Formatted output
        """
        config = config or ProjectionConfig(format="json")

        path = Path(state_file)

        if not path.exists():
            return json.dumps({"error": "State file not found"})

        with open(path) as f:
            state = json.load(f)

        formatter = self.formatters.get(config.format, self._format_json)
        return formatter(state, config)

    def _format_json(self, state: dict, config: ProjectionConfig) -> str:
        """Format as JSON."""
        output = {}

        if config.include_metadata:
            output["metadata"] = {
                "generated_at": datetime.now().isoformat(),
                "version": state.get("version"),
            }

        atoms = state.get("atoms", {})

        if config.max_items:
            output["atoms"] = {
                "text": atoms.get("text", [])[: config.max_items],
                "code": atoms.get("code", [])[: config.max_items],
                "total": atoms.get("total", 0),
            }
        else:
            output["atoms"] = atoms

        return json.dumps(output, indent=2)

    def _format_markdown(self, state: dict, config: ProjectionConfig) -> str:
        """Format as Markdown."""
        lines = [
            "# UAKS Atom Report",
            "",
            f"Generated: {datetime.now().isoformat()}",
            "",
        ]

        atoms = state.get("atoms", {})

        lines.append(f"## Summary")
        lines.append("")
        lines.append(f"- Total Atoms: {atoms.get('total', 0)}")
        lines.append(f"- Text Atoms: {len(atoms.get('text', []))}")
        lines.append(f"- Code Atoms: {len(atoms.get('code', []))}")
        lines.append("")

        text_atoms = atoms.get("text", [])[: config.max_items]
        if text_atoms:
            lines.append("## Text Atoms")
            lines.append("")
            for atom in text_atoms:
                lines.append(f"### {atom.get('id', 'unknown')}")
                lines.append(f"- Hash: {atom.get('hash', 'unknown')}")
                lines.append(f"- Status: {atom.get('status', 'unknown')}")
                content = atom.get("content", "")
                if content:
                    lines.append(f"- Content: {content[:100]}...")
                lines.append("")

        return "\n".join(lines)

    def _format_html(self, state: dict, config: ProjectionConfig) -> str:
        """Format as HTML."""
        atoms = state.get("atoms", {})

        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>UAKS Report</title>
    <style>
        body {{ font-family: system-ui, sans-serif; margin: 40px; }}
        .summary {{ background: #f5f5f5; padding: 20px; border-radius: 8px; }}
        .atom {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 4px; }}
        .atom-id {{ font-weight: bold; color: #333; }}
        .status {{ display: inline-block; padding: 3px 8px; border-radius: 3px; font-size: 12px; }}
        .status-raw {{ background: #ffeeba; }}
        .status-refined {{ background: #d4edda; }}
    </style>
</head>
<body>
    <h1>UAKS Atom Report</h1>
    <p>Generated: {datetime.now().isoformat()}</p>
    
    <div class="summary">
        <h2>Summary</h2>
        <p>Total Atoms: {atoms.get("total", 0)}</p>
        <p>Text Atoms: {len(atoms.get("text", []))}</p>
        <p>Code Atoms: {len(atoms.get("code", []))}</p>
    </div>
    
    <h2>Text Atoms</h2>
"""

        for atom in atoms.get("text", [])[: config.max_items]:
            status_class = f"status-{atom.get('status', 'unknown')}"
            html += f"""
    <div class="atom">
        <div class="atom-id">{atom.get("id", "unknown")}</div>
        <span class="status {status_class}">{atom.get("status", "unknown")}</span>
        <p>Hash: {atom.get("hash", "unknown")}</p>
    </div>
"""

        html += """
</body>
</html>"""

        return html

    def _format_api(self, state: dict, config: ProjectionConfig) -> str:
        """Format as API response."""
        atoms = state.get("atoms", {})

        response = {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "data": {
                "atoms": {
                    "text": atoms.get("text", [])[: config.max_items],
                    "code": atoms.get("code", [])[: config.max_items],
                    "total": atoms.get("total", 0),
                }
            },
        }

        return json.dumps(response, indent=2)

    def export_to_file(
        self,
        output_file: str,
        state_file: str = "data/pipeline_state.json",
        format: str = "json",
    ):
        """Export to file."""
        config = ProjectionConfig(format=format)
        output = self.project(state_file, config)

        with open(output_file, "w") as f:
            f.write(output)

        return output_file


def main():
    """CLI for portal projection."""
    import sys

    projector = PortalProjection()

    if len(sys.argv) < 3:
        print("Usage: portal_projection.py <format> <output_file>")
        print("  Formats: json, markdown, html, api")
        return

    format_type = sys.argv[1]
    output_file = sys.argv[2]

    if format_type not in ["json", "markdown", "html", "api"]:
        print(f"Unknown format: {format_type}")
        return

    result = projector.export_to_file(output_file, format=format_type)
    print(f"Exported to: {result}")


if __name__ == "__main__":
    main()
