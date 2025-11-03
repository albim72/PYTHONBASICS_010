from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Iterable, Mapping, List
import json
import csv
from pathlib import Path


class DataExporter(ABC):
    """
    Interface (abstract base class) for all data exporters.
    Every exporter must implement two methods:
    - validate(data): check if the data is acceptable
    - export(data): return a string representation or write to a file
    """

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if data is valid for this exporter, otherwise raise an error."""
        pass

    @abstractmethod
    def export(self, data: Any) -> str:
        """
        Export the data in a given format and return it as a string.
        (In a real system, this could also write directly to a file.)
        """
        pass


class JSONExporter(DataExporter):
    """
    Concrete implementation of DataExporter.
    Exports data as JSON.
    """

    def validate(self, data: Any) -> bool:
        # For JSON export, we require data to not be empty
        # and to be something that can be serialized by json.dumps.
        if data is None:
            raise ValueError("Cannot export None as JSON.")
        if data == [] or data == {}:
            raise ValueError("Cannot export empty data as JSON.")
        try:
            json.dumps(data)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Data is not JSON-serializable: {e}")
        return True

    def export(self, data: Any) -> str:
        # We assume validate() was already called by save_report().
        return json.dumps(data, indent=4)


class CSVExporter(DataExporter):
    """
    Concrete implementation of DataExporter.
    Exports data as CSV text.
    We assume the data is a list of dictionaries with the same keys.
    Example:
    [
        {"name": "Alice", "score": 10},
        {"name": "Bob",   "score": 12}
    ]
    """

    def validate(self, data: Any) -> bool:
        # Check basic conditions for CSV:
        # 1. data must be a non-empty iterable
        # 2. each row must be a mapping (dict-like)
        if not data:
            raise ValueError("Cannot export empty data as CSV.")

        if not isinstance(data, Iterable):
            raise ValueError("CSVExporter expects an iterable of rows.")

        first_row = None
        for row in data:
            first_row = row
            break

        if first_row is None:
            raise ValueError("CSVExporter received an empty iterable.")

        if not isinstance(first_row, Mapping):
            raise ValueError("CSVExporter expects each row to be a dict-like object.")

        # Optional: ensure all rows share the same keys
        expected_keys = set(first_row.keys())
        for row in data:
            if set(row.keys()) != expected_keys:
                raise ValueError("All rows must have the same columns for CSV export.")

        return True

    def export(self, data: Iterable[Mapping[str, Any]]) -> str:
        # Convert rows to CSV format and return as string (not file).
        rows: List[Mapping[str, Any]] = list(data)
        if not rows:
            return ""

        # Extract column names from keys of the first row
        fieldnames = list(rows[0].keys())

        # We'll build CSV output in memory using csv.writer-like logic
        # but without touching the filesystem.
        from io import StringIO
        buffer = StringIO()

        writer = csv.DictWriter(buffer, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

        return buffer.getvalue()


def save_report(data: Any, exporter: DataExporter, output_path: Path | None = None) -> str:
    """
    High-level function that uses the interface, NOT the concrete class.
    This is the important part: 'save_report' depends on the DataExporter interface only.
    - It validates the data.
    - It exports the data.
    - Optionally writes it to a file if output_path is provided.
    - Returns the exported data as string (for printing/logging).
    """
    # 1. Validate according to the exporter's own rules
    exporter.validate(data)

    # 2. Export into the target format
    result_str = exporter.export(data)

    # 3. Optionally store the result in a file
    if output_path is not None:
        output_path.write_text(result_str, encoding="utf-8")

    return result_str


# ------------------------------------------------------------
# Demonstration / Example usage
# ------------------------------------------------------------

if __name__ == "__main__":
    # Sample data set we will export in two different formats.
    # Note: this is realistic reporting-style data.
    sales_data = [
        {"product": "Laptop", "units_sold": 12, "unit_price": 1200.0},
        {"product": "Mouse", "units_sold": 58, "unit_price": 25.5},
        {"product": "Monitor", "units_sold": 17, "unit_price": 320.0},
    ]

    # We will also prepare a dict-style summary for JSON
    summary_data = {
        "report_name": "Weekly Sales Summary",
        "total_items": len(sales_data),
        "currency": "GBP",
        "sales": sales_data,
    }

    # Create exporter objects
    json_exporter = JSONExporter()
    csv_exporter = CSVExporter()

    # 1. Export summary_data using JSONExporter
    print("=== JSON EXPORT ===")
    json_result = save_report(
        data=summary_data,
        exporter=json_exporter,
        output_path=Path("sales_report.json")
    )
    print(json_result)
    print()

    # 2. Export sales_data using CSVExporter
    print("=== CSV EXPORT ===")
    csv_result = save_report(
        data=sales_data,
        exporter=csv_exporter,
        output_path=Path("sales_report.csv")
    )
    print(csv_result)
    print()

    # At this point:
    # - sales_report.json and sales_report.csv have been written.
    # - We demonstrated polymorphism: save_report() works with ANY DataExporter.
