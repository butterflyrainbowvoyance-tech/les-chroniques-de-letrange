import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { ChevronLeft, Bookmark, MapPin, Calendar } from "lucide-react";
import ReactMarkdown from "@/components/lite-markdown";
import { fetchStory } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";
import { useFavorites } from "@/context/FavoritesContext";

export default function StoryPage() {
  const { storyId } = useParams();
  const [story, setStory] = useState(null);
  const [error, setError] = useState(false);
  const { has, toggle } = useFavorites();

  useEffect(() => {
    setStory(null);
    setError(false);
    fetchStory(storyId).then(setStory).catch(() => setError(true));
    window.scrollTo({ top: 0, behavior: "instant" });
  }, [storyId]);

  if (error) return <div className="p-16 text-center text-copper-muted">Récit introuvable.</div>;
  if (!story) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  const isFav = has(story.id);

  return (
    <article className="pb-32" data-testid={`story-page-${story.id}`}>
      <section className="relative border-b border-copper/15">
        <div className="absolute inset-0 -z-10">
          {story.hero_image && (
            <img src={story.hero_image} alt="" className="w-full h-full object-cover opacity-30" />
          )}
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/60 via-[#050814]/90 to-[#050814]" />
        </div>
        <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16">
          <Link to={`/univers/${story.universe}`} className="inline-flex items-center gap-2 text-sm font-ui text-copper-muted hover:text-copper mb-8">
            <ChevronLeft className="w-4 h-4" strokeWidth={1.5} /> {story.universe.replace(/-/g, " ")}
          </Link>

          <StatusBadge status={story.status_key || story.status} />

          <h1 className="mt-6 font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
            {story.title}
          </h1>
          {story.subtitle && <p className="mt-4 italic text-copper-muted text-xl">{story.subtitle}</p>}

          <div className="mt-8 flex flex-wrap gap-6 text-sm font-ui text-parchment/70">
            {story.era_label && (
              <span className="inline-flex items-center gap-2"><Calendar className="w-4 h-4 text-copper" strokeWidth={1.5} /> {story.era_label}</span>
            )}
            {story.region && (
              <span className="inline-flex items-center gap-2"><MapPin className="w-4 h-4 text-copper" strokeWidth={1.5} /> {story.region}</span>
            )}
            <button
              type="button"
              onClick={() => toggle(story.id)}
              data-testid={`fav-toggle-${story.id}`}
              className="inline-flex items-center gap-2 text-copper hover:text-copper-light"
            >
              <Bookmark className={`w-4 h-4 ${isFav ? "fill-copper" : ""}`} strokeWidth={1.5} />
              {isFav ? "Retiré de ma bibliothèque" : "Ajouter à ma bibliothèque"}
            </button>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-3xl px-6 lg:px-10 pt-16">
        <p className="font-heading text-2xl sm:text-3xl italic text-copper-light leading-relaxed">
          {story.excerpt}
        </p>

        <div className="divider-copper my-12" />

        <div className="narrative">
          {(story.content || []).map((p, i) => (
            <ReactMarkdown key={i}>{p}</ReactMarkdown>
          ))}
        </div>

        {story.sources && story.sources.length > 0 && (
          <div className="mt-16 border-t border-copper/20 pt-8">
            <div className="overline mb-4">Pour aller plus loin</div>
            <ul className="space-y-3 font-ui text-sm text-parchment/70">
              {story.sources.map((src, i) => (
                <li key={i} className="pl-4 border-l border-copper/40">{src}</li>
              ))}
            </ul>
          </div>
        )}

        {story.tags && (
          <div className="mt-10 flex flex-wrap gap-2">
            {story.tags.map(t => (
              <span key={t} className="px-3 py-1 text-xs font-ui uppercase tracking-widest border border-copper/25 text-copper-muted rounded-full">{t}</span>
            ))}
          </div>
        )}
      </section>
    </article>
  );
}
