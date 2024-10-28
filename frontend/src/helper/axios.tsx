import axios from "axios";

export default axios.create({
    baseURL: "https://il8lc.com/",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});
