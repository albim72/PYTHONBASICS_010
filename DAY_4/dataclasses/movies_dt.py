from dataclasses import dataclass,field
from typing import List

@dataclass
class Movie:
    title: str
    year: int
    director: str
    rating: float = 0.0
    cast: List[str] = field(default_factory=list)

    def add_actor(self, actor: str) -> None:
        self.cast.append(actor)

    def is_classic(self) -> bool:
        return 2025 - self.year > 25

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) directed by {self.director}"


movie1 = Movie("The Matrix", 1999, "The Wachowskis",8.7)
movie1.add_actor("Keanu Reeves")
movie1.add_actor("Carrie-Anne Moss")


print(movie1)
print(movie1.is_classic())
