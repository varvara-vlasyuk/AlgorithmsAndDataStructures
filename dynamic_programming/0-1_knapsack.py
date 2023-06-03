
# top-down w/o memorisation
def knapsack_tb(weights: list, values: list, av_space: int = 0, index: int = 0):
    if index >= len(weights) or av_space - weights[index] < 0:
        return 0
    include = values[index] + knapsack_tb(weights, values, av_space - weights[index], index + 1)
    exclude = knapsack_tb(weights, values, av_space, index + 1)
    return max(include, exclude)

# w/ memorisation
def knapsack_bu(weights: list, values: list, av_space: int):
    map_max = {len(weights): 0}
    for ind in range(len(weights)-1, -1, 0):
        if ind not in map_max[ind]:
            include = values[ind] + map_max[ind + 1]
            exclude = map_max[ind + 1]
            map_max = max(include, exclude)
        else:
            if map_max[ind] != map_max[ind + 1]:
                if av_space

weights = [50, 10, 11, 30, 10]
values = [80, 15, 5, 100, 10]
space = 65
print(knapsack_tb(weights, values, space))
