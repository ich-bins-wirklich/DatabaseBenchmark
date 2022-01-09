class AllQueriesStatistics:
    def __init__(self, size):
        self.exec_times = [[] for _ in range(size)]

    def submit_time(self, delta, index):
        self.exec_times[index].append(delta)

    def first(self, index):
        return self.exec_times[index][0]

    def last(self, index):
        return self.exec_times[index][-1]

    def current_sum(self):
        sum = 0.0
        for i in range(len(self.exec_times)):
            sum += self.last(i)
        return sum
