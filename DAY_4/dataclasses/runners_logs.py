from dataclasses import dataclass
from typing import List

@dataclass
class RunRecord:
    date: str
    distance_km: float
    duration_min: float

class RunLog:
    def __init__(self) -> None:
        self.runs: List[RunRecord] = []

    def add_run(self, run:RunRecord) -> None:
        self.runs.append(run)

    #computing total distance
    def total_distance(self) -> float:
        return sum(r.distance_km for r in self.runs)

    #calculating pace
    @staticmethod
    def _pace_min_per_km(run: RunRecord) -> float:
        return run.duration_min / run.distance_km if run.distance_km > 0 else 0

    #exporting data to a text file
    def export_txt(self,path:str) -> None:
        with open(path,"w",encoding="utf-8") as f:
            for r in self.runs:
                pace = self._pace_min_per_km(r)
                line = f"{r.date},{r.distance_km},{r.duration_min},{pace:.2f}min/km\n"
                f.write(line)
            f.write(f"Total distance: {self.total_distance()}km\n")


def main():
    log = RunLog()
    log.add_run(RunRecord("2023-01-01", 10.5, 5.5))
    log.add_run(RunRecord("2023-01-02", 5.5, 27.4))
    log.add_run(RunRecord("2023-01-03", 36, 231.5))
    log.add_run(RunRecord("2023-01-05", 12, 58))
    log.export_txt("runs.txt")
    print(f"Total distance: {log.total_distance():.2f}km")

if __name__ == '__main__':
    main()

