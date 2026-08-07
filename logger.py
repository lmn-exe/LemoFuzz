import options
import requests

class Logger:
    def log(self, response: requests.Response, job_url: str):
        print(f"URL: {job_url}, Status Code: {response.status_code}, Length: {len(response.content)}, Content Type: {response.headers.get('Content-Type', '')}")


    def create_log_file(self, file_name: str, response: requests.Response, job_url: str):
        with open(file_name, 'a')as f:
            f.write(f"URL: {job_url}, Status Code: {response.status_code}, Length: {len(response.content)}, Content Type: {response.headers.get('Content-Type', '')}\n")