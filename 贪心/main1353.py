from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0] * 100000 + x[1])
        total_day = 0
        today = events[0][0]
        while len(events) > 0:
            index = 0
            today = max(today, events[0][0])
            chosen_index = 0

            while index < len(events):
                if events[index][1] < today:
                    events.pop(index)
                    continue
                if events[index][0] <= today <= events[index][1]:
                    if events[index][1] <= events[chosen_index][1]:
                        chosen_index = index
                        if events[chosen_index][1] == today:
                            break
                    index += 1


                elif events[index][0] > today:
                    break
            if len(events) == 0:
                break
            today += 1
            events.pop(chosen_index)
            total_day += 1

        return total_day


if __name__ == '__main__':
    s = [[1,1],[1,2],[1,3],[1,4],[1,5]]
    print(Solution().maxEvents(s))
