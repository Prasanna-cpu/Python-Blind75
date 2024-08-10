def MaxArea(height):
    l = 0
    r = len(height) - 1

    max_area = float("-inf")

    while l < r:
        area = min(height[l], height[r]) * abs(l - r)

        max_area = max(area, max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


print(MaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
