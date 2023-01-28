classes = []
winners = []
winner = ['', '', '', 0, 0]

def winnerFunc(line, winners):
    lineSum = int(line[3]) + int(line[4])
    winnerSum = winner[3] + winner[4]
    #print(lineSum)
    #print(winnerSum)
    if lineSum > winnerSum:
        winner[0] = line[0]
        winner[1] = line[1]
        winner[2] = line[2]
        winner[3] = int(line[3])
        winner[4] = int(line[4])
    if lineSum == winnerSum:
        winners.append(line)
    return (winner, winners)

f = open('mat_dv.txt', 'r')
for i in f:
    line = i.split()
    #print(line)
    if line[2] == '8':
        winnerFunc(line, winners)
winners.append(winner)
print(winners)
