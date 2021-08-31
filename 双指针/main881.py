from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        result = 0
        while start <= end:
            if people[end] + people[start] <= limit:
                result += 1
                end -= 1
                start += 1
                continue
            else:
                result += 1
                end -= 1
                continue
        return result


if __name__ == '__main__':
    print(Solution().numRescueBoats(people = [3,5,3,4], limit = 5))
