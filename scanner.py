import options
import wordlist
import job
import queuemanager

class Scanner:
    options: options.Options
    wordlist: wordlist.Wordlist

    def __init__(self, options: options.Options):
        self.options = options
        self.wordlist = wordlist.Wordlist(options.wordlist_path, options.extension)
        
    def run(self):
        self.wordlist.load()
        jobs = job.Job(self.options, self.wordlist)
        queue = queuemanager.QueueManager()
        for word in self.wordlist:
            job_ =jobs.concatenate_url(word)
            queue._queue.put(job_) 
            print(f"the words are: {word}")
        print(f"the queue size is: {queue.qsize()}")
        
        
