import pandas as pd
import numpy as np


def calculate_new_elo(winnerElo, loserElo, K):
    dr = winnerElo - loserElo
    we = 1 / (10 ** (-dr / 400) + 1)

    winnerElo = winnerElo + (1 - we) * K
    loserElo = loserElo + (we - 1) * K

    ptsExc = abs(1 - we) * K

    return winnerElo, loserElo, ptsExc, we


def create_list_of_players(matches):
    players = matches["winner_id"].astype(str)
    players = pd.concat([players, matches["loser_id"].astype(str)])
    players = players.unique()

    players = dict.fromkeys(players)

    for key in players.keys():
        players[key] = {"CurrentElo": 1600, "Activity": 0}

    return players


def calculate_elo_history(matches, K):
    players = create_list_of_players(matches)

    matches["startWinnerElo"] = 0
    matches["startLoserElo"] = 0
    matches["endWinnerElo"] = 0
    matches["endLoserElo"] = 0
    matches["ptsExc"] = 0
    matches["we"] = 0

    start_winner_elo_list = []
    start_loser_elo_list = []
    end_winner_elo_list = []
    end_loser_elo_list = []
    pts_exc_list = []
    win_ex_list = []

    # for id in range(len(matches)):
    for id in range(len(matches)):
        if id % 1000 == 0:
            print(id)

        winner_id = matches.iloc[id, :]["winner_id"]
        loser_id = matches.iloc[id, :]["loser_id"]
        tourney_date = matches.iloc[id, :]["tourney_date"]

        winner_elo = players[str(winner_id)]["CurrentElo"]
        loser_elo = players[str(loser_id)]["CurrentElo"]

        new_winner_elo, new_loser_elo, PtsExc, WinEx = calculate_new_elo(
            winnerElo=winner_elo, loserElo=loser_elo, K=K
        )

        start_winner_elo_list.append(winner_elo)
        start_loser_elo_list.append(loser_elo)
        end_winner_elo_list.append(new_winner_elo)
        end_loser_elo_list.append(new_loser_elo)
        pts_exc_list.append(PtsExc)
        win_ex_list.append(WinEx)

        players[str(winner_id)]["CurrentElo"] = new_winner_elo
        players[str(loser_id)]["CurrentElo"] = new_loser_elo
        players[str(winner_id)]["Activity"] = tourney_date
        players[str(loser_id)]["Activity"] = tourney_date

    matches["startWinnerElo"] = start_winner_elo_list
    matches["startLoserElo"] = start_loser_elo_list
    matches["endWinnerElo"] = end_winner_elo_list
    matches["endLoserElo"] = end_loser_elo_list
    matches["ptsExc"] = pts_exc_list
    matches["we"] = win_ex_list

    return matches, players


def get_current_elo(player_master, player_elos):
    player_ids = []
    player_elo_rating = []
    player_activity = []
    for k, v in player_elos.items():
        player_ids.append(int(k))
        player_elo_rating.append(v["CurrentElo"])
        player_activity.append(v["Activity"])

    player_df = pd.DataFrame()
    player_df["player_id"] = player_ids
    player_df["elo"] = player_elo_rating
    player_df["activity"] = player_activity

    player_df = player_df.merge(player_master, how="left", on="player_id")
    player_df = player_df[player_df["activity"] >= 20220801]
    player_df = player_df.sort_values(by="elo", ascending=False)

    return player_df
