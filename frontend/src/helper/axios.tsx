import axios from "axios";

export default axios.create({
    baseURL: "https://il8rigour.com/",
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});
