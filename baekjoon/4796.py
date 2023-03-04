count = 1
while True:
    l,p,v = map(int,input().split())
    case = 0
    if l == 0 and p == 0 and v == 0:
        break
    else:
        while True:
            if v > p:
                v -= p
                case += l
            else:
                if v > l:
                    case += l
                    print(f'Case {count}: {case}')
                    break
                else:
                    case += v
                    print(f'Case {count}: {case}')
                    break
    count+=1