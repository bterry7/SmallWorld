def smallWorld(monsters,curMon):
    i = 0
    n = 0
    matches = []    
    maxcounter = len(monsters)
    while (i < maxcounter):
        # print(curMon)
        test = []
        while(n<5):
            # print(n)
            # print(stats[i][n+1])
            if monsters[i][n+1] == curMon[n+1]:
                test.append(1)
            else:
                test.append(0)
            n+=1
        n = 0
        if sum(test) == 1:
            matches.append(i)
        i+=1
    return matches