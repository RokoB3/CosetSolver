option = input("\nLeft(1) or Right(2) cosets? ")

orders = input("\nInput |G|, |H| and the max number in permutation (eg.: 24 6 4)\n").split(' ')
oG = int(orders[0])
oH = int(orders[1])
maxNum = int(orders[2])
G = []
G2 = []
H = []

print("""
/////////Input form/////////////\n
 Perm.      Program Input
(1 2 3)   : 1 2 3
(1 2)(3 4): 1 2,3 4
(Id)      : 1\n
////////////////////////////////""")


print("\nInput all elements of G seperated by new lines:")
for i in range(oG):
    G2.append(input())
    G.append(G2[-1].split(','))
    G[i] = [g.split(' ') for g in G[i]]
    for perm in range(len(G[i])):
        for element in range(len(G[i][perm])):
            G[i][perm][element] = int(G[i][perm][element])


print("\nInput all elements of H seperated by new lines:")
for i in range(oH):
    H.append(input().split(','))
    H[i] = [h.split(' ') for h in H[i]]
    for perm in range(len(H[i])):
        for element in range(len(H[i][perm])):
            H[i][perm][element] = int(H[i][perm][element])


def getIndex(perm, num):
    if num in perm:
        return perm.index(num)
    else: return None


# [full_permutation][permutation_index][element]
def multiply(g, h):
    perm = []
    for num in range(1, maxNum +1):
        index = None
        tran = None
        if num not in [z[0] for z in perm]:
            # Check h
            for p in range(len(h)):
                index = getIndex(h[p], num)
                if index != None:
                    if index == len(h[p]) -1:
                        tran = h[p][0]
                    else:
                        tran = h[p][index+1]
                    break
            
            # If in h check g
            if index != None:
                for p in range(len(g)):
                    index = getIndex(g[p], tran)
                    if index != None:
                        if index == len(g[p]) -1:
                            tran = g[p][0]
                        else:
                            tran = g[p][index+1]
                        break
                perm.append([num, tran])
            
            # If not in h check g
            else:
                for p in range(len(g)):
                    index = getIndex(g[p], num)
                    if index != None:
                        if index == len(g[p]) -1:
                            tran = g[p][0]
                        else:
                            tran = g[p][index+1]
                        break
            
                if index != None:
                    perm.append([num, tran])
    
    perm1 = []
    nums = []
    for num in range(1, maxNum +1):
        perm2 = []
        while num in [z[0] for z in perm] and num not in nums:
            perm2.append(num)
            nums.append(num)
            index = [x[0] for x in perm].index(num)
            num = perm[index][1]
        if len(perm2) > 1: perm1.append(perm2)
        if len(perm2) == 1 and ([1] not in perm1) and (perm1 == []): perm1.append([1])
    if [1] in perm1 and len(perm1) > 1: perm1.pop(0)
    return perm1


if option == '1':
    print('\n ~~~THE LEFT COSETS~~~')
    for i in range(len(G)):
        ls = []
        for j in range(len(H)):
            ls.append(multiply(G[i], H[j]))

        la = ls
        string = ''
        for a in range(len(la)):
            ls = la[a]
            true = True
            for cycle in range(len(ls)):
                for z in range(len(ls[cycle])):
                    ls[cycle][z] = str(ls[cycle][z])
                string += '(' + ''.join(ls[cycle]) + ')'

                if (ls[cycle] == 0): true = False
            if (a != len(la)-1) and (true == True): string += ', '

        print('(' + G2[i] + ') : {'+string+'}')

else:
    print('\n ~~~THE RIGHT COSETS~~~')
    for i in range(len(G)):
        ls = []
        for j in range(len(H)):
            ls.append(multiply(H[j], G[i]))

        la = ls
        string = ''
        for a in range(len(la)):
            ls = la[a]
            true = True
            for cycle in range(len(ls)):
                for z in range(len(ls[cycle])):
                    ls[cycle][z] = str(ls[cycle][z])
                string += '(' + ''.join(ls[cycle]) + ')'

                if (ls[cycle] == 0): true = False
            if (a != len(la)-1) and (true == True): string += ', '

        print('(' + G2[i] + ') : {'+string+'}')

