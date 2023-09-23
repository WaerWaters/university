# Daniel Elsborg Johnsen, djohns22@student.aau.dk, cs-22-dvml-1-p1-01
# Programmet er ikke baseret på fælles arbejde i gruppen

import os
  
def scoreboard():
    # Laver en liste med filernes navne i mappen
    rounds = os.listdir('assignment2Rounds')
    
    # Læser hvilke hold der er med
    with open('nations','r') as f:
        #sorter listen  med holdene i alfabetisk rækkefølge.
        nations = sorted([nation.strip() for nation in f.readlines()])
        goals = ["", "", "", ""]
        goals_scored = [0,0,0,0]
        opponent_goals_scored = [0,0,0,0]
        won = [0,0,0,0]
        lost = [0,0,0,0]
        tied = [0,0,0,0]
        points = [0,0,0,0]
        for round in rounds:
            print("\n{}".format(round))
            # Hver runde læs den nuværende rundes fil
            with open('assignment2Rounds/{}'.format(round),'r') as f:
                # Den første for loop renser filen og returneres til variablen matches_fixed.
                # matches_fixed index position 0 er en liste med hold navne og \
                # index position 1 er en liste over hvor mange mål det hold scorede
                matches_in_round = [match.strip().replace("\t", " ") for match in f.readlines()]
                matches_fixed = [[],[]]
                for match in matches_in_round:
                    index = 0
                    match = match.replace(" ", "")
                    for character in match:
                        if character.isdigit():
                            index = match.find(character)
                            break
                    match = match[:index], match[index:]
                    match = match[0].split("-",1), match[1].split("-",1)
                    for team in match[0]:
                        matches_fixed[0].append(team)
                    for goal in match[1]:
                        matches_fixed[1].append(goal)
                
                # Denne for loop returner scoreboarded for hvert hold. (hold navn, kampe vundet, uafgjort, tabt, scorede mål - mostanderens mål, hold points)
                for nation in nations:
                    index = matches_fixed[0].index(nation)
                    goals_scored_int = int(matches_fixed[1][index])
                    opponent_goals_scored_int = 0
                    goals_scored[nations.index(nation)] += int(matches_fixed[1][index])
                    # Tjekker hvis det nuværende holds index position er lige eller ulige, og henter mængden af mål modstander holdet scorede
                    if index % 2 == 0:
                        opponent_goals_scored_int = int(matches_fixed[1][index+1])
                        opponent_goals_scored[nations.index(nation)] += int(matches_fixed[1][index+1])
                    else:
                        opponent_goals_scored_int = int(matches_fixed[1][index-1])
                        opponent_goals_scored[nations.index(nation)] += int(matches_fixed[1][index-1])
                        
                    # Tjekker om det nuværende hold vandt, tabte eller stod lige
                    goals[nations.index(nation)] = "{} - {}".format(goals_scored[nations.index(nation)], opponent_goals_scored[nations.index(nation)])
                    if goals_scored_int > opponent_goals_scored_int:
                        won[nations.index(nation)] += 1
                        points[nations.index(nation)] += 3
                    elif goals_scored_int < opponent_goals_scored_int:
                        lost[nations.index(nation)] += 1
                    else:
                        tied[nations.index(nation)] += 1
                        points[nations.index(nation)] += 1
                # For hvert hold, print holdets scoreboard
                for i in range(len(nations)):
                    stats = "{}\t {} {} {}  {}\t {}".format(nations[i],won[i],tied[i],lost[i],goals[i],points[i])
                    print(stats)

#kalder funktionen/programmet
scoreboard()



