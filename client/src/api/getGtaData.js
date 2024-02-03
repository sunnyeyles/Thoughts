// import axios from "axios";
// export const getGtaData = async () => {
//   try {
//     const data = await axios.get("/api/gta");
//     console.log(data);
//   } catch (error) {
//     throw new error();
//   }
// };
import axios from "axios";

export const getGtaData = async () => {
  try {
    const year = 1997; // Replace with the actual year from your client side
    const data = await axios.get(`/api/by-year?year=${year}`);
    console.log(data);
  } catch (error) {
    throw new Error();
  }
};
