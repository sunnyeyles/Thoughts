import axios from "axios";

export const createPost = async (req) => {
  try {
    const { body } = req;
    console.log(body);
    if (!body || !body.post || !body.userId) {
      throw new Error("Invalid request body");
    }

    const { post, userId, file } = body;
    const formData = new FormData();
    formData.append("post", post);
    formData.append("userId", userId);
    if (file) {
      formData.append("imageFile", file);
    }

    await axios.post("/api/create-post", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  } catch (error) {
    console.error("Error in createPost:", error);
    throw new Error("Error in createPost");
  }
};
