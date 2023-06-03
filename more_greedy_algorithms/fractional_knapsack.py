"""
Given  set of items, each with a weight and a value. Determine the number of each item to include in a collection
so that the total weight is less than or equal to a given limit and the total value is as large as possible.
"""

weights = [40, 30, 1, 25]
values = [130, 29, 111, 3]
knapsack_limit = 87

item_values = []
for i in range(0, len(weights)):
    item_values.append(((values[i] / weights[i]), i))       # tuple item value, index

total_value = 0
items_used = []
item_values.sort(key=(lambda x: x[0]),reverse=True)
print(item_values)
for item_val in item_values:
    item_ind = item_val[1]
    if knapsack_limit - weights[item_ind] > 0:
        knapsack_limit -= weights[item_ind]
        total_value += values[item_ind]
        items_used.append(weights[item_ind])
    else:
        part = weights[item_ind] - knapsack_limit
        total_value += part * item_val[0]
        items_used.append(weights[item_ind])
        break

print(total_value)
print(items_used)
