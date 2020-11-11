def adjacent_element_product(array):
    return max(list(i * j for i, j in zip(array, array[1:])))
