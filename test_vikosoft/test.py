def calculate_water_amount(heights):
    n = len(heights)
    if n < 3:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    water_amount = 0
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    for i in range(1, n - 1):
        water_level = min(left_max[i], right_max[i])
        if water_level > heights[i]:
            water_amount += water_level - heights[i]
    return water_amount


if __name__ == "__main__":
    heights = input().split()
    int_heights = [int(i) for i in heights]
    water = calculate_water_amount(int_heights)
    print(water, "m^3")