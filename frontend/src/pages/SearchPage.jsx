import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { fetchStories } from "@/lib/api";
import StoryCard from "@/components/StoryCard";

export default function SearchPage() {
  const [params] = useSearchParams();
  const q = params.get("q") || "";
  const [results, setResults] = useState([]);

  useEffect(() => {
    if (!q) { setResults([]); return; }
    fetchStories({ search: q, limit: 100 }).then(setResults).catch(() => {});
  }, [q]);

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="search-page">
      <div className="overline mb-3">Recherche</div>
      <h1 className="font-heading font-light text-4xl sm:text-5xl text-parchment tracking-tight">
        « {q} » — {results.length} résultat{results.length > 1 ? "s" : ""}
      </h1>

      {results.length === 0 && q && (
        <p className="mt-10 text-copper-muted italic">Aucun récit ne correspond à votre recherche pour l'instant.</p>
      )}

      <div className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {results.map(s => <StoryCard key={s.id} story={s} />)}
      </div>
    </div>
  );
}
