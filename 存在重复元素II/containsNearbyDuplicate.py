from typing import List, Mapping


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping.keys():
                mapping[nums[i]] = [i]
            else:
                mapping[nums[i]].append(i)
        for m,v in mapping.items():
            if len(v) > 1:
                for i in range(len(v)):
                    for j in range(i+1,len(v)):
                        if abs(v[j]-v[i]) <= k:
                            return True
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping.keys():
                mapping[nums[i]] = [i]
            else:
                if abs(i - mapping[nums[i]][-1]) <= k:
                    return True
                else:
                    mapping[nums[i]].append(i)
        return False

s = Solution()
nums = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate2(nums,k))