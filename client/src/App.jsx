import { useState, useEffect } from "react";
import { getGtaData } from "./api/getGtaData";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch("/api/data");
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  getGtaData();

  return (
    <div>
      <h1 className="text-3xl font-bold underline">Hello world!</h1>
      <p>Data from Server: {message}</p>
    </div>
  );
}

export default App;
