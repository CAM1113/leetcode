class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        max_num = arr[1] - arr[0]
        max_list = [[arr[0],arr[1]]]
        for i in range(1,len(arr)-1):
            if arr[i+1] - arr[i] == max_num:
                max_list.append([arr[i],arr[i+1]])
            elif arr[i+1] - arr[i] < max_num:
                max_num = arr[i+1] - arr[i]
                max_list = [[arr[i],arr[i+1]]]
        return max_list