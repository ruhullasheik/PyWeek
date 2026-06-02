"""Example 4: Slicing Deep Dive

Master slicing with this demo.
"""

lst = list(range(10))
print(f"Original: {lst}")
print(f"lst[2:5]     = {lst[2:5]}")
print(f"lst[:4]      = {lst[:4]}")
print(f"lst[6:]      = {lst[6:]}")
print(f"lst[-3:]     = {lst[-3:]}")
print(f"lst[::2]     = {lst[::2]}")
print(f"lst[1::2]    = {lst[1::2]}")
print(f"lst[::-1]    = {lst[::-1]}")
print(f"lst[5:2:-1]  = {lst[5:2:-1]}")

# Slice assignment (modifying part of a list)
nums = [1, 2, 3, 4, 5]
nums[1:4] = [99, 100]
print(f"\nSlice assign: {nums}")
