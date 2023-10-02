
# PROBLEM STATEMENT:
#   EACH NUMBRT ON THE LIST HAS A SPECFIC COLOT OF THE SOCK
#   FIND HOW MANY PAIR ARE IN THE SAME COLOR
#

SOCKS = [1,2,2,1,1,3,5,1,4,4]
socks_repo = {}

for item in SOCKS:
    if item in socks_repo:
        socks_repo[item] +=1
    else:
        socks_repo[item] = 1

final = {}

for key,value in socks_repo.items():
    if value % 2 == 0:
        final[key] = int(value / 2)

for key,value in final.items():
    print(" color {} has {} pair of socks".format(key,value))
