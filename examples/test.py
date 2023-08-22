from tennis_elo.get_data.get_match_data import (
    get_atp_matches,
    open_github_csv_as_dataframe,
)
from tennis_elo.elo.calculate_elo import calculate_elo_history, get_current_elo
import pandas as pd

atp_matches = get_atp_matches(range(1968, 2024))
players_master = open_github_csv_as_dataframe(
    "https://github.com/JeffSackmann/tennis_atp", f"atp_players.csv"
)
matches, elos = calculate_elo_history(atp_matches, 20)
current_elos = get_current_elo(players_master, elos)
current_elos.to_csv("data/04_model_output/current_elos.csv")

print(current_elos)
