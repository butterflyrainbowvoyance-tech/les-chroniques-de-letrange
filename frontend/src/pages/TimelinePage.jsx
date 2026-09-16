import { useEffect, useState, useMemo, useRef } from "react";
import { Link } from "react-router-dom";
import { ChevronLeft, ChevronRight, MapPin } from "lucide-react";
import { fetchTimeline, fetchEras } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";

// Fixed era ranges (in years, negative for BCE)
const ERA_BOUNDS = {
  "prehistoire":  { start: -40000, end: -3000, label: "Préhistoire" },
  "antiquite":    { start: -3000,  end: 476,   label: "Antiquité" },
  "moyen-age":    { start: 476,    end: 1400,  label: "Moyen Âge" },
  "renaissance":  { start: 1400,   end: 1650,  label: "Renaissance" },
  "moderne":      { start: 1650,   end: 1789,  label: "Époque moderne" },
  "xixe":         { start: 1789,   end: 1914,  label: "XIXe siècle" },
  "contemporain": { start: 1914,   end: 2050,  label: "Époque contemporaine" },
};
const ERA_ORDER = ["prehistoire", "antiquite", "moyen-age", "renaissance", "moderne", "xixe", "contemporain"];

const BAND_WIDTH = 640; // px per era band

function fmtYear(y) {
  if (y < 0) return `${Math.abs(y)} av. J.-C.`;
  return `${y}`;
}

export default function TimelinePage() {
  const [items, setItems] = useState([]);
  const [selected, setSelected] = useState(null);
  const scrollerRef = useRef(null);

  useEffect(() => {
    fetchTimeline().then(list => { setItems(list); if (list.length) setSelected(list[0]); }).catch(() => {});
    fetchEras().catch(() => {});
  }, []);

  const byEra = useMemo(() => {
    const map = {};
    for (const era of ERA_ORDER) map[era] = [];
    for (const it of items) {
      if (map[it.era]) map[it.era].push(it);
      else if (it.year < -3000) map["prehistoire"].push(it);
      else map["antiquite"].push(it);
    }
    // For each era, distribute along y axis to avoid overlap (small offsets)
    return map;
  }, [items]);

  const scroll = (dir) => {
    scrollerRef.current?.scrollBy({ left: dir * BAND_WIDTH * 0.9, behavior: "smooth" });
  };

  return (
    <div className="pb-24" data-testid="timeline-page">
      <div className="mx-auto max-w-7xl px-6 lg:px-10 pt-16">
        <div className="overline mb-4">Frise panoramique</div>
        <h1 className="font-heading font-light text-5xl sm:text-6xl lg:text-7xl text-parchment tracking-tight max-w-4xl leading-[1.02]">
          Trente siècles, d'un seul coup d'œil.
        </h1>
        <p className="mt-6 max-w-2xl text-parchment/70 leading-relaxed">
          Faites défiler la frise horizontalement. Chaque marque est un récit, placé à sa date, coloré selon son
          statut. Cliquez pour ouvrir la fiche.
        </p>
      </div>

      {/* Controls */}
      <div className="mx-auto max-w-7xl px-6 lg:px-10 mt-10 flex items-center justify-between">
        <div className="text-xs font-ui uppercase tracking-widest text-copper-muted">
          {items.length} récits · glisser ou molette horizontale
        </div>
        <div className="flex items-center gap-2">
          <button type="button" onClick={() => scroll(-1)} data-testid="frise-prev" className="w-10 h-10 border border-copper/30 hover:border-copper text-copper flex items-center justify-center rounded-full">
            <ChevronLeft className="w-4 h-4" strokeWidth={1.5} />
          </button>
          <button type="button" onClick={() => scroll(1)} data-testid="frise-next" className="w-10 h-10 border border-copper/30 hover:border-copper text-copper flex items-center justify-center rounded-full">
            <ChevronRight className="w-4 h-4" strokeWidth={1.5} />
          </button>
        </div>
      </div>

      {/* Horizontal frise */}
      <div className="mt-8 relative">
        <div
          ref={scrollerRef}
          className="overflow-x-auto overflow-y-hidden scroll-smooth"
          style={{ scrollbarColor: "#8A6D4C #050814" }}
          data-testid="frise-scroller"
        >
          <div className="relative flex" style={{ width: `${ERA_ORDER.length * BAND_WIDTH}px`, minHeight: "440px" }}>
            {ERA_ORDER.map((eraId, eIdx) => {
              const era = ERA_BOUNDS[eraId];
              const eraStories = byEra[eraId] || [];
              return (
                <div key={eraId} className="relative border-r border-copper/15" style={{ width: BAND_WIDTH }}>
                  {/* Era header */}
                  <div className={`sticky top-0 px-6 py-5 ${eIdx % 2 === 0 ? "bg-[#0A0F1D]/60" : "bg-[#0F1528]/60"}`}>
                    <div className="overline text-copper">{era.label}</div>
                    <div className="text-xs font-ui text-copper-muted mt-1">
                      {fmtYear(era.start)} → {fmtYear(era.end)} · {eraStories.length} récit{eraStories.length > 1 ? "s" : ""}
                    </div>
                  </div>
                  {/* Central axis */}
                  <div className="absolute left-0 right-0 top-[130px] h-px bg-gradient-to-r from-transparent via-copper/40 to-transparent" />
                  {/* Stories */}
                  <div className="relative pt-16 pb-8 px-4" style={{ minHeight: "360px" }}>
                    {eraStories.map((s, i) => {
                      const p = Math.max(0, Math.min(1, (s.year - era.start) / (era.end - era.start)));
                      const isSel = selected?.id === s.id;
                      const top = 40 + (i % 7) * 32;
                      return (
                        <button
                          key={s.id}
                          type="button"
                          onClick={() => setSelected(s)}
                          data-testid={`frise-pin-${s.id}`}
                          className="absolute -translate-x-1/2 group"
                          style={{ left: `${p * 100}%`, top: `${top}px`, zIndex: isSel ? 30 : 10 }}
                          aria-label={s.title}
                        >
                          <span className={`block w-3 h-3 rounded-full border-2 ${isSel ? "bg-copper border-copper scale-125" : "bg-[#050814] border-copper hover:bg-copper/60"} transition-transform`} />
                          <span className={`absolute left-4 top-1/2 -translate-y-1/2 whitespace-nowrap font-ui text-[0.7rem] px-2 py-0.5 rounded bg-[#050814]/90 border border-copper/40 ${isSel ? "opacity-100 text-copper-light" : "opacity-0 group-hover:opacity-100 text-parchment"} transition-opacity pointer-events-none`}>
                            {fmtYear(s.year)} — {s.title.length > 40 ? s.title.slice(0, 40) + "…" : s.title}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Selected detail */}
      {selected && (
        <div className="mx-auto max-w-7xl px-6 lg:px-10 mt-12">
          <article className="border border-copper/25 bg-[#0F1528]/60 copper-frame p-8 grid md:grid-cols-[auto_1fr] gap-8" data-testid="frise-selected">
            <div className="md:min-w-[240px]">
              <div className="overline text-copper mb-2">{fmtYear(selected.year)}</div>
              <div className="text-sm font-ui text-copper-muted">{selected.era_label}</div>
              {selected.region && (
                <div className="mt-2 inline-flex items-center gap-2 text-xs font-ui text-copper-muted">
                  <MapPin className="w-3.5 h-3.5" strokeWidth={1.5} /> {selected.region}
                </div>
              )}
            </div>
            <div>
              <StatusBadge status={selected.status_key} size="sm" />
              <h2 className="mt-4 font-heading text-3xl sm:text-4xl text-parchment leading-tight">{selected.title}</h2>
              <Link to={`/recit/${selected.id}`} data-testid="frise-open-story" className="mt-6 inline-flex items-center gap-2 px-5 py-2.5 border border-copper text-copper font-ui text-xs uppercase tracking-widest hover:bg-copper/10">
                Lire le récit
              </Link>
            </div>
          </article>
        </div>
      )}
    </div>
  );
}
