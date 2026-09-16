export default function Footer() {
  return (
    <footer className="mt-32 border-t border-copper/15 bg-[#050814] relative z-10" data-testid="footer">
      <div className="mx-auto max-w-7xl px-6 lg:px-10 py-12 grid md:grid-cols-3 gap-10">
        <div>
          <div className="font-heading text-2xl text-parchment">Les Chroniques de l'Étrange</div>
          <p className="mt-3 text-sm text-copper-muted leading-relaxed max-w-sm">
            Une exploration de l'histoire de la spiritualité, du mysticisme et des grandes légendes.
            Toujours distinguer le fait, la croyance, la légende et l'hypothèse.
          </p>
        </div>
        <div>
          <div className="overline mb-3">Principe éditorial</div>
          <p className="text-sm text-parchment/70 leading-relaxed">
            Nous ne cherchons pas à convaincre de croire ou de ne pas croire.
            Nous racontons comment l'être humain, depuis des siècles, essaie de comprendre l'invisible.
          </p>
        </div>
        <div>
          <div className="overline mb-3">Sources</div>
          <p className="text-sm text-parchment/70 leading-relaxed">
            Chaque récit indique ses sources : ouvrages, archives, musées et documents pour aller plus loin.
          </p>
        </div>
      </div>
      <div className="divider-copper" />
      <div className="mx-auto max-w-7xl px-6 lg:px-10 py-5 text-xs text-copper-muted font-ui flex flex-wrap justify-between gap-3">
        <span>© Les Chroniques de l'Étrange</span>
        <span className="italic">« Ce que l'on sait, ce que l'on croit, ce que l'on raconte. »</span>
      </div>
    </footer>
  );
}
