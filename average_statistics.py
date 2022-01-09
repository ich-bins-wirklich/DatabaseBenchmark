class AverageStatistics:
    def __init__(self):
        self.min_time = 1000.0
        self.max_time = 0.0
        self._exec_times = []

    def current_iteration(self):
        return len(self._exec_times)

    def submit_time(self, delta):
        self._exec_times.append(delta)

        if delta < self.min_time:
            self.min_time = delta

        if delta > self.max_time:
            self.max_time = delta

    # sum of first i exec times
    def sum(self, i):
        if i < 0 or i > self.current_iteration():
            print(f'Error in Statistics.sum(): sum({i}) requested, current iteration={self.current_iteration()}')
            return -1

        return sum(self._exec_times[:i])

    def average(self, i):
        if i <= 0 or i > self.current_iteration():
            print(f'Error in Statistics.average(): average({i}) requested, current iteration={self.current_iteration()}')
            return -1

        return self.sum(i) / i
