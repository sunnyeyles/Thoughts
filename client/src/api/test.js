import axios from "axios";

export const addUser = async (userData) => {
  try {
    const response = await axios.post("api/add-user", userData);
    return response.data;
  } catch (error) {
    throw new Error("Failed to add user");
  }
};
