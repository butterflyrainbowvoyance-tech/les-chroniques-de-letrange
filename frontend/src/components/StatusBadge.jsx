import { CheckCircle2, BookMarked, Sparkles, HelpCircle } from "lucide-react";

const CONFIG = {
  fait_historique: {
    label: "Fait historique attesté",
    icon: CheckCircle2,
    color: "text-[#8FB4A1] border-[#4A6B5D]/60 bg-[#4A6B5D]/15",
  },
  tradition: {
    label: "Tradition ou croyance",
    icon: BookMarked,
    color: "text-[#C4A87A] border-[#6B5D4A]/60 bg-[#6B5D4A]/15",
  },
  legende: {
    label: "Conte ou légende",
    icon: Sparkles,
    color: "text-[#8FA9C4] border-[#4A5D6B]/60 bg-[#4A5D6B]/15",
  },
  hypothese: {
    label: "Hypothèse ou controverse",
    icon: HelpCircle,
    color: "text-[#C48FA9] border-[#6B4A5D]/60 bg-[#6B4A5D]/15",
  },
};

export default function StatusBadge({ status, size = "md" }) {
  const cfg = CONFIG[status] || CONFIG.hypothese;
  const Icon = cfg.icon;
  const padding = size === "sm" ? "px-2 py-0.5 text-[0.65rem]" : "px-3 py-1 text-xs";
  return (
    <span
      data-testid={`badge-${status}`}
      className={`inline-flex items-center gap-1.5 rounded-full border font-ui uppercase tracking-[0.15em] ${padding} ${cfg.color}`}
    >
      <Icon className="w-3 h-3" strokeWidth={2} />
      {cfg.label}
    </span>
  );
}
