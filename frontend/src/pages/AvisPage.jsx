import { useEffect, useState } from "react";
import { Star, Send } from "lucide-react";
import { toast } from "sonner";
import { fetchReviews, fetchReviewsSummary, postReview } from "@/lib/api";

export default function AvisPage() {
  const [reviews, setReviews] = useState([]);
  const [summary, setSummary] = useState({ count: 0, average: 0 });
  const [form, setForm] = useState({ name: "", rating: 5, comment: "" });
  const [sending, setSending] = useState(false);

  useEffect(() => {
    fetchReviews().then(setReviews).catch(() => {});
    fetchReviewsSummary().then(setSummary).catch(() => {});
  }, []);

  const submit = async (e) => {
    e.preventDefault();
    if (!form.name.trim() || !form.comment.trim()) return;
    setSending(true);
    try {
      await postReview(form);
      toast.success("Merci — votre avis sera lu par la rédaction avant publication.");
      setForm({ name: "", rating: 5, comment: "" });
    } catch { toast.error("Erreur lors de l'envoi."); }
    setSending(false);
  };

  return (
    <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16" data-testid="avis-page">
      <div className="overline mb-4">Vos retours</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
        Ce que vous en dites.
      </h1>
      <p className="mt-6 text-parchment/75 leading-relaxed max-w-2xl">
        Tous les avis sont lus avant publication. Rien n'apparaît automatiquement.
      </p>
      {summary.count > 0 && (
        <div className="mt-8 inline-flex items-center gap-4 border border-copper/30 px-5 py-3 copper-frame" data-testid="avis-summary">
          <div className="flex gap-0.5">
            {[1,2,3,4,5].map(i => (
              <Star key={i} className={`w-5 h-5 ${i <= Math.round(summary.average) ? "fill-copper text-copper" : "text-copper/30"}`} strokeWidth={1.2} />
            ))}
          </div>
          <div className="text-parchment font-heading text-xl">{summary.average}/5</div>
          <div className="text-xs font-ui text-copper-muted">· {summary.count} avis publiés</div>
        </div>
      )}

      <form onSubmit={submit} className="mt-14 border border-copper/25 bg-[#0F1528]/60 copper-frame p-6 sm:p-8 space-y-5" data-testid="avis-form">
        <div className="overline">Laisser un avis</div>
        <input type="text" placeholder="Votre nom (ou pseudonyme)" required value={form.name} onChange={e => setForm(f => ({...f, name: e.target.value}))}
          data-testid="avis-name" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
        <div>
          <div className="overline mb-2">Votre note</div>
          <div className="flex gap-1">
            {[1,2,3,4,5].map(i => (
              <button type="button" key={i} onClick={() => setForm(f => ({...f, rating: i}))} data-testid={`avis-star-${i}`}
                className="p-1"><Star className={`w-8 h-8 ${i <= form.rating ? "fill-copper text-copper" : "text-copper/30"}`} strokeWidth={1.2} /></button>
            ))}
          </div>
        </div>
        <textarea placeholder="Ce que vous en pensez…" required rows={4} value={form.comment} onChange={e => setForm(f => ({...f, comment: e.target.value}))}
          data-testid="avis-comment" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
        <button type="submit" disabled={sending} data-testid="avis-submit"
          className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light disabled:opacity-50">
          <Send className="w-4 h-4" strokeWidth={2} /> Envoyer pour modération
        </button>
      </form>

      <div className="mt-16 space-y-6" data-testid="avis-list">
        {reviews.length === 0 && <p className="text-center italic text-copper-muted">Aucun avis publié pour l'instant.</p>}
        {reviews.map(r => (
          <div key={r.id} className="border border-copper/20 p-6 copper-frame">
            <div className="flex items-center justify-between mb-3">
              <div className="font-heading text-lg text-parchment">{r.name}</div>
              <div className="flex gap-0.5">
                {[1,2,3,4,5].map(i => <Star key={i} className={`w-4 h-4 ${i <= r.rating ? "fill-copper text-copper" : "text-copper/20"}`} strokeWidth={1.2} />)}
              </div>
            </div>
            <p className="text-parchment/80 leading-relaxed">{r.comment}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
