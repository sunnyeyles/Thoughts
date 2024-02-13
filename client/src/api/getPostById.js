import axios from "axios";

export const getPostById = async () => {
  const postId = "dsferfsdfvdsfesfsdr";
  const response = await axios.get(`/api/get-post-by-id?id=${postId}`);
  console.log(response.data);
};
