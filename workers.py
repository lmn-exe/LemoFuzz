import queuemanager
import http_engine
import job
import wildcard
import filter_engine
import options
import logger


class workers:
    def __init__(
            self,
            queuemanager: queuemanager.QueueManager,
            http_engine: http_engine.HttpEngine,
            wildcard: wildcard.Wildcard,
            filter_engine: filter_engine.Filter_engine,
            logger: logger.Logger,
        ):
            self.queuemanager = queuemanager
            self.http_engine = http_engine
            self.wildcard = wildcard
            self.filter_engine = filter_engine
            self.logger = logger


    def run(self):
        while True:
            try:
                # Get the next job
                job = self.queuemanager.get()
                # print("worker got job: ", job.url , "id: ", id(self))

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
                if self.filter_engine.should_keep(result):
                    ### call log here
                    self.logger.log(result, job_.url)
                    self.logger.create_log_file("log.txt", result, job_.url)
                    #print("the result is kept for url: ", job_.url)
                    #rint(f"Status Code: {result.status_code}")
                else:
                    print("the result is filtered for url: ", job_.url)
                    print(f"Status Code: {result.status_code}")
                # print(f"URL: {result.url}")