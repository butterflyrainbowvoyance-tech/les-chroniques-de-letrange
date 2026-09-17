import { useEffect, useState, useMemo } from "react";
import { Link } from "react-router-dom";
import { MapPin } from "lucide-react";
import { fetchStories } from "@/lib/api";

/** Parchment-styled inline map for lieux-hantes universe. */
export default function ParchmentMap({ dossierFilter }) {
  const [points, setPoints] = useState([]);
  const [hover, setHover] = useState(null);

  useEffect(() => {
    fetchStories({ universe: "lieux-hantes", limit: 200 }).then(setPoints).catch(() => {});
  }, []);

  const filtered = useMemo(
    () => dossierFilter ? points.filter(p => p.dossier === dossierFilter) : points,
    [points, dossierFilter]
  );

  const projected = useMemo(() => {
    // If France-only, project on France bounding box; else worldwide
    const franceOnly = dossierFilter === "france";
    return filtered.map(p => {
      const [lat, lng] = p.coords || [0, 0];
      let x, y;
      if (franceOnly) {
        // France bbox approx: lat 41-51, lng -5 → 10
        x = ((lng - (-5)) / (10 - (-5))) * 100;
        y = ((51 - lat) / (51 - 41)) * 100;
      } else {
        x = ((lng + 180) / 360) * 100;
        y = ((90 - lat) / 180) * 100;
      }
      return { ...p, x, y };
    });
  }, [filtered, dossierFilter]);

  return (
    <div className="relative aspect-[16/9] border border-copper/40 overflow-hidden copper-frame" data-testid="parchment-map">
      {/* Parchment background */}
      <div className="absolute inset-0" style={{ background: "linear-gradient(135deg, #2a1f14 0%, #3d2c1a 50%, #2a1f14 100%)" }} />
      {/* Aged paper texture */}
      <svg className="absolute inset-0 w-full h-full opacity-40" viewBox="0 0 200 100" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <pattern id="parchment-lines" width="30" height="30" patternUnits="userSpaceOnUse">
            <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#8A6D4C" strokeWidth="0.15" />
          </pattern>
          <pattern id="parchment-fibers" width="8" height="8" patternUnits="userSpaceOnUse">
            <circle cx="4" cy="4" r="0.25" fill="#C69C6D" opacity="0.4" />
          </pattern>
          <radialGradient id="parchment-glow" cx="50%" cy="50%" r="60%">
            <stop offset="0%" stopColor="#5a4224" stopOpacity="0.4" />
            <stop offset="100%" stopColor="#000" stopOpacity="0.6" />
          </radialGradient>
        </defs>
        <rect width="200" height="100" fill="url(#parchment-lines)" />
        <rect width="200" height="100" fill="url(#parchment-fibers)" />
        <rect width="200" height="100" fill="url(#parchment-glow)" />
      </svg>
      {/* Ornate border corners */}
      <div className="absolute top-3 left-3 w-6 h-6 border-l-2 border-t-2 border-copper/60" />
      <div className="absolute top-3 right-3 w-6 h-6 border-r-2 border-t-2 border-copper/60" />
      <div className="absolute bottom-3 left-3 w-6 h-6 border-l-2 border-b-2 border-copper/60" />
      <div className="absolute bottom-3 right-3 w-6 h-6 border-r-2 border-b-2 border-copper/60" />

      {/* Cartouche */}
      <div className="absolute top-6 left-1/2 -translate-x-1/2 z-10 px-4 py-1 bg-[#050814]/70 border border-copper/50 rounded-sm">
        <span className="font-heading text-parchment tracking-widest text-sm">
          {dossierFilter === "france" ? "Ex regno Franciae" : dossierFilter === "monde" ? "Orbis Terrarum" : "Loca famosa"}
        </span>
      </div>

      {/* Pins */}
      {projected.map(p => (
        <Link
          key={p.id}
          to={`/recit/${p.id}`}
          onMouseEnter={() => setHover(p)}
          onMouseLeave={() => setHover(null)}
          data-testid={`parchment-pin-${p.id}`}
          className="absolute -translate-x-1/2 -translate-y-1/2 group"
          style={{ left: `${p.x}%`, top: `${p.y}%`, zIndex: 20 }}
          aria-label={p.title}
        >
          <span className="block w-4 h-4 rounded-full bg-copper border-2 border-[#050814] ring-2 ring-copper/40 group-hover:ring-copper transition-all" />
        </Link>
      ))}

      {/* Hover tooltip */}
      {hover && (
        <div className="absolute bottom-6 left-1/2 -translate-x-1/2 z-30 px-5 py-3 bg-[#050814]/90 border border-copper/60 max-w-md text-center pointer-events-none">
          <div className="overline text-copper mb-1">{hover.place_type || "Lieu"}</div>
          <div className="font-heading text-parchment text-lg">{hover.title}</div>
          <div className="text-xs font-ui text-copper-muted mt-1 flex items-center justify-center gap-1.5">
            <MapPin className="w-3 h-3" strokeWidth={1.5} /> {hover.region}
          </div>
        </div>
      )}
    </div>
  );
}
