import time

from all_queries_statistics import AllQueriesStatistics


class AllQueriesTimerService:
    start_time = 0.0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self, stats: AllQueriesStatistics, index):
        delta = time.time() - self.start_time
        print(f'#{index + 1:02} Completed query: {delta:3.3f}')

        stats.submit_time(delta, index)
