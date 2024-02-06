import axios from "axios";

export const createPost = async (req) => {
  try {
    const { body } = req;
    if (!body || !body.post || !body.userId) {
      throw new Error("Invalid request body");
    }

    const { post, userId } = body;
    await axios.post("/api/new-post", { post, userId });
  } catch (error) {
    console.error("Error in createPost:", error);
    throw new Error("Error in createPost");
  }
};
