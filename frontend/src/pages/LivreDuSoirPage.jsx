import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Moon, ArrowUpRight, Bookmark } from "lucide-react";
import { fetchLivreDuSoir, fetchLivreDuSoirHistory } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";
import StoryCard from "@/components/StoryCard";
import AudioPlayer from "@/components/AudioPlayer";
import { useFavorites } from "@/context/FavoritesContext";

function formatDate(iso) {
  try {
    const d = new Date(iso + "T00:00:00Z");
    return d.toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" });
  } catch { return iso; }
}

export default function LivreDuSoirPage() {
  const [today, setToday] = useState(null);
  const [history, setHistory] = useState([]);
  const { has, toggle } = useFavorites();

  useEffect(() => {
    fetchLivreDuSoir().then(setToday).catch(() => {});
    fetchLivreDuSoirHistory(7).then(setHistory).catch(() => {});
  }, []);

  if (!today) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  const s = today.story;
  const isFav = has(s.id);
  const past = history.slice(1); // hide today from history

  return (
    <div className="pb-32" data-testid="livre-du-soir-page">
      <section className="relative border-b border-copper/15">
        <div className="absolute inset-0 -z-10">
          {s.hero_image && <img src={s.hero_image} alt="" className="w-full h-full object-cover opacity-30" />}
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/60 via-[#050814]/90 to-[#050814]" />
        </div>
        <div className="mx-auto max-w-5xl px-6 lg:px-10 py-20">
          <div className="inline-flex items-center gap-2 mb-8 px-3 py-1 border border-copper text-copper text-xs font-ui uppercase tracking-[0.2em] rounded-full">
            <Moon className="w-3 h-3" strokeWidth={2} /> Le livre du soir
          </div>
          <div className="overline mb-3">{formatDate(today.date)}</div>
          <p className="font-heading italic text-2xl sm:text-3xl text-copper-light mb-8">
            {today.greeting}
          </p>

          <article className="border border-copper/25 bg-[#0F1528]/60 copper-frame p-8 sm:p-10" data-testid="livre-du-soir-card">
            <StatusBadge status={s.status_key || s.status} />
            <h1 className="mt-6 font-heading font-light text-4xl sm:text-5xl text-parchment tracking-tight leading-[1.1]">
              {s.title}
            </h1>
            {s.subtitle && <p className="mt-3 italic text-copper-muted text-lg">{s.subtitle}</p>}
            <p className="mt-8 font-heading italic text-xl sm:text-2xl text-parchment/90 leading-relaxed">
              {s.excerpt}
            </p>

            <div className="mt-8">
              <AudioPlayer storyId={s.id} />
            </div>

            <div className="mt-10 flex flex-wrap gap-3">
              <Link to={`/recit/${s.id}`} data-testid="livre-du-soir-open" className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light">
                Lire la chronique <ArrowUpRight className="w-4 h-4" strokeWidth={2} />
              </Link>
              <button type="button" onClick={() => toggle(s.id)} data-testid="livre-du-soir-fav" className="inline-flex items-center gap-2 px-6 py-3 border border-copper text-copper font-ui text-sm uppercase tracking-widest hover:bg-copper/10">
                <Bookmark className={`w-4 h-4 ${isFav ? "fill-copper" : ""}`} strokeWidth={1.5} />
                {isFav ? "Dans ma bibliothèque" : "Garder pour plus tard"}
              </button>
            </div>
          </article>

          <p className="mt-8 text-sm text-copper-muted italic max-w-2xl">
            Une chronique différente chaque soir, tirée automatiquement des 45 récits de la bibliothèque.
            Revenez demain pour la suivante.
          </p>
        </div>
      </section>

      {past.length > 0 && (
        <section className="mx-auto max-w-7xl px-6 lg:px-10 pt-16" data-testid="livre-du-soir-history">
          <div className="overline mb-3">Ces derniers soirs</div>
          <h2 className="font-heading text-3xl sm:text-4xl text-parchment mb-10">Ce que la bibliothèque a proposé</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {past.map(entry => (
              <div key={entry.date} className="relative">
                <div className="absolute -top-3 left-4 z-10 px-3 py-0.5 bg-[#050814] border border-copper/40 text-copper text-[0.65rem] font-ui uppercase tracking-widest rounded">
                  {formatDate(entry.date)}
                </div>
                <StoryCard story={entry.story} />
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
