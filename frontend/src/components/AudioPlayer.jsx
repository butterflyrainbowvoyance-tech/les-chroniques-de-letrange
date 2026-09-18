import { useEffect, useRef, useState } from "react";
import { Play, Pause, Square, AudioLines } from "lucide-react";

export default function AudioPlayer({ storyId, text = "", compact = false }) {
const [status, setStatus] = useState("idle");
const chunksRef = useRef([]);
const indexRef = useRef(0);

useEffect(() => {
return () => {
window.speechSynthesis?.cancel();
};
}, [storyId]);

const cleanText = (value) =>
String(value || "")
.replace(/[#*_>`~[\]()]/g, " ")
.replace(/\s+/g, " ")
.trim();

const makeChunks = (value) => {
const cleaned = cleanText(value);
if (!cleaned) return [];

const sentences =
cleaned.match(/[^.!?…]+[.!?…]+|[^.!?…]+$/g) || [cleaned];

const chunks = [];
let current = "";

sentences.forEach((sentence) => {
if ((current + sentence).length > 220 && current) {
chunks.push(current.trim());
current = sentence;
} else {
current += " " + sentence;
}
});

if (current.trim()) chunks.push(current.trim());
return chunks;
};

const getFrenchVoice = () => {
const voices = window.speechSynthesis.getVoices();
const french = voices.filter((voice) =>
voice.lang?.toLowerCase().startsWith("fr")
);

return (
french.find((voice) =>
/thomas|audrey|amelie|amélie|marie|google/i.test(voice.name)
) ||
french[0] ||
null
);
};

const speakNext = () => {
if (indexRef.current >= chunksRef.current.length) {
setStatus("idle");
indexRef.current = 0;
return;
}

const utterance = new SpeechSynthesisUtterance(
chunksRef.current[indexRef.current]
);

utterance.lang = "fr-FR";
utterance.rate = 0.95;
utterance.pitch = 1;

const voice = getFrenchVoice();
if (voice) utterance.voice = voice;

utterance.onend = () => {
indexRef.current += 1;
speakNext();
};

utterance.onerror = () => {
setStatus("idle");
};

window.speechSynthesis.speak(utterance);
};

const toggle = () => {
if (!("speechSynthesis" in window)) return;

if (status === "playing") {
window.speechSynthesis.pause();
setStatus("paused");
return;
}

if (status === "paused") {
window.speechSynthesis.resume();
setStatus("playing");
return;
}

chunksRef.current = makeChunks(text);
indexRef.current = 0;

if (!chunksRef.current.length) return;

window.speechSynthesis.cancel();
setStatus("playing");
speakNext();
};

const stop = () => {
window.speechSynthesis?.cancel();
indexRef.current = 0;
setStatus("idle");
};

return (
<div className="border border-copper/30 bg-[#050814] rounded-lg p-4">
<div className="flex items-center gap-3">
<button
type="button"
onClick={toggle}
aria-label={status === "playing" ? "Pause" : "Écouter"}
className={`shrink-0 flex items-center justify-center rounded-full border border-copper/40 ${
compact ? "w-10 h-10" : "w-12 h-12"
}`}
>
{status === "playing" ? (
<Pause className="w-5 h-5" />
) : (
<Play className="w-5 h-5 ml-0.5" />
)}
</button>

<div className="flex-1">
<div className="flex items-center gap-2">
<AudioLines className="w-4 h-4" />
<span>
{status === "playing"
? "Lecture en cours…"
: status === "paused"
? "Lecture en pause"
: "Écouter cette histoire"}
</span>
</div>
</div>

{status !== "idle" && (
<button
type="button"
onClick={stop}
aria-label="Arrêter"
className="p-2"
>
<Square className="w-4 h-4" />
</button>
)}
</div>
</div>
);
}
