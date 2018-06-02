from bs4 import BeautifulSoup
from utils import result, home_score, away_score
from utils import goal_goal, over_1, over_2, over_3, over_4
import datetime
import os

directory = os.fsencode("database")

f = open("data.csv", "w")
f.write("home,score,away,result,home_score,away_score,goal_goal,over_1,over_2,over_3,over_4\n")


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print("database/" + filename)
    count = 0
    now = str(datetime.datetime.now())
    soup = BeautifulSoup(open("database/" + filename), 'html.parser')
    weeks = soup.findAll('td', {'style':'width: 33%; text-align:center; background-color: #E1E3E6; padding: 7px'})
    odds = soup.findAll('td', {'style':'width:19%; text-align:center'})

    for week in weeks:
        weekn = week.findAll('tr')
        count = count +1
        #print("Week " + str(count) + " ...")
        print(":", end="")

        for match in weekn:
            match1 = match.findAll('td')
            if len(match1) == 3:
                home = match1[0].text
                score = match1[1].text
                away = match1[2].text
                f.write(home + "," + score + "," + away + "," + result(score) + "," + home_score(score) + "," + away_score(score) + "," + goal_goal(score) + "," + over_1(score) + "," + over_2(score) + "," + over_3(score) + "," + over_4(score) + "\n")

    print(">>database/" + filename)

f.close()
print("Porting Successfully Finished")