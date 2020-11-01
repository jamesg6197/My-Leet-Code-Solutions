def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutionset = set()
        for i in range(len(nums) - 1):
            if nums[i] != nums[i-1] or i == 0:
                other = nums[i+1:]
                self.twoSum(other, -nums[i], solutionset)
        return solutionset
    def twoSum(self, jnums: List[int], target: int, solutionset) -> List[int]:
        mydict = {}      
        for idx, val in enumerate(jnums):
            zother = target - val
            if zother in mydict:
                solutionset.add(tuple(sorted(([val, -target, zother]))))
                
            mydict[val] = idx
