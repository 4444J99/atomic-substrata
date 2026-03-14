#!/usr/bin/env python3
"""
Assembly Engine
==============
On-demand knowledge assembly from atoms with vector similarity.

Features:
- Vector-based similarity search
- Context window assembly
- Relevance ranking
- Caching for repeated queries

This module re-exports the implementation from scripts/assembly.py.
"""

import sys
from pathlib import Path

_script_path = Path(__file__).parent.parent.parent.parent / "scripts" / "assembly.py"

if _script_path.exists():
    _module_name = _script_path.stem
    if str(_script_path.parent) not in sys.path:
        sys.path.insert(0, str(_script_path.parent))
    from assembly import Atom, AssembledOutput, SimpleVectorizer, AssemblyEngine

    __all__ = ["Atom", "AssembledOutput", "SimpleVectorizer", "AssemblyEngine"]
else:
    raise ImportError(f"assembly.py not found at {_script_path}")
