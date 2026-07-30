import options
import wordlist
import job
import queuemanager
import workers
import http_engine

class Scanner:
    options: options.Options
    wordlist: wordlist.Wordlist

    def __init__(self, options: options.Options):
        self.options = options
        self.wordlist = wordlist.Wordlist(options.wordlist_path, options.extension)
        
    def run(self):
        self.wordlist.load()

        # jobs = job.Job(self.options, self.wordlist)

        queue = queuemanager.QueueManager()
        http_engine_instance = http_engine.HttpEngine(self.options)

        for word in self.wordlist:
            # job_ =jobs.concatenate_url(word)
            job_obj = job.Job()
            job_obj.url = self.options.url + "/" + word
            job_obj.word = word

            # queue._queue.put(job_) 
            queue._queue.put(job_obj) ## gotta check it later

            print(f"the job word is : {job_obj.word} and the url is :{job_obj.url}")
        print(f"the queue size is: {queue.qsize()}")
        # test_job = queue.get()
        # print(f"the test job word is : {test_job.word} and the url is :{test_job.url}")
        

        worker_inprogress = workers.workers(queue, http_engine_instance)
        worker_inprogress.run()
        












