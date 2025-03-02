from typing import List

#merge sort
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l1=len(nums1)
        l2=len(nums2)

        i=0
        j=0

        res=[]

        while i<l1 and j<l2:
            if nums1[i][0]<nums2[j][0]:
                res.append(nums1[i])
                i+=1

            elif nums1[i][0]>nums2[j][0]:
                res.append(nums2[j])
                j+=1

            else :
                res.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                j+=1
                i+=1

        while i<l1:
            res.append(nums1[i])
            i+=1

        while j<l2:
            res.append(nums2[j])
            j+=1



        return res

        