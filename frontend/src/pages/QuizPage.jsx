import { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import { RefreshCw, CheckCircle2, XCircle } from "lucide-react";
import { fetchQuizPool } from "@/lib/api";
import StatusBadge from "@/components/StatusBadge";

const OPTIONS = [
  { key: "fait_historique", label: "Fait historique attesté" },
  { key: "tradition", label: "Tradition / croyance" },
  { key: "legende", label: "Conte / légende" },
  { key: "hypothese", label: "Hypothèse / controverse" },
];

export default function QuizPage() {
  const [pool, setPool] = useState([]);
  const [idx, setIdx] = useState(0);
  const [answer, setAnswer] = useState(null);
  const [score, setScore] = useState({ ok: 0, total: 0 });

  const load = useCallback(() => {
    fetchQuizPool(6).then(list => { setPool(list); setIdx(0); setAnswer(null); }).catch(() => {});
  }, []);

  useEffect(() => { load(); }, [load]);

  const current = pool[idx];

  const submit = (key) => {
    if (answer) return;
    const correct = key === current.status_key;
    setAnswer({ key, correct });
    setScore(s => ({ ok: s.ok + (correct ? 1 : 0), total: s.total + 1 }));
  };

  const next = () => {
    setAnswer(null);
    if (idx + 1 >= pool.length) load();
    else setIdx(idx + 1);
  };

  if (!current) return <div className="p-16 text-center text-copper-muted">Chargement…</div>;

  return (
    <div className="mx-auto max-w-4xl px-6 lg:px-10 py-16" data-testid="quiz-page">
      <div className="text-center">
        <div className="overline mb-3">Un petit test</div>
        <h1 className="font-heading font-light text-5xl sm:text-6xl text-parchment tracking-tight">
          Vrai, croyance ou légende ?
        </h1>
        <p className="mt-5 text-parchment/70 max-w-xl mx-auto">
          Lisez l'introduction, puis devinez la nature du récit. On révèle ensuite le vrai statut.
        </p>
        <div className="mt-6 inline-flex items-center gap-6 text-sm font-ui text-copper-muted">
          <span data-testid="quiz-score">Score : <strong className="text-copper-light">{score.ok}/{score.total}</strong></span>
          <span>Question {idx + 1} / {pool.length}</span>
        </div>
      </div>

      <article className="mt-14 border border-copper/25 bg-[#0F1528]/60 copper-frame overflow-hidden animate-fade-up" key={current.id}>
        {current.hero_image && (
          <div className="aspect-[16/6] overflow-hidden border-b border-copper/15 relative">
            <img src={current.hero_image} alt="" className="w-full h-full object-cover opacity-40" />
            <div className="absolute inset-0 bg-gradient-to-t from-[#0F1528] via-transparent to-transparent" />
          </div>
        )}
        <div className="p-8 sm:p-10">
          <h2 className="font-heading text-3xl sm:text-4xl text-parchment leading-tight">{current.title}</h2>
          {current.subtitle && <p className="mt-2 italic text-copper-muted">{current.subtitle}</p>}
          <p className="mt-6 text-parchment/80 leading-relaxed">{current.excerpt}</p>

          {!answer && (
            <div className="mt-8 grid sm:grid-cols-2 gap-3" data-testid="quiz-options">
              {OPTIONS.map(opt => (
                <button
                  key={opt.key}
                  type="button"
                  data-testid={`quiz-option-${opt.key}`}
                  onClick={() => submit(opt.key)}
                  className="text-left px-5 py-4 border border-copper/30 hover:border-copper hover:bg-copper/5 font-ui text-sm text-parchment transition-colors"
                >
                  {opt.label}
                </button>
              ))}
            </div>
          )}

          {answer && (
            <div className="mt-8 p-6 border border-copper/30 bg-[#050814]" data-testid="quiz-result">
              <div className="flex items-center gap-3">
                {answer.correct ? (
                  <><CheckCircle2 className="w-6 h-6 text-[#8FB4A1]" strokeWidth={1.5} /><span className="font-heading text-2xl text-parchment">Bien vu.</span></>
                ) : (
                  <><XCircle className="w-6 h-6 text-[#C48FA9]" strokeWidth={1.5} /><span className="font-heading text-2xl text-parchment">Pas tout à fait.</span></>
                )}
              </div>
              <div className="mt-4">
                <div className="overline mb-2">Statut réel</div>
                <StatusBadge status={current.status_key} />
              </div>
              <p className="mt-4 text-sm text-parchment/70">
                {current.status_meta?.description}
              </p>
              <div className="mt-6 flex flex-wrap gap-3">
                <button
                  type="button"
                  onClick={next}
                  data-testid="quiz-next"
                  className="inline-flex items-center gap-2 px-5 py-2.5 bg-copper text-[#050814] font-ui text-xs uppercase tracking-widest hover:bg-copper-light"
                >
                  <RefreshCw className="w-4 h-4" strokeWidth={2} /> Suivant
                </button>
                <Link
                  to={`/recit/${current.id}`}
                  className="inline-flex items-center gap-2 px-5 py-2.5 border border-copper text-copper font-ui text-xs uppercase tracking-widest hover:bg-copper/10"
                >
                  Lire le récit complet
                </Link>
              </div>
            </div>
          )}
        </div>
      </article>
    </div>
  );
}
