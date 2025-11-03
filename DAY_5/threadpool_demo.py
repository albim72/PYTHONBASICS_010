"""
ThreadPoolExecutor – Practical Demo (I/O-bound patterns)
--------------------------------------------------------
This script showcases several common patterns for using
concurrent.futures.ThreadPoolExecutor with clear, commented examples.

What you will learn:
1) Basic parallel execution with executor.map
2) Collecting results as they complete with as_completed
3) Handling exceptions from worker functions
4) Timeouts and cancellation
5) Choosing a sensible max_workers for I/O-bound tasks
6) A tiny 'realistic' example: hashing multiple files in parallel

Run:
    python threadpool_demo.py
"""

from __future__ import annotations

import concurrent.futures as cf
import hashlib
import logging
import os
import random
import string
import time
from pathlib import Path
from typing import Iterable, List, Tuple


# ---------- Logging setup so you can see which threads are running ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(threadName)s | %(message)s",
)


# ----------------------------- Helper functions -----------------------------
def simulated_io_task(name: str, min_delay: float = 0.2, max_delay: float = 1.2) -> str:
    """
    Simulates an I/O-bound task by sleeping for a random duration.
    Returns a small message including the 'name' and elapsed time.
    """
    delay = random.uniform(min_delay, max_delay)
    logging.info(f"[{name}] starting (sleeping {delay:.2f}s)")
    time.sleep(delay)
    msg = f"[{name}] done in {delay:.2f}s"
    logging.info(msg)
    return msg


def unstable_task(i: int) -> str:
    """
    A task that sometimes fails to demonstrate exception handling.
    Raises ValueError for certain inputs.
    """
    delay = random.uniform(0.1, 0.8)
    time.sleep(delay)
    if i % 5 == 0:  # cause a failure every 5th task
        raise ValueError(f"Intentional failure for item {i}")
    return f"ok-{i}"


def create_random_files(folder: Path, count: int = 8, size_kb: int = 64) -> List[Path]:
    """
    Creates 'count' random files of approximately 'size_kb' kilobytes each.
    Returns list of created file paths.
    """
    folder.mkdir(parents=True, exist_ok=True)
    paths: List[Path] = []
    for idx in range(count):
        p = folder / f"sample_{idx:02d}.bin"
        with p.open("wb") as f:
            # ~size_kb*1024 bytes of random ASCII letters to keep it deterministic-ish
            data = "".join(random.choices(string.ascii_letters, k=size_kb * 1024)).encode("ascii")
            f.write(data)
        paths.append(p)
    return paths


def md5sum(path: Path) -> Tuple[Path, str]:
    """
    Computes the MD5 hash of a file. Suitable for I/O-bound parallelism.
    Returns (path, hex_digest).
    """
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return path, h.hexdigest()


# --------------------------------- Demos ------------------------------------
def demo_map_basic() -> None:
    """
    1) Basic parallel execution with executor.map
    - Submits a list of small I/O tasks and collects results in input order.
    """
    print("\n=== Demo 1: executor.map (ordered results) ===")
    names = [f"TASK-{i}" for i in range(1, 8)]
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for result in ex.map(simulated_io_task, names):
            print("Result:", result)


def demo_as_completed_and_exceptions() -> None:
    """
    2) as_completed + exception handling
    - Submits tasks that may fail and handles exceptions gracefully.
    - Shows how to retrieve results as soon as they finish.
    """
    print("\n=== Demo 2: as_completed + exception handling ===")
    futures: List[cf.Future] = []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for i in range(1, 16):  # submit more tasks to see some failures
            futures.append(ex.submit(unstable_task, i))

        for fut in cf.as_completed(futures):
            try:
                res = fut.result()
                print("Completed:", res)
            except Exception as e:
                print("Task failed with:", repr(e))


def demo_timeouts() -> None:
    """
    3) Timeouts
    - Demonstrates how to impose a timeout on getting a future's result.
    - Any task exceeding the timeout raises a TimeoutError (we handle it).
    """
    print("\n=== Demo 3: timeouts on future.result(timeout=...) ===")
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        futs = [ex.submit(simulated_io_task, f"SLOW-{i}", 0.5, 2.0) for i in range(5)]
        for fut in futs:
            try:
                # Short timeout for demonstration
                print("Got:", fut.result(timeout=0.6))
            except cf.TimeoutError:
                print("TimeoutError: task took too long (will still complete in background)")


def demo_io_parallel_hashing() -> None:
    """
    4) Realistic I/O example: hash multiple files in parallel
    - Creates sample files (non-destructive, inside ./_demo_files)
    - Computes MD5 for each using a thread pool
    - Collects and prints results in completion order
    """
    print("\n=== Demo 4: parallel file hashing (MD5) ===")
    base = Path(__file__).parent / "_demo_files"
    files = create_random_files(base, count=8, size_kb=64)

    with cf.ThreadPoolExecutor(max_workers=min(8, (os.cpu_count() or 2) * 5)) as ex:
        # For I/O-bound tasks, max_workers can be higher than CPU count.
        fut_to_path = {ex.submit(md5sum, p): p for p in files}
        for fut in cf.as_completed(fut_to_path):
            p, digest = fut.result()
            print(f"{p.name}: {digest}")


def main() -> None:
    random.seed(42)  # deterministic-ish sleeps and file contents for demo

    demo_map_basic()
    demo_as_completed_and_exceptions()
    demo_timeouts()
    demo_io_parallel_hashing()

    print("\nAll demos finished.")


if __name__ == "__main__":
    main()
