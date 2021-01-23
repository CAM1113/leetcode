def dfs(is_used, current_index, rooms):
    is_used[current_index] = True
    keys = rooms[current_index]
    for key in keys:
        if is_used[key]:
            continue
        dfs(is_used, key, rooms)


class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        is_used = [False for _ in rooms]
        dfs(is_used, 0, rooms)
        for i in is_used:
            if not i:
                return False
        return True
