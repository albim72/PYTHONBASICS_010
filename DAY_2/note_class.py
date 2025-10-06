from pathlib import Path

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.file_path = Path(f"notes/{self.title}.txt")

    def save(self):
        """Save the note content to text file."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(self.content)
        print(f"Saved to {self.file_path}")

    def read(self):
        """Read the note content from text file."""
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as f:
                text = f.read()
            print("___ note content ___")
            print(text)
        else:
            return "No note found."

note1 = Note("myFirstNote", "This is first note created by ptyhon class")
note1.save()
note1.read()

note2 = Note("mySecondNote", "This is first second note.... 634529385934895")
note2.save()
note2.read()
