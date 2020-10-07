import React, { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  useEffect(() => {
    const MakeAPICall = () => {
      axios
        .get("http://127.0.0.1:8000/blogpost_get/")
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          if (error) {
            console.log(error);
          }
        });
    };
    MakeAPICall();
  }, []);

  return (
    <div className="App">
      <h1>Home</h1>
    </div>
  );
}

export default App;
