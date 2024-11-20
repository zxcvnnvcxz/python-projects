class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def meetingRoom(self, times: list[int]) -> bool:
        mini = 0
        maxi = 0
        for i in range(len(times)):
            for j in range(len(times[0])):
                var = times[i][j]
                mini = min(mini, var)
                maxi = max(maxi, var)
                if mini < times[i][j] < maxi:
                    return False

        return True


class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False

        return True

solution = Solution()
eg1 = [[0, 30], [5, 10], [15,20]]
eg2 = [[0, 8], [8, 10]]
print(solution.canAttendMeetings(eg1))