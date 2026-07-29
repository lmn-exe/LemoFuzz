class Job:
    def __init__(self, options, wordlist):
        self.options = options
        self.wordlist = wordlist
        
    def concatenate_url(self, word):
        return f"{self.options.url}/{word}"