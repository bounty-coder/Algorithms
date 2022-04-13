# Search an element in a sorted and rotated array with duplicates

# Input: arr[] = {3, 3, 3, 1, 2, 3}, key = 3 
# Output: 0 
# arr[0] = 3

# The idea is the same as the without duplicates. The only
# difference is that due to the existence of duplicates, arr[low] == arr[mid]
# could be possible, the first half could be out of order 
# and we have to deal this case separately. 
# In that case, it is guaranteed that arr[high] also equal to arr[mid], so the
# condition arr[mid] == arr[low] == arr[high] can be checked before the original logic,
# and if so then move left and right both towards the middle by 1 and repeat.

def search(nums, target):
    left, mid, right = 0, 0, len(nums) - 1
    def moveRight(): return mid + 1, right
    def moveLeft(): return left, mid - 1
    while left <= right:
        mid = (left + right) // 2
        curr = nums[mid]
        if curr == target:
            return True
        if left == right:
            return nums[left] == target
        if nums[left] < nums[right]:
            left, right = moveRight() if curr < target else moveLeft()
        elif nums[left] > nums[right]:
            if curr >= nums[left]:
                if curr < target:
                    left, right = moveRight()
                else:
                    left, right = moveRight() if target < nums[left] else moveLeft()
            else:
                if curr < target:
                    left, right = moveRight() if nums[right] >= target else moveLeft()
                else:
                    left, right = moveLeft()
        else:
            left += 1
    return False