## Brute Force - Nested Iterations
def container_with_most_water_1(height):
    """
    TC: O(n^2)
    AS: O(1)
    """
    n = len(height)

    maxArr = float('-inf')

    for i in range(0, n):
        for j in range(i+1, n):
            width_each_iteration = j - i
            height_each_iteration = min(height[i], height[j])
    
            currArea = width_each_iteration * height_each_iteration
            maxArr = max(currArea, maxArr)

    return maxArr

height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water_1(height))

## Two Pointers
def container_with_most_water_2(height):
    '''
    TC: O(n)
    As: O(1)
    '''
    n = len(height)
    low = 0
    high = n-1
    maxArr = float("-inf")

    while low < high:
        diff_width = high - low
        height_each_iteration = min(height[low], height[high])
        currArr = diff_width * height_each_iteration
        maxArr = max(currArr, maxArr)

        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    
    return maxArr

                    
height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water_2(height))
