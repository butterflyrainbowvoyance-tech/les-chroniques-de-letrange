import { Link, NavLink, useNavigate } from "react-router-dom";
import { BookOpenText, Compass, Map as MapIcon, Sparkles, HelpCircle, Bookmark, Search } from "lucide-react";
import { useState } from "react";

const links = [
  { to: "/frise", label: "Frise", icon: Compass },
  { to: "/carte", label: "Carte", icon: MapIcon },
  { to: "/etrange", label: "Quelque chose d'étrange", icon: Sparkles },
  { to: "/quiz", label: "Vrai ou légende ?", icon: HelpCircle },
];

export default function Navbar() {
  const [q, setQ] = useState("");
  const navigate = useNavigate();

  const submit = (e) => {
    e.preventDefault();
    if (q.trim()) navigate(`/recherche?q=${encodeURIComponent(q.trim())}`);
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 border-b border-copper/20 backdrop-blur-xl bg-[#050814]/80" data-testid="navbar">
      <div className="mx-auto max-w-7xl px-6 lg:px-10 py-4 flex items-center gap-6">
        <Link to="/" className="flex items-center gap-3 group shrink-0" data-testid="logo-link">
          <BookOpenText className="w-6 h-6 text-copper group-hover:text-copper-light" strokeWidth={1.5} />
          <div className="hidden sm:block leading-tight">
            <div className="font-heading text-xl tracking-tight text-parchment">La Bibliothèque</div>
            <div className="overline">Secrète</div>
          </div>
        </Link>

        <nav className="hidden lg:flex items-center gap-1 ml-4">
          {links.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              data-testid={`nav-${to.slice(1)}`}
              className={({ isActive }) =>
                `flex items-center gap-2 px-3 py-2 text-sm font-ui rounded-sm transition-colors duration-300 ${
                  isActive ? "text-copper-light" : "text-parchment/70 hover:text-copper-light"
                }`
              }
            >
              <Icon className="w-4 h-4" strokeWidth={1.5} />
              {label}
            </NavLink>
          ))}
        </nav>

        <form onSubmit={submit} className="ml-auto flex items-center gap-2 flex-1 max-w-xs">
          <div className="relative w-full">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-copper-muted" strokeWidth={1.5} />
            <input
              data-testid="search-input"
              value={q}
              onChange={(e) => setQ(e.target.value)}
              placeholder="Chercher un récit…"
              className="w-full pl-9 pr-3 py-2 bg-[#0F1528] border border-copper/20 rounded-sm text-sm font-ui text-parchment placeholder:text-copper-muted/60 focus:outline-none focus:border-copper/60"
            />
          </div>
        </form>

        <NavLink to="/bibliotheque" data-testid="nav-favoris" className="flex items-center gap-2 px-3 py-2 text-sm font-ui text-parchment/80 hover:text-copper-light">
          <Bookmark className="w-4 h-4" strokeWidth={1.5} />
          <span className="hidden md:inline">Ma bibliothèque</span>
        </NavLink>
      </div>
    </header>
  );
}
