import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { ChevronLeft, Eye, Wand2, Users, Gem, Skull } from "lucide-react";
import { fetchPanorama } from "@/lib/api";
import StoryCard from "@/components/StoryCard";

const PANELS = [
  { key: "belief",   label: "Ce que l'on croyait",    icon: Eye },
  { key: "practice", label: "Ce que l'on pratiquait", icon: Wand2 },
  { key: "consult",  label: "Qui l'on consultait",    icon: Users },
  { key: "objects",  label: "Les objets du quotidien", icon: Gem },
  { key: "fear",     label: "Ce que l'on craignait",  icon: Skull },
];

export default function VoyageEraPage() {
  const { eraId } = useParams();
  const [pano, setPano] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    setPano(null); setError(false);
    fetchPanorama(eraId).then(setPano).catch(() => setError(true));
    window.scrollTo({ top: 0, behavior: "instant" });
  }, [eraId]);

  if (error) return <div className="p-16 text-center text-copper-muted">Époque introuvable.</div>;
  if (!pano) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  return (
    <div className="pb-32" data-testid={`voyage-era-${pano.id}`}>
      <section className="relative border-b border-copper/15">
        <div className="absolute inset-0 -z-10">
          <img src={pano.hero_image} alt="" className="w-full h-full object-cover opacity-30" />
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/60 via-[#050814]/90 to-[#050814]" />
        </div>
        <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16">
          <Link to="/voyage" className="inline-flex items-center gap-2 text-sm font-ui text-copper-muted hover:text-copper mb-8">
            <ChevronLeft className="w-4 h-4" strokeWidth={1.5} /> Toutes les époques
          </Link>
          <div className="overline mb-4 text-copper">{pano.period}</div>
          <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
            {pano.label}
          </h1>
          <p className="mt-6 italic text-copper-light text-xl">{pano.tagline}</p>
          <p className="mt-6 text-parchment/80 leading-relaxed text-lg">{pano.intro}</p>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-6 lg:px-10 pt-16 grid md:grid-cols-2 gap-6" data-testid="panorama-panels">
        {PANELS.map(({ key, label, icon: Icon }) => {
          const items = pano[key] || [];
          if (items.length === 0) return null;
          return (
            <div key={key} data-testid={`panel-${key}`} className="border border-copper/25 bg-[#0F1528]/60 copper-frame p-8">
              <div className="flex items-center gap-3 mb-6">
                <Icon className="w-5 h-5 text-copper" strokeWidth={1.5} />
                <h2 className="font-heading text-2xl text-parchment">{label}</h2>
              </div>
              <ul className="space-y-3">
                {items.map((it, i) => (
                  <li key={i} className="text-parchment/80 leading-relaxed pl-4 border-l border-copper/30">{it}</li>
                ))}
              </ul>
            </div>
          );
        })}
      </section>

      {pano.linked_stories && pano.linked_stories.length > 0 && (
        <section className="mx-auto max-w-7xl px-6 lg:px-10 mt-24" data-testid="panorama-linked">
          <div className="overline mb-3">Récits de cette époque</div>
          <h2 className="font-heading text-3xl sm:text-4xl text-parchment mb-10">Continuez l'exploration</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {pano.linked_stories.map(s => <StoryCard key={s.id} story={s} />)}
          </div>
        </section>
      )}
    </div>
  );
}
