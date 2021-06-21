from typing import List


def get_time(position_list):
    hour = 0
    minute = 0
    for i in position_list:
        # hour
        if i < 4:
            h = 2 ** (3 - i)
            hour += h
        else:
            i -= 4
            m = 2 ** (5 - i)
            minute += m
    return hour, minute


def dfs(start_position, total_bit, position_list: List[int], result: List[str]):
    if len(position_list) == total_bit:
        h, m = get_time(position_list)
        if h < 12 and m < 60:
            str_m = f"{m}"
            if len(str_m) < 2:
                str_m = f"0{m}"
            result.append(f"{h}:{str_m}")
        return
    position_list.append(start_position)
    dfs(start_position + 1, total_bit, position_list, result)
    position_list.pop()
    dfs(start_position + 1, total_bit, position_list, result)


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        dfs(0, turnedOn, [], res)
        return res
