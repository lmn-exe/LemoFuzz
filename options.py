# class Options:
#     url: str
#     wordlist_path: str
#     extension: str
#     status: str

#     def __init__(self, url: str, wordlist_path: str, extension: str, status: str):
#         self.url = url
#         self.wordlist_path = wordlist_path
#         self.extension = extension
#         self.status = status

import random
from pathlib import Path

class Options:
    def __init__(
        self,
        url: str,
        wordlist_path: str,
        extension: str = "",
        headers: dict | None = None,
        user_agent: str | None = None,
        cookies: dict | None = None,
        proxy: str | None = None,
        timeout: int = 10,
        allow_redirects: bool = False,

        num_threads: int = 4,
        status: int | None = None,
        size: int | None = None,
        content_type : str | None = None, 
        text: str | None = None,
        response_time: int | None = None
    ):
        self.url = url
        self.wordlist_path = wordlist_path
        self.extension = extension
        self.status = status
        self.num_threads = num_threads
        self.size = size
        self.content_type = content_type
        self.text = text
        self.response_time = response_time

        # HTTP options
        self.headers = headers or {}

        if user_agent:
            self.user_agent = user_agent
        else:
            self.user_agent = self.random_user_agent()

        self.cookies = cookies or {}
        self.proxy = proxy
        self.timeout = timeout
        self.allow_redirects = allow_redirects



    def random_user_agent(self):
        path = Path("user_agents.txt")

        if not path.exists():
            raise FileNotFoundError("user_agents.txt not found")

        with path.open("r", encoding="utf-8") as file:
            user_agents = [
                line.strip()
                for line in file
                if line.strip()
            ]

        return random.choice(user_agents)