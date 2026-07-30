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


class Options:
    def __init__(
        self,
        url: str,
        wordlist_path: str,
        extension: str = "",
        status: str = "",
        headers: dict | None = None,
        user_agent: str = "PythonFuzzer/1.0",
        cookies: dict | None = None,
        proxy: str | None = None,
        timeout: int = 10,
        allow_redirects: bool = False,
        num_threads: int = 4
    ):
        self.url = url
        self.wordlist_path = wordlist_path
        self.extension = extension
        self.status = status
        self.num_threads = num_threads

        # HTTP options
        self.headers = headers or {}
        self.user_agent = user_agent
        self.cookies = cookies or {}
        self.proxy = proxy
        self.timeout = timeout
        self.allow_redirects = allow_redirects