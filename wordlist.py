from pathlib import Path

class Wordlist:
    
    def __init__(self, path: str, extension: list[str] | str ):
        self.path = Path(path)
        self.extension = extension

    def load(self):
        if not self.path.exists():
            #raise FileNotFoundError(f"Wordlist file not found: {self.path}")
            print(f"Wordlist file not found: {self.path}")
        else:
            print("Path is correct")
            