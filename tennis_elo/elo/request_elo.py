import pandas as pd
import numpy as np


def calculate_we(elo1, elo2):
    dr = elo1 - elo2
    we = 1 / (10 ** (-dr / 400) + 1)

    return we


def find_player_elo(elo_data, player_id):
    player_elo = elo_data[elo_data["player_id"] == int(player_id)]["elo"].values[0]
    return player_elo
