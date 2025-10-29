from dataclasses import dataclass,field
from typing import List
import datetime

@dataclass(order=True,frozen=True)
class Movie:
    sort_index:float = field(init=False,repr=False)
    title: str
    year: int
    director: str
    rating: float = 0.0
    genres:list[str] = field(default_factory=list,repr=False)
    cast: List[str] = field(default_factory=list,repr=False)

    def __post_init__(self) -> None:
        current_year = datetime.datetime.now().year
        if not (1888 <= self.year <= current_year):
            raise ValueError(
                f"Invalid year {self.year} for movie {self.title}"
            )
        #validate rating
        if not(0.0<=self.rating<=10.0):
            raise ValueError(
                f"Invalid rating {self.rating} for movie {self.title} - rating between 0.0 and 10.0"
            )
        object.__setattr__(self,"sort_index",-self.rating)

    def summary(self) -> str:
        genres_str = ", ".join(self.genres) if self.genres else "N/A"
        return (
            f"{self.title} ({self.year}) directed by {self.director}"
            f" with rating {self.rating} and genres {self.genres}"
        )


def main():
    movies = [
        Movie("The Matrix", 1999, "The Wachowskis",8.7,["Sci-fi","Action"],["Keanu Reeves","Carrie-Ann Moss"]),
        Movie("Inception",2010,"Christopher Nolan",8.8,["Sci-fi","Thriller"],["Christopher Nolan","Kevin Bacon"]),
        Movie("The Dark Knight",2008,"Christopher Nolan",9.0,["Action","Drama"],["Christopher Nolan","Kevin Bacon"]),
        Movie("The Prestige",2006,"Christopher Nolan",9.5,["Drama"],["Christopher Nolan","Kevin Bacon"]),
        Movie("Interstellar",2014,"Christopher Nolan",8.5,["Sci-fi","Adventure"],["Christopher Nolan","Kevin Bacon"])
    ]

    print(f"movies: {movies}")
    print(f"movie summaries:\n")
    for m in movies:
        print(" -",m.summary())

    print(f"\nmovies sorted by rating:\n")
    for m in sorted(movies):
        print(" -",m.title,m.rating)

    try:
        movies[0].rating = 9.9
    except Exception as e:
        print(f"Error setting rating: {e}")

if __name__ == '__main__':
    main()
