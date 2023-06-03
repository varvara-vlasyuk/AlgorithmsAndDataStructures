# Question 1: find the missing number in array from 1 to 100
def find_missing():
    arr = []
    for i in range(1, 101):
        arr.append(i)

    arr.remove(73)
    # sum of arithmetic sequence with step 1 starting w 1 = n(n+1)/2
    sum_of_100 = 100 * 101 / 2
    sum_of_arr = sum(arr)
    print(f'missing element {sum_of_100 - sum_of_arr}')


# Question 2: find pairs of indexes of an array sum of which equals target value
def find_pairs():  # linear solution, O(n^2)
    arr = [5, 4, 8, 11, 3, 1, 4]
    target = 9
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if target - arr[i] == arr[j]:
                result.append([i, j])

    print(result)


# Question 3: check if array contains a value
def search_element():
    arr = [1, 3, 4, 5, 7]
    target = 3
    for elem in arr:
        if elem == target:
            print('exists')


# Question 4: find a max product of 2 int elements of an integer array
def find_max_product():
    arr = [2, 10, 4, 5, 7, 20]
    max_product = 0
    pair = tuple()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if max_product < product:
                max_product = product
                pair = (i, j)

    print(f'{pair} , {max_product}')


# Question 5: check if the list contains only unique elements
def if_unique():
    arr = [2, 20, 4, 5, 7, 20]
    is_unique = True
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                is_unique = False
                break

    print(f'Is unique? - {is_unique}')


# Question 6: check if two lists contain the same elements
def if_permutation():
    list1 = 'h e l l o'.split()
    list2 = 'o l l e h'.split()
    if len(list1) != len(list2):
        print('False')
    else:
        list1.sort()
        list2.sort()

        if list2 == list1:
            print('True')
        else:
            print('False')


# Question 7: write a method to rotate nxn sized matrix to 90 degrees
def rotate_matrix():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
              ]

    rotated = []
    n = len(matrix) - 1
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix)):
            print(f'{i},{j} -> {n-j},{i}')
            print(matrix[n-j][i])
            new_row.append(matrix[n-j][i])
        rotated.append(new_row)

    print(rotated)


def firstSecond(givenList):
    first = givenList[0]
    second = givenList[0]
    for i in range(1, len(givenList)):
        if givenList[i] > first:
            first = givenList[i]
            second = first
        elif givenList[i] > second:
            second = givenList[i]

    print(f'first={first},second={second}')

    # return first, second
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList)
# Question 4: find a max product of 2 int elements of an integer array
# Question 4: find a max product of 2 int elements of an integer array
# Question 4: find a max product of 2 int elements of an integer array
