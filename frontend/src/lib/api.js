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
export const fetchOrigines = () => api.get("/origines").then(r => r.data);
export const fetchOrigine = (id) => api.get(`/origines/${id}`).then(r => r.data);
export const fetchLivreDuSoir = () => api.get("/livre-du-soir").then(r => r.data);
export const fetchLivreDuSoirHistory = (days = 7) => api.get("/livre-du-soir/history", { params: { days } }).then(r => r.data);

// Reviews
export const fetchReviews = () => api.get("/reviews").then(r => r.data);
export const fetchReviewsSummary = () => api.get("/reviews/summary").then(r => r.data);
export const postReview = (payload) => api.post("/reviews", payload).then(r => r.data);
// Témoignages
export const fetchTemoignages = () => api.get("/temoignages").then(r => r.data);
export const postTemoignage = (payload) => api.post("/temoignages", payload).then(r => r.data);
// Admin
export const adminHeaders = (token) => ({ headers: { Authorization: `Bearer ${token}` } });
export const adminCheck = (token) => api.get("/admin/check", adminHeaders(token)).then(r => r.data);
export const adminListStories = (token) => api.get("/admin/stories", adminHeaders(token)).then(r => r.data);
export const adminCreateStory = (token, payload) => api.post("/admin/stories", payload, adminHeaders(token)).then(r => r.data);
export const adminEditStory = (token, id, payload) => api.patch(`/admin/stories/${id}`, payload, adminHeaders(token)).then(r => r.data);
export const adminDeleteStory = (token, id) => api.delete(`/admin/stories/${id}`, adminHeaders(token)).then(r => r.data);
export const adminListReviews = (token) => api.get("/admin/reviews", adminHeaders(token)).then(r => r.data);
export const adminModerateReview = (token, id, payload) => api.patch(`/admin/reviews/${id}`, payload, adminHeaders(token)).then(r => r.data);
export const adminDeleteReview = (token, id) => api.delete(`/admin/reviews/${id}`, adminHeaders(token)).then(r => r.data);
export const adminListTemoignages = (token) => api.get("/admin/temoignages", adminHeaders(token)).then(r => r.data);
export const adminModerateTemoignage = (token, id, payload) => api.patch(`/admin/temoignages/${id}`, payload, adminHeaders(token)).then(r => r.data);
export const adminDeleteTemoignage = (token, id) => api.delete(`/admin/temoignages/${id}`, adminHeaders(token)).then(r => r.data);
// Collaborations
export const postCollaboration = (payload) => api.post("/collaborations", payload).then(r => r.data);
export const postEnquete = (payload) => api.post("/enquetes", payload).then(r => r.data);
export const adminListCollaborations = (token) => api.get("/admin/collaborations", adminHeaders(token)).then(r => r.data);
export const adminModCollaboration = (token, id, payload) => api.patch(`/admin/collaborations/${id}`, payload, adminHeaders(token)).then(r => r.data);
export const adminDeleteCollaboration = (token, id) => api.delete(`/admin/collaborations/${id}`, adminHeaders(token)).then(r => r.data);
export const adminListEnquetes = (token) => api.get("/admin/enquetes", adminHeaders(token)).then(r => r.data);
export const adminModEnquete = (token, id, payload) => api.patch(`/admin/enquetes/${id}`, payload, adminHeaders(token)).then(r => r.data);
export const adminDeleteEnquete = (token, id) => api.delete(`/admin/enquetes/${id}`, adminHeaders(token)).then(r => r.data);
