from fastapi import FastAPI

GAMES = [
        {
            "id": 1,
            "name": "Elden Ring",
            "price": 59.99,
            "rating": 4.9
        },
    ]
app = FastAPI()
@app.get("/games/{game_id}")
def get_games(game_id : int):
    for game in GAMES:
        if game["id"] == game_id:
            return game
        
    return{"error": "Game not found"}

