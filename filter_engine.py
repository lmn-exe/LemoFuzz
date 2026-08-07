from urllib import response

import options
import requests

class Filter_engine:

    def __init__(self, options: options.Options):
        self.options = options
    
    def should_keep(self, response: requests.Response) -> bool:
        return (
            self.status_code_filter(response) and
            self.response_size_filter(response) and
            self.content_type_filter(response) and
            self.text_matching_filter(response) and
            self.response_time_filter(response)
        )
        
    
    def status_code_filter(self, response: requests.Response ) -> bool:
        return response.status_code == self.options.status or self.options.status == 0


    def response_size_filter(self, response: requests.Response) -> bool:
        return len(response.content) == self.options.size or self.options.size == 0

    def content_type_filter(self, response: requests.Response) -> bool:
        content_type = response.headers.get("Content-Type", "")
        return content_type == self.options.content_type or self.options.content_type == ""

    def text_matching_filter(self, response: requests.Response) -> bool:
        return self.options.text in response.text.lower() or self.options.text == ""

    def response_time_filter(self, response: requests.Response) -> bool:
        response_time_ms = response.elapsed.total_seconds() * 1000
        return response_time_ms > self.options.response_time or self.options.response_time == 0