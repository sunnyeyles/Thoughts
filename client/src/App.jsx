import { useState, useEffect } from "react";
import "./App.css";
import { addUser } from "./api/test";
import { SignUp } from "./components/SignUp";
import { CreatePost } from "./components/CreatePost";
import { Posts } from "./components/Posts";
import { getPostById } from "./api/getPostById";
import { getAllPosts } from "./api/getAllPosts";

import {
  SignOutButton,
  SignInButton,
  SignedIn,
  SignedOut,
} from "@clerk/clerk-react";

function App() {
  return (
    <div>
      <CreatePost />
      <Posts />
      {/* <h1 className="text-3xl font-bold underline">Hello world!</h1>

       <div>
      <SignedOut>
        <SignInButton />
        <p>This content is public. Only signed out users can see the SignInButton above this text.</p>
      </SignedOut>
      <SignedIn>
        <SignOutButton signOutCallback={() => redirect('/')} />
        <p>This content is private. Only signed in users can see the SignOutButton above this text.</p>
      </SignedIn>
    </div> */}
    </div>
  );
}

export default App;
