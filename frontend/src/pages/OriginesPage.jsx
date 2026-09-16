import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ArrowUpRight, Sparkle } from "lucide-react";
import { fetchOrigines } from "@/lib/api";

export default function OriginesPage() {
  const [items, setItems] = useState([]);

  useEffect(() => { fetchOrigines().then(setItems).catch(() => {}); }, []);

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="origines-page">
      <div className="overline mb-4">Fonction signature</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl lg:text-7xl text-parchment tracking-tight max-w-4xl leading-[1.02]">
        À l'origine de<em className="text-copper-light not-italic">…</em>
      </h1>
      <p className="mt-6 max-w-2xl text-parchment/75 leading-relaxed text-lg">
        Les gestes qu'on fait sans y penser. Le sel jeté par-dessus l'épaule, le miroir cassé, le chat noir,
        le vendredi 13. On raconte l'origine attestée, comment ça s'est transformé, ce qu'on en dit
        aujourd'hui — et l'écart, souvent immense, entre les deux.
      </p>

      <div className="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-testid="origines-grid">
        {items.map((o, i) => (
          <Link
            key={o.id}
            to={`/origine/${o.id}`}
            data-testid={`origine-card-${o.id}`}
            className={`group relative border border-copper/25 bg-[#0F1528]/70 hover-lift copper-frame overflow-hidden ${
              i === 0 ? "md:col-span-2 lg:col-span-2" : ""
            }`}
          >
            <div className={`relative overflow-hidden ${i === 0 ? "aspect-[16/8]" : "aspect-[16/9]"}`}>
              <img src={o.hero_image} alt="" className="w-full h-full object-cover opacity-50 group-hover:opacity-70 transition-opacity duration-700" />
              <div className="absolute inset-0 bg-gradient-to-t from-[#0F1528] via-[#0F1528]/60 to-transparent" />
              <Sparkle className="absolute top-6 right-6 w-6 h-6 text-copper" strokeWidth={1.2} />
            </div>
            <div className="p-8">
              <div className="overline text-copper mb-3">À l'origine de</div>
              <h2 className={`font-heading text-parchment leading-tight ${i === 0 ? "text-4xl sm:text-5xl" : "text-3xl"}`}>
                {o.symbol}
              </h2>
              <p className="mt-3 italic text-copper-muted">{o.hook}</p>
              <p className="mt-4 text-sm text-parchment/70 leading-relaxed">{o.one_liner}</p>
              <div className="mt-6 inline-flex items-center gap-2 text-copper text-sm font-ui uppercase tracking-widest">
                Ouvrir ce dossier <ArrowUpRight className="w-4 h-4" strokeWidth={1.5} />
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
