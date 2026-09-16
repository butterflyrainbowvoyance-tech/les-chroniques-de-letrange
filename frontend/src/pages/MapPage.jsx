import { useEffect, useState, useMemo } from "react";
import { Link } from "react-router-dom";
import { MapPin } from "lucide-react";
import { fetchMapPoints } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";

export default function MapPage() {
  const [points, setPoints] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    fetchMapPoints().then(setPoints).catch(() => {});
  }, []);

  // Project lat/lng to a stylized 2D canvas (world equirectangular)
  const projected = useMemo(() => points.map(p => {
    const [lat, lng] = p.coords || [0, 0];
    const x = ((lng + 180) / 360) * 100;
    const y = ((90 - lat) / 180) * 100;
    return { ...p, x, y };
  }), [points]);

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="map-page">
      <div className="overline mb-4">Cartographie</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight max-w-3xl leading-[1.05]">
        Là où les histoires se sont passées, ou racontées.
      </h1>
      <p className="mt-6 max-w-2xl text-parchment/70 leading-relaxed">
        Chaque marque est un lieu associé à un récit. Cliquez pour découvrir ce qui s'y est passé — ou ce qu'on
        a raconté qu'il s'y était passé.
      </p>

      <div className="mt-12 grid lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 relative aspect-[2/1] border border-copper/30 bg-[#0A0F1D] overflow-hidden copper-frame">
          <svg
            className="absolute inset-0 w-full h-full opacity-25"
            viewBox="0 0 200 100"
            preserveAspectRatio="none"
            aria-hidden="true"
          >
            <defs>
              <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
                <path d="M 10 0 L 0 0 0 10" fill="none" stroke="#8A6D4C" strokeWidth="0.15" />
              </pattern>
              <pattern id="dots" width="4" height="4" patternUnits="userSpaceOnUse">
                <circle cx="2" cy="2" r="0.35" fill="#C69C6D" />
              </pattern>
            </defs>
            <rect width="200" height="100" fill="url(#grid)" />
            <rect width="200" height="100" fill="url(#dots)" opacity="0.6" />
          </svg>
          <div className="absolute inset-0 bg-gradient-to-b from-[#050814]/40 via-transparent to-[#050814]/60" />
          {projected.map(p => (
            <button
              key={p.id}
              type="button"
              onClick={() => setSelected(p)}
              data-testid={`map-pin-${p.id}`}
              className="absolute -translate-x-1/2 -translate-y-1/2 group"
              style={{ left: `${p.x}%`, top: `${p.y}%` }}
              aria-label={p.title}
            >
              <span className="block w-3 h-3 rounded-full bg-copper ring-4 ring-copper/20 group-hover:ring-copper/40 animate-flicker" />
            </button>
          ))}
        </div>

        <aside className="border border-copper/25 bg-[#0F1528]/70 p-6 copper-frame min-h-[400px]" data-testid="map-details">
          {!selected && (
            <div className="text-copper-muted italic text-center py-12">
              <MapPin className="w-8 h-8 text-copper mx-auto mb-4" strokeWidth={1.2} />
              Cliquez sur un point de la carte pour découvrir un récit.
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
              <Link to={`/recit/${selected.id}`} className="mt-6 inline-flex items-center gap-2 px-4 py-2 border border-copper text-copper font-ui text-xs uppercase tracking-widest hover:bg-copper/10">
                Lire le récit
              </Link>
            </div>
          )}
        </aside>
      </div>
    </div>
  );
}
