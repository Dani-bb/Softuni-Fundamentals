team_A = ["A-" + str(s) for s in range(1,12)]
team_B = ["B-" + str(s) for s in range(1,12)]

players_sent_off = input().split()
game_was_terminated = False

for player in players_sent_off:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)
    if len(team_A )< 7 or len(team_B) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if game_was_terminated:
    print("Game was terminated")

