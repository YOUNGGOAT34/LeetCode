class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups=[]
        num_to_group={}

        for n in sorted(nums):
           if not groups or abs(groups[-1][-1]-n)>limit:
              groups.append(deque())



           groups[-1].append(n)
           num_to_group[n]=len(groups)-1


        res=[]

        for n in nums:
            index=num_to_group[n]
            res.append(groups[index].popleft())
           

        return res
        