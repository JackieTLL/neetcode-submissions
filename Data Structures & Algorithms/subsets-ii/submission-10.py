class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subSets(nums):
            if nums == []:
                return [[]]
            first = nums[0]
            other = nums[1:]
            tempSet = subSets(other)
            return sorted([[first] + subList for subList in tempSet] + tempSet)
        subsetsWithoutDup = subSets(nums)
        print(subsetsWithoutDup)
        setSet = []
        for subset in subsetsWithoutDup:
            subset = sorted(subset)
            if subset not in setSet:
                setSet.append(subset)
            continue
        return list(setSet)