import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function FeatureImportance() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/model/feature-importance")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div style={{ width: "100%", height: 400 }}>
      <h2>Model Feature Importance</h2>
      <ResponsiveContainer>
        <BarChart data={data}>
          <XAxis dataKey="feature" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="importance" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default FeatureImportance;
