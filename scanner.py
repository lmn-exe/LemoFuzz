import http_engine, workers
import options
import wordlist
import job
import queuemanager
import threading

class Scanner:
    options: options.Options
    wordlist: wordlist.Wordlist

    def __init__(self, options: options.Options):
        self.options = options
        self.wordlist = wordlist.Wordlist(options.wordlist_path, options.extension)
        
    def run(self):
        self.wordlist.load()
        queue = queuemanager.QueueManager()
        for word in self.wordlist:
            job_obj = job.Job()
            job_obj.url = self.options.url + "/" + word
            job_obj.word = word
            queue.fill(job_obj) 
            
            print(f"the words are: {word}")
        
        threads = []
        
        for _ in range(self.options.num_threads):
            engine = http_engine.HttpEngine(self.options)
            worker = workers.workers(queue, engine)
            thread = threading.Thread(target=worker.run)
            thread.start()
            threads.append(thread)
        queue.join()

        for thread in threads:
            thread.join()
        print(f"the queue size is: {queue.qsize()}")
        