##CHECK SUDOKU
def check_sudoku(square):
    for row in square:
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True


________________________________________
##Factorials

def prod(a,b):
    return a*b
    
def fact_gen():
    i = 1
    n = 1
    while True:
        output = prod(n,i)
        yield output
        i += 1
        n = output


________________________________________
##Select the smallest_positive number
def smallest_positive(in_list):
    smallest_positive = None
    for num in in_list:
        if num > 0:
            if smallest_positive == None or smallest_positive > num:
                smallest_positive = num
    return smallest_positive




