# Move all zeros to the end while maintaining relative order of non-zero elements.
# This is a common problem that can be solved using a two-pointer technique.
# Time complexity: O(n), Space complexity: O(1) 

def move_zeroes(nums):
    # Two-pointer approach
    write_index = 0
    
    # Move all non-zero elements to the front
    for read_index in range(len(nums)):
        if nums[read_index] != 0:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    # Fill remaining positions with zeros
    while write_index < len(nums):
        nums[write_index] = 0
        write_index += 1

# What if we want to move all instances of a specific value? A: Generalize the two-pointer approach:
def move_element(nums, val):
    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    # Fill remaining with the value
    while write_index < len(nums):
        nums[write_index] = val
        write_index += 1

# What if we need to maintain relative order of both zero and non-zero elements? A: Use extra space or stable partitioning:
def move_zeroes_stable(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros = [x for x in nums if x == 0]
    return non_zeros + zeros

# Example usage:
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print("After moving zeroes:", nums)  # Output: After moving zeroes: [1, 3, 12, 0, 0]
    nums = [0, 0, 1]
    move_zeroes(nums)
    print("After moving zeroes:", nums)  # Output: After moving zeroes: [1, 0, 0]
    nums = [1, 2, 3]
    move_zeroes(nums)
    print("After moving zeroes:", nums)  # Output: After moving zeroes: [1, 2, 3]
    nums = [0, 0, 0, 0]
    move_zeroes(nums)
    print("After moving zeroes:", nums)  # Output: After moving zeroes: [0, 0, 0, 0]

    nums = [1, 2, 3, 4, 5]
    move_element(nums, 3)
    print("After moving element 3:", nums)  # Output: After moving element 3: [1, 2, 4, 5, 3]
    nums = [3, 3, 2, 1, 3]
    move_element(nums, 3)
    print("After moving element 3:", nums)  # Output: After moving element 3: [2, 1, 3, 3, 3]
    nums = [3, 2, 3, 1, 2, 3]
    move_element(nums, 2)
    print("After moving element 2:", nums)  # Output: After moving element 2: [3, 3, 1, 2, 2, 2

    nums = [1, 2, 3, 0, 0, 0]
    print("Stable move zeroes:", move_zeroes_stable(nums))  # Output: