import axios from "axios";

export const getGtaData = async () => {
  try {
    const year = 1997;
    const data = await axios.get(`/api/by-year?year=${year}`);
    console.log(data);
  } catch (error) {
    throw new Error();
  }
};
