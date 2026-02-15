from fastapi import FastAPI
from pydantic import BaseModel

# This is your temporary "database"
GAMES = [
    {
        "id": 1,
        "name": "Elden Ring",
        "price": 59.99,
        "rating": 4.9
    }
]

# This defines what data is required when creating a new game
class GameCreate(BaseModel):
    name: str
    price: float
    rating: float

# Create the FastAPI app
app = FastAPI()

# GET /games → returns all games
@app.get("/games")
def get_all_games():
    return GAMES


# GET /games/{game_id} → returns one specific game
@app.get("/games/{game_id}")
def get_game(game_id: int):
    for game in GAMES:
        if game["id"] == game_id:
            return game
    
    return {"error": "Game not found"}


# POST /games → creates a new game
@app.post("/games")
def create_game(game: GameCreate):

    # Generate a new ID
    new_id = len(GAMES) + 1

    # Create new game object
    new_game = {
        "id": new_id,
        "name": game.name,
        "price": game.price,
        "rating": game.rating
    }

    # Add to GAMES list
    GAMES.append(new_game)

    # Return the new game
    return new_game
