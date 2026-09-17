import { useEffect, useState } from "react";
import { Ghost, Send, MapPin } from "lucide-react";
import { toast } from "sonner";
import { fetchTemoignages, postTemoignage } from "@/lib/api";

export default function TemoignagesPage() {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({ name: "", location: "", title: "", story: "" });
  const [sending, setSending] = useState(false);

  useEffect(() => { fetchTemoignages().then(setItems).catch(() => {}); }, []);

  const submit = async (e) => {
    e.preventDefault();
    if (!form.name.trim() || !form.title.trim() || !form.story.trim()) return;
    setSending(true);
    try {
      await postTemoignage(form);
      toast.success("Merci — votre témoignage sera lu par la rédaction avant publication.");
      setForm({ name: "", location: "", title: "", story: "" });
    } catch { toast.error("Erreur lors de l'envoi."); }
    setSending(false);
  };

  return (
    <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16" data-testid="temoignages-page">
      <div className="overline mb-4">Vos expériences</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
        Racontez-nous ce que vous avez vécu.
      </h1>
      <p className="mt-6 text-parchment/75 leading-relaxed max-w-2xl">
        Lieu inexpliqué, coïncidence troublante, phénomène observé, tradition familiale.
        <br />Tous les récits sont lus avant publication. Ils restent identifiés comme <span className="text-copper-light">témoignages personnels</span> — jamais présentés comme des faits attestés.
      </p>

      <form onSubmit={submit} className="mt-14 border border-copper/25 bg-[#0F1528]/60 copper-frame p-6 sm:p-8 space-y-5" data-testid="temoignage-form">
        <div className="overline">Envoyer un témoignage</div>
        <div className="grid sm:grid-cols-2 gap-4">
          <input type="text" placeholder="Votre nom" required value={form.name} onChange={e => setForm(f => ({...f, name: e.target.value}))}
            data-testid="temoignage-name" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
          <input type="text" placeholder="Lieu (facultatif)" value={form.location} onChange={e => setForm(f => ({...f, location: e.target.value}))}
            data-testid="temoignage-location" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
        </div>
        <input type="text" placeholder="Titre de votre récit" required value={form.title} onChange={e => setForm(f => ({...f, title: e.target.value}))}
          data-testid="temoignage-title" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
        <textarea placeholder="Votre récit…" required rows={8} value={form.story} onChange={e => setForm(f => ({...f, story: e.target.value}))}
          data-testid="temoignage-story" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
        <button type="submit" disabled={sending} data-testid="temoignage-submit"
          className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light disabled:opacity-50">
          <Send className="w-4 h-4" strokeWidth={2} /> Envoyer pour modération
        </button>
      </form>

      <div className="mt-16 space-y-8" data-testid="temoignages-list">
        {items.length === 0 && <p className="text-center italic text-copper-muted">Aucun témoignage publié pour l'instant.</p>}
        {items.map(t => (
          <article key={t.id} className="border border-copper/25 p-6 sm:p-8 copper-frame bg-[#0F1528]/60">
            <div className="inline-flex items-center gap-2 mb-3 px-2.5 py-0.5 border border-copper/50 rounded-full text-[0.6rem] font-ui uppercase tracking-[0.2em] text-copper">
              <Ghost className="w-3 h-3" strokeWidth={1.5} /> Témoignage personnel
            </div>
            <h3 className="font-heading text-2xl sm:text-3xl text-parchment mt-1">{t.title}</h3>
            <div className="mt-2 flex items-center gap-3 text-xs font-ui text-copper-muted">
              <span>par {t.name}</span>
              {t.location && <span className="inline-flex items-center gap-1"><MapPin className="w-3 h-3" strokeWidth={1.5} /> {t.location}</span>}
            </div>
            <p className="mt-5 text-parchment/80 leading-relaxed whitespace-pre-line">{t.story}</p>
          </article>
        ))}
      </div>
    </div>
  );
}
