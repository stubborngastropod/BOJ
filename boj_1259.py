while True:
    try:
        n = str(input())
        if n == '0':
            break
        else:
            wrong = 0
            if len(n) == 1:
                print('yes')
            else:
                for i in range(len(n)//2):
                    if n[i] != n[-i-1]:
                        wrong += 1
                        break
                if wrong:
                    print('no')
                else:
                    print('yes')
    except:
        break