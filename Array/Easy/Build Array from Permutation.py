def buildArray(self, nums: List[int]) -> List[int]:
    # nums[i]=qn+b//n
    n=len(nums)
    for i in range(len(nums)):
        b=nums[i]
        q=nums[nums[i]]%n
        nums[i]=q*n+b
        
    for i in range(len(nums)):
        nums[i]=nums[i]//n

    return nums            
            
