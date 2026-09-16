import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { ChevronLeft, Sparkle, Anchor, Waves, Clock, GitCompare } from "lucide-react";
import { fetchOrigine } from "@/lib/api";
import LiteMarkdown from "@/components/lite-markdown";

const ICONS = [Anchor, Waves, Clock, GitCompare];

export default function OrigineDetailPage() {
  const { origineId } = useParams();
  const [o, setO] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    setO(null); setError(false);
    fetchOrigine(origineId).then(setO).catch(() => setError(true));
    window.scrollTo({ top: 0, behavior: "instant" });
  }, [origineId]);

  if (error) return <div className="p-16 text-center text-copper-muted">Dossier introuvable.</div>;
  if (!o) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  return (
    <article className="pb-32" data-testid={`origine-page-${o.id}`}>
      <section className="relative border-b border-copper/15">
        <div className="absolute inset-0 -z-10">
          <img src={o.hero_image} alt="" className="w-full h-full object-cover opacity-30" />
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/60 via-[#050814]/90 to-[#050814]" />
        </div>
        <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16">
          <Link to="/origine" className="inline-flex items-center gap-2 text-sm font-ui text-copper-muted hover:text-copper mb-8">
            <ChevronLeft className="w-4 h-4" strokeWidth={1.5} /> Tous les dossiers
          </Link>

          <div className="inline-flex items-center gap-2 mb-4 px-3 py-1 border border-copper text-copper text-xs font-ui uppercase tracking-[0.2em] rounded-full">
            <Sparkle className="w-3 h-3" strokeWidth={2} /> À l'origine de
          </div>

          <h1 className="mt-2 font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
            {o.symbol}
          </h1>
          <p className="mt-4 italic text-copper-muted text-xl">{o.hook}</p>
          <p className="mt-6 text-parchment/80 leading-relaxed text-lg">{o.one_liner}</p>
        </div>
      </section>

      <section className="mx-auto max-w-3xl px-6 lg:px-10 pt-16 space-y-14">
        {o.sections.map((sec, i) => {
          const Icon = ICONS[i] || Anchor;
          return (
            <div key={i} data-testid={`origine-section-${i}`}>
              <div className="flex items-center gap-3 mb-4">
                <Icon className="w-5 h-5 text-copper" strokeWidth={1.5} />
                <div className="overline">Étape {i + 1}</div>
              </div>
              <h2 className="font-heading text-3xl text-parchment mb-6">{sec.title}</h2>
              <div className="narrative">
                {(sec.paragraphs || []).map((p, j) => (<LiteMarkdown key={j}>{p}</LiteMarkdown>))}
              </div>
            </div>
          );
        })}

        {o.sources && o.sources.length > 0 && (
          <div className="mt-16 border-t border-copper/20 pt-8">
            <div className="overline mb-4">Pour aller plus loin</div>
            <ul className="space-y-3 font-ui text-sm text-parchment/70">
              {o.sources.map((src, i) => (<li key={i} className="pl-4 border-l border-copper/40">{src}</li>))}
            </ul>
          </div>
        )}

        {o.tags && (
          <div className="mt-10 flex flex-wrap gap-2">
            {o.tags.map(t => (
              <Link to={`/recherche?q=${encodeURIComponent(t)}`} key={t} className="px-3 py-1 text-xs font-ui uppercase tracking-widest border border-copper/25 text-copper-muted rounded-full hover:border-copper hover:text-copper">
                {t}
              </Link>
            ))}
          </div>
        )}
      </section>
    </article>
  );
}
