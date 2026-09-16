import { useState, useRef, useEffect } from "react";
import { Play, Pause, Loader2, AudioLines } from "lucide-react";
import { API } from "@/lib/api";

export default function AudioPlayer({ storyId, compact = false }) {
  const [state, setState] = useState("idle"); // idle | loading | playing | paused | error
  const [progress, setProgress] = useState(0);
  const [duration, setDuration] = useState(0);
  const audioRef = useRef(null);
  const src = `${API}/audio/story/${storyId}.mp3`;

  useEffect(() => {
    // reset on story change
    setState("idle"); setProgress(0); setDuration(0);
    if (audioRef.current) { audioRef.current.pause(); audioRef.current = null; }
    return () => { if (audioRef.current) audioRef.current.pause(); };
  }, [storyId]);

  const toggle = async () => {
    if (state === "playing") { audioRef.current.pause(); setState("paused"); return; }
    if (state === "paused") { audioRef.current.play(); setState("playing"); return; }
    setState("loading");
    try {
      const a = new Audio(src);
      audioRef.current = a;
      a.addEventListener("loadedmetadata", () => setDuration(a.duration || 0));
      a.addEventListener("timeupdate", () => setProgress(a.currentTime || 0));
      a.addEventListener("ended", () => { setState("idle"); setProgress(0); });
      a.addEventListener("error", () => setState("error"));
      await a.play();
      setState("playing");
    } catch {
      setState("error");
    }
  };

  const fmt = (t) => {
    if (!t || isNaN(t)) return "0:00";
    const m = Math.floor(t / 60);
    const s = Math.floor(t % 60);
    return `${m}:${s.toString().padStart(2, "0")}`;
  };

  const isBusy = state === "loading";
  const isOn = state === "playing";
  const pct = duration ? (progress / duration) * 100 : 0;

  return (
    <div
      data-testid={`audio-player-${storyId}`}
      className={`border border-copper/30 bg-[#050814]/60 copper-frame ${compact ? "p-3" : "p-5"} flex items-center gap-4`}
    >
      <button
        type="button"
        onClick={toggle}
        disabled={isBusy}
        data-testid="audio-toggle"
        aria-label={isOn ? "Pause" : "Écouter"}
        className={`shrink-0 flex items-center justify-center rounded-full border-2 border-copper transition-colors ${
          isOn ? "bg-copper text-[#050814]" : "bg-transparent text-copper hover:bg-copper/10"
        } ${compact ? "w-10 h-10" : "w-12 h-12"}`}
      >
        {isBusy ? <Loader2 className="w-5 h-5 animate-spin" strokeWidth={1.5} />
         : isOn ? <Pause className="w-5 h-5" strokeWidth={1.5} />
         : <Play className="w-5 h-5 ml-0.5" strokeWidth={1.5} />}
      </button>
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 text-copper font-ui text-[0.7rem] uppercase tracking-[0.2em] mb-1.5">
          <AudioLines className="w-3.5 h-3.5" strokeWidth={1.5} />
          {state === "error" ? "Audio indisponible" : "Écouter cette chronique"}
        </div>
        <div className="relative h-1 bg-copper/15 rounded-full overflow-hidden">
          <div className="absolute inset-y-0 left-0 bg-copper transition-[width] duration-300" style={{ width: `${pct}%` }} />
        </div>
        <div className="mt-1 flex justify-between text-[0.65rem] font-ui text-copper-muted tabular-nums">
          <span>{fmt(progress)}</span>
          <span>{duration ? fmt(duration) : (isBusy ? "génération en cours…" : "voix : Nova · qualité HD")}</span>
        </div>
      </div>
    </div>
  );
}
