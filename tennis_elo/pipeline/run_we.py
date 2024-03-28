import pandas as pd
from tennis_elo.elo.request_elo import calculate_we, find_player_elo

player1_id = input("Enter player 1 id: ")
player2_id = input("Enter player 2 id: ")

current_elos = pd.read_csv("data/04_model_output/current_elos_atp.csv")

player1_elo = find_player_elo(current_elos, player1_id)
player2_elo = find_player_elo(current_elos, player2_id)

we = calculate_we(player1_elo, player2_elo)

print("Win probability ", player1_id, ": ", we)
print("Win probability ", player2_id, ": ", 1 - we)
