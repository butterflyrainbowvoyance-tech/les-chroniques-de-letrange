import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Bookmark } from "lucide-react";
import { useFavorites } from "@/context/FavoritesContext";
import { fetchStories } from "@/lib/api";
import StoryCard from "@/components/StoryCard";

export default function FavoritesPage() {
  const { ids } = useFavorites();
  const [stories, setStories] = useState([]);

  useEffect(() => {
    fetchStories({ limit: 200 }).then(all => {
      setStories(all.filter(s => ids.includes(s.id)));
    }).catch(() => {});
  }, [ids]);

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="favorites-page">
      <div className="overline mb-4">Votre coin de bibliothèque</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight max-w-3xl leading-[1.05]">
        Ma bibliothèque personnelle.
      </h1>
      <p className="mt-6 max-w-2xl text-parchment/70 leading-relaxed">
        Vos récits mis de côté. Ils sont sauvegardés dans votre navigateur — aucune inscription.
      </p>

      {ids.length === 0 ? (
        <div className="mt-16 border border-copper/20 p-16 text-center copper-frame">
          <Bookmark className="w-8 h-8 text-copper mx-auto mb-4" strokeWidth={1.2} />
          <p className="text-copper-muted italic">Aucun récit dans votre bibliothèque pour l'instant.</p>
          <Link to="/" className="mt-6 inline-flex items-center gap-2 px-5 py-2.5 border border-copper text-copper font-ui text-xs uppercase tracking-widest hover:bg-copper/10">
            Découvrir des récits
          </Link>
        </div>
      ) : (
        <div className="mt-14 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {stories.map(s => <StoryCard key={s.id} story={s} />)}
        </div>
      )}
    </div>
  );
}
