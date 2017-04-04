import copy

cols=['a','b','c','d','e','f','g','h']
array = []
arr = []
read_file = open("input.txt", "r")

to_win = list(read_file.readline())[0]
type(to_win)
print type(to_win)
if to_win == 'X':
    to_lose = 'O'
else:
    to_lose = 'X'
level=0
depth = int(list(read_file.readline())[0])
start = read_file.readlines()
for s in range(0, 8):
    start[s] = list(start[s])


next_move=[]

tester=[]
r=[]
queue=[]
def make_move(b,p1,p2,g, h):
    #print "called make_move"
    #print "Turning ct 1"
    #ct=1
    #print "make move, %s %s"%(p1,p2)
    temp = copy.deepcopy(b)
    #print "checking for below"
    if g!=7 and temp[g + 1][h] == p2:
        for x in range(g + 1, 8):
            if temp[x][h] == '*':
                break
            elif temp[x][h] == p2:
                continue
            elif temp[x][h] == p1:
                for u in range(g, x):
                    temp[u][h] = p1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp

    #print "checking for above"
    if g!=0 and temp[g - 1][h] == p2:
        for x in range(g - 1, 0, -1):
            # print "x %s" %x
            if temp[x][h] == '*':
                break
            elif temp[x][h] == p2:
                continue
            elif temp[x][h] == p1:
                # print temp[x][i]
                # print "place X there"
                for u in range(x, g + 1):
                    temp[u][h] = p1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp

    #print "Checking to the right"
    if h!=7 and temp[g][h + 1] == p2:
        for x in range(h + 1, 8):
            # print "x %s" %x
            if temp[g][x] == '*':
                break
            elif temp[g][x] == p2:
                continue
            elif temp[g][x] == p1:
                # print temp[x][i]
                # print "place X there"
                for u in range(h, x):
                    temp[g][u] = p1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp

    #print "Checking to the left"
    if h!=0 and temp[g][h - 1] == p2:
        for x in range(h - 1, 0, -1):
            # print "x %s" %x
            if temp[g][x] == '*':
                break
            elif temp[g][x] == p2:
                continue
            elif temp[g][x] == p1:
                # print temp[x][i]
                # print "place X there"
                for u in range(x, h + 1):
                    temp[g][u] = p1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp

    #print "Check right below"
    if g!=7 and h!=7 and temp[g + 1][h + 1] == p2:
        x = g
        y = h
        while (x < 7 and y < 7):
            x += 1
            y += 1
            if temp[x][y] == '*':
                break
            elif temp[x][y] == p2:
                continue
            elif temp[x][y] == p1:
                u = g
                v = h
                while (u < x and v < y):
                    temp[u][v] = p1
                    u += 1
                    v += 1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp


    #print "Check left above"
    if g!=0 and h!=0 and temp[g - 1][h - 1] == p2:
        x = g
        y = h
        while (x >= 0 and y >= 0):
            x -= 1
            y -= 1
            if temp[x][y] == '*':
                break
            elif temp[x][y] == p2:
                continue
            elif temp[x][y] == p1:
                u = x
                v = y
                while (u <= g and v <= h):
                    temp[u][v] = p1
                    u += 1
                    v += 1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp


    #print "Check left below"
    if g!=7 and h!=0 and temp[g + 1][h - 1] == p2:
        x = g
        y = h
        while x < 7 and y >=0:
            x += 1
            y -= 1
            if temp[x][y] == '*':
                break
            elif temp[x][y] == p2:
                continue
            elif temp[x][y] == p1:
                u = g
                v = h
                while (u < x and v > y):
                    temp[u][v] = p1
                    u += 1
                    v -= 1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp


    #print "Check right above"
    if g!=0 and h!=7 and temp[g - 1][h + 1] == p2:
        x = g
        y = h
        while (x >= 0 and y < 8):
            x -= 1
            y += 1
            if temp[x][y] == '*':
                break
            elif temp[x][y] == p2:
                "I saw O here"
                continue
            elif temp[x][y] == p1:
                u = g
                v = h
                while (u > x and v < y):
                    temp[u][v] = p1
                    "Making temp x here"
                    u -= 1
                    v += 1
                #for y in range(0, 8):
                    #print temp[y]
                #return temp

    return temp


def valid_move(board,player1,player2,array,pos):
    ct=0
    #print "Calling valid move"
    #print ct
    #print "valid move %s %s"%(player1, player2)

    for i in range(1, 7):
        for j in range(1, 7):
            if board[i][j] == player2:
                #print i,j
                if board[i - 1][j - 1] == '*':

                    #print "Bottom right"
                    x = i + 1
                    y = j + 1
                    while (x < 8 and y < 8):
                        if board[x][y] == '*':
                            break
                        elif board[x][y] == player2:
                            x += 1
                            y += 1
                            continue
                        elif board[x][y] == player1:
                            '''if level==1:
                                level1.append(make_move(board,player1,player2,i - 1, j - 1))
                            else:'''
                            if (cols[j - 1] + str(i)) in pos:
                                continue
                            else:
                                array.append(make_move(board, player1, player2, i - 1, j - 1))
                                ct = 1
                                pos.append(cols[j - 1] + str(i))
                                break

                        x += 1
                        y += 1


                if board[i - 1][j] == '*':
                    #print "Below"
                    for x in range(i + 1, 8):
                        if board[x][j] == '*':
                            break;
                        elif board[x][j] == player2:
                            continue;
                        elif board[x][j] == player1:
                            if (cols[j]+str(i)) in pos:
                                continue
                            else:
                                array.append(make_move(board,player1,player2,i - 1, j))
                                ct=1
                                pos.append(cols[j]+str(i))
                                break

                if board[i - 1][j + 1] == '*':
                    #print "Bottom left"
                    x = i+1
                    y = j-1
                    #print "Values of  %s %s" % (x, y)
                    while x < 8 and y >= 0:
                        #print "Hi"
                        if board[x][y] == '*':
                            #print "breaking for %s %s" %(x,y)
                            break
                        elif board[x][y] == player2:
                            x += 1
                            y -= 1
                            continue
                        elif board[x][y] == player1:
                            #print "making move"
                            '''if level==1:
                                level1.append( make_move(board,player1,player2,i - 1, j + 1))
                            else:'''
                            if (cols[j+1]+str(i)) not in pos:
                                array.append( make_move(board,player1,player2,i - 1, j + 1))
                                ct = 1
                                pos.append(cols[j+1]+str(i))
                                break

                        x += 1
                        y -= 1


                if board[i][j - 1] == '*':
                    #print "Right"
                    for x in range(j + 1, 8):
                        if board[i][x] == '*':
                            break
                        elif board[i][x] == player2:
                            continue
                        elif board[i][x] == player1:
                            if (cols[j-1]+str(i+1)) in pos:
                                continue
                            else:
                                array.append(make_move(board,player1,player2,i, j - 1))
                                ct=1
                                pos.append(cols[j-1]+str(i+1))
                                break


                if board[i][j + 1] == '*':
                    #print "Left"
                    for x in range(j - 1, 0, -1):
                        # print "x %s" %x
                        if board[i][x] == '*':
                            break
                        elif board[i][x] == player2:
                            continue
                        elif board[i][x] == player1:
                            '''if level==1:
                                level1.append(make_move(board,player1,player2,i, j + 1))
                            else:'''
                            if (cols[j+1]+str(i+1)) in pos:
                                continue
                            else:
                                array.append(make_move(board,player1,player2,i, j+1))
                                ct=1
                                pos.append(cols[j+1]+str(i+1))
                                break

                if board[i + 1][j - 1] == '*':
                    #print "Top right"
                    x = i-1
                    y = j+1
                    while (x >= 0 and y < 8):
                        if board[x][y] == '*':
                            break
                        elif board[x][y] == player2:
                            x -= 1
                            y += 1
                            continue
                        elif board[x][y] == player1:
                            '''if level==1:
                                level1.append( make_move(board,player1,player2,i + 1, j - 1))
                            else:'''
                            if (cols[j-1]+str(i+2)) in pos:
                                continue
                            else:
                                array.append( make_move(board,player1,player2,i + 1, j - 1))
                                ct = 1
                                pos.append(cols[j-1]+str(i+2))
                                break


                        x -= 1
                        y += 1


                if board[i + 1][j] == '*':
                    #print "Above"
                    for x in range(i - 1, 0, -1):
                        # print "x %s" %x
                        if board[x][j] == '*':
                            break;
                        elif board[x][j] == player2:
                            continue;
                        elif board[x][j] == player1:
                            '''if level==1:
                                level1.append(make_move(board,player1,player2,i + 1, j))
                            else:'''
                            if (cols[j]+str(i+2)) in pos:
                                continue
                            else:
                                array.append(make_move(board,player1,player2,i + 1, j))
                                ct = 1
                                pos.append(cols[j]+str(i+2))
                                break



                if board[i + 1][j + 1] == '*':
                    #print "Top left"
                    x = i-1
                    y = j-1
                    while (x >= 0 and y >= 0):
                        if board[x][y] == '*':
                            break
                        elif board[x][y] == player2:
                            x -= 1
                            y -= 1
                            continue
                        elif board[x][y] == player1:
                            if (cols[j+1]+str(i+2)) not in pos:
                                continue
                            else:
                                array.append(make_move(board,player1,player2,i + 1, j + 1))
                                ct = 1
                                pos.append(cols[j+1]+str(i+2))
                                break


                        x -= 1
                        y -= 1

    if (ct==0):
        #print "pass case %s"%ct
        array.append(board)
        pos.append("pass")


def evaluate(leaf):
    win=0
    lose=0
    total=0
    weights= [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8],
              [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6],
              [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8],
              [99, -8, 8, 6, 6, 8, -8, 99]]
    for i in range (0,8):
        for j in range(0,8):
            #print leaf[i][j]
            if leaf[i][j]==to_win:
                win=win+weights[i][j]
            elif leaf[i][j]==to_lose:
                lose=lose+weights[i][j]
    total=win-lose
    #print "total %s"%total
    return total

'''def terminal_test(state,position):
    if position[0]=="pass":
        counter=0
        for i in range(1, 7):
            for j in range(1, 7):
                if state[i][j] == '*':
                    continue
                elif state[i][j]==to_win:
                    for x in range (i,7):
                        for y in range(j,7):
                            if state[x][y]==to_lose:
                                counter=1
                                break
                elif state[i][j]==to_lose:
                     for x in range (i,7):
                         for y in range(j,7):
                             if state[x][y]==to_win:
                                 counter=1
                                 break

        if(counter==0):
             print "Returning true"
             return True
        else:
            return False'''


def max_value(state,position, alpha,beta,level,play1,play2,terminal_test):
    if level==depth or terminal_test==2:
        queue.append("%s,"%position+"%s," % level + "%s," % change(evaluate(state)) + "%s," % change(alpha) + "%s" % change(beta))
        print "Max leaf     %s,"%position+"%s," % level + "%s," % evaluate(state) + "%s," % alpha + "%s" % beta
        return evaluate(state)

    v=float("-inf")
    successor=[]

    p=[]
    queue.append("%s," % position + "%s," % level + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
    print "max before v     %s," % position + "%s," % level + "%s," % v + "%s," % alpha + "%s" % beta

    t = play1
    play1 = play2
    play2 = t
    level += 1
    '''if (terminal_test == True):
        queue.append(
            "%s," % position + "%s," % level + "%s," % change(evaluate(state)) + "%s," % change(alpha) + "%s" % change(
                beta))
        print "Max leaf     %s," % position + "%s," % level + "%s," % evaluate(state) + "%s," % alpha + "%s" % beta'''
        #return evaluate(state)
    valid_move(state, play1, play2, successor,p)

    if p[0]=="pass":
        if terminal_test==1:
            terminal_test=2
        else:
            terminal_test=1
    else:
        terminal_test=0
        '''print "CHECKING %s" % p[0]
        valid_move(successor[0], play2, play1, tester,r)

        if r[0]=="pass":
            "SETTIG TERMINAL TEST CASE TO TRUE"
            terminal_test=True'''
    print "successor %s" % p

    global next_move
    for s in range (0,len(successor)):

        #print min_value(successor[s],p[s],alpha,beta,level,play1,play2)
        check=min_value(successor[s], p[s], alpha, beta, level, play1, play2,terminal_test)
        if check > v:
            v = check
            #print "Changing v %s"%v
            if (level==1):
                #print "Changing next move"
                next_move=successor[s]


        #v=max(v,max(value))
        #print "v%s"%v



        if v>=beta:
            queue.append("%s," % position + "%s," % (level-1) + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
            print "Max after v   1.   %s," % position + "%s," % (level-1) + "%s," % v + "%s," % alpha + "%s" % beta
            return v
        alpha = max(alpha, v)
        # print "aplha %s"%alpha
        # queue.append("%s," % position + "%s," % (level - 1) + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
        print "max after v   2.  %s," % position + "%s," % (level - 1) + "%s," % v + "%s," % alpha + "%s" % beta
        queue.append("%s," % position + "%s," % (level - 1) + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))


    return v


def change(para):
    if para==float("-inf"):
        return "-Infinity"
    elif para==float("inf"):
        return "Infinity"
    else:
        return para


def min_value(state,position,alpha,beta,level,play1,play2,terminal_test):
    if level==depth or terminal_test==2:
        queue.append("%s," %position+"%s,"% level + "%s," % change(evaluate(state)) + "%s," % change(alpha) + "%s" % change(beta))
        print "Min leaf    %s," %position+"%s,"% level + "%s," % evaluate(state) + "%s," % alpha + "%s" % beta
        return evaluate(state)


    v = float("inf")
    successor = []
    p=[]
    queue.append("%s," % position + "%s," % level + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
    print "Min before v     %s," % position + "%s," % level + "%s," % v + "%s," % alpha + "%s" % beta

    t = play1
    play1 = play2
    play2 = t
    level += 1
    '''if (terminal_test == True):
        queue.append("%s," % position + "%s," % level + "%s," % change(evaluate(state)) + "%s," % change(alpha) + "%s" % change(beta))
        print "Min leaf    %s," % position + "%s," % level + "%s," % evaluate(state) + "%s," % alpha + "%s" % beta'''
        #return evaluate(state)
    valid_move(state, play1, play2, successor,p)
    if p[0]=="pass":
        if terminal_test==1:
            terminal_test=2
        else:
            terminal_test=1
    else:
        terminal_test=0
    '''if p[0]=="pass":
        valid_move(successor[0], play2, play1, tester,r)
        if r[0]=="pass":
            "SETTING TERMINAL TEST TO TRUE"
            terminal_test=True'''
    #print p
    for s in range(0,len(successor)):

        v = min(v, max_value(successor[s], p[s],alpha, beta,level,play1,play2,terminal_test))



        if v<=alpha:
            queue.append("%s," % position + "%s," % (level-1) + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
            print "Min after v 1.     %s," % position + "%s," % (level-1) + "%s," % v + "%s," % alpha + "%s" % beta
            return v

        beta = min(beta, v)
        # queue.append("%s," % position + "%s," % (level - 1) + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
        print "Min after v  2.    %s," % position + "%s," % (level - 1) + "%s," % v + "%s," % alpha + "%s" % beta
        queue.append("%s," % position + "%s," % (level - 1) + "%s," % change(v) + "%s," % change(alpha) + "%s" % change(beta))
    return v




def alpha_beta_search(state,level,play1,play2):
    v=max_value(state,"root",float("-inf"),float("inf"),level,play2,play1,0)
    #print "next move"
    #printing in output file
    f = open("output.txt", "w")
    for n in next_move:
        f.write(''.join(n))
    f.write("\n"+"Node,Depth,Value,Alpha,Beta"+"\n")
    for q in queue:
        f.write(q + "\n")

    f.close()

    #for q in next_move:
        #print ''.join(q)








'''def tree(arr,level,play1,play2):
    while level <= depth:
        print "in while"
        t = play1
        play1 = play2
        play2 = t
        level += 1
        if (level>depth):
            break
        print "level %s %s %s" % (level, play1, play2)
        for n in arr:
            print "length of arr %s" %arr.index(n)
            children = []
            print " calling valid move from children %s " %len(children)
            valid_move(n, play1, play2, children)
            for s in children:
                print "printing from children %s"%s
            #level += 1
            tree(children,level,play1,play2)


    else:
        print "returning"
        return'''



'''valid_move(start,to_win,to_lose,level1)
for s in level1:
    print s
tree(level1,1,to_win,to_lose)'''

#print "root,%s," %level +"%s,"%ninf+"%s,"%ninf+"%s"%pinf
alpha_beta_search(start,0,to_win,to_lose)