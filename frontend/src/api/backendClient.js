const BASE_URL = "http://127.0.0.1:8000/api/v1";                            //Central place to handle backend calls.

export async function fetchPlayerPerformance() {
  const response = await fetch(`${BASE_URL}/players/performance`);
  return response.json();
}

export const applyManualEvent = async (playerId, action) => {
  const response = await fetch("http://127.0.0.1:8000/api/v1/players/manual-event", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      player_id: playerId,
      action: action,
    }),
  });

  return response.json();
};
