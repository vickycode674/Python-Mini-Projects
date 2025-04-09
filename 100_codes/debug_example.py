def add_numbers(a, b):
    result = a + b  # ❌ Bug: should be a + b
    return result

x = 5
y = 3
sum_result = add_numbers(x, y)

print("Sum is:", sum_result)
