import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import { ArrowUpRight, Sparkles, Compass, Map as MapIcon, HelpCircle } from "lucide-react";
import { fetchUniverses, fetchStories } from "@/lib/api";
import StoryCard from "@/components/StoryCard";

export default function HomePage() {
  const [universes, setUniverses] = useState([]);
  const [featured, setFeatured] = useState([]);

  useEffect(() => {
    fetchUniverses().then(setUniverses).catch(() => {});
    fetchStories({ limit: 6 }).then(setFeatured).catch(() => {});
  }, []);

  return (
    <div data-testid="home-page">
      {/* HERO */}
      <section className="relative min-h-[calc(100vh-5rem)] overflow-hidden">
        <div className="absolute inset-0">
          <img
            src="https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg"
            alt=""
            className="w-full h-full object-cover opacity-40"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/70 via-[#050814]/85 to-[#050814]" />
        </div>

        <div className="relative z-10 mx-auto max-w-7xl px-6 lg:px-16 pt-24 pb-32 grid lg:grid-cols-12 gap-10">
          <div className="lg:col-span-8 animate-fade-up">
            <div className="overline text-copper mb-8">Une invitation</div>
            <h1 className="font-heading font-light text-5xl sm:text-6xl lg:text-7xl xl:text-8xl tracking-tight text-parchment leading-[1.05]">
              Entrez dans la <em className="text-copper-light not-italic">bibliothèque</em>
              <br />
              qu'on n'ouvre qu'à la nuit tombée.
            </h1>
            <p className="mt-10 text-lg lg:text-xl text-parchment/75 max-w-2xl leading-relaxed">
              Une exploration honnête de l'histoire de la spiritualité, du mysticisme,
              des arts divinatoires et des grandes légendes.
              Ici, on distingue toujours <span className="text-copper-light">ce que l'on sait</span>,{" "}
              <span className="text-copper-light">ce que l'on croit</span>,{" "}
              <span className="text-copper-light">ce que l'on raconte</span>.
            </p>

            <div className="mt-10 flex flex-wrap gap-3">
              <Link to="/frise" data-testid="cta-timeline" className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light transition-colors duration-300">
                Explorer par époque <ArrowUpRight className="w-4 h-4" strokeWidth={2} />
              </Link>
              <Link to="/etrange" data-testid="cta-strange" className="inline-flex items-center gap-2 px-6 py-3 border border-copper text-copper font-ui text-sm uppercase tracking-widest hover:bg-copper/10 transition-colors duration-300">
                <Sparkles className="w-4 h-4" strokeWidth={1.5} /> Raconte-moi quelque chose d'étrange
              </Link>
            </div>
          </div>
        </div>

        {/* Signature bar */}
        <div className="absolute bottom-0 left-0 right-0 z-10 border-t border-copper/20 bg-[#050814]/60 backdrop-blur">
          <div className="mx-auto max-w-7xl px-6 lg:px-10 py-4 grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-ui uppercase tracking-widest text-copper-muted">
            <SignatureLink to="/frise" icon={Compass} label="Frise chronologique" />
            <SignatureLink to="/carte" icon={MapIcon} label="Carte des légendes" />
            <SignatureLink to="/etrange" icon={Sparkles} label="Récits aléatoires" />
            <SignatureLink to="/quiz" icon={HelpCircle} label="Vrai, croyance ou légende ?" />
          </div>
        </div>
      </section>

      {/* UNIVERSES BENTO */}
      <section className="mx-auto max-w-7xl px-6 lg:px-10 py-24" data-testid="universes-section">
        <div className="mb-14 flex flex-col md:flex-row md:items-end md:justify-between gap-6">
          <div>
            <div className="overline mb-4">Sept univers</div>
            <h2 className="font-heading text-4xl sm:text-5xl text-parchment tracking-tight">
              Choisissez la porte que vous ouvrez ce soir.
            </h2>
          </div>
          <p className="max-w-md text-parchment/70 leading-relaxed">
            Chaque univers rassemble des dossiers, des personnages et des récits,
            avec toujours la même exigence : nommer ce que l'on raconte.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 auto-rows-fr">
          {universes.map((u, i) => (
            <Link
              key={u.id}
              to={`/univers/${u.id}`}
              data-testid={`universe-card-${u.id}`}
              className={`group relative border border-copper/25 bg-[#0F1528]/70 hover-lift copper-frame p-8 overflow-hidden min-h-[280px] flex flex-col justify-end ${
                i === 0 ? "sm:col-span-2 lg:row-span-2 min-h-[400px]" : ""
              } ${i === 3 ? "lg:col-span-2" : ""}`}
            >
              {u.image && (
                <div className="absolute inset-0 -z-10">
                  <img src={u.image} alt="" className="w-full h-full object-cover opacity-20 group-hover:opacity-30 transition-opacity duration-700" />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#0F1528] via-[#0F1528]/85 to-transparent" />
                </div>
              )}
              <span className="overline text-copper mb-3">{u.story_count} récit{u.story_count > 1 ? "s" : ""}</span>
              <h3 className="font-heading text-3xl text-parchment group-hover:text-copper-light transition-colors leading-tight">
                {u.title}
              </h3>
              <p className="mt-2 italic text-copper-muted text-sm">{u.subtitle}</p>
              <p className="mt-4 text-sm text-parchment/70 leading-relaxed line-clamp-3">
                {u.description}
              </p>
              <div className="mt-6 inline-flex items-center gap-2 text-copper text-sm font-ui">
                Entrer <ArrowUpRight className="w-4 h-4" strokeWidth={1.5} />
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* FEATURED STORIES */}
      <section className="mx-auto max-w-7xl px-6 lg:px-10 pb-24" data-testid="featured-section">
        <div className="mb-10 flex items-end justify-between gap-6">
          <div>
            <div className="overline mb-3">À découvrir</div>
            <h2 className="font-heading text-3xl sm:text-4xl text-parchment tracking-tight">Récits d'ouverture</h2>
          </div>
          <Link to="/frise" className="text-sm font-ui text-copper hover:text-copper-light">Voir tout →</Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {featured.map(s => <StoryCard key={s.id} story={s} />)}
        </div>
      </section>
    </div>
  );
}

function SignatureLink({ to, icon: Icon, label }) {
  return (
    <Link to={to} className="flex items-center gap-2 hover:text-copper transition-colors">
      <Icon className="w-3.5 h-3.5" strokeWidth={1.5} /> {label}
    </Link>
  );
}
