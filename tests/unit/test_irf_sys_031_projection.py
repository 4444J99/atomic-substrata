#!/usr/bin/env python3
"""Regression tests for the IRF-SYS-031 projection records."""

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPH_FILE = REPO_ROOT / "data" / "graph_storage.json"
PROJECTION_FILE = REPO_ROOT / "data" / "projections" / "irf_sys_031_issue_projection.json"


def _load_graph() -> dict:
    with GRAPH_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def _load_projection() -> dict:
    with PROJECTION_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def _find_node_by_role(data: dict, atom_role: str) -> dict:
    for node in data["nodes"].values():
        if node.get("metadata", {}).get("atom_role") == atom_role:
            return node
    raise AssertionError(f"Missing node with atom_role={atom_role!r}")


def _find_edge(data: dict, source_id: str, target_id: str, relationship: str) -> dict:
    for edge in data["edges"].values():
        if (
            edge["source_id"] == source_id
            and edge["target_id"] == target_id
            and edge["relationship"] == relationship
        ):
            return edge
    raise AssertionError(
        f"Missing edge {relationship!r} from {source_id!r} to {target_id!r}"
    )


def test_legacy_irf_atom_preserves_legacy_id() -> None:
    data = _load_graph()
    node = _find_node_by_role(data, "legacy_irf_atom")

    assert node["metadata"]["legacy_id"] == "IRF-SYS-031"
    assert node["content"] == "Create ~/Workspace/a-organvm/ instance"


def test_legacy_irf_atom_derives_from_source_file_atom() -> None:
    data = _load_graph()
    legacy_atom = _find_node_by_role(data, "legacy_irf_atom")
    source_atom = _find_node_by_role(data, "irf_source_file_atom")
    edge = _find_edge(
        data,
        legacy_atom["id"],
        source_atom["id"],
        "derives_from",
    )

    assert source_atom["metadata"]["legacy_id"] == "IRF-SYS-031"
    assert source_atom["metadata"]["source_path"].endswith(
        "INST-INDEX-RERUM-FACIENDARUM.md"
    )
    assert edge["metadata"]["lineage"] == "legacy_irf_entry"


def test_irf_issue_projection_payload_is_recorded_locally() -> None:
    graph = _load_graph()
    projection = _load_projection()
    legacy_atom = _find_node_by_role(graph, "legacy_irf_atom")

    assert legacy_atom["metadata"]["issue_projection_ref"] == (
        "data/projections/irf_sys_031_issue_projection.json"
    )
    assert projection["legacy_id"] == "IRF-SYS-031"
    assert projection["issue"]["title"] == (
        "IRF-SYS-031: Create ~/Workspace/a-organvm/ instance"
    )
    assert projection["projection_target"]["board_url"] == (
        "https://github.com/orgs/a-organvm/projects/1/views/1"
    )


def test_issue_linkage_status_is_recorded_without_fabricating_number() -> None:
    graph = _load_graph()
    projection = _load_projection()
    legacy_atom = _find_node_by_role(graph, "legacy_irf_atom")

    assert legacy_atom["metadata"]["existing_issue_number"] is None
    assert legacy_atom["metadata"]["issue_linkage_status"] == (
        "unresolved_remote_lookup"
    )
    assert projection["issue_linkage"]["existing_issue_number"] is None
    assert projection["issue_linkage"]["lookup_status"] == (
        "unresolved_remote_lookup"
    )


def test_permanent_issue_atom_uses_issue_title_plus_body_payload() -> None:
    graph = _load_graph()
    projection = _load_projection()
    permanent_atom = _find_node_by_role(graph, "permanent_issue_atom")
    legacy_atom = _find_node_by_role(graph, "legacy_irf_atom")
    edge = _find_edge(
        graph,
        permanent_atom["id"],
        legacy_atom["id"],
        "references",
    )

    expected_payload = (
        projection["issue"]["title"] + "\n\n" + projection["issue"]["body_markdown"]
    )
    assert permanent_atom["content"] == expected_payload
    assert permanent_atom["metadata"]["legacy_id"] == "IRF-SYS-031"
    assert permanent_atom["metadata"]["issue_projection_ref"] == (
        "data/projections/irf_sys_031_issue_projection.json"
    )
    assert projection["source_refs"]["permanent_atom_id"] == permanent_atom["id"]
    assert edge["metadata"]["reason"] == "Permanent issue-derived atom preserves the richer issue payload."
