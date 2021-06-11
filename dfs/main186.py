from typing import List


def get_position_id(x, y):
    return x * 1000 + y


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        door_set = set()
        INF = 2147483647
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    door_set.add((i, j))
        length = 0
        while len(door_set) != 0:
            temp_set = set()
            length += 1
            for position in door_set:
                x, y = position
                if x - 1 > 0 and rooms[x - 1][y] == INF:
                    rooms[x - 1][y] = length
                    temp_set.add((x - 1, y))
                if x + 1 < len(rooms) and rooms[x + 1][y] == INF:
                    rooms[x + 1][y] = length
                    temp_set.add((x + 1, y))
                if y - 1 > 0 and rooms[x][y - 1] == INF:
                    rooms[x][y - 1] = length
                    temp_set.add((x, y - 1))
                if y + 1 < len(rooms[0]) and rooms[x][y + 1] == INF:
                    rooms[x][y + 1] = length
                    temp_set.add((x, y + 1))
            door_set = temp_set
