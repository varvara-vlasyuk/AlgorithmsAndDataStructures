def binary_search(in_list: list, value) -> int:
    mid = int(len(in_list) / 2)
    beg = 0
    end = len(in_list) - 1
    while beg <= end:
        if value > in_list[mid]:
            beg = mid + 1
        elif value < in_list[mid]:
            end = mid - 1
        else:
            return mid
        mid = beg + int((end - beg) / 2)
    return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(lst, 1))
