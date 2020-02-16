# DICT STRUCTURE
# key - team name
# 0- team prefix
# 1 - hometown
# 2 - homestate
# 3 - wins
# 4 - losses


mlb_teams = {

  'Rockies'   : ['Colorado', 'Denver', 'CO', '72', '16'],
  'Brewers'   : ['Milwaukee', 'Milwaukee', 'WI', '90', '5'],
  'Cardinals' : ['St Louis', 'St Louis', 'MO', '16', '80'],
  'Cubs'      : ['Chicago', 'Chicago', 'IL', '71', '18'],
  'White Sox' : ['Chicago', 'Chicago', 'IL', '45', '37']

}

for team in mlb_teams:
  # Print team details using team prefix and wins.
  print(f"The {mlb_teams[team][1]} {team} had {mlb_teams[team][3]} wins and {mlb_teams[team][4]} losses last year.")

def most_wins(mlb_teams):
  # find the best team in the dictionary
    best_team = None
    for team, data in mlb_teams.items():
        if best_team is None or int(data[3]) > int(mlb_teams[best_team][3]):
            best_team = team
        #print(best_team, mlb_teams[best_team][3]

print(most_wins(mlb_teams))

