import { useEffect, useState, useMemo } from "react";
import { Link } from "react-router-dom";
import { MapPin } from "lucide-react";
import { fetchMapPoints, fetchRegions } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";

export default function MapPage() {
  const [points, setPoints] = useState([]);
  const [regions, setRegions] = useState([]);
  const [selected, setSelected] = useState(null);
  const [activeRegion, setActiveRegion] = useState(null);

  useEffect(() => {
    fetchMapPoints().then(setPoints).catch(() => {});
    fetchRegions().then(setRegions).catch(() => setRegions([]));
  }, []);

  const filteredPoints = useMemo(
    () => activeRegion ? points.filter(p => p.region === activeRegion) : points,
    [points, activeRegion]
  );

  const projected = useMemo(() => filteredPoints.map(p => {
    const [lat, lng] = p.coords || [0, 0];
    return { ...p, x: ((lng + 180) / 360) * 100, y: ((90 - lat) / 180) * 100 };
  }), [filteredPoints]);

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="map-page">
      <div className="overline mb-4">Cartographie</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight max-w-3xl leading-[1.05]">
        Là où les histoires se sont passées, ou racontées.
      </h1>
      <p className="mt-6 max-w-2xl text-parchment/70 leading-relaxed">
        Chaque marque est un lieu associé à un récit. Filtrez par région ou cliquez sur un point.
      </p>

      {regions.length > 0 && (
        <div className="mt-10 flex flex-wrap gap-2" data-testid="region-filters">
          <FilterChip active={activeRegion === null} onClick={() => { setActiveRegion(null); setSelected(null); }} label={`Toutes les régions · ${points.length}`} />
          {regions.map(r => (
            <FilterChip
              key={r.region}
              active={activeRegion === r.region}
              onClick={() => { setActiveRegion(r.region); setSelected(null); }}
              label={`${r.region} · ${r.story_count}`}
              testId={`region-${r.region}`}
            />
          ))}
        </div>
      )}

      <div className="mt-10 grid lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 relative aspect-[2/1] border border-copper/30 bg-[#0A0F1D] overflow-hidden copper-frame">
       <img
src="/carte_ancienne_mystique_du_monde.png"
alt="Carte ancienne des Chroniques de l'Étrange"
className="absolute inset-0 w-full h-full object-cover"
draggable="false"
/>   
          
          <div className="absolute inset-0 pointer-events-none bg-gradient-to-b from-[#050814]/40 via-transparent to-[#050814]/60" />
          {projected.map(p => (
            <button
              key={p.id}
              type="button"
              onClick={() => setSelected(p)}
              data-testid={`map-pin-${p.id}`}
     className="absolute z-20 w-10 h-10 -translate-x-1/2 -translate-y-1/2 flex items-center justify-center cursor-pointer group"
              style={{ left: `${p.x}%`, top: `${p.y}%` }}
              aria-label={p.title}
            >
              <span className={`block w-3 h-3 rounded-full bg-copper ring-4 ring-copper/20 group-hover:ring-copper/40 ${selected?.id === p.id ? "ring-copper/60 scale-125" : ""} transition-transform`} />
            </button>
          ))}
        </div>

        <aside className="border border-copper/25 bg-[#0F1528]/70 p-6 copper-frame min-h-[400px]" data-testid="map-details">
          {!selected && (
            <div className="text-copper-muted italic text-center py-12">
              <MapPin className="w-8 h-8 text-copper mx-auto mb-4" strokeWidth={1.2} />
              Cliquez sur un point pour découvrir un récit.
            </div>
          )}
          {selected && (
            <div>
              <StatusBadge status={selected.status_key} size="sm" />
              <h3 className="mt-4 font-heading text-3xl text-parchment leading-tight">{selected.title}</h3>
              {selected.region && (
                <div className="mt-2 flex items-center gap-2 text-sm font-ui text-copper-muted">
                  <MapPin className="w-4 h-4" strokeWidth={1.5} /> {selected.region}
                </div>
              )}
              <p className="mt-5 text-sm text-parchment/70 leading-relaxed">{selected.excerpt}</p>
              <Link to={`/recit/${selected.id}`} data-testid="map-open-story" className="mt-6 inline-flex items-center gap-2 px-4 py-2 border border-copper text-copper font-ui text-xs uppercase tracking-widest hover:bg-copper/10">
                Lire le récit
              </Link>
            </div>
          )}
        </aside>
      </div>
    </div>
  );
}

function FilterChip({ active, onClick, label, testId }) {
  return (
    <button type="button" onClick={onClick} data-testid={testId}
      className={`px-3 py-1.5 text-xs font-ui uppercase tracking-widest border rounded-full transition-colors ${
        active ? "border-copper bg-copper/20 text-copper-light" : "border-copper/30 text-copper-muted hover:border-copper/60 hover:text-copper"
      }`}>
      {label}
    </button>
  );
}
