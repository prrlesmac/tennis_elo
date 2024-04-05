from tennis_elo.get_data.get_match_data import (
    get_atp_matches,
    open_github_csv_as_dataframe,
    get_wta_matches,
)
from tennis_elo.elo.calculate_elo import calculate_elo_history, get_current_elo
import os

atp_matches = get_atp_matches(range(2020, 2024))
wta_matches = get_wta_matches(range(2020, 2024))

players_master = open_github_csv_as_dataframe(
    "https://github.com/JeffSackmann/tennis_atp", f"atp_players.csv"
)
matches, elos = calculate_elo_history(atp_matches, 20)
current_elos = get_current_elo(players_master, elos)

current_elos.to_csv("data/04_model_output/current_elos_atp.csv")

players_master = open_github_csv_as_dataframe(
    "https://github.com/JeffSackmann/tennis_wta", f"wta_players.csv"
)
matches, elos = calculate_elo_history(wta_matches, 20)
current_elos = get_current_elo(players_master, elos)

if not os.path.exists("data/04_model_output"):
    os.makedirs("data/04_model_output")
current_elos.to_csv("data/04_model_output/current_elos_wta.csv")

print(current_elos)
