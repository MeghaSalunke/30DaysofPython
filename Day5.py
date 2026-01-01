# Day5- Challenge 5 Defining functions, parameters, return values, lambda functions
# Write a function that computes the sum and average of a list of numbers

def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average


# Example usage
nums = [10, 20, 30, 40]
result_sum, result_avg = sum_and_average(nums)

print("Sum:", result_sum)
print("Average:", result_avg)

