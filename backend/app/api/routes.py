import joblib
import os
import random
from fastapi import APIRouter
from app.schemas.player import PlayerPerformance

router = APIRouter(prefix="/api/v1")

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "trained_model.pkl") #loads the trained model once the backend starts.
MODEL_PATH = os.path.abspath(MODEL_PATH)

model = joblib.load(MODEL_PATH)

# Global match state
match_state = {
    "current_minute": 0,
    "possession_team": random.choice(["Arsenal", "Manchester City", "Liverpool"])
}

# Persistent in-memory match state
player_states = {
    7: {
        "name": "Bukayo Saka",
        "team": "Arsenal",
        "position": "FW",
        "minutes_played": 0,
        "passes_attempted": 0,
        "passes_completed": 0,
        "key_passes": 0,
        "shots": 0,
        "shots_on_target": 0,
        "goals": 0,
        "assists": 0,
        "tackles": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "fouls_committed": 0,
        "yellow_cards": 0,
        "red_card": 0,
        "previous_score": 50,
        "is_sent_off": False,
        "score_history": []
    },
    9: {
        "name": "Erling Haaland",
        "team": "Manchester City",
        "position": "FW",
        "minutes_played": 0,
        "passes_attempted": 0,
        "passes_completed": 0,
        "key_passes": 0,
        "shots": 0,
        "shots_on_target": 0,
        "goals": 0,
        "assists": 0,
        "tackles": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "fouls_committed": 0,
        "yellow_cards": 0,
        "red_card": 0,
        "previous_score": 50,
        "is_sent_off": False,
        "score_history": []
    },
    8: {
        "name": "Kevin De Bruyne",
        "team": "Manchester City",
        "position": "MF",
        "minutes_played": 0,
        "passes_attempted": 0,
        "passes_completed": 0,
        "key_passes": 0,
        "shots": 0,
        "shots_on_target": 0,
        "goals": 0,
        "assists": 0,
        "tackles": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "fouls_committed": 0,
        "yellow_cards": 0,
        "red_card": 0,
        "previous_score": 50,
        "is_sent_off": False,
        "score_history": []
    },
    10: {
        "name": "Martin Odegaard",
        "team": "Arsenal",
        "position": "MF",
        "minutes_played": 0,
        "passes_attempted": 0,
        "passes_completed": 0,
        "key_passes": 0,
        "shots": 0,
        "shots_on_target": 0,
        "goals": 0,
        "assists": 0,
        "tackles": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "fouls_committed": 0,
        "yellow_cards": 0,
        "red_card": 0,
        "previous_score": 50,
        "is_sent_off": False,
        "score_history": []
    },
    4: {
        "name": "Virgil van Dijk",
        "team": "Liverpool",
        "position": "DF",
        "minutes_played": 0,
        "passes_attempted": 0,
        "passes_completed": 0,
        "key_passes": 0,
        "shots": 0,
        "shots_on_target": 0,
        "goals": 0,
        "assists": 0,
        "tackles": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "fouls_committed": 0,
        "yellow_cards": 0,
        "red_card": 0,
        "previous_score": 50,
        "is_sent_off": False,
        "score_history": []
    },
    3: {
        "name": "Ruben Dias",
        "team": "Manchester City",
        "position": "DF",
        "minutes_played": 0,
        "passes_attempted": 0,
        "passes_completed": 0,
        "key_passes": 0,
        "shots": 0,
        "shots_on_target": 0,
        "goals": 0,
        "assists": 0,
        "tackles": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "fouls_committed": 0,
        "yellow_cards": 0,
        "red_card": 0,
        "previous_score": 50,
        "is_sent_off": False,
        "score_history": []
    }
}

def simulate_minute(player, match_state):

    # Stop simulation after 90 minutes
    if match_state["current_minute"] > 90:
        return

    # Sync minute
    player["minutes_played"] = match_state["current_minute"]

    # Randomly change possession sometimes
    if random.random() < 0.1:
        match_state["possession_team"] = random.choice(
            ["Arsenal", "Manchester City", "Liverpool"]
        )

    # --- POSSESSION PHASE ---
    if player["team"] == match_state["possession_team"]:

        if player["position"] == "MF":
            passes = random.randint(1, 3)
            player["passes_attempted"] += passes
            player["passes_completed"] += int(passes * random.uniform(0.8, 0.95))

            if random.random() < 0.08:
                player["key_passes"] += 1

        elif player["position"] == "FW":
            passes = random.randint(1, 2)
            player["passes_attempted"] += passes
            player["passes_completed"] += int(passes * random.uniform(0.75, 0.9))

            if random.random() < 0.12:
                player["key_passes"] += 1

            if random.random() < 0.15:
                player["shots"] += 1
                if random.random() < 0.4:
                    player["shots_on_target"] += 1
                    if random.random() < 0.3:
                        player["goals"] += 1

        elif player["position"] == "DF":
            if random.random() < 0.20:
                player["shots"] += 1
                if random.random() < 0.45:
                    player["shots_on_target"] += 1
                    if random.random() < 0.35:
                        player["goals"] += 1

    # --- DEFENSIVE PHASE ---
    else:
        if player["position"] == "DF":
            if random.random() < 0.15:
                player["tackles"] += 1
            if random.random() < 0.10:
                player["clearances"] += 1

        if player["position"] == "MF":
            if random.random() < 0.12:
                player["interceptions"] += 1

    # --- DISCIPLINE ---
    if player.get("is_sent_off"):
        return

    if random.random() < 0.01:
        if player["yellow_cards"] == 0:
            player["yellow_cards"] = 1
        else:
            player["red_card"] = 1
            player["is_sent_off"] = True

    if random.random() < 0.002:
        player["red_card"] = 1
        player["is_sent_off"] = True

def extract_features(player):

    pass_accuracy = (
        player["passes_completed"] / player["passes_attempted"]
        if player["passes_attempted"] > 0 else 0
    )

    total_actions = (
        player["passes_attempted"] +
        player["shots"] +
        player["tackles"] +
        player["interceptions"] +
        player["clearances"] +
        player["blocks"]
    )

    activity_rate = total_actions / player["minutes_played"] if player["minutes_played"] > 0 else 0

    return {
        "pass_accuracy": pass_accuracy,
        "goals": player["goals"],
        "assists": player["assists"],
        "shots_on_target": player["shots_on_target"],
        "key_passes": player["key_passes"],
        "tackles": player["tackles"],
        "interceptions": player["interceptions"],
        "clearances": player["clearances"],
        "blocks": player["blocks"],
        "yellow_cards": player["yellow_cards"],
        "activity_rate": activity_rate
    }

def model_predict(features):

    attacking_score = (
        features["goals"] * 10 +
        features["assists"] * 6 +
        features["shots_on_target"] * 3 +
        features["key_passes"] * 2
    )

    defensive_score = (
        features["tackles"] * 2 +
        features["interceptions"] * 2 +
        features["clearances"] +
        features["blocks"]
    )

    discipline_penalty = features["yellow_cards"] * 5

    raw_score = (
        features["pass_accuracy"] * 20 +
        attacking_score +
        defensive_score -
        discipline_penalty +
        features["activity_rate"] * 5
    )

    return max(0, min(100, int(raw_score)))

def calculate_trend(old_score, new_score):
    if new_score > old_score:
        return "UP"
    elif new_score < old_score:
        return "DOWN"
    return "STABLE"

@router.get("/players/performance", response_model=list[PlayerPerformance])
def get_player_performance():

    global match_state

    # Stop incrementing after 90
    if match_state["current_minute"] < 90:
        match_state["current_minute"] += 1

    results = []


    for player_id, player in player_states.items():
        simulate_minute (player, match_state)
        features = extract_features(player)
        
        previous_score = player["previous_score"]
        new_score = previous_score

        # POSITIVE IMPACT
        new_score += player["goals"] * 8
        new_score += player["assists"] * 6
        new_score += player["shots_on_target"] * 2
        new_score += player["key_passes"] * 1.5

        # Passing influence
        pass_accuracy = (
            player["passes_completed"] / player["passes_attempted"]
            if player["passes_attempted"] > 0 else 0
        )

        if pass_accuracy > 0.85:
            new_score += 2
        elif pass_accuracy < 0.6:
            new_score -= 3

        # Defensive contribution
        new_score += player["tackles"] * 1
        new_score += player["interceptions"] * 1
        new_score += player["blocks"] * 1

        # NEGATIVE IMPACT

        if player["yellow_cards"] > 0:
            new_score *= 0.9   # -10%

        if player["red_card"] > 0:
            new_score *= 0.7   # -30%

        new_score -= player["fouls_committed"] * 0.5

        # Small natural drift
        new_score += random.uniform(-2, 2)

        # Clamp
        new_score = max(0, min(100, int(new_score)))


        # Clamp between 0 and 100
        new_score = max(0, min(100, new_score))

        trend = calculate_trend(player["previous_score"], new_score)
        player["previous_score"] = new_score
        
        player["score_history"].append(new_score)
        
        # Keep last 50 points only
        if len(player["score_history"]) > 50:
            player["score_history"].pop(0)
        score = new_score

        results.append(
            PlayerPerformance(
                player_id=player_id,
                name=player["name"],
                team=player["team"],
                position=player["position"],
                minutes_played=player["minutes_played"],
                passes_attempted=player["passes_attempted"],
                passes_completed=player["passes_completed"],
                key_passes=player["key_passes"],
                shots=player["shots"],
                shots_on_target=player["shots_on_target"],
                goals=player["goals"],
                assists=player["assists"],
                tackles=player["tackles"],
                interceptions=player["interceptions"],
                clearances=player["clearances"],
                blocks=player["blocks"],
                fouls_committed=player["fouls_committed"],
                yellow_cards=player["yellow_cards"],
                red_card=player["red_card"],
                performance_score=score,
                trend=trend,
                score_history=player["score_history"]
            )
        )

    return results

@router.get("/model/feature-importance")
def get_feature_importance():

    feature_names = [
        "pass_accuracy",
        "goals",
        "assists",
        "shots_on_target",
        "key_passes",
        "tackles",
        "interceptions",
        "clearances",
        "blocks",
        "yellow_cards",
        "activity_rate",
    ]

    importances = model.feature_importances_

    results = [
        {"feature": name, "importance": float(importance)}
        for name, importance in zip(feature_names, importances)
    ]

    # Sort highest first
    results.sort(key=lambda x: x["importance"], reverse=True)

from pydantic import BaseModel

class ManualEvent(BaseModel):
    player_id: int
    action: str


@router.post("/players/manual-event")
def apply_manual_event(event: ManualEvent):

    player = player_states.get(event.player_id)

    if not player:
        return {"error": "Player not found"}

    action = event.action.lower()

    # --- APPLY EVENT ---
    if action == "goal":
        player["goals"] += 1

    elif action == "assist":
        player["assists"] += 1

    elif action == "key_pass":
        player["key_passes"] += 1

    elif action == "shot_on_target":
        player["shots"] += 1
        player["shots_on_target"] += 1

    elif action == "tackle":
        player["tackles"] += 1

    elif action == "interception":
        player["interceptions"] += 1

    else:
        return {"error": "Invalid action"}

    # Recalculate score immediately
    features = extract_features(player)
    new_score = model_predict(features)

    trend = calculate_trend(player["previous_score"], new_score)
    player["previous_score"] = new_score
    player["score_history"].append(new_score)

    if len(player["score_history"]) > 50:
        player["score_history"].pop(0)

    return {
        "message": "Event applied",
        "new_score": new_score,
        "trend": trend
    }
