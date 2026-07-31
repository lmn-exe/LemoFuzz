import queuemanager
import http_engine
import job
import wildcard

class workers:
    def __init__(
            self,
            queuemanager: queuemanager.QueueManager,
            http_engine: http_engine.HttpEngine,
            wildcard: wildcard.Wildcard

        ):
            self.queuemanager = queuemanager
            self.http_engine = http_engine
            self.wildcard = wildcard


    def run(self):
        while True:
            try:
                # Get the next job
                job = self.queuemanager.get()
                print("worker got job: ", job.url , "id: ", id(self))

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
            if self.wildcard.is_wildcard(result):
                print("wildcard detected for url: ", job_.url)
            else:
                print(f"Status Code: {result.status_code}")
                print(f"URL: {result.url}")
                