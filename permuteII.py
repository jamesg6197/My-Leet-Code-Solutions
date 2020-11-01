def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        for idx in range(len(nums)):
            numsleft = nums[:idx] + nums[idx+1:]
            for num in self.permuteUnique(numsleft):
                if ([nums[idx]] + num) not in perms:
                    perms.append([nums[idx]] + num)

        return perms
