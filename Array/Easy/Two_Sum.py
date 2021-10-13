def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap=dict()
    for index,element in enumerate(nums):
        if(target-element in hashmap):
            return [index,hashmap[target-element]]
        else:
            hashmap[element]=index
        return []
