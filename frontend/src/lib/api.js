import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

export const api = axios.create({ baseURL: API });

export const fetchUniverses = () => api.get("/universes").then(r => r.data);
export const fetchEras = () => api.get("/eras").then(r => r.data);
export const fetchRegions = () => api.get("/regions").then(r => r.data);
export const fetchStories = (params = {}) => api.get("/stories", { params }).then(r => r.data);
export const fetchStory = (id) => api.get(`/stories/${id}`).then(r => r.data);
export const fetchRelated = (id) => api.get(`/stories/${id}/related`).then(r => r.data);
export const fetchRandomStory = (exclude) => api.get("/stories/random", { params: exclude ? { exclude } : {} }).then(r => r.data);
export const fetchTimeline = () => api.get("/stories/timeline").then(r => r.data);
export const fetchMapPoints = () => api.get("/stories/map").then(r => r.data);
export const fetchQuizPool = (limit = 6) => api.get("/stories/quiz", { params: { limit } }).then(r => r.data);
export const fetchDossiers = (universeId) => api.get(`/dossiers/${universeId}`).then(r => r.data);
export const fetchPanoramas = () => api.get("/panoramas").then(r => r.data);
export const fetchPanorama = (id) => api.get(`/panoramas/${id}`).then(r => r.data);
