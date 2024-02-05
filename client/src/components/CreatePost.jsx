import avatarPhoto from "../../dieter.jpeg";
const imagePresent = true;

export const CreatePost = () => {
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
      <div class="relative w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600">
        <svg
          class="absolute w-12 h-12 text-gray-400"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </div>

      <input className="bg-slate-300 p-2" type="text" />
    </div>
  );
};
