import options
import requests

class Filter_engine:
    def should_keep(self, response: requests.Response) -> bool:
        if response.status_code == 200:
            return False
        return True