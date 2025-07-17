# Given a sorted array, return a new array with squares of elements, also sorted.
# Time complexity: O(n)
# Space complexity: O(n)

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1
    
    return result

# What if array is not sorted? A: Sort after squaring - O(n log n):
def squares_unsorted(nums):
    return sorted([x * x for x in nums])

# Example usage:
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print("Sorted squares:", sorted_squares(nums))  # Output: Sorted squares: [0, 1, 9, 16, 100]
    nums = [-7, -3, 2, 3, 11]
    print("Sorted squares:", sorted_squares(nums))  # Output: Sorted squares: [4, 9, 9, 49, 121]
    nums = [-2, -1, 0, 1, 2]
    print("Sorted squares:", sorted_squares(nums))  # Output: Sorted squares: [0, 1, 1, 4, 4]
    nums = [0, 1, 2, 3, 4]
    print("Sorted squares:", sorted_squares(nums))  # Output: Sorted squares: [0, 1, 4, 9, 16]
    nums = [-5, -4, -3, -2, -1]
    print("Sorted squares:", sorted_squares(nums))  # Output: Sorted squares: [1, 4, 9, 16, 25]

    nums = [1, 2, 3, 4, 5]
    print("Unsorted squares:", squares_unsorted(nums))  # Output: Unsorted squares: [1, 4, 9, 16, 25]
    nums = [-3, -2, -1, 0, 1, 2, 3]
    print("Unsorted squares:", squares_unsorted(nums))  # Output: Unsorted squares: [0, 1, 1, 4, 4, 9, 9]
    nums = [0, 0, 0, 0]
    print("Unsorted squares:", squares_unsorted(nums))  # Output: Unsorted squares: [0, 0, 0, 0]