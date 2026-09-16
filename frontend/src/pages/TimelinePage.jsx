import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchTimeline, fetchEras } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";

export default function TimelinePage() {
  const [items, setItems] = useState([]);
  const [eras, setEras] = useState([]);
  const [filter, setFilter] = useState(null);

  useEffect(() => {
    fetchTimeline().then(setItems).catch(() => {});
    fetchEras().then(setEras).catch(() => {});
  }, []);

  const filtered = filter ? items.filter(i => i.era === filter) : items;

  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-10 py-16" data-testid="timeline-page">
      <div className="overline mb-4">Voyage dans les siècles</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight max-w-3xl leading-[1.05]">
        La frise du visible et de l'invisible.
      </h1>
      <p className="mt-6 max-w-2xl text-parchment/70 leading-relaxed">
        Trente siècles, sept univers, une seule chronologie. Chaque récit affiche clairement son statut : fait,
        tradition, légende ou hypothèse.
      </p>

      <div className="mt-10 flex flex-wrap gap-2" data-testid="era-filters">
        <FilterChip active={filter === null} onClick={() => setFilter(null)} label="Toutes les époques" />
        {eras.map(e => (
          <FilterChip key={e.id} active={filter === e.id} onClick={() => setFilter(e.id)} label={`${e.label} · ${e.story_count}`} />
        ))}
      </div>

      <div className="mt-16 relative">
        <div className="absolute left-6 top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-copper/40 to-transparent" />
        <ol className="space-y-10">
          {filtered.map(item => (
            <li key={item.id} className="relative pl-16" data-testid={`timeline-item-${item.id}`}>
              <span className="absolute left-4 top-2 w-4 h-4 rounded-full border-2 border-copper bg-[#050814]" />
              <div className="overline text-copper">{item.year < 0 ? `${Math.abs(item.year)} av. J.-C.` : item.year} · {item.era_label}</div>
              <Link to={`/recit/${item.id}`} className="mt-2 block font-heading text-3xl text-parchment hover:text-copper-light transition-colors">
                {item.title}
              </Link>
              <div className="mt-3 flex flex-wrap items-center gap-3">
                <StatusBadge status={item.status_key} size="sm" />
                {item.region && <span className="text-sm font-ui text-copper-muted">{item.region}</span>}
              </div>
            </li>
          ))}
        </ol>
      </div>
    </div>
  );
}

function FilterChip({ active, onClick, label }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`px-3 py-1.5 text-xs font-ui uppercase tracking-widest border rounded-full transition-colors ${
        active ? "border-copper bg-copper/20 text-copper-light" : "border-copper/30 text-copper-muted hover:border-copper/60 hover:text-copper"
      }`}
    >
      {label}
    </button>
  );
}
