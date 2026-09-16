import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ArrowUpRight, Hourglass } from "lucide-react";
import { fetchPanoramas } from "@/lib/api";

export default function VoyagePage() {
  const [panoramas, setPanoramas] = useState([]);

  useEffect(() => { fetchPanoramas().then(setPanoramas).catch(() => {}); }, []);

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="voyage-page">
      <div className="overline mb-4">Fonction signature</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl lg:text-7xl text-parchment tracking-tight max-w-4xl leading-[1.02]">
        Voyage dans le <em className="text-copper-light not-italic">temps</em>.
      </h1>
      <p className="mt-6 max-w-2xl text-parchment/75 leading-relaxed text-lg">
        Choisissez une époque. On vous raconte ce que l'on croyait, ce que l'on pratiquait,
        qui l'on consultait, quels objets on portait et ce que l'on craignait à ce moment-là.
      </p>

      <div className="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-testid="panoramas-grid">
        {panoramas.map((p, i) => (
          <Link
            key={p.id}
            to={`/voyage/${p.id}`}
            data-testid={`panorama-card-${p.id}`}
            className={`group relative border border-copper/25 bg-[#0F1528]/70 hover-lift copper-frame overflow-hidden ${
              i === 0 ? "md:col-span-2 lg:col-span-2 lg:row-span-2" : ""
            }`}
          >
            <div className={`relative ${i === 0 ? "aspect-[16/10]" : "aspect-[16/9]"} overflow-hidden`}>
              <img src={p.hero_image} alt="" className="w-full h-full object-cover opacity-50 group-hover:opacity-70 transition-opacity duration-700" />
              <div className="absolute inset-0 bg-gradient-to-t from-[#0F1528] via-[#0F1528]/60 to-transparent" />
              <Hourglass className="absolute top-6 right-6 w-6 h-6 text-copper" strokeWidth={1.2} />
            </div>
            <div className="p-8">
              <div className="overline text-copper">{p.period}</div>
              <h2 className={`mt-3 font-heading text-parchment leading-tight ${i === 0 ? "text-5xl" : "text-3xl"}`}>
                {p.label}
              </h2>
              <p className="mt-3 italic text-copper-muted">{p.tagline}</p>
              <div className="mt-6 inline-flex items-center gap-2 text-copper text-sm font-ui uppercase tracking-widest">
                Ouvrir cette époque <ArrowUpRight className="w-4 h-4" strokeWidth={1.5} />
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
