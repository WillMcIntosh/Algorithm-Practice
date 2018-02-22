def factorialize(_num):
    if _num == 0:
        return 1
    else:
        return _num * factorialize(_num - 1)

print(factorialize(40)%10**9)
