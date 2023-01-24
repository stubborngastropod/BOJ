while True:
    try:
        n = int(input())
        icount = 1
        while 1:
            if int('1'*icount) % n == 0:
                print(icount)
                break
            else:
                icount += 1
                continue
    except:
        break