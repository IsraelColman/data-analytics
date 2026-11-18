# Israel Colman
# 11/17/2026

import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# Experimenting with a subset of integers 1-100
sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

print('\n----- Statistics of vals_sample -----')
print(f'Sum of 75 values from 1-100: {sample_sum}')
print(f'Average of 75 sample values: {sample_avg:.2f}')
print(f'Median of 75 sample values: {sample_median}')
print('-' * 37)


# Experimenting with a superset of 200 values, integers 1-100
choices_avg = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

print('\n----- Statistics of vals_choices -----')
print(f'Average of 200 values: {choices_avg:.2f}')
print(f'Median of 200 values: {choices_median}')
print(f'Mode of 200 values: {choices_mode}')
print(f'Standard Deviation of 200 values: {choices_stdev:.2f}')
print(f'Variance of 200 values: {choices_variance:.2f}')
print('-' * 39)


# Modeling a random circle
area = pi * radius ** 2

print('\n----- Calculating Radius -----')
print(f"Radius = {radius}, area = {math.ceil(area)} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {math.floor(area)} (rounded down to the nearest integer)")
print('-' * 30)