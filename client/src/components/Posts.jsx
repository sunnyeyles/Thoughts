import { useState, useEffect } from "react";
import { getAllPosts } from "../api/getAllPosts";

import avatarPhoto from "../../dieter.jpeg";

export const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getAllPosts();
        setPosts(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);
  return (
    <div>
      <ul>
        {posts.map((e, index) => {
          return (
            <li className="m-12 p-6 border" key={index}>
              <div className="flex gap-6">
                <div className="relative">
                  <img
                    className="w-10 h-10 rounded-full shadow-2xl"
                    src={avatarPhoto}
                    alt=""
                  />
                  <span className="top-0 left-7 absolute  w-3.5 h-3.5 bg-green-400 shadow-2xl rounded-full"></span>
                </div>
                <h5>{e[0]}</h5>
              </div>
              <div>
                <h5>{e[1]}</h5>
              </div>
              <img href={e[2]} alt="image" />
            </li>
          );
        })}
      </ul>
    </div>
  );
};
