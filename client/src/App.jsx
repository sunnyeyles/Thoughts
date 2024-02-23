import { useState, useEffect } from "react";
import { getGtaData } from "./api/getGtaData";
import "./App.css";
import { addUser } from "./api/test";
import { SignUp } from "./components/SignUp";
import { CreatePost } from "./components/CreatePost";
import { Posts } from "./components/Posts";
import { getPostById } from "./api/getPostById";
import { getAllPosts } from "./api/getAllPosts";
function App() {
  return (
    <div>
      <h1 className="text-3xl font-bold underline">Hello world!</h1>
      <CreatePost />
      <Posts />
    </div>
  );
}

export default App;
