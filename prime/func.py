def isp(num):
    isp = False
    if num == 2:
        return True
    if num > 1:
        for x in range(2,num):
            if num % x == 0:
                isp = False
                break
    return isp

print(isp(2))