import { Link } from "react-router-dom";
import { Bookmark, ArrowUpRight } from "lucide-react";
import StatusBadge from "./StatusBadge";
import { useFavorites } from "@/context/FavoritesContext";

export default function StoryCard({ story }) {
  const { has, toggle } = useFavorites();
  const isFav = has(story.id);

  return (
    <article
      data-testid={`story-card-${story.id}`}
      className="group relative border border-copper/25 bg-[#0F1528]/60 hover-lift copper-frame overflow-hidden"
    >
      <Link to={`/recit/${story.id}`} className="block">
        {story.hero_image && (
          <div className="aspect-[16/10] overflow-hidden border-b border-copper/15 relative">
            <img
              src={story.hero_image}
              alt={story.title}
              loading="lazy"
              className="w-full h-full object-cover opacity-70 group-hover:opacity-90 group-hover:scale-[1.03] transition-[opacity,transform] duration-700"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-[#050814] via-transparent to-transparent" />
          </div>
        )}
        <div className="p-6">
          <div className="flex items-center justify-between gap-3 mb-4">
            <StatusBadge status={story.status_key || story.status} size="sm" />
            <span className="overline">{story.era_label}</span>
          </div>
          <h3 className="font-heading text-2xl leading-tight text-parchment group-hover:text-copper-light transition-colors duration-300">
            {story.title}
          </h3>
          {story.subtitle && (
            <p className="mt-2 italic text-copper-muted text-sm">{story.subtitle}</p>
          )}
          <p className="mt-4 text-sm text-parchment/70 leading-relaxed line-clamp-3">
            {story.excerpt}
          </p>
          <div className="mt-5 flex items-center gap-2 text-copper text-sm font-ui">
            <span>Lire le récit</span>
            <ArrowUpRight className="w-4 h-4" strokeWidth={1.5} />
          </div>
        </div>
      </Link>
      <button
        type="button"
        onClick={() => toggle(story.id)}
        data-testid={`fav-toggle-${story.id}`}
        aria-label={isFav ? "Retirer des favoris" : "Ajouter aux favoris"}
        className="absolute top-4 right-4 p-2 rounded-full bg-[#050814]/70 border border-copper/30 hover:border-copper text-parchment"
      >
        <Bookmark className={`w-4 h-4 ${isFav ? "fill-copper text-copper" : ""}`} strokeWidth={1.5} />
      </button>
    </article>
  );
}
