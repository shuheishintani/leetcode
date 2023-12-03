import collections
from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_map = collections.defaultdict(list)
        res = []
        access_times = sorted(access_times, key=lambda x: x[1])
        for employee, timestamp in access_times:
            access_map[employee].append(int(timestamp[:2]) * 60 + int(timestamp[2:]))
        for employee, timestamps in access_map.items():
            for i in range(len(timestamps) - 2):
                if timestamps[i + 2] - timestamps[i] < 60:
                    res.append(employee)
                    break
        return res
