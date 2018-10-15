import csv
from pprint import pprint

Wteams = ["Atlanta Falcons", "New England Patriots", "Boston Patriots", "Dallas Cowboys", "Seattle Seahawks"]
Lteams = ["Denver Broncos"]
teams = Wteams+Lteams
scores = []

with open('scores.csv') as sc:
    reader = csv.reader(sc)
    for row in reader:
        if len(row) == 0:
            continue
        if row[4].strip() in teams or row[2].strip() in teams:
            scores.append(row)
print(len(scores))
pw = []
count=0
for i in range(len(scores)):
    w = [scores[i]]
    for k in range(i+1, len(scores)):
        if (scores[i][0] == scores[k][0]) and (scores[i][1] == scores[k][1]):
            w.append(scores[k])
    if len(w) < 4:
        continue
    if len(w) == 4:    
        isGood = True
        for k in w:
            if k[2].strip() in Lteams:
                if k[4].strip() in Wteams:
                    continue
            if k[4].strip() in Lteams:
                if k[2].strip() in Wteams:
                    continue
            else:
                isGood = False
        if not isGood:
            continue
    count+=1
    isGood = True
    for k in w:
        
        if (k[2].strip() in Wteams and int(k[3])>int(k[5])):
            continue
        if (k[4].strip() in Wteams and int(k[3])<int(k[5])):
            continue
        if (k[2].strip() in Lteams and int(k[3])<int(k[5])):
            continue
        if (k[4].strip() in Lteams and int(k[3])>int(k[5])):
            continue
        else:
            isGood = False
    if isGood is True:
        pw.append(w)
    else:
        #print("{} week {} isn't perfect".format(w[0][0], w[0][1]))
        #pprint(w)
        pass

for i in pw:
    pprint(i)
print("A SMK Perfect week has happened {} times out of {} possible weeks ({}%)".format(len(pw), count, 100.0*len(pw)/count))