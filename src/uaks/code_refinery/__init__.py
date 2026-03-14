#!/usr/bin/env python3
"""
Code Refinery
=============
Processes raw code into refined CodeAtoms.

Features:
- AST parsing
- Dependency extraction
- Function/class detection
- Import analysis
- Metadata generation
"""

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class CodeAtom:
    """Represents a refined code atom."""

    id: str
    content: str
    hash: str
    language: str
    functions: list[dict] = field(default_factory=list)
    classes: list[dict] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    refined_at: str = field(default_factory=lambda: datetime.now().isoformat())


LANGUAGE_EXTENSIONS = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "javascript",
    ".tsx": "typescript",
    ".go": "go",
    ".rs": "rust",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".h": "c",
    ".hpp": "cpp",
    ".cs": "csharp",
    ".rb": "ruby",
    ".php": "php",
    ".swift": "swift",
    ".kt": "kotlin",
    ".scala": "scala",
}


class CodeRefinery:
    """Refines raw code into CodeAtoms."""

    def __init__(self):
        self.function_patterns = {
            "python": re.compile(r"def\s+(\w+)\s*\([^)]*\)\s*:"),
            "javascript": re.compile(
                r"(?:function\s+(\w+)|(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>)"
            ),
            "typescript": re.compile(
                r"(?:function\s+(\w+)|(\w+)\s*:\s*(?:async\s*)?\([^)]*\)\s*=>|(\w+)\s*\([^)]*\)\s*[:{])"
            ),
            "go": re.compile(r"func\s+(?:\(\w+\s+\*?\w+\)\s+)?(\w+)\s*\("),
            "rust": re.compile(r"fn\s+(\w+)\s*\([^)]*\)"),
            "java": re.compile(
                r"(?:public|private|protected|static)?\s*(?:\w+\s+)+(\w+)\s*\([^)]*\)\s*\{"
            ),
        }
        self.class_patterns = {
            "python": re.compile(r"class\s+(\w+)(?:\([^)]*\))?:"),
            "javascript": re.compile(r"class\s+(\w+)"),
            "typescript": re.compile(r"class\s+(\w+)"),
            "java": re.compile(
                r"class\s+(\w+)(?:\s+extends\s+\w+)?(?:\s+implements\s+\w+)?"
            ),
        }
        self.import_patterns = {
            "python": re.compile(r"^(?:from\s+([\w.]+)\s+)?import\s+([\w.,\s*]+)"),
            "javascript": re.compile(
                r"^(?:import\s+(?:\{[^}]*\}|\*\s+as\s+\w+|\w+)\s+from\s+['\"]([^'\"]+)['\"]|require\s*\(['\"]([^'\"]+)['\"]\))"
            ),
            "typescript": re.compile(
                r"^(?:import\s+(?:\{[^}]*\}|\*\s+as\s+\w+|\w+)\s+from\s+['\"]([^'\"]+)['\"]|require\s*\(['\"]([^'\"]+)['\"]\))"
            ),
        }

    def detect_language(self, source: str, filepath: str = "") -> str:
        """Detect programming language."""
        if filepath:
            ext = Path(filepath).suffix
            if ext in LANGUAGE_EXTENSIONS:
                return LANGUAGE_EXTENSIONS[ext]

        # Simple heuristic based on content
        if "def " in source and ":" in source:
            return "python"
        if "function " in source or "=>" in source:
            return "javascript"
        if "func " in source and "package " in source:
            return "go"
        if "fn " in source and "let " in source:
            return "rust"

        return "unknown"

    def refine(self, content: str, source: str = "", filepath: str = "") -> CodeAtom:
        """
        Refine raw code into a CodeAtom.

        Args:
            content: Raw code content
            source: Optional source identifier
            filepath: Optional file path for language detection

        Returns:
            CodeAtom with extracted features
        """
        # Compute hash
        atom_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        atom_id = f"code_{atom_hash}"

        # Detect language
        language = self.detect_language(content, filepath)

        # Extract functions
        functions = self.extract_functions(content, language)

        # Extract classes
        classes = self.extract_classes(content, language)

        # Extract imports
        imports = self.extract_imports(content, language)

        # Extract dependencies
        dependencies = self.extract_dependencies(imports, language)

        # Generate metadata
        metadata = {
            "source": source,
            "filepath": filepath,
            "char_count": len(content),
            "line_count": len(content.split("\n")),
            "function_count": len(functions),
            "class_count": len(classes),
            "import_count": len(imports),
        }

        return CodeAtom(
            id=atom_id,
            content=content,
            hash=atom_hash,
            language=language,
            functions=functions,
            classes=classes,
            imports=imports,
            dependencies=dependencies,
            metadata=metadata,
        )

    def extract_functions(self, code: str, language: str) -> list[dict]:
        """Extract function definitions."""
        functions = []
        pattern = self.function_patterns.get(language)

        if not pattern:
            return functions

        for match in pattern.finditer(code):
            func_name = match.group(1) or match.group(2) or match.group(3)
            if func_name and not func_name.startswith("_"):
                functions.append(
                    {
                        "name": func_name,
                        "line": code[: match.start()].count("\n") + 1,
                    }
                )

        return functions

    def extract_classes(self, code: str, language: str) -> list[dict]:
        """Extract class definitions."""
        classes = []
        pattern = self.class_patterns.get(language)

        if not pattern:
            return classes

        for match in pattern.finditer(code):
            class_name = match.group(1)
            if class_name:
                classes.append(
                    {
                        "name": class_name,
                        "line": code[: match.start()].count("\n") + 1,
                    }
                )

        return classes

    def extract_imports(self, code: str, language: str) -> list[str]:
        """Extract import statements."""
        imports = []
        pattern = self.import_patterns.get(language)

        if not pattern:
            return imports

        for match in pattern.finditer(code, re.MULTILINE):
            groups = match.groups()
            for g in groups:
                if g and g.strip():
                    imports.append(g.strip())

        return imports

    def extract_dependencies(self, imports: list[str], language: str) -> list[str]:
        """Extract external dependencies from imports."""
        dependencies = []

        for imp in imports:
            # Filter out relative imports
            if imp.startswith("."):
                continue

            # Extract package name
            if language == "python":
                pkg = imp.split(".")[0].split(",")[0].strip()
            else:
                pkg = imp.split("/")[0]

            if pkg and pkg not in dependencies:
                dependencies.append(pkg)

        return dependencies

    def batch_refine(self, codes: list[tuple[str, str, str]]) -> list[CodeAtom]:
        """
        Refine multiple code snippets.

        Args:
            codes: List of (content, source, filepath) tuples

        Returns:
            List of CodeAtoms
        """
        return [
            self.refine(content, source, filepath)
            for content, source, filepath in codes
        ]


def main():
    """CLI for code refinery."""
    import sys

    refinery = CodeRefinery()

    if len(sys.argv) < 2:
        print("Usage: code_refinery.py <code>")
        print("  or:  code_refinery.py --file <path>")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Error: --file requires a path")
            sys.exit(1)

        path = Path(sys.argv[2])
        if not path.exists():
            print(f"Error: File not found: {path}")
            sys.exit(1)

        content = path.read_text()
        source = str(path)
        filepath = str(path)
    else:
        content = " ".join(sys.argv[1:])
        source = "cli"
        filepath = ""

    atom = refinery.refine(content, source, filepath)

    print(f"CodeAtom: {atom.id}")
    print(f"Language: {atom.language}")
    print(f"Hash: {atom.hash}")
    print(f"Functions: {len(atom.functions)}")
    print(f"Classes: {len(atom.classes)}")
    print(f"Imports: {len(atom.imports)}")
    print(f"Dependencies: {atom.dependencies}")
    print(f"\nMetadata:")
    for key, value in atom.metadata.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
