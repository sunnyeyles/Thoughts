import { useState } from "react";
import { addUser } from "../api/test";
export const SignUp = () => {
  const [userDetails, setUserDetails] = useState({});
  const [submittedData, setSubmittedData] = useState(null);

  const handleChange = (e) => {
    setUserDetails({ ...userDetails, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmittedData(userDetails);
    console.log("Submitted Data:", userDetails);
    addUser(userDetails);
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="flex flex-col p-12 m-12">
        <label htmlFor="email">email</label>
        <input
          type="email"
          name="email"
          onChange={handleChange}
          className="border-2 border-black rounded p-2"
        />
        <label htmlFor="name">name</label>
        <input
          type="text"
          name="name"
          onChange={handleChange}
          className="border-2 border-black rounded p-2"
        />
        <label htmlFor="city">city</label>
        <input
          type="text"
          name="city"
          onChange={handleChange}
          className="border-2 border-black rounded p-2"
        />
        <button
          type="submit"
          className="border-2 border-black rounded my-6 p-4"
        >
          Submit
        </button>
      </form>
    </div>
  );
};
