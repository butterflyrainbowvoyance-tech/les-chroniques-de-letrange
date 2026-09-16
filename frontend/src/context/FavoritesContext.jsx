import { createContext, useContext, useEffect, useState, useCallback } from "react";

const FavoritesContext = createContext(null);
const STORAGE_KEY = "biblio_secrete_favoris_v1";

export function FavoritesProvider({ children }) {
  const [ids, setIds] = useState([]);

  useEffect(() => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) setIds(JSON.parse(raw));
    } catch { /* ignore */ }
  }, []);

  const persist = useCallback((next) => {
    setIds(next);
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(next)); } catch { /* ignore */ }
  }, []);

  const toggle = useCallback((id) => {
    persist(ids.includes(id) ? ids.filter(x => x !== id) : [...ids, id]);
  }, [ids, persist]);

  const has = useCallback((id) => ids.includes(id), [ids]);

  return (
    <FavoritesContext.Provider value={{ ids, toggle, has }}>
      {children}
    </FavoritesContext.Provider>
  );
}

export const useFavorites = () => useContext(FavoritesContext);
