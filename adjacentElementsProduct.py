def adjacentElementsProduct(*nums):
    largest = nums[0] * nums[1];

    for i in range(1, len(nums) - 1):
        product = nums[i] * nums[i + 1];

        if product > largest: largest = product;

    return largest;

print(adjacentElementsProduct(3, 6, -2, -5, 7, 3))
