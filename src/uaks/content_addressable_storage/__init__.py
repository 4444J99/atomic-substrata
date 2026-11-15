#!/usr/bin/env python3
"""
Content Addressable Storage
==========================
Hash-based storage for atoms with deduplication.

Features:
- SHA256-based addressing
- Deduplication
- Integrity verification
- Efficient storage
"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class CASEntry:
    """Represents an entry in content-addressable storage."""

    hash: str
    size: int
    created_at: str
    reference_count: int = 1
    metadata: dict = field(default_factory=dict)


class ContentAddressableStorage:
    """Content-addressable storage using SHA256 hashes."""

    def __init__(self, storage_root: Optional[Path] = None):
        self.storage_root = storage_root or Path("data/cas")
        self.storage_root.mkdir(parents=True, exist_ok=True)
        self.index_file = self.storage_root / "index.json"
        self.objects_dir = self.storage_root / "objects"
        self.objects_dir.mkdir(exist_ok=True)

        self.index: dict[str, CASEntry] = {}
        self.load_index()

    def load_index(self):
        """Load the index from disk."""
        if self.index_file.exists():
            try:
                with open(self.index_file, "r") as f:
                    data = json.load(f)
                    self.index = {k: CASEntry(**v) for k, v in data.items()}
            except Exception as e:
                print(f"Error loading index: {e}")
                self.index = {}

    def save_index(self):
        """Save the index to disk."""
        data = {
            k: {
                "hash": v.hash,
                "size": v.size,
                "created_at": v.created_at,
                "reference_count": v.reference_count,
                "metadata": v.metadata,
            }
            for k, v in self.index.items()
        }

        with open(self.index_file, "w") as f:
            json.dump(data, f, indent=2)

    def compute_hash(self, content: str) -> str:
        """Compute SHA256 hash of content."""
        return hashlib.sha256(content.encode()).hexdigest()

    def store(self, content: str, metadata: dict = None) -> str:
        """
        Store content and return its address.

        Args:
            content: Content to store
            metadata: Optional metadata

        Returns:
            Content address (hash)
        """
        content_hash = self.compute_hash(content)
        object_path = self.objects_dir / content_hash

        # Check if already stored
        if content_hash in self.index:
            if not object_path.exists():
                # Missing object file: restore from supplied content
                with open(object_path, "w") as f:
                    f.write(content)
                self.index[content_hash].reference_count += 1
                self.save_index()
                return content_hash

            # Object file exists: verify content hash matches expected content_hash
            existing_content = object_path.read_text()
            if self.compute_hash(existing_content) != content_hash:
                raise ValueError(
                    f"CAS object corruption detected for address {content_hash}: "
                    "existing object bytes do not match address hash."
                )

            # Increment reference count
            self.index[content_hash].reference_count += 1
            self.save_index()
            return content_hash

        # Store the content
        with open(object_path, "w") as f:
            f.write(content)

        # Add to index
        self.index[content_hash] = CASEntry(
            hash=content_hash,
            size=len(content),
            created_at=datetime.now().isoformat(),
            reference_count=1,
            metadata=metadata or {},
        )

        self.save_index()
        return content_hash

    def retrieve(self, address: str) -> Optional[str]:
        """
        Retrieve content by address.

        Args:
            address: Content address (hash)

        Returns:
            Content if found, None otherwise
        """
        if address not in self.index:
            return None

        object_path = self.objects_dir / address
        if not object_path.exists():
            return None

        return object_path.read_text()

    def exists(self, address: str) -> bool:
        """Check if content exists."""
        return address in self.index

    def delete(self, address: str) -> bool:
        """
        Delete content (decrement reference count).

        Args:
            address: Content address

        Returns:
            True if deleted, False if not found or still referenced
        """
        if address not in self.index:
            return False

        entry = self.index[address]
        entry.reference_count -= 1

        if entry.reference_count <= 0:
            # Actually delete
            object_path = self.objects_dir / address
            if object_path.exists():
                object_path.unlink()
            del self.index[address]
            self.save_index()
            return True

        self.save_index()
        return True

    def get_stats(self) -> dict:
        """Get storage statistics."""
        total_size = sum(e.size for e in self.index.values())

        return {
            "total_objects": len(self.index),
            "total_size": total_size,
            "total_references": sum(e.reference_count for e in self.index.values()),
            "objects_dir": str(self.objects_dir),
        }

    def verify_integrity(self) -> dict:
        """
        Verify integrity of all stored content.

        Returns:
            Dictionary with verification results
        """
        issues = []

        for address, entry in self.index.items():
            object_path = self.objects_dir / address

            if not object_path.exists():
                issues.append(
                    {
                        "address": address,
                        "issue": "Object file missing",
                    }
                )
                continue

            content = object_path.read_text()
            computed_hash = self.compute_hash(content)

            if computed_hash != address:
                issues.append(
                    {
                        "address": address,
                        "issue": "Hash mismatch",
                        "expected": address,
                        "actual": computed_hash,
                    }
                )

        return {
            "verified": len(issues) == 0,
            "total_checked": len(self.index),
            "issues": issues,
        }

    def export_index(self) -> str:
        """Export index as JSON."""
        data = {
            "exported_at": datetime.now().isoformat(),
            "stats": self.get_stats(),
            "entries": [
                {
                    "address": addr,
                    "size": entry.size,
                    "references": entry.reference_count,
                    "created": entry.created_at,
                }
                for addr, entry in self.index.items()
            ],
        }
        return json.dumps(data, indent=2)


def main():
    """CLI for content-addressable storage."""
    import sys

    cas = ContentAddressableStorage()

    if len(sys.argv) < 2:
        print("Usage: cas.py <command>")
        print("  Commands:")
        print("    store <content>   - Store content")
        print("    retrieve <addr>  - Retrieve content")
        print("    exists <addr>    - Check if exists")
        print("    delete <addr>    - Delete content")
        print("    stats            - Show statistics")
        print("    verify           - Verify integrity")
        return

    cmd = sys.argv[1]

    if cmd == "store":
        if len(sys.argv) < 3:
            print("Error: store requires content")
            return
        content = sys.argv[2]
        address = cas.store(content)
        print(f"Stored at: {address}")

    elif cmd == "retrieve":
        if len(sys.argv) < 3:
            print("Error: retrieve requires address")
            return
        content = cas.retrieve(sys.argv[2])
        if content:
            print(content)
        else:
            print("Not found")

    elif cmd == "exists":
        if len(sys.argv) < 3:
            print("Error: exists requires address")
            return
        print(cas.exists(sys.argv[2]))

    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Error: delete requires address")
            return
        cas.delete(sys.argv[2])
        print("Deleted")

    elif cmd == "stats":
        stats = cas.get_stats()
        print("=== CAS Statistics ===")
        for key, value in stats.items():
            print(f"  {key}: {value}")

    elif cmd == "verify":
        result = cas.verify_integrity()
        print(f"Verified: {result['verified']}")
        print(f"Total checked: {result['total_checked']}")
        if result["issues"]:
            print("Issues:")
            for issue in result["issues"]:
                print(f"  - {issue}")


if __name__ == "__main__":
    main()
