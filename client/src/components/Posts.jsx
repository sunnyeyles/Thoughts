const posts = [
  {
    userName: "user1",
    post: "Hello World!",
  },
  {
    userName: "user2",
    post: "Hello World    sdasdcasdcsdc",
  },
  {
    userName: "user3",
    post: "Hello there World",
  },
  {
    userName: "user4",
    post: "Hello World sdasdcsadcasdcasdc",
  },
];
import avatarPhoto from "../../dieter.jpeg";

export const Posts = () => {
  return (
    <div>
      <ul>
        {posts.map((e, index) => {
          // create unique id for the posts primary key
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
                <h5>{e.userName}</h5>
              </div>
              <div>
                <h5>{e.post}</h5>
              </div>
            </li>
          );
        })}
      </ul>
    </div>
  );
};
