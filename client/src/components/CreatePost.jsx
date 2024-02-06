import { useState, useEffect } from "react";
import avatarPhoto from "../../dieter.jpeg";
const imagePresent = true;
import { createPost } from "../api/createPost";
import { v4 as uuidv4 } from "uuid";

export const CreatePost = () => {
  const [post, setPost] = useState("");
  const [submittedData, setSubmittedData] = useState("");

  const handleChange = (e) => {
    setPost(e.target.value);
  };

  useEffect(() => {}, [submittedData]);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmittedData(post);
    createPost({ body: { post, userId: uuidv4() } });
  };
  return (
    <div className="flex bg-slate-500 p-12 shadow-2xl">
      <div className="relative">
        <img
          className="w-10 h-10 rounded-full shadow-2xl"
          src={avatarPhoto}
          alt=""
        />
        <span className="top-0 left-7 absolute  w-3.5 h-3.5 bg-green-400 shadow-2xl rounded-full"></span>
      </div>
      <div className="relative w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600">
        <svg
          className="absolute w-12 h-12 text-gray-400"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fillRule="evenodd"
            d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
            clipRule="evenodd"
          ></path>
        </svg>
      </div>
      <form action="submit" onSubmit={handleSubmit}>
        <input
          className="bg-slate-300 p-2"
          type="text"
          onChange={handleChange}
        />
        <button type="submit">Post</button>
      </form>
    </div>
  );
};