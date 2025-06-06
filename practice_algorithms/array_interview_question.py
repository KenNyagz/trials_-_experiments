arr = [1,3,5,6,9,34,56,67,68,69,70,73,74,78,80,86,88]


def find_num_in_array(num):
    '''Finding number in an array'''
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False

#print(find_num_in_array(73))

def iterate_find_num(start, end, num):
    '''Finding number in array'''
    while True:
        if num >= arr[len(arr) // 2]:
            if num == arr[len(arr) // 2]:
                return True
            iterate_find_num(len(arr) // 2, len(arr) - 1, num)
        elif num < arr[len(arr) // 2]:
            iterate_find_num(0, len(arr) - 1, num)
    return False
        
#print(find_num_in_array(88))

def find_combination(input):
    '''Finding the first two numbers that sum up to the input given'''
    for i in range(len(arr)):
        for j in range(i+ 1, len(arr)):
            if arr[i] + arr[j] == input:
                return [arr[i], arr[j]]
    else:
        return -1

print(find_combination(143))