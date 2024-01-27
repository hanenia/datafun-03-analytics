""" Query to calculate statistical values fro a set of input numbers by Hanna """

import statistics

import statistics

# Input the numbers
numbers = [5, 8, 10, 11, 12]

# Calculate the mean
mean = statistics.mean(numbers)
print(f"The mean is {mean:.2f}")

# Calculate the standard deviation
std_dev = statistics.stdev(numbers)
print(f"The standard deviation is {std_dev:.2f}")

# Calculate the median
median = statistics.median(numbers)
print(f"The median is {median:.2f}")

# Calculate the minimum and maximum
minimum = min(numbers)
maximum = max(numbers)
print(f"The minimum is {minimum:.2f}")
print(f"The maximum is {maximum:.2f}")