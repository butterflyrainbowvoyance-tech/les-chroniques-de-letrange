import { useState } from "react";
import { Handshake, Send, MapPin, Feather } from "lucide-react";
import { toast } from "sonner";
import { postCollaboration, postEnquete } from "@/lib/api";

const KINDS = [
  "Podcast", "Vidéo / documentaire", "Interview", "Conférence",
  "Enquête de terrain", "Visite de lieu", "Recherche documentaire",
  "Projet culturel", "Création de contenu", "Autre"
];

export default function CollaborerPage() {
  const [tab, setTab] = useState("collab");
  const [collab, setCollab] = useState({ name: "", email: "", kind: KINDS[0], project: "", links: "", message: "" });
  const [enquete, setEnquete] = useState({ name: "", email: "", role: "", place_name: "", place_location: "", tradition_summary: "", message: "" });
  const [sending, setSending] = useState(false);

  const send = async (fn, payload, reset) => {
    setSending(true);
    try {
      await fn(payload);
      toast.success("Proposition envoyée. La rédaction vous répondra.");
      reset();
    } catch (err) { toast.error(err?.response?.data?.detail || "Erreur lors de l'envoi."); }
    setSending(false);
  };

  return (
    <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16" data-testid="collaborer-page">
      <div className="overline mb-4">Ouvrons les portes ensemble</div>
      <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight leading-[1.05]">
        Collaborer avec nous.
      </h1>
      <p className="mt-6 text-parchment/75 leading-relaxed max-w-2xl">
        Les Chroniques de l'Étrange sont ouvertes aux collaborations et partenariats :
        podcasts, vidéos, interviews, conférences, enquêtes de terrain, visites de lieux,
        recherches documentaires, projets culturels et créations de contenus.
      </p>
      <p className="mt-4 text-sm italic text-copper-muted max-w-2xl border-l-2 border-copper/40 pl-4">
        Ligne éditoriale : une enquête sur un phénomène paranormal n'est jamais présentée comme
        une preuve. Faits historiques, témoignages, croyances, traditions, légendes et hypothèses
        restent toujours distingués.
      </p>
      <p className="mt-4 text-sm text-parchment/70 max-w-2xl">
        Vous préférez écrire directement ?{" "}
        <a href="mailto:ooleschroniquesdeletrangeoo@gmail.com" className="text-copper hover:text-copper-light break-all" data-testid="collab-email-link">
          ooleschroniquesdeletrangeoo@gmail.com
        </a>
      </p>

      <div className="mt-10 flex flex-wrap gap-2" role="tablist">
        <TabButton active={tab === "collab"} onClick={() => setTab("collab")} testId="tab-collab" icon={Handshake}>Proposer une collaboration</TabButton>
        <TabButton active={tab === "enquete"} onClick={() => setTab("enquete")} testId="tab-enquete" icon={Feather}>Nous inviter à enquêter</TabButton>
      </div>

      {tab === "collab" && (
        <form onSubmit={e => { e.preventDefault(); send(postCollaboration, collab, () => setCollab({ name: "", email: "", kind: KINDS[0], project: "", links: "", message: "" })); }}
          className="mt-8 border border-copper/25 bg-[#0F1528]/60 copper-frame p-6 sm:p-8 space-y-5" data-testid="collab-form">
          <div className="grid sm:grid-cols-2 gap-4">
            <Field label="Nom / prénom ou organisme" required><input required value={collab.name} onChange={e => setCollab({...collab, name: e.target.value})} data-testid="collab-name" className={inp} /></Field>
            <Field label="E-mail" required><input type="email" required value={collab.email} onChange={e => setCollab({...collab, email: e.target.value})} data-testid="collab-email" className={inp} /></Field>
          </div>
          <Field label="Type de collaboration" required>
            <select value={collab.kind} onChange={e => setCollab({...collab, kind: e.target.value})} data-testid="collab-kind" className={inp}>
              {KINDS.map(k => <option key={k} value={k}>{k}</option>)}
            </select>
          </Field>
          <Field label="Présentation du projet" required><input required value={collab.project} onChange={e => setCollab({...collab, project: e.target.value})} data-testid="collab-project" className={inp} /></Field>
          <Field label="Liens (site, réseaux sociaux)"><input value={collab.links} onChange={e => setCollab({...collab, links: e.target.value})} placeholder="https://…" className={inp} /></Field>
          <Field label="Message détaillé" required><textarea rows={7} required value={collab.message} onChange={e => setCollab({...collab, message: e.target.value})} data-testid="collab-message" className={inp} /></Field>
          <button type="submit" disabled={sending} data-testid="collab-submit" className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light disabled:opacity-50">
            <Send className="w-4 h-4" strokeWidth={2} /> Envoyer la proposition
          </button>
        </form>
      )}

      {tab === "enquete" && (
        <form onSubmit={e => { e.preventDefault(); send(postEnquete, enquete, () => setEnquete({ name: "", email: "", role: "", place_name: "", place_location: "", tradition_summary: "", message: "" })); }}
          className="mt-8 border border-copper/25 bg-[#0F1528]/60 copper-frame p-6 sm:p-8 space-y-5" data-testid="enquete-form">
          <p className="text-sm text-parchment/75 leading-relaxed">
            Propriétaire de château, association, commune, particulier — proposez-nous un lieu, une histoire
            ou une tradition à documenter. Nous ne validons pas de phénomène surnaturel : nous documentons ce
            qui est attesté, ce qui est raconté, et ce qui est cru.
          </p>
          <div className="grid sm:grid-cols-2 gap-4">
            <Field label="Nom / prénom" required><input required value={enquete.name} onChange={e => setEnquete({...enquete, name: e.target.value})} data-testid="enquete-name" className={inp} /></Field>
            <Field label="E-mail" required><input type="email" required value={enquete.email} onChange={e => setEnquete({...enquete, email: e.target.value})} data-testid="enquete-email" className={inp} /></Field>
          </div>
          <Field label="À quel titre proposez-vous ce lieu ?"><input value={enquete.role} onChange={e => setEnquete({...enquete, role: e.target.value})} placeholder="Propriétaire, association, guide, curieux…" className={inp} /></Field>
          <Field label="Nom du lieu ou de l'histoire" required><input required value={enquete.place_name} onChange={e => setEnquete({...enquete, place_name: e.target.value})} data-testid="enquete-place" className={inp} /></Field>
          <Field label="Localisation (ville, région, pays)" required><input required value={enquete.place_location} onChange={e => setEnquete({...enquete, place_location: e.target.value})} className={inp} /></Field>
          <Field label="Ce que la tradition raconte" required><textarea rows={5} required value={enquete.tradition_summary} onChange={e => setEnquete({...enquete, tradition_summary: e.target.value})} data-testid="enquete-tradition" className={inp} /></Field>
          <Field label="Message complémentaire (facultatif)"><textarea rows={4} value={enquete.message} onChange={e => setEnquete({...enquete, message: e.target.value})} className={inp} /></Field>
          <button type="submit" disabled={sending} data-testid="enquete-submit" className="inline-flex items-center gap-2 px-6 py-3 bg-copper text-[#050814] font-ui text-sm uppercase tracking-widest hover:bg-copper-light disabled:opacity-50">
            <MapPin className="w-4 h-4" strokeWidth={2} /> Envoyer la proposition
          </button>
        </form>
      )}
    </div>
  );
}

const inp = "w-full px-3 py-2.5 bg-[#050814] border border-copper/25 text-parchment font-ui text-sm focus:outline-none focus:border-copper/60";
function Field({ label, required, children }) {
  return (<label className="block"><div className="overline mb-1.5">{label}{required && <span className="text-copper"> *</span>}</div>{children}</label>);
}
function TabButton({ active, onClick, testId, icon: Icon, children }) {
  return (
    <button type="button" onClick={onClick} data-testid={testId}
      className={`inline-flex items-center gap-2 px-4 py-2 text-sm font-ui border ${active ? "border-copper bg-copper/15 text-copper-light" : "border-copper/25 text-copper-muted hover:text-copper"}`}>
      <Icon className="w-4 h-4" strokeWidth={1.5} /> {children}
    </button>
  );
}
