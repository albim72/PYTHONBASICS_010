"""
protocol_interface.py

Demonstrates Python "interfaces" using typing.Protocol (structural typing).
- Define a Protocol: Exporter (requires an `export` method).
- Any object that has the right shape (method signature) is accepted — no inheritance required.
"""

from __future__ import annotations
from typing import Protocol, Iterable, Mapping, Any
import json


class Exporter(Protocol):
    """Structural interface: any object with .export(rows) -> str matches."""
    def export(self, rows: Iterable[Mapping[str, Any]]) -> str: ...


class MinimalJSON:
    """A class that happens to match the Exporter protocol."""
    def export(self, rows: Iterable[Mapping[str, Any]]) -> str:
        return json.dumps(list(rows))


class PrettyJSON:
    """Another class matching Exporter — with a different implementation."""
    def export(self, rows: Iterable[Mapping[str, Any]]) -> str:
        return json.dumps(list(rows), ensure_ascii=False, indent=2)


def use_exporter(rows: Iterable[Mapping[str, Any]], exporter: Exporter) -> str:
    """
    This function accepts anything that *conforms* to Exporter protocol.
    No base class or registration is required.
    """
    return exporter.export(rows)


if __name__ == "__main__":
    demo_rows = [
        {"title": "The Matrix", "year": 1999},
        {"title": "Inception", "year": 2010},
    ]
    print("=== Minimal JSON ===")
    print(use_exporter(demo_rows, MinimalJSON()))
    print("\n=== Pretty JSON ===")
    print(use_exporter(demo_rows, PrettyJSON()))
