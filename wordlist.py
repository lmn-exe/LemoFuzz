from pathlib import Path

class Wordlist:
    
    
    #Give the scanner one word at a time.
    #for word in self.wordlist:

    def __init__(self, path: str, extension:str ):
        self.path = Path(path)
        self.extension = extension
        self.words = []

    def load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"Wordlist file not found: {self.path}")

        self.words.clear()

        with self.path.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue          # blank line

                if line.startswith("#"):
                    continue          # comment

                self.words.append(line)
                
    def with_extensions(self, word: str):
        yield word
        #for ext in self.extension:
        yield f"{word}{self.extension}"
            
    def __iter__(self):
        for word in self.words:
            yield from self.with_extensions(word)

