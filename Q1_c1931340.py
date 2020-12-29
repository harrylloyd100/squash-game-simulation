import csv
import matplotlib.pyplot as plt
import random

def game(ra, rb):
    p = (ra) / (ra +rb)
    scoreA = 0
    scoreB = 0
    while True:
        if (scoreA >= 11 or scoreB >= 11) and (scoreA - scoreB >= 2 or scoreB - scoreA >= 2):
            break
        else:
            r = random.random()
            if r < p:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
    return scoreA,scoreB

def winProb(ra, rb, n):
    aW=0
    bW=0
    for i in range(n):
        games = game(ra, rb)
        if games[0] > games[1]:
            aW += 1
        else:
            bW += 1
    return round(aW/n,2)


def data():
        list = []
        with open('test.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader ,None)
            for row in reader:
                list.append(eval("(" + row[0] + "," + row[1] + ")"))
            skills = list
        return skills

def plot(o):
    ra,rb = 0,0
    ploter, ok = [], []
    for tries in o:
        ra, rb = tries[0], tries[1]
        reso1 = int(ra)/int(rb)
        reso =  winProb(int(ra),int(rb), 100000)
        ploter.append(reso)
        ok.append(reso1)
    plt.plot(ok, ploter)
    plt.ylabel('Probability')
    plt.xlabel('rA/rB')
    plt.title('Probability of player A beating player B')
    plt.show()
