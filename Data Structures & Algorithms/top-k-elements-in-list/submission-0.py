class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele = list(set(nums))
        lst = []
        for each in ele:
            lst.append((each, nums.count(each)))
        
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        
        fn = []
        for i in range(k):
            fn.append(lst[i][0])
        return (fn)