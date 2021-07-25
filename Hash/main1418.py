import collections
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_dict = {}
        dish_set = set()
        for o in orders:
            dish_set.add(o[2])
            if o[1] in table_dict.keys():
                table_dict[o[1]][o[2]] += 1
            else:
                table_dict[o[1]] = collections.defaultdict(int)
                table_dict[o[1]][o[2]] += 1
        dish_list = list(dish_set)
        dish_list.sort()
        result = [["Table"] + dish_list]
        keys = list(table_dict.keys())
        keys.sort(key=lambda x: int(x))
        for k in keys:
            line = [k]
            table_line = table_dict[k]
            for d in dish_list:
                line.append(str(table_line[d]))
            result.append(line)
        return result


if __name__ == '__main__':
    print(Solution().displayTable(
        orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    ))
