import axios from "axios";
export const getAllPosts = async () => {
  try {
    const data = await axios.get("/api/get-all-posts");
    return data;
  } catch (error) {
    console.error(error);
  }
};
