import collections
from typing import List


# 超时
class Solution2:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        station_map = collections.defaultdict(set)
        for s in routes:
            for i in s:
                station_map[i] = station_map[i].union(set(s))
        step = 0
        level = station_map[source]
        used = set()
        while len(level) != 0:
            next_level = set()
            step += 1
            for s in level:
                if s == target:
                    return step
                if s in used:
                    continue
                used.add(s)
                next_level = next_level.union(station_map[s].difference(used))
            level = next_level
        return -1


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        source_line = set()
        target_line = set()
        # 根据车站获得路线的index
        station_line_map = collections.defaultdict(set)
        for index, s in enumerate(routes):
            for i in s:
                station_line_map[i].add(index)
                if i == source:
                    source_line.add(index)
                if i == target:
                    target_line.add(index)

        level = source_line
        step = 0
        used = set()
        while len(level) != 0:
            next_level = set()
            step += 1
            for sl in level:
                if sl in target_line:
                    return step
                if sl in used:
                    continue
                used.add(sl)
                stations = routes[sl]
                for station in stations:
                    for li in station_line_map[station]:
                        if li not in used:
                            next_level.add(li)
            level = next_level
        return -1


a = Solution().numBusesToDestination(
    routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6
)
print(a)
