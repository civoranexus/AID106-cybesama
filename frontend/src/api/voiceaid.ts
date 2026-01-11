import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const fetchScheme = async (schemeName: string) => {
  const res = await api.get(`/schemes/${schemeName}`);
  return res.data;
};
