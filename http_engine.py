import requests  # type: ignore
import options
# class http_engine:
#     url : str
    
    
#     def build_session(self) -> requests.Session:
#         session = requests.Session()
#         session.headers.update(self.options.headers)
#         session.headers.setdefault("User-Agent", self.options.user_agent)
#         if self.options.cookies:
#             session.cookies.update(self.options.cookies)
#         if self.options.proxy:
#             session.proxies.update(
#                 {"http": self.options.proxy, "https": self.options.proxy}
#             )
#         return session

#     def send (self, url: str):
#         try:
#             response = self.session.request(
#                 method="GET",
#                 url=url,
#                 timeout=10,
#                 allow_redirects=false,
#                 )
#         except requests.exceptions.RequestException:
#             return None
class HttpEngine:
    
    def __init__(self, options: options.Options):
        self.options = options
        self.session = self.build_session()


    def build_session(self):
        session = requests.Session()

        session.headers.update(self.options.headers)
        session.headers.setdefault("User-Agent", self.options.user_agent)

        if self.options.cookies:
            session.cookies.update(self.options.cookies)

        if self.options.proxy:
            session.proxies.update({
                "http": self.options.proxy,
                "https": self.options.proxy,
            })

        return session


    def send(self, url: str):
        try:
            response = self.session.request(
                method="GET",
                url=url,
                timeout=self.options.timeout,
                allow_redirects=self.options.allow_redirects,
            )
            return response

        except requests.exceptions.RequestException as e:
            print(e)
            return None
        
    