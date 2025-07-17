# Find two numbers in an array that add up to a target sum.
# Time complexity: O(n)
# Space complexity: O(n)


#What if the array is sorted? A: Use two pointers from both ends - O(n) time, O(1) space:

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# def two_sum_sorted(nums, target):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return [left, right]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return []


#What if we need all pairs that sum to target? A: Modify to collect all pairs and handle duplicates:

# def two_sum_all_pairs(nums, target):
#     seen = set()
#     result = []
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             result.append((min(num, complement), max(num, complement)))
#         seen.add(num)
#     return list(set(result))

# What about Three Sum? A: Sort array, then use Two Sum for each element:
# def three_sum(nums):
#     nums.sort()
#     result = []
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
#             continue
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#             if total == 0:
#                 result.append([nums[i], nums[left], nums[right]])
#                 # Skip duplicates
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#             elif total < 0:
#                 left += 1
#             else:
#                 right -= 1
#     return result

# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
# Output: Indices of the two numbers that add up to 9: [0, 1]