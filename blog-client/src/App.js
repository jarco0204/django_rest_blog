import React, { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [data, setData] = useState("");
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    const MakeAPICall = () => {
      axios
        .get("http://127.0.0.1:8000/users/")
        .then((data) => {
          console.log(data);
          setData(data.data[0]);
          setPosts(data.data);
        })
        .catch((error) => {
          if (error) {
            console.log(error);
          }
        });
    };
    MakeAPICall();
  }, []);

  // console.log(data[0]);
  // console.log(posts.posts);
  posts.forEach((element, index) => {
    console.log(element.posts);
  });

  return (
    <div className="App">
      <h1>Home</h1>
      <img src={data.user_image} alt="img" />
    </div>
  );
}

export default App;
