from tennis_elo.elo.calculate_elo import create_list_of_players
import pandas as pd
from pandas.testing import assert_frame_equal


def test_create_list_of_players():
    matches = [("1234", "5678"), ("5678", "1234")]

    matches_df = pd.DataFrame(matches, columns=["winner_id", "loser_id"])
    players = create_list_of_players(matches_df)

    players_out = {
        "1234": {"CurrentElo": 1600, "Activity": 0},
        "5678": {"CurrentElo": 1600, "Activity": 0},
    }

    assert players == players_out
