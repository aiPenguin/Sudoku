
su_can=[[]]*81


def trav_select(su):

    for n in range(0,3):
        for i in range(len(su)):
            row=i//9
            col=i%9
            if su[i] != 0:
                for j in range(0,9):
                    if n==0:
                        pos=row*9+j
                    elif n==1:
                        pos=j*9+col
                    elif n==2:
                        r=row//3
                        c=col//3
                        k=j%3
                        l=j//3
                        pos=r*9*3+c*3+l*9+k
                    if su[i] in su_can[pos]:
                        if len(su_can[pos])>1:
                            su_can[pos].remove(su[i])
                        elif len(su_can[pos])==1 and pos != i:
                            su[pos]=su_can[pos]
                            if n==0:
                                raise Exception('Row %d has repeated numbers.'
                                                %(row+1))
                            elif n==1:
                                raise Exception('Colum %d has repeated numbers.'
                                                %(col+1))
                            elif n==2:
                                raise Exception('Block %d has repeated numbers.'
                                                %(r*3+c+1))                        
            else:
                if len(su_can[i])==1:
                    su[i]=su_can[i][0]


def unique_check(su):

    for n in range(0,3):
        for i in range(len(su)):
            row=i//9
            col=i%9
            flag=False
            if su[i] == 0:
                for num in su_can[i]:
                    for j in range(0,9):
                        if n==0:
                            pos=row*9+j
                        elif n==1:
                            pos=j*9+col
                        elif n==2:
                            r=row//3
                            c=col//3
                            k=j%3
                            l=j//3
                            pos=r*9*3+c*3+l*9+k
                        if num in su_can[pos] and pos != i:
                            break
                        elif j==8:
                            su_can[i]=[num]
                            su[i]=num
                            flag=True
                    if flag==True:
                        break


def su_can_setup(su):

    for i in range(len(su)):
        if su[i] == 0:
            su_can[i]=list(range(1,10))
        else:
            su_can[i]=[su[i]]

def print_su(su):

    for i in range(len(su)):
        print (su[i],end=' ')
        if i%9==8:
            print()
        elif i%3==2:
            print('|',end=' ')
        if i%27==26 and i != 80:
            print('------+-------+------')


def solve_su(su):

    su_can_setup(su)
    while True:
        su_l=su[:]
        try:
            trav_select(su)
            unique_check(su)
        except Exception as e:
            print(e)
            print_su(su)
            break
        if 0 not in su:
            print('Done')
            print_su(su)
            break
        elif su_l==su:
            print ('No solution or multi solutions')
            print_su(su)
            break


if __name__ == '__main__':
    sudoku1 = [
        0, 8, 2, 0, 9, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 5,
        0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 3, 2, 0,
        7, 0, 0, 5, 0, 6, 0, 0, 0,
        0, 0, 0, 7, 0, 0, 0, 0, 0,
        0, 3, 0, 9, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 2, 0, 0, 8, 0,
        5, 0, 0, 0, 0, 0, 0, 0, 6
    ]

    sudoku2 = [
        0, 0, 0, 0, 0, 0, 8, 0, 0,
        4, 0, 0, 2, 0, 8, 0, 5, 1,
        0, 8, 3, 9, 0, 0, 0, 0, 7,
        0, 4, 0, 5, 0, 0, 0, 8, 2,
        0, 0, 5, 0, 0, 0, 4, 0, 0,
        8, 7, 0, 0, 0, 9, 0, 3, 0,
        2, 0, 0, 0, 0, 7, 1, 6, 0,
        3, 6, 0, 1, 0, 5, 0, 0, 4,
        0, 0, 4, 0, 0, 0, 0, 0, 0
    ]

    sudoku3 = [
        0, 9, 0, 1, 0, 0, 3, 7, 8,
        0, 0, 0, 7, 0, 9, 0, 0, 0,
        0, 1, 0, 4, 0, 8, 0, 0, 6,
        0, 0, 0, 2, 0, 0, 6, 5, 9,
        0, 0, 0, 0, 4, 3, 0, 0, 0,
        0, 5, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 2, 3, 5, 1, 7, 0, 0,
        0, 6, 0, 8, 9, 0, 5, 0, 2,
        0, 0, 0, 0, 0, 2, 8, 0, 0
    ]
    
    su = sudoku1
    print_su(su)
    solve_su(su)
