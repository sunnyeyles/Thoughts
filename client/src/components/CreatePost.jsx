import React, { useState, useEffect } from "react";
import avatarPhoto from "../../dieter.jpeg";
import { createPost } from "../api/createPost";
import { v4 as uuidv4 } from "uuid";

export const CreatePost = () => {
  const [post, setPost] = useState("");
  const [file, setFile] = useState(null);
  const [submittedData, setSubmittedData] = useState("");
  const handleChange = (e) => {
    setPost(e.target.value);
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  useEffect(() => {}, [submittedData]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmittedData(post);

    try {
      await createPost({ post, userId: uuidv4(), file });
    } catch (error) {
      console.error("Error submitting post:", error);
    }
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
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <input
          className="bg-slate-300 p-2"
          type="text"
          onChange={handleChange}
          value={post}
        />

        <label
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          htmlFor="file_input"
        >
          Upload file
        </label>
        <input
          className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
          id="file_input"
          type="file"
          onChange={handleFileChange}
        />

        <button type="submit">Post</button>
      </form>
    </div>
  );
};
