import queue
from typing import Iterable
import job


class QueueManager:
    def __init__(self, maxsize: int =0):
        self._queue: queue.Queue = queue.Queue(maxsize=maxsize)

    def fill(self, jobs: job.Job) -> None:
        self._queue.put(jobs)

    def get(self) -> job.Job | None:
        return self._queue.get()

    def task_done(self) -> None:
        self._queue.task_done()

    def join(self) -> None:
        self._queue.join()

    def qsize(self) -> int:
        return self._queue.qsize()

    def empty(self) -> bool:
        return self._queue.empty()
    
    # def put_sentinel(self, count: int) -> None:
    #     #"""Push `count` None values - one stop signal per worker thread."""
    #     for _ in range(count):
    #         self._queue.put(None)