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

            if self.queuemanager.qsize() == 0:
                print("No more jobs in the queue. Exiting.")
                break

            job_todo = job.Job()
            job_todo = self.queuemanager.get()
            self.process_job(job_todo)
            print("Job processed successfully.")
            self.queuemanager.task_done()


    def process_job(self, job: job.Job):
        result = self.http_engine.send(job.url)
        if result is None:
            print("Request failed.")
        else:
            print(f"Status Code: {result.status_code}")
            print(f"URL: {result.url}")
            print(result.text[:200])  # Print first 200 characters

