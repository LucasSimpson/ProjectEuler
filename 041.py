def nPandigital (num_):
    num = str (num_)
    for a in num:
        if int (a) == 0 or int (a) > len (num):
            return False
    while (num != ''):
        for a in range (1, len (num)):
            if num [0] == num [a]:
                return False
        num = num [1:]
    return True

print nPandigital (1)
print nPandigital (123)
print nPandigital (124)
print nPandigital (154322)
print nPandigital (123456789)
