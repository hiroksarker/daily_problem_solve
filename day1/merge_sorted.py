# Merge two sorted arrays in-place into the first array.
# Time complexity: O(m + n)
# Space complexity: O(1)

def merge(nums1, m, nums2, n):
    # Start from the end of both arrays
    i = m - 1  # Last element in nums1
    j = n - 1  # Last element in nums2
    k = m + n - 1  # Last position in merged array
    
    # Merge from the back
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Copy remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# What if we have k sorted arrays to merge? A: Use min-heap:
import heapq

def merge_k_sorted(arrays):
    heap = []
    result = []
    
    # Initialize heap with first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    while heap:
        val, array_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same array
        if element_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, array_idx, element_idx + 1))
    
    return result

# Example usage:
if __name__ == "__main__":
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Merged k sorted arrays:", merge_k_sorted(arrays))  # Output: Merged k sorted arrays: [1, 1, 2, 3, 4, 4, 5, 6]


    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print("Merged array:", nums1)  # Output: Merged array: [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print("Merged array:", nums1)  # Output: Merged array: [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print("Merged array:", nums1)  # Output: Merged array: [1]