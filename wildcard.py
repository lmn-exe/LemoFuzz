import requests
import options
import http_engine
import uuid

class Wildcard:
    wildcard_status = None
    wildcard_length = None
    wildcard_hash = None
    wildcard_title = None
    #enabled = False
    
    def initialise(self, http_engine:http_engine.HttpEngine,options: options.Options):
        randome_word = str(uuid.uuid4())
        url = options.url + "/" + randome_word
        #url = options.url + "/" + "stic"
        response = http_engine.send(url)
        if response is None:
            print("Request failed.")
        else:
            self.wildcard_status = response.status_code
            self.wildcard_length = len(response.text)
            self.wildcard_hash = hash(response.text)
            self.wildcard_title = self.extract_title(response.text)
            print(f"Wildcard Response: Status Code: {self.wildcard_status}, Length: {self.wildcard_length}, Hash: {self.wildcard_hash}, Title: {self.wildcard_title}")
        
    def is_wildcard(self, response):
        if response is None:
            return False
        status = response.status_code
        length = len(response.text)
        hash_value = hash(response.text)
        title = self.extract_title(response.text)
        
        return (status == self.wildcard_status and
                length == self.wildcard_length and
                title == self.wildcard_title)
    
    def extract_title(self, html):
        start_tag = "<title>"
        end_tag = "</title>"
        start_index = html.find(start_tag)
        end_index = html.find(end_tag)
        
        if start_index != -1 and end_index != -1:
            start_index += len(start_tag)
            return html[start_index:end_index].strip()
        return None