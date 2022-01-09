import time

from average_statistics import AverageStatistics


class AverageTimerService:
    start_time = 0.0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self, stats: AverageStatistics):
        delta = time.time() - self.start_time
        print(f'#{stats.current_iteration() + 1:02} Completed query: {delta:3.3f}')

        stats.submit_time(delta)
