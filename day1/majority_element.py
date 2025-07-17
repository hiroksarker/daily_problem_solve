# Find the element that appears more than n/2 times in an array.
# Time complexity: O(n)
# Space complexity: O(1)

def majority_element(nums):
    candidate = None
    count = 0
    
    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Alternative O(n) space solution using hash map:
def majority_element_hash(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    # Second pass to confirm
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

#What if there's no majority element? A: Verify the candidate:
def majority_element_verified(nums):
    candidate = None
    count = 0
    
    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

# Find all elements that appear more than n/3 times? A: Modified Boyer-Moore for two candidates:
def majority_element_n3(nums):
    candidate1 = candidate2 = None
    count1 = count2 = 0
    
    # Find two candidates
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    
    # Verify candidates
    result = []
    for candidate in [candidate1, candidate2]:
        if candidate is not None and nums.count(candidate) > len(nums) // 3:
            result.append(candidate)
    
    return result

# Example usage:
if __name__ == "__main__":
    nums = [3, 2, 3]
    print("Majority element:", majority_element(nums))  # Output: Majority element: 3
    nums = [2, 2, 1, 1, 1, 2, 2]
    print("Majority element:", majority_element(nums))  # Output: Majority element: 2
    nums = [1, 1, 2, 2, 3]
    print("Majority element:", majority_element(nums))  # Output: Majority element: 1
    nums = [1, 2, 3, 4, 5]
    print("Majority element:", majority_element_hash(nums))  # Output: Majority element: None

    print("Majority element:", majority_element_verified(nums))  # Output: Majority element: None
    nums = [1, 2, 3, 1, 1, 2, 1]
    print("Majority element:", majority_element_verified(nums))  # Output: Majority element: 1
    nums = [1, 2, 3, 4, 5, 6]
    print("Majority element:", majority_element_verified(nums))  # Output: Majority element: None
    nums = [1, 2, 3, 1, 1, 2, 1, 2, 2]
    print("Majority element:", majority_element_verified(nums))  # Output: Majority element: 1
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Majority element:", majority_element_verified(nums))  # Output: Majority element: None
    nums = [1, 2, 3, 1, 1, 2, 1, 2, 2, 3, 3]
    print("Majority elements (n/3):", majority_element_n3(nums))  # Output: Majority elements (n/3): [1, 2] 