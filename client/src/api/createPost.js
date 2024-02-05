export const createPost = async (req) => {
  try {
    const { post } = req.body();
    axios.post("/api/new-post", post);
  } catch (error) {
    throw new error();
  }
};
