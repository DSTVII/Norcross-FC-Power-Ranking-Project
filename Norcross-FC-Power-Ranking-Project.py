"""
Norcross FC Power Ranking Project

Description:
This Python program manages the weekly power rankings of players from the Norcross FC soccer team, using data collected from a Google Form where all players vote on each person's 
performance across six key stats: Pace, Shooting, Passing, Dribbling, Defense, and Physicality. The voting data is then transferred into the Python code for processing and ranking. 

Key Features:
1. **Player Attendance Tracking**: Players who are absent can be marked, and they will be excluded from the weekly rankings.
2. **Performance-Based Ranking**: Players are ranked based on their total score, which is calculated by summing their performance stats, as voted on by their peers.
3. **Google Form Integration**: Player stats are determined by data collected from a Google Form, where teammates rate each other in different categories. The data is manually transferred into the code for further processing.
4. **Team Balancing**: Players are split into two evenly matched teams for each week's game, ensuring fair play.
5. **Weekly Stat Updates**: After each game, player stats can be updated based on their performance (e.g., increasing or decreasing their pace, shooting, etc.). The rankings are adjusted accordingly to reflect these changes.
6. **Goalkeeper Assignment**: Specific goalkeepers (Luis and Eder) are assigned to different teams to maintain balance.

Process:
- Players vote on each other's performance using a Google Form, with categories such as Pace, Shooting, Passing, Dribbling, Defense, and Physicality.
- The collected data is then manually input into the Python program, which calculates a total score for each player and ranks them accordingly.
- Teams are created based on the power rankings, ensuring balanced teams for the weekly matches.
- Each week, stats can be updated after the games to reflect real-time performance improvements or declines, and rankings are recalculated.

Usage:
- This program allows for the manual update of player stats after each game, which automatically adjusts the power rankings for the following week.
- Teams are created based on the power rankings, ensuring balanced teams for the weekly matches.
- Google Form data is the primary source of player performance stats, providing an inclusive and transparent method for ranking players.

Tools & Skills:
- Python (OOP, data structures, input/output)
- Google Forms integration for data collection and voting
- Player ranking system based on peer-reviewed performance statistics
- Team balancing algorithm for weekly matches
- Attendance filtering and performance tracking

"""


print("Norcross FC Power Rankings")

class Player:
    def __init__(self, name, pace, shooting, passing, dribbling, defense, physicality):
        self.name = name
        self.stats = {
            'pace': pace,
            'shooting': shooting,
            'passing': passing,
            'dribbling': dribbling,
            'defense': defense,
            'physicality': physicality
        }
        self.attendance = True

    def total_score(self):
        return sum(self.stats.values())

    def update_stats(self, pace_change, shooting_change, passing_change, dribbling_change, defense_change, physicality_change):
        self.stats['pace'] += pace_change
        self.stats['shooting'] += shooting_change
        self.stats['passing'] += passing_change
        self.stats['dribbling'] += dribbling_change
        self.stats['defense'] += defense_change
        self.stats['physicality'] += physicality_change

def mark_absent(players, absent_names):
    for player in players:
        if player.name in absent_names:
            player.attendance = False

def rank_players(players):
    return sorted(players, key=lambda player: player.total_score(), reverse=True)

def filter_attendance(players):
    return [player for player in players if player.attendance]

def split_teams(players):
    team1, team2 = [], []
    for i, player in enumerate(players):
        if i % 2 == 0:
            team1.append(player)
        else:
            team2.append(player)
    return team1, team2

def update_player_stats(players):
    for player in players:
        print(f"Update stats for {player.name}:")
        pace_change = int(input("Pace change: "))
        shooting_change = int(input("Shooting change: "))
        passing_change = int(input("Passing change: "))
        dribbling_change = int(input("Dribbling change: "))
        defense_change = int(input("Defense change: "))
        physicality_change = int(input("Physicality change: "))
        player.update_stats(pace_change, shooting_change, passing_change, dribbling_change, defense_change, physicality_change)

# Players list (excluding Luis and Eder)
players = [
    Player("David", 97, 91, 92, 93, 90, 92),
    Player("Newhsa", 94, 97, 92, 93, 85, 91),
    Player("Dean", 93, 83, 87, 87, 78, 88),  
    Player("Fabian", 80, 82, 86, 90, 84, 85),
    Player("Lucas", 93, 84, 85, 87, 89, 86),
    Player("Facu", 91, 84, 85, 87, 89, 86),
    Player("Juan", 91, 84, 85, 87, 89, 86),
    Player("Ian", 88, 84, 85, 87, 89, 86),
    Player("Federico", 88, 84, 85, 87, 89, 86),
    Player("Ivan", 88, 84, 85, 87, 89, 86),
    Player("Juan Pablo", 88, 84, 85, 87, 89, 86),
    Player("Manuel", 88, 84, 85, 87, 89, 86),
    Player("Nicolas U", 88, 84, 85, 87, 89, 86),
    Player("Christian", 88, 84, 85, 87, 89, 86),
    Player("Sergio", 88, 84, 85, 87, 89, 86),
    Player("Alan", 88, 84, 85, 87, 89, 86),
    Player("Nicolas M", 88, 84, 85, 87, 89, 86),
    Player("Max", 88, 84, 85, 87, 89, 86),
    Player("Sebastian", 88, 84, 85, 87, 89, 86),
    Player("Daet", 88, 84, 85, 87, 89, 86),
    Player("Andres", 88, 84, 85, 87, 89, 86),
    Player("Jonny Jr", 88, 84, 85, 87, 89, 86),
    Player("Daniel", 88, 84, 85, 87, 89, 86),
    Player("Amy", 88, 84, 85, 87, 89, 86),
    Player("German", 88, 84, 85, 87, 89, 86),
    Player("Santiago", 88, 84, 85, 87, 89, 86),
    Player("Omar", 88, 84, 85, 87, 89, 86),
    Player("Alejandro", 88, 84, 85, 87, 89, 86),
    Player("Jonny Sr", 88, 84, 85, 87, 89, 86)
]

# Goalkeepers (Luis and Eder)
luis = Player("Luis", 0, 0, 0, 0, 0, 0)
eder = Player("Eder", 88, 84, 85, 87, 89, 86)

# Input names of players who are absent
absent_names = input("Absent, please separate by commas: ").split(", ")

# Step 1: Mark the absent players
mark_absent(players, absent_names)

# Step 2: Filter players based on attendance
active_players = filter_attendance(players)

# Step 3: Rank players based on their total score
ranked_players = rank_players(active_players)

# Step 4: Split players into two balanced teams
team1, team2 = split_teams(ranked_players)

# Ensure Luis and Eder are split between the two teams
team1.append(luis)
team2.append(eder)

# Display teams
print("\nTeam 1:")
for player in team1:
    print(f"{player.name} - Total Score: {player.total_score()}")

print("\nTeam 2:")
for player in team2:
    print(f"{player.name} - Total Score: {player.total_score()}")

# Step 5: Update player stats based on the performance in the game
update_player_stats(players)
