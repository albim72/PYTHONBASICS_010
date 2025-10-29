"""
duck_typing_example.py

Shows classic duck typing in Python:
- A function that uses .serialize() if present (EAFP style).
- Multiple classes that provide .serialize() with different internals.
"""

from __future__ import annotations
from typing import Any
import json
import csv
import io


def to_text(obj: Any) -> str:
    """
    Convert an object to a text representation.
    EAFP (Easier to Ask Forgiveness than Permission): try to call .serialize().
    """
    try:
        return obj.serialize()
    except AttributeError:
        # Fallback: use str() if no serialize() is available
        return str(obj)


class JsonPacket:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def serialize(self) -> str:
        return json.dumps(self.payload, ensure_ascii=False)


class CsvTable:
    def __init__(self, rows: list[dict]) -> None:
        self.rows = rows

    def serialize(self) -> str:
        if not self.rows:
            return ""
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=list(self.rows[0].keys()))
        writer.writeheader()
        writer.writerows(self.rows)
        return buffer.getvalue()


if __name__ == "__main__":
    jp = JsonPacket({"runner": "Marek", "distance_km": 10.0})
    ct = CsvTable([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    print("JSON via duck typing:", to_text(jp))
    print("CSV via duck typing:\n", to_text(ct))
    print("Fallback str():", to_text(42))
