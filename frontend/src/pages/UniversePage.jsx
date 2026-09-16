import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { ChevronLeft } from "lucide-react";
import { fetchStories, fetchUniverses } from "@/lib/api";
import StoryCard from "@/components/StoryCard";

export default function UniversePage() {
  const { universeId } = useParams();
  const [stories, setStories] = useState([]);
  const [universe, setUniverse] = useState(null);

  useEffect(() => {
    fetchStories({ universe: universeId }).then(setStories).catch(() => {});
    fetchUniverses().then(list => setUniverse(list.find(u => u.id === universeId))).catch(() => {});
  }, [universeId]);

  if (!universe) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  return (
    <div className="pb-24" data-testid="universe-page">
      <section className="relative border-b border-copper/15">
        <div className="absolute inset-0 -z-10">
          <img src={universe.image} alt="" className="w-full h-full object-cover opacity-25" />
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/60 via-[#050814]/85 to-[#050814]" />
        </div>
        <div className="mx-auto max-w-7xl px-6 lg:px-10 py-20">
          <Link to="/" className="inline-flex items-center gap-2 text-sm font-ui text-copper-muted hover:text-copper mb-8">
            <ChevronLeft className="w-4 h-4" strokeWidth={1.5} /> Bibliothèque
          </Link>
          <div className="overline text-copper mb-6">{universe.story_count} récit{universe.story_count > 1 ? "s" : ""}</div>
          <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight max-w-4xl leading-[1.05]">
            {universe.title}
          </h1>
          <p className="mt-6 italic text-copper-muted text-lg">{universe.subtitle}</p>
          <p className="mt-6 max-w-2xl text-parchment/75 leading-relaxed">{universe.description}</p>
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-6 lg:px-10 pt-14">
        {stories.length === 0 && (
          <div className="text-center py-20 text-copper-muted italic">Aucun récit encore. Ce dossier grandira bientôt.</div>
        )}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {stories.map(s => <StoryCard key={s.id} story={s} />)}
        </div>
      </section>
    </div>
  );
}
