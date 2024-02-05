import { useState, useEffect } from "react";
import { getGtaData } from "./api/getGtaData";
import "./App.css";
import { addUser } from "./api/test";
import { SignUp } from "./components/SignUp";
import { CreatePost } from "./components/CreatePost";
function App() {
  return (
    <div>
      <h1 className="text-3xl font-bold underline">Hello world!</h1>
      <CreatePost />
      <SignUp />
    </div>
  );
}

export default App;
