from fastapi import FastAPI
from tennis_elo.elo.request_elo import calculate_we, find_player_elo
import pandas as pd
from pydantic import BaseModel

app = FastAPI()


class Players(BaseModel):
    player1_id: str
    player2_id: str


@app.post("/we")
async def get_we(player_ids: Players):
    current_elos = pd.read_csv("data/04_model_output/current_elos_atp.csv")

    player1_elo = find_player_elo(current_elos, player_ids.player1_id)
    player2_elo = find_player_elo(current_elos, player_ids.player2_id)

    we = calculate_we(player1_elo, player2_elo)

    return {player_ids.player1_id: we, player_ids.player2_id: 1 - we}
