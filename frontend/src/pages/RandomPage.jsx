import { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import { Sparkles, RefreshCw } from "lucide-react";
import { fetchRandomStory } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";

export default function RandomPage() {
  const [story, setStory] = useState(null);
  const [loading, setLoading] = useState(false);

  const pick = useCallback(() => {
    setLoading(true);
    fetchRandomStory().then(setStory).catch(() => {}).finally(() => setLoading(false));
  }, []);

  useEffect(() => { pick(); }, [pick]);

  return (
    <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16" data-testid="random-page">
      <div className="text-center">
        <Sparkles className="w-10 h-10 text-copper mx-auto animate-flicker" strokeWidth={1.2} />
        <div className="overline mt-4 mb-3">Raconte-moi</div>
        <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight">
          quelque chose d'étrange.
        </h1>
        <p className="mt-6 text-parchment/70 max-w-xl mx-auto leading-relaxed">
          Un récit tiré au hasard. On indique toujours son statut : fait attesté, tradition, légende ou hypothèse.
          Puis on clique pour en obtenir un nouveau.
        </p>
        <button
          type="button"
          onClick={pick}
          disabled={loading}
          data-testid="random-refresh"
          className="mt-8 inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light disabled:opacity-50 transition-colors"
        >
          <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin" : ""}`} strokeWidth={2} />
          Un autre récit
        </button>
      </div>

      {story && (
        <article className="mt-16 border border-copper/25 bg-[#0F1528]/60 copper-frame p-10 animate-fade-up" data-testid="random-card">
          <StatusBadge status={story.status_key || story.status} />
          <h2 className="mt-4 font-heading text-4xl text-parchment leading-tight">{story.title}</h2>
          {story.subtitle && <p className="mt-2 italic text-copper-muted">{story.subtitle}</p>}
          <p className="mt-6 font-heading italic text-xl text-copper-light leading-relaxed">{story.excerpt}</p>
          <div className="divider-copper my-8" />
          <div className="text-sm text-parchment/70 leading-relaxed">
            {(story.content || []).slice(0, 2).map((p, i) => (
              <p key={i} className="mb-4">{p.replace(/\*\*/g, "").replace(/\*/g, "")}</p>
            ))}
          </div>
          <Link to={`/recit/${story.id}`} className="mt-8 inline-flex items-center gap-2 px-5 py-2.5 border border-copper text-copper font-ui text-xs uppercase tracking-widest hover:bg-copper/10">
            Lire le récit complet
          </Link>
        </article>
      )}
    </div>
  );
}
