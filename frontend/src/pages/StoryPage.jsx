import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { ChevronLeft, Bookmark, MapPin, Calendar, CheckCircle2, HelpCircle, XCircle, Clock } from "lucide-react";
import LiteMarkdown from "@/components/lite-markdown";
import { fetchStory, fetchRelated } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";
import StoryCard from "@/components/StoryCard";
import AudioPlayer from "@/components/AudioPlayer";
import { useFavorites } from "@/context/FavoritesContext";

const VERDICT_COLORS = {
  "Attesté":         { icon: CheckCircle2, cls: "text-[#8FB4A1] border-[#4A6B5D]/60 bg-[#4A6B5D]/15" },
  "Probable":        { icon: CheckCircle2, cls: "text-[#C4A87A] border-[#6B5D4A]/60 bg-[#6B5D4A]/15" },
  "Contesté":        { icon: HelpCircle,   cls: "text-[#C48FA9] border-[#6B4A5D]/60 bg-[#6B4A5D]/15" },
  "Non prouvé":      { icon: XCircle,      cls: "text-[#8FA9C4] border-[#4A5D6B]/60 bg-[#4A5D6B]/15" },
  "Légende tardive": { icon: XCircle,      cls: "text-[#C48FA9] border-[#6B4A5D]/60 bg-[#6B4A5D]/15" },
};

export default function StoryPage() {
  const { storyId } = useParams();
  const [story, setStory] = useState(null);
  const [related, setRelated] = useState([]);
  const [error, setError] = useState(false);
  const { has, toggle } = useFavorites();

  useEffect(() => {
    setStory(null); setRelated([]); setError(false);
    fetchStory(storyId).then(setStory).catch(() => setError(true));
    fetchRelated(storyId).then(setRelated).catch(() => setRelated([]));
    window.scrollTo({ top: 0, behavior: "instant" });
  }, [storyId]);

  if (error) return <div className="p-16 text-center text-copper-muted">Récit introuvable.</div>;
  if (!story) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  const isFav = has(story.id);
  const isLegendVsArchives = story.format === "legende-vs-archives";
  const isIlsYCroyaient = story.format === "ils-y-croyaient";

  return (
    <article className="pb-32" data-testid={`story-page-${story.id}`}>
<div className="relative z-10 mx-auto w-full max-w-5xl px-6 lg:px-10 py-20 lg:py-28">
        <div className="absolute inset-0 -z-10">
        <div  className="w-full h-full object-cover opacity-40 scale-[1.02]"
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/60 via-[#050814]/90 to-[#050814]" />
        </div>
<section className="mx-auto max-w-4xl px-6 lg:px-10 pt-16 pb-10">
  <div className="rounded-2xl border border-cuivre/20 bg-[#0B1020]/70 backdrop-blur-sm p-7 lg:p-10 shadow-[0_20px_60px_rgba(0,0,0,0.25)]">
    </div>
          <Link to={`/univers/${story.universe}`} className="inline-flex items-center gap-2 text-sm font-ui text-copper-muted hover:text-copper mb-8">
            <ChevronLeft className="w-4 h-4" strokeWidth={1.5} /> {story.universe.replace(/-/g, " ")}
          </Link>

          {isLegendVsArchives && (
            <div className="inline-flex items-center gap-2 mb-4 px-3 py-1 border border-copper text-copper text-xs font-ui uppercase tracking-[0.2em] rounded-full">
              La légende contre les archives
            </div>
          )}
          {isIlsYCroyaient && (
            <div className="inline-flex items-center gap-2 mb-4 px-3 py-1 border border-copper text-copper text-xs font-ui uppercase tracking-[0.2em] rounded-full">
              <Clock className="w-3 h-3" strokeWidth={2} /> Ils y croyaient vraiment
            </div>
          )}

          <StatusBadge status={story.status_key || story.status} />

          <h1 className="mt-6 font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
            {story.title}
          </h1>
          {story.subtitle && <p className="mt-4 italic text-copper-muted text-xl">{story.subtitle}</p>}

          <div className="mt-8 flex flex-wrap gap-6 text-sm font-ui text-parchment/70">
            {story.era_label && (<span className="inline-flex items-center gap-2"><Calendar className="w-4 h-4 text-copper" strokeWidth={1.5} /> {story.era_label}</span>)}
            {story.region && (<span className="inline-flex items-center gap-2"><MapPin className="w-4 h-4 text-copper" strokeWidth={1.5} /> {story.region}</span>)}
            <button type="button" onClick={() => toggle(story.id)} data-testid={`fav-toggle-${story.id}`} className="inline-flex items-center gap-2 text-copper hover:text-copper-light">
              <Bookmark className={`w-4 h-4 ${isFav ? "fill-copper" : ""}`} strokeWidth={1.5} />
              {isFav ? "Retirer de ma bibliothèque" : "Ajouter à ma bibliothèque"}
            </button>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-3xl px-6 lg:px-10 pt-16">
        <AudioPlayer
storyId={story.id}
text={
story.sections?.length
? story.sections
.flatMap(section =>
Array.isArray(section.paragraphs) ? section.paragraphs : []
)
.join(" ")
: Array.isArray(story.content)
? story.content.join(" ")
: (story.content || "")
}
/>

        {story.specs && story.specs.length > 0 && (
          <div className="mt-10 border border-copper/30 bg-[#050814] copper-frame p-6" data-testid="specs-block">
            <div className="flex items-center justify-between mb-4">
              <div className="overline">Fiche technique</div>
              {story.place_type && <span className="text-xs font-ui uppercase tracking-widest text-copper">{story.place_type}</span>}
            </div>
            <dl className="grid sm:grid-cols-2 gap-x-6 gap-y-3">
              {story.specs.map((sp, i) => (
                <div key={i} className="grid grid-cols-[110px_1fr] gap-3 items-baseline">
                  <dt className="text-[0.65rem] font-ui uppercase tracking-widest text-copper-muted">{sp.label}</dt>
                  <dd className="text-sm text-parchment/85 leading-snug">{sp.value}</dd>
                </div>
              ))}
            </dl>
          </div>
        )}

        <p className="mt-10 font-heading text-2xl sm:text-3xl italic text-copper-light leading-relaxed">
          {story.excerpt}
        </p>

        <div className="divider-copper my-12" />

        {/* Content: sections take priority if present */}
        {story.sections && story.sections.length > 0 ? (
          <div className="space-y-14">
            {story.sections.map((sec, i) => (
              <div key={i} data-testid={`story-section-${i}`}>
                <div className="overline mb-3">Section {i + 1}</div>
                <h2 className="font-heading text-3xl text-parchment mb-6">{sec.title}</h2>
                <div className="narrative">
                  {(sec.paragraphs || []).map((p, j) => (<LiteMarkdown key={j}>{p}</LiteMarkdown>))}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="narrative">
            {(story.content || []).map((p, i) => (<LiteMarkdown key={i}>{p}</LiteMarkdown>))}
          </div>
        )}

        {/* Verdict block for "légende vs archives" */}
        {story.verdict && story.verdict.length > 0 && (
          <div className="mt-16 border border-copper/30 copper-frame p-8 bg-[#050814]" data-testid="verdict-block">
            <div className="overline mb-6">Le verdict, point par point</div>
            <ul className="space-y-4">
              {story.verdict.map((v, i) => {
                const cfg = VERDICT_COLORS[v.label] || VERDICT_COLORS["Contesté"];
                const Icon = cfg.icon;
                return (
                  <li key={i} className="grid grid-cols-[auto_1fr] gap-4 items-start">
                    <span className={`inline-flex items-center gap-1.5 px-3 py-1 text-[0.65rem] font-ui uppercase tracking-[0.2em] border rounded-full whitespace-nowrap ${cfg.cls}`}>
                      <Icon className="w-3 h-3" strokeWidth={2} /> {v.label}
                    </span>
                    <p className="text-parchment/80 text-sm leading-relaxed pt-1">{v.text}</p>
                  </li>
                );
              })}
            </ul>
          </div>
        )}

        {story.sources && story.sources.length > 0 && (
          <div className="mt-16 border-t border-copper/20 pt-8">
            <div className="overline mb-4">Pour aller plus loin</div>
            <ul className="space-y-3 font-ui text-sm text-parchment/70">
              {story.sources.map((src, i) => (<li key={i} className="pl-4 border-l border-copper/40">{src}</li>))}
            </ul>
          </div>
        )}

        {story.tags && (
          <div className="mt-10 flex flex-wrap gap-2">
            {story.tags.map(t => (
              <Link to={`/recherche?q=${encodeURIComponent(t)}`} key={t} data-testid={`tag-${t}`} className="px-3 py-1 text-xs font-ui uppercase tracking-widest border border-copper/25 text-copper-muted rounded-full hover:border-copper hover:text-copper">
                {t}
              </Link>
            ))}
          </div>
        )}
      </section>

      {related.length > 0 && (
        <section className="mx-auto max-w-7xl px-6 lg:px-10 mt-24" data-testid="related-section">
          <div className="overline mb-3">Continuer l'exploration</div>
          <h2 className="font-heading text-3xl sm:text-4xl text-parchment mb-10">Récits en résonance</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {related.map(s => <StoryCard key={s.id} story={s} />)}
          </div>
        </section>
      )}
    </article>
  );
}
