from pydantic import BaseModel

class PlayerPerformance(BaseModel):
    player_id: int
    name: str
    team: str
    position: str
    minutes_played: int

    passes_attempted: int
    passes_completed: int
    key_passes: int

    shots: int
    shots_on_target: int
    goals: int
    assists: int

    tackles: int
    interceptions: int
    clearances: int
    blocks: int

    fouls_committed: int
    yellow_cards: int
    red_card: int

    performance_score: int
    trend: str
    score_history: list[int]
