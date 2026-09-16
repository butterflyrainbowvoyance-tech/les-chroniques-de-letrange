import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

export const api = axios.create({ baseURL: API });

export const fetchUniverses = () => api.get("/universes").then(r => r.data);
export const fetchEras = () => api.get("/eras").then(r => r.data);
export const fetchStories = (params = {}) => api.get("/stories", { params }).then(r => r.data);
export const fetchStory = (id) => api.get(`/stories/${id}`).then(r => r.data);
export const fetchRandomStory = () => api.get("/stories/random").then(r => r.data);
export const fetchTimeline = () => api.get("/stories/timeline").then(r => r.data);
export const fetchMapPoints = () => api.get("/stories/map").then(r => r.data);
export const fetchQuizPool = (limit = 5) => api.get("/stories/quiz", { params: { limit } }).then(r => r.data);
