
def double_eights(n):
    flag1 = False
    while(n != 0):
        m = n % 10
        n //= 10
        if m == 8:
            if flag1 == True:
                return True
            else:
                flag1 = True
    return False

print(double_eights(8))