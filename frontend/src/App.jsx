import { useEffect, useState } from "react";
import PerformanceChart from "./components/PerformanceChart";
import { fetchPlayerPerformance, applyManualEvent } from "./api/backendClient";


function App() {
  const [players, setPlayers] = useState([]);
  const [selectedPlayerId, setSelectedPlayerId] = useState(null);
  const [manualPlayerId, setManualPlayerId] = useState(null);
  const [manualAction, setManualAction] = useState("goal");

  const handleManualEvent = async () => {
    if (!manualPlayerId) return;
  
    await applyManualEvent(manualPlayerId, manualAction);
    loadData(); // refresh UI immediately
  };

  const loadData = async () => {
    const data = await fetchPlayerPerformance();
    setPlayers(data)
  
    setSelectedPlayerId(prevSelected => {
      // If nothing selected yet → pick first
      if (!prevSelected && data.length > 0) {
        return data[0].player_id;
      }
  
      // If previously selected player still exists → keep it
      const stillExists = data.some(
        p => p.player_id === prevSelected
      );
  
      return stillExists ? prevSelected : data[0]?.player_id;
    });
  };
  
  useEffect(() => {
    loadData();

    const interval = setInterval(() => {
      loadData();
    }, 20000);

    return () => clearInterval(interval);
  }, []);

  const getTrendSymbol = (trend) => {
    if (trend === "UP") return "⬆";
    if (trend === "DOWN") return "⬇";
    return "➖";
  };

  // Find selected player
  const selectedPlayer = players.find(
    (player) => player.player_id === selectedPlayerId
  );

  return (
    <div style={{ padding: "20px" }}>
      <h1>Live Football Player Performance</h1>

      {/* Dropdown */}
      <select
        value={selectedPlayerId || ""}
        onChange={(e) => setSelectedPlayerId(Number(e.target.value))}
        style={{ marginBottom: "20px", padding: "5px" }}
      >
        {players.map((player) => (
          <option key={player.player_id} value={player.player_id}>
            {player.name}
          </option>
        ))}
      </select>

      <hr style={{ margin: "20px 0" }} />

      <h3>Manual Event Override</h3>

      <select
        value={manualPlayerId || ""}
        onChange={(e) => setManualPlayerId(Number(e.target.value))}
        style={{ marginRight: "10px", padding: "5px" }}
      >
        <option value="">Select Player</option>
        {players.map((player) => (
          <option key={player.player_id} value={player.player_id}>
            {player.name}
          </option>
        ))}
      </select>

      <select
        value={manualAction}
        onChange={(e) => setManualAction(e.target.value)}
        style={{ marginRight: "10px", padding: "5px" }}
      >
        <option value="goal">Goal</option>
        <option value="assist">Assist</option>
        <option value="key_pass">Key Pass</option>
        <option value="shot_on_target">Shot On Target</option>
        <option value="tackle">Tackle</option>
        <option value="interception">Interception</option>
      </select>

      <button
        onClick={handleManualEvent}
        style={{
          padding: "6px 12px",
          backgroundColor: "#1f77b4",
          color: "white",
          border: "none",
          cursor: "pointer",
        }}
      >
        Apply
      </button>


      {/* Selected Player View */}
      {selectedPlayer && (
        <div style={{ marginTop: "20px" }}>
          <h2>
            {selectedPlayer.name} ({selectedPlayer.team})
          </h2>
          <p>Minutes: {selectedPlayer.minutes_played}</p>
          <p>
            Goals: {selectedPlayer.goals} | Assists: {selectedPlayer.assists}
          </p>
          <p>
            Passes: {selectedPlayer.passes_completed}/
            {selectedPlayer.passes_attempted}
          </p>
          <p>
            Score:{" "}
            <strong>{selectedPlayer.performance_score}</strong>{" "}
            {getTrendSymbol(selectedPlayer.trend)}
          </p>

          <PerformanceChart history={selectedPlayer.score_history} />
        </div>
      )}
    </div>
  );
}

export default App;
