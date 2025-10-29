"""
abc_interface.py

Demonstrates a Python "interface" using Abstract Base Classes (ABCs).
- Define an abstract interface: DataExporter.
- Implement two concrete exporters: CSVExporter and JSONExporter.
- Show a function that depends on the interface, not implementations.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Mapping, Any
import csv
import io
import json


class DataExporter(ABC):
    """
    Abstract interface for exporters.
    Concrete classes must implement `export` and `validate`.
    """

    @abstractmethod
    def export(self, rows: Iterable[Mapping[str, Any]]) -> str:
        """Convert an iterable of dict rows into a string representation."""
        raise NotImplementedError

    @abstractmethod
    def validate(self, rows: Iterable[Mapping[str, Any]]) -> None:
        """Optionally validate rows and raise ValueError on errors."""
        raise NotImplementedError


class CSVExporter(DataExporter):
    """Concrete exporter to CSV format."""

    def export(self, rows: Iterable[Mapping[str, Any]]) -> str:
        # Convert rows to a list so we can iterate multiple times
        rows_list = list(rows)
        self.validate(rows_list)

        if not rows_list:
            return ""

        # Use an in-memory text buffer to build the CSV string
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=list(rows_list[0].keys()))
        writer.writeheader()
        writer.writerows(rows_list)
        return buffer.getvalue()

    def validate(self, rows: Iterable[Mapping[str, Any]]) -> None:
        # Basic validation: ensure all rows have the same keys
        keys = None
        for i, row in enumerate(rows, start=1):
            if keys is None:
                keys = set(row.keys())
            elif set(row.keys()) != keys:
                raise ValueError(f"Row {i} has different keys: {row.keys()} vs {keys}")


class JSONExporter(DataExporter):
    """Concrete exporter to JSON format."""

    def export(self, rows: Iterable[Mapping[str, Any]]) -> str:
        rows_list = list(rows)
        self.validate(rows_list)
        return json.dumps(rows_list, ensure_ascii=False, indent=2)

    def validate(self, rows: Iterable[Mapping[str, Any]]) -> None:
        # Basic validation: check JSON-serializability by attempting a dump
        try:
            json.dumps(list(rows))
        except TypeError as e:
            raise ValueError(f"Data not JSON-serializable: {e}")


def save_report(rows: Iterable[Mapping[str, Any]], exporter: DataExporter) -> str:
    """
    High-level function that depends on the interface, not on concrete exporters.
    Returns the exported string so the caller can save it to a file or send over network.
    """
    return exporter.export(rows)


if __name__ == "__main__":
    demo_rows = [
        {"name": "Marek", "distance_km": 10.0, "time_min": 47},
        {"name": "Anna", "distance_km": 21.1, "time_min": 100},
    ]

    print("=== CSV Export ===")
    print(save_report(demo_rows, CSVExporter()))

    print("=== JSON Export ===")
    print(save_report(demo_rows, JSONExporter()))
