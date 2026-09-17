import { useEffect, useState, useCallback } from "react";
import { LogOut, Plus, Trash2, Check, X, Edit3, ShieldCheck, ScrollText, Star, Ghost, Save, Handshake, Feather } from "lucide-react";
import { toast } from "sonner";
import {
  adminCheck, adminListStories, adminCreateStory, adminEditStory, adminDeleteStory,
  adminListReviews, adminModerateReview, adminDeleteReview,
  adminListTemoignages, adminModerateTemoignage, adminDeleteTemoignage,
  adminListCollaborations, adminModCollaboration, adminDeleteCollaboration,
  adminListEnquetes, adminModEnquete, adminDeleteEnquete,
  fetchUniverses
} from "@/lib/api";

const TOKEN_KEY = "chroniques_admin_token";

const STATUSES = [
  { key: "fait_historique", label: "Fait historique attesté" },
  { key: "tradition", label: "Tradition ou croyance" },
  { key: "legende", label: "Conte ou légende" },
  { key: "hypothese", label: "Hypothèse ou controverse" },
];
const ERAS = ["prehistoire","antiquite","moyen-age","renaissance","moderne","xixe","contemporain"];

const emptyStory = {
  universe: "esoterisme", dossier: "", title: "", subtitle: "", status: "hypothese",
  era: "antiquite", era_label: "", year: 0, region: "", latitude: "", longitude: "",
  hero_image: "", excerpt: "", content: "", sources: "", tags: ""
};

export default function AdminPage() {
  const [token, setToken] = useState(() => localStorage.getItem(TOKEN_KEY) || "");
  const [authed, setAuthed] = useState(false);
  const [tab, setTab] = useState("chroniques");
  const [universes, setUniverses] = useState([]);
  const [stories, setStories] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [temoignages, setTemoignages] = useState([]);
  const [collabs, setCollabs] = useState([]);
  const [enquetes, setEnquetes] = useState([]);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState(emptyStory);

  const loadAll = useCallback(async (t) => {
    try {
      await adminCheck(t);
      setAuthed(true);
      localStorage.setItem(TOKEN_KEY, t);
      const [u, s, r, tm, c, en] = await Promise.all([
        fetchUniverses(), adminListStories(t), adminListReviews(t), adminListTemoignages(t),
        adminListCollaborations(t), adminListEnquetes(t)
      ]);
      setUniverses(u); setStories(s); setReviews(r); setTemoignages(tm); setCollabs(c); setEnquetes(en);
    } catch {
      setAuthed(false);
      localStorage.removeItem(TOKEN_KEY);
    }
  }, []);

  useEffect(() => { if (token) loadAll(token); }, [token, loadAll]);

  const login = (e) => { e.preventDefault(); loadAll(token); };
  const logout = () => { localStorage.removeItem(TOKEN_KEY); setToken(""); setAuthed(false); };

  // ---- Story CRUD ----
  const startEdit = (s) => {
    setEditing(s.id);
    setForm({
      universe: s.universe, dossier: s.dossier || "", title: s.title, subtitle: s.subtitle || "",
      status: s.status, era: s.era || "antiquite", era_label: s.era_label || "", year: s.year || 0,
      region: s.region || "", latitude: s.coords?.[0] ?? "", longitude: s.coords?.[1] ?? "",
      hero_image: s.hero_image || "", excerpt: s.excerpt || "",
      content: (s.content || []).join("\n\n"), sources: (s.sources || []).join("\n"),
      tags: (s.tags || []).join(", ")
    });
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const resetForm = () => { setEditing(null); setForm(emptyStory); };

  const saveStory = async (e) => {
    e.preventDefault();
    const payload = {
      universe: form.universe,
      dossier: form.dossier || null,
      title: form.title.trim(),
      subtitle: form.subtitle.trim(),
      status: form.status,
      era: form.era,
      era_label: form.era_label.trim(),
      year: parseInt(form.year) || 0,
      region: form.region.trim(),
      coords: (form.latitude !== "" && form.longitude !== "") ? [parseFloat(form.latitude), parseFloat(form.longitude)] : null,
      hero_image: form.hero_image.trim(),
      excerpt: form.excerpt.trim(),
      content: form.content.split(/\n\n+/).map(s => s.trim()).filter(Boolean),
      sources: form.sources.split("\n").map(s => s.trim()).filter(Boolean),
      tags: form.tags.split(",").map(s => s.trim()).filter(Boolean),
    };
    try {
      if (editing) {
        await adminEditStory(token, editing, payload);
        toast.success("Chronique modifiée.");
      } else {
        await adminCreateStory(token, payload);
        toast.success("Chronique ajoutée.");
      }
      resetForm();
      const s = await adminListStories(token); setStories(s);
    } catch (err) { toast.error("Erreur : " + (err?.response?.data?.detail || err.message)); }
  };

  const deleteStory = async (id) => {
    if (!window.confirm("Supprimer définitivement cette chronique ?")) return;
    await adminDeleteStory(token, id);
    setStories(await adminListStories(token));
    toast.success("Chronique supprimée.");
  };

  // ---- Moderation ----
  const modReview = async (id, action, edits = {}) => {
    await adminModerateReview(token, id, { action, ...edits });
    setReviews(await adminListReviews(token));
    toast.success(action === "approve" ? "Avis approuvé." : "Avis refusé.");
  };
  const modTemoignage = async (id, action, edits = {}) => {
    await adminModerateTemoignage(token, id, { action, ...edits });
    setTemoignages(await adminListTemoignages(token));
    toast.success(action === "approve" ? "Témoignage approuvé." : "Témoignage refusé.");
  };

  // ---- Login screen ----
  if (!authed) {
    return (
      <div className="mx-auto max-w-md px-6 py-24" data-testid="admin-login">
        <div className="text-center mb-8">
          <ShieldCheck className="w-10 h-10 text-copper mx-auto" strokeWidth={1.2} />
          <h1 className="mt-4 font-heading text-4xl text-parchment">Espace administrateur</h1>
          <p className="mt-2 text-sm text-copper-muted">Accès réservé à la rédaction.</p>
        </div>
        <form onSubmit={login} className="space-y-4 border border-copper/25 copper-frame p-6">
          <input type="password" placeholder="Jeton d'accès" required value={token} onChange={e => setToken(e.target.value)}
            data-testid="admin-token-input" className="w-full px-4 py-3 bg-[#050814] border border-copper/25 text-parchment font-ui focus:outline-none focus:border-copper/60" />
          <button type="submit" data-testid="admin-login-btn" className="w-full px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light">
            Entrer
          </button>
        </form>
      </div>
    );
  }

  // ---- Pending counts ----
  const pendingReviews = reviews.filter(r => r.status === "pending" || r.published === false && r.status !== "refused").length;
  const pendingTemoignages = temoignages.filter(t => t.status === "pending" || t.published === false && t.status !== "refused").length;

  return (
    <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-10 py-10" data-testid="admin-page">
      <div className="flex items-center justify-between gap-4 mb-8 flex-wrap">
        <div>
          <div className="overline">Rédaction</div>
          <h1 className="font-heading text-4xl sm:text-5xl text-parchment tracking-tight">Espace administrateur</h1>
        </div>
        <button onClick={logout} data-testid="admin-logout" className="inline-flex items-center gap-2 px-3 py-1.5 border border-copper/30 text-copper text-xs font-ui uppercase tracking-widest hover:border-copper">
          <LogOut className="w-3.5 h-3.5" strokeWidth={1.5} /> Déconnexion
        </button>
      </div>

      <div className="flex flex-wrap gap-2 mb-10" role="tablist">
        {[
          { id: "chroniques", label: `Chroniques (${stories.length})`, icon: ScrollText },
          { id: "avis", label: `Avis ${pendingReviews ? `(${pendingReviews} à modérer)` : ""}`.trim(), icon: Star },
          { id: "temoignages", label: `Témoignages ${pendingTemoignages ? `(${pendingTemoignages} à modérer)` : ""}`.trim(), icon: Ghost },
          { id: "collabs", label: `Collaborations (${collabs.filter(c => c.status === "pending").length})`, icon: Handshake },
          { id: "enquetes", label: `Enquêtes (${enquetes.filter(e => e.status === "pending").length})`, icon: Feather },
        ].map(t => (
          <button key={t.id} onClick={() => setTab(t.id)} data-testid={`admin-tab-${t.id}`}
            className={`inline-flex items-center gap-2 px-4 py-2 text-sm font-ui border ${tab === t.id ? "border-copper bg-copper/15 text-copper-light" : "border-copper/25 text-copper-muted hover:text-copper"}`}>
            <t.icon className="w-4 h-4" strokeWidth={1.5} /> {t.label}
          </button>
        ))}
      </div>

      {tab === "chroniques" && (
        <div className="space-y-10">
          <form onSubmit={saveStory} className="border border-copper/25 copper-frame p-5 sm:p-8 space-y-4" data-testid="admin-story-form">
            <div className="flex items-center gap-2">
              <div className="overline flex-1">{editing ? "Modifier la chronique" : "Ajouter une chronique"}</div>
              {editing && <button type="button" onClick={resetForm} className="text-xs text-copper-muted hover:text-copper font-ui uppercase">Annuler l'édition</button>}
            </div>

            <div className="grid sm:grid-cols-2 gap-4">
              <Field label="Univers" required>
                <select value={form.universe} onChange={e => setForm({...form, universe: e.target.value})} data-testid="story-universe" className={inputCls}>
                  {universes.map(u => <option key={u.id} value={u.id}>{u.title}</option>)}
                </select>
              </Field>
              <Field label="Dossier (facultatif)">
                <input value={form.dossier} onChange={e => setForm({...form, dossier: e.target.value})} placeholder="p. ex. france, occultistes-enigmatiques" className={inputCls} />
              </Field>
            </div>

            <Field label="Titre" required>
              <input value={form.title} onChange={e => setForm({...form, title: e.target.value})} required data-testid="story-title" className={inputCls} />
            </Field>
            <Field label="Sous-titre">
              <input value={form.subtitle} onChange={e => setForm({...form, subtitle: e.target.value})} className={inputCls} />
            </Field>

            <div className="grid sm:grid-cols-2 gap-4">
              <Field label="Statut éditorial" required>
                <select value={form.status} onChange={e => setForm({...form, status: e.target.value})} data-testid="story-status" className={inputCls}>
                  {STATUSES.map(s => <option key={s.key} value={s.key}>{s.label}</option>)}
                </select>
              </Field>
              <Field label="Époque">
                <select value={form.era} onChange={e => setForm({...form, era: e.target.value})} className={inputCls}>
                  {ERAS.map(e => <option key={e} value={e}>{e}</option>)}
                </select>
              </Field>
            </div>
            <div className="grid sm:grid-cols-3 gap-4">
              <Field label="Libellé époque"><input value={form.era_label} onChange={e => setForm({...form, era_label: e.target.value})} placeholder="p. ex. XVIIe siècle" className={inputCls} /></Field>
              <Field label="Année (int, -300 = av. J.-C.)"><input type="number" value={form.year} onChange={e => setForm({...form, year: e.target.value})} className={inputCls} /></Field>
              <Field label="Région"><input value={form.region} onChange={e => setForm({...form, region: e.target.value})} placeholder="p. ex. Bretagne, France" className={inputCls} /></Field>
            </div>
            <div className="grid sm:grid-cols-2 gap-4">
              <Field label="Latitude"><input type="number" step="0.0001" value={form.latitude} onChange={e => setForm({...form, latitude: e.target.value})} className={inputCls} /></Field>
              <Field label="Longitude"><input type="number" step="0.0001" value={form.longitude} onChange={e => setForm({...form, longitude: e.target.value})} className={inputCls} /></Field>
            </div>
            <Field label="Image (URL)"><input value={form.hero_image} onChange={e => setForm({...form, hero_image: e.target.value})} placeholder="https://..." className={inputCls} /></Field>
            <Field label="Résumé (excerpt)" required>
              <textarea value={form.excerpt} onChange={e => setForm({...form, excerpt: e.target.value})} required rows={3} className={inputCls} />
            </Field>
            <Field label="Contenu (paragraphes séparés par une ligne vide)" required>
              <textarea value={form.content} onChange={e => setForm({...form, content: e.target.value})} required rows={10} data-testid="story-content" className={inputCls + " font-serif leading-relaxed"} />
            </Field>
            <Field label="Sources (une par ligne)"><textarea value={form.sources} onChange={e => setForm({...form, sources: e.target.value})} rows={4} className={inputCls} /></Field>
            <Field label="Tags (séparés par virgules)"><input value={form.tags} onChange={e => setForm({...form, tags: e.target.value})} className={inputCls} /></Field>

            <button type="submit" data-testid="story-save" className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light">
              <Save className="w-4 h-4" strokeWidth={2} /> {editing ? "Enregistrer les modifications" : "Ajouter la chronique"}
            </button>
          </form>

          <div>
            <div className="overline mb-4">Chroniques ajoutées ({stories.length})</div>
            {stories.length === 0 && <p className="italic text-copper-muted">Aucune chronique ajoutée par l'admin pour l'instant. Utilisez le formulaire ci-dessus.</p>}
            <ul className="space-y-3">
              {stories.map(s => (
                <li key={s.id} className="border border-copper/20 p-4 flex items-center justify-between gap-4 flex-wrap" data-testid={`admin-story-${s.id}`}>
                  <div className="min-w-0 flex-1">
                    <div className="font-heading text-lg text-parchment truncate">{s.title}</div>
                    <div className="text-xs font-ui text-copper-muted">{s.universe} · {s.era_label}</div>
                  </div>
                  <div className="flex gap-2">
                    <button onClick={() => startEdit(s)} className="p-2 border border-copper/30 hover:border-copper text-copper"><Edit3 className="w-4 h-4" strokeWidth={1.5} /></button>
                    <button onClick={() => deleteStory(s.id)} className="p-2 border border-copper/30 hover:border-copper text-copper"><Trash2 className="w-4 h-4" strokeWidth={1.5} /></button>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {tab === "avis" && (
        <ModerationList items={reviews} type="avis"
          renderItem={r => (<>
            <div className="flex items-center gap-2 mb-1">
              <span className="font-heading text-lg text-parchment">{r.name}</span>
              <div className="flex gap-0.5">{[1,2,3,4,5].map(i => <Star key={i} className={`w-3.5 h-3.5 ${i <= r.rating ? "fill-copper text-copper" : "text-copper/20"}`} strokeWidth={1.2} />)}</div>
            </div>
            <p className="text-parchment/80 text-sm leading-relaxed">{r.comment}</p>
          </>)}
          onApprove={id => modReview(id, "approve")}
          onRefuse={id => modReview(id, "refuse")}
          onEdit={(id, edits) => modReview(id, "approve", edits)}
          onDelete={async id => { await adminDeleteReview(token, id); setReviews(await adminListReviews(token)); }}
          editFields={[
            { key: "name", label: "Nom" },
            { key: "rating", label: "Note (1-5)", type: "number" },
            { key: "comment", label: "Commentaire", type: "textarea" }
          ]}
        />
      )}

      {tab === "temoignages" && (
        <ModerationList items={temoignages} type="témoignages"
          renderItem={t => (<>
            <div className="text-xs font-ui text-copper-muted mb-1">{t.name}{t.location ? ` · ${t.location}` : ""}</div>
            <div className="font-heading text-xl text-parchment mb-2">{t.title}</div>
            <p className="text-parchment/80 text-sm leading-relaxed whitespace-pre-line">{t.story}</p>
          </>)}
          onApprove={id => modTemoignage(id, "approve")}
          onRefuse={id => modTemoignage(id, "refuse")}
          onEdit={(id, edits) => modTemoignage(id, "approve", edits)}
          onDelete={async id => { await adminDeleteTemoignage(token, id); setTemoignages(await adminListTemoignages(token)); }}
          editFields={[
            { key: "name", label: "Nom" },
            { key: "location", label: "Lieu" },
            { key: "title", label: "Titre" },
            { key: "story", label: "Récit", type: "textarea" }
          ]}
        />
      )}
      {tab === "collabs" && (
        <ContactList
          items={collabs}
          type="collaborations"
          renderItem={c => (<>
            <div className="flex items-center gap-2 text-xs font-ui text-copper-muted mb-1">
              <span className="uppercase tracking-widest">{c.kind}</span>
              {c.status && <span>· {c.status}</span>}
            </div>
            <div className="font-heading text-xl text-parchment">{c.project}</div>
            <div className="text-xs font-ui text-copper-muted mt-1">{c.name} · <a href={`mailto:${c.email}`} className="text-copper hover:text-copper-light">{c.email}</a></div>
            {c.links && <div className="text-xs font-ui text-copper mt-1 break-all">{c.links}</div>}
            <p className="mt-3 text-sm text-parchment/80 whitespace-pre-line leading-relaxed">{c.message}</p>
          </>)}
          onApprove={async id => { await adminModCollaboration(token, id, { action: "approve" }); setCollabs(await adminListCollaborations(token)); toast.success("Marqué approuvé."); }}
          onRefuse={async id => { await adminModCollaboration(token, id, { action: "refuse" }); setCollabs(await adminListCollaborations(token)); toast.success("Marqué refusé."); }}
          onDone={async id => { await adminModCollaboration(token, id, { action: "processed" }); setCollabs(await adminListCollaborations(token)); toast.success("Marqué traité."); }}
          onDelete={async id => { await adminDeleteCollaboration(token, id); setCollabs(await adminListCollaborations(token)); }}
        />
      )}

      {tab === "enquetes" && (
        <ContactList
          items={enquetes}
          type="enquêtes"
          renderItem={e => (<>
            {e.status && <div className="text-xs font-ui text-copper-muted uppercase tracking-widest mb-1">{e.status}</div>}
            <div className="font-heading text-xl text-parchment">{e.place_name}</div>
            <div className="text-xs font-ui text-copper-muted mt-1">{e.place_location} · proposé par {e.name}{e.role ? ` (${e.role})` : ""} · <a href={`mailto:${e.email}`} className="text-copper hover:text-copper-light">{e.email}</a></div>
            <p className="mt-3 text-sm text-parchment/80 whitespace-pre-line leading-relaxed"><span className="text-copper-muted">Tradition rapportée :</span> {e.tradition_summary}</p>
            {e.message && <p className="mt-2 text-sm text-parchment/70 whitespace-pre-line leading-relaxed border-l border-copper/25 pl-3">{e.message}</p>}
          </>)}
          onApprove={async id => { await adminModEnquete(token, id, { action: "approve" }); setEnquetes(await adminListEnquetes(token)); toast.success("Marqué approuvé."); }}
          onRefuse={async id => { await adminModEnquete(token, id, { action: "refuse" }); setEnquetes(await adminListEnquetes(token)); toast.success("Marqué refusé."); }}
          onDone={async id => { await adminModEnquete(token, id, { action: "processed" }); setEnquetes(await adminListEnquetes(token)); toast.success("Marqué traité."); }}
          onDelete={async id => { await adminDeleteEnquete(token, id); setEnquetes(await adminListEnquetes(token)); }}
        />
      )}
    </div>
  );
}

const inputCls = "w-full px-3 py-2.5 bg-[#050814] border border-copper/25 text-parchment font-ui text-sm focus:outline-none focus:border-copper/60";

function ContactList({ items, type, renderItem, onApprove, onRefuse, onDone, onDelete }) {
  const pending = items.filter(i => i.status === "pending" || !i.status);
  const others = items.filter(i => i.status && i.status !== "pending");
  const Section = ({ title, list }) => (
    <div className="mb-10">
      <div className="overline mb-4">{title} ({list.length})</div>
      {list.length === 0 && <p className="italic text-copper-muted text-sm">Aucune entrée dans cette section.</p>}
      <ul className="space-y-4">
        {list.map(item => (
          <li key={item.id} className="border border-copper/20 p-5 copper-frame" data-testid={`contact-${item.id}`}>
            {renderItem(item)}
            <div className="mt-4 flex flex-wrap items-center gap-2 pt-3 border-t border-copper/15">
              <button onClick={() => onApprove(item.id)} className="inline-flex items-center gap-1.5 px-3 py-1.5 border border-copper text-copper text-xs font-ui uppercase tracking-widest hover:bg-copper/10"><Check className="w-3.5 h-3.5" strokeWidth={2} /> Approuver</button>
              <button onClick={() => onDone(item.id)} className="inline-flex items-center gap-1.5 px-3 py-1.5 border border-copper/30 text-copper-muted text-xs font-ui uppercase tracking-widest hover:text-copper">Marquer traité</button>
              <button onClick={() => onRefuse(item.id)} className="inline-flex items-center gap-1.5 px-3 py-1.5 border border-copper/30 text-copper-muted text-xs font-ui uppercase tracking-widest hover:text-copper"><X className="w-3.5 h-3.5" strokeWidth={2} /> Refuser</button>
              <button onClick={() => { if (window.confirm("Supprimer définitivement ?")) onDelete(item.id); }} className="ml-auto inline-flex items-center gap-1.5 px-3 py-1.5 text-copper-muted text-xs font-ui hover:text-copper"><Trash2 className="w-3.5 h-3.5" strokeWidth={1.5} /> Supprimer</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
  return (<div><Section title="À traiter" list={pending} /><Section title="Historique" list={others} /></div>);
}

function Field({ label, required, children }) {
  return (<label className="block"><div className="overline mb-1.5">{label}{required && <span className="text-copper"> *</span>}</div>{children}</label>);
}

function ModerationList({ items, type, renderItem, onApprove, onRefuse, onEdit, onDelete, editFields }) {
  const [editing, setEditing] = useState(null);
  const [edits, setEdits] = useState({});
  const pending = items.filter(i => i.status === "pending" || (!i.published && i.status !== "refused"));
  const others = items.filter(i => !(i.status === "pending" || (!i.published && i.status !== "refused")));

  const startEdit = (item) => { setEditing(item.id); setEdits({ ...item }); };
  const saveEdit = () => {
    const cleaned = {};
    editFields.forEach(f => { if (edits[f.key] !== undefined && edits[f.key] !== "") cleaned[f.key] = f.type === "number" ? parseInt(edits[f.key]) : edits[f.key]; });
    onEdit(editing, cleaned);
    setEditing(null);
  };

  const Section = ({ title, list }) => (
    <div className="mb-10">
      <div className="overline mb-4">{title} ({list.length})</div>
      {list.length === 0 && <p className="italic text-copper-muted text-sm">Aucun {type} dans cette section.</p>}
      <ul className="space-y-4">
        {list.map(item => (
          <li key={item.id} className="border border-copper/20 p-5 copper-frame" data-testid={`mod-item-${item.id}`}>
            {editing === item.id ? (
              <div className="space-y-3">
                {editFields.map(f => (
                  <label key={f.key} className="block">
                    <div className="overline mb-1">{f.label}</div>
                    {f.type === "textarea"
                      ? <textarea rows={5} value={edits[f.key] || ""} onChange={e => setEdits({...edits, [f.key]: e.target.value})} className={inputCls} />
                      : <input type={f.type || "text"} value={edits[f.key] ?? ""} onChange={e => setEdits({...edits, [f.key]: e.target.value})} className={inputCls} />}
                  </label>
                ))}
                <div className="flex gap-2">
                  <button onClick={saveEdit} data-testid={`mod-save-${item.id}`} className="inline-flex items-center gap-1.5 px-4 py-2 bg-copper text-[#050814] font-ui text-xs uppercase tracking-widest"><Check className="w-3.5 h-3.5" strokeWidth={2} /> Enregistrer & approuver</button>
                  <button onClick={() => setEditing(null)} className="px-4 py-2 border border-copper/30 text-copper font-ui text-xs uppercase tracking-widest">Annuler</button>
                </div>
              </div>
            ) : (
              <>
                {renderItem(item)}
                <div className="mt-4 flex flex-wrap items-center gap-2 pt-3 border-t border-copper/15">
                  {item.status && <span className="text-[0.6rem] font-ui uppercase tracking-widest text-copper-muted">{item.status}</span>}
                  {(item.status === "pending" || !item.published) && item.status !== "refused" && (
                    <button onClick={() => onApprove(item.id)} data-testid={`mod-approve-${item.id}`} className="inline-flex items-center gap-1.5 px-3 py-1.5 border border-copper text-copper text-xs font-ui uppercase tracking-widest hover:bg-copper/10"><Check className="w-3.5 h-3.5" strokeWidth={2} /> Approuver</button>
                  )}
                  <button onClick={() => startEdit(item)} data-testid={`mod-edit-${item.id}`} className="inline-flex items-center gap-1.5 px-3 py-1.5 border border-copper/30 text-copper-muted text-xs font-ui uppercase tracking-widest hover:text-copper hover:border-copper/60"><Edit3 className="w-3.5 h-3.5" strokeWidth={1.5} /> Modifier</button>
                  {item.status !== "refused" && (
                    <button onClick={() => onRefuse(item.id)} data-testid={`mod-refuse-${item.id}`} className="inline-flex items-center gap-1.5 px-3 py-1.5 border border-copper/30 text-copper-muted text-xs font-ui uppercase tracking-widest hover:text-copper hover:border-copper/60"><X className="w-3.5 h-3.5" strokeWidth={2} /> Refuser</button>
                  )}
                  <button onClick={() => onDelete(item.id)} data-testid={`mod-delete-${item.id}`} className="ml-auto inline-flex items-center gap-1.5 px-3 py-1.5 text-copper-muted text-xs font-ui hover:text-copper"><Trash2 className="w-3.5 h-3.5" strokeWidth={1.5} /> Supprimer</button>
                </div>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );

  return (
    <div data-testid="moderation-list">
      <Section title="À modérer" list={pending} />
      <Section title="Traités" list={others} />
    </div>
  );
}
