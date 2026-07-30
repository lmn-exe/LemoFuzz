import queuemanager
import http_engine
import job

class workers:
    def __init__(
            self,
            queuemanager: queuemanager.QueueManager,
            http_engine: http_engine.HttpEngine,
        ):
            self.queuemanager = queuemanager
            self.http_engine = http_engine


    def run(self):
        while True:
            try:
                # Get the next job
                job = self.queuemanager.get()

            except queuemanager.empty:
                # No more jobs
                break

            try:
                # Process the job
                self.process_job(job)

            finally:
                # Mark this job as finished
                self.queuemanager.task_done()  
                
                
    def process_job(self, job_: job.Job):
        result = self.http_engine.send(job_.url)
        if result is None:
            print("Request failed.")
        else:
            print(f"Status Code: {result.status_code}")
            print(f"URL: {result.url}")
            #print(result.text[:200])  # Print first 200 characters