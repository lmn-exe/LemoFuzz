import http_engine, workers
import options
import wordlist
import job
import queuemanager
import threading
import wildcard
import http_engine
import filter_engine

class Scanner:
    options: options.Options
    wordlist: wordlist.Wordlist

    def __init__(self, options: options.Options):
        self.options = options
        self.wordlist = wordlist.Wordlist(options.wordlist_path, options.extension)
        
    def run(self):
        self.wordlist.load()
        queue = queuemanager.QueueManager()
        wildcard_instance = wildcard.Wildcard()
        http_engine_instance = http_engine.HttpEngine(self.options)
        wildcard_instance.initialise(http_engine_instance, self.options)
        filter_engine_instance = filter_engine.Filter_engine(self.options)
        
        for word in self.wordlist:
            job_obj = job.Job()
            job_obj.url = self.options.url + "/" + word
            job_obj.word = word
            queue.fill(job_obj) 
            
            print(f"the words are: {word}")
        
        threads = []
        
        for i in range(self.options.num_threads):
            #print(f"created thread {i}")
            engine = http_engine.HttpEngine(self.options)
            worker = workers.workers(queue, engine,wildcard_instance, filter_engine_instance)
            thread = threading.Thread(target=worker.run)
            thread.start()
            threads.append(thread)
        queue.join()

        for thread in threads:
            thread.join()
        print(f"the queue size is: {queue.qsize()}")
        
        
