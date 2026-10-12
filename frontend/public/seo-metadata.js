/* Métadonnées publiques : aucun texte ni lien caché dans l’interface. */
(() => {
  'use strict';
  const topics = {
    dream: ['Dream Even','roman Dream Even','Dorothée Lancelot Dream Even','Dans mes yeux','roman fantastique','univers Dream Even','personnages Dream Even','lieux Dream Even','Dolmen Blissim','Loryan Halow','Martin Balma','Bella Tikka','Hell-Heaven','Mc Carthney’s','Cruise-Thea','ville imaginaire','lecture immersive','exploration narrative','roman et rêves','fiction de Dorothée Lancelot'],
    chroniques: ['Les Chroniques de l’Étrange','histoire de l’ésotérisme','histoire des croyances','histoire de l’occultisme','histoire du mysticisme','arts divinatoires','contes et légendes','récits documentés','faits historiques','traditions populaires','symboles historiques','frise chronologique','carte des légendes','voyage dans le temps','cabinet de curiosités','origine des superstitions','livre du soir','quiz historique','lieux étranges','sources historiques'],
    book: ['Ésotérisme Book','histoire de l’astrologie','histoire du tarot','cartomancie','écriture automatique','symbolique des bougies','numérologie','histoire du magnétisme','histoire de la médiumnité','lithothérapie et croyances','radiesthésie','histoire du ouija','histoire de la voyance','glossaire ésotérique','bibliographie ésotérique','lecture numérique','livre interactif','anecdotes ésotériques','symbolisme des nombres','origines des pratiques ésotériques'],
    aaesad: ['AAESAD','Association d’Aide et Soutien au Deuil','cafés deuil','café deuil Oise','café deuil Nogent-sur-Oise','soutien au deuil','rencontres autour du deuil','association deuil Oise','association laïque','lutte contre l’isolement','entraide associative','écoute sans jugement','souvenirs des défunts','témoignages de deuil','activités AAESAD','agenda AAESAD','adhésion AAESAD','dons AAESAD','bénévolat Oise','solidarité Nogent-sur-Oise'],
    dorothee: ['Dorothée Lancelot','auteure Dorothée Lancelot','livres Dorothée Lancelot','conférences Dorothée Lancelot','biographie Dorothée Lancelot','médium Dorothée Lancelot','onirothérapie','médiumnité','rêves et symboles','histoire de la spiritualité','écriture et transmission','conférences dans l’Oise','conférences sur l’ésotérisme','interviews Dorothée Lancelot','presse Dorothée Lancelot','vidéos Dorothée Lancelot','bibliographie Dorothée Lancelot','rencontres littéraires','univers de Dorothée Lancelot','accompagnement du deuil']
  };
  const host = location.hostname.replace(/^www\./, '');
  const sites = {
    'dreameven.dorotheelancelot.fr': {key:'dream',name:'Dream Even',origin:'https://dreameven.dorotheelancelot.fr',description:'Explorez les personnages, les lieux et le récit immersif de Dream Even, le roman de Dorothée Lancelot.'},
    'leschroniquesdeletrange.fr': {key:'chroniques',name:'Les Chroniques de l’Étrange',origin:'https://www.leschroniquesdeletrange.fr',description:'Explorez l’histoire, les croyances et les légendes avec des récits documentés et leurs sources.'},
    'esoterismebook.dorotheelancelot.fr': {key:'book',name:'Ésotérisme Book',origin:'https://esoterismebook.dorotheelancelot.fr',description:'Découvrez l’histoire des pratiques ésotériques, leurs symboles, leurs anecdotes et leur bibliographie.'},
    'aaesad.fr': {key:'aaesad',name:'AAESAD',origin:'https://aaesad.fr',description:'L’AAESAD propose des cafés deuil et des rencontres solidaires dans l’Oise, autour de Nogent-sur-Oise.'},
    'dorotheelancelot.fr': {key:'dorothee',name:'Dorothée Lancelot',origin:'https://dorotheelancelot.fr',description:'Découvrez les livres, les conférences et les différents univers de Dorothée Lancelot, auteure et médium.'},
    'biographie.dorotheelancelot.fr': {key:'dorothee',name:'Biographie de Dorothée Lancelot',origin:'https://biographie.dorotheelancelot.fr',description:'Découvrez le parcours, les livres, les conférences et les vidéos de Dorothée Lancelot.'}
  };
  const site = sites[host];
  if (!site || !document.head) return;
  const initialDescription = document.querySelector('meta[name="description"]')?.content || site.description;
  const initialTitle = document.title;
  const initialRobots = document.querySelector('meta[name="robots"]')?.content || 'index, follow, max-image-preview:large';
  function meta(name, value, property = false) {
    const attr = property ? 'property' : 'name';
    const nodes = [...document.head.querySelectorAll(`meta[${attr}="${name}"]`)];
    const node = nodes.shift() || document.head.appendChild(document.createElement('meta'));
    node.setAttribute(attr, name);
    if (node.content !== value) node.content = value;
    nodes.forEach(n => n.remove());
  }
  function update() {
    const path = location.pathname;
    const privatePage = /(?:^|\/)(?:admin|administration|creatrice|connexion|login|rendez-vous)(?:\/|$)/i.test(path);
    if (privatePage) { meta('robots','noindex, follow');document.getElementById('page-seo-20261012')?.remove();return; }
    meta('robots', initialRobots);
    const root = /^\/(?:index\.html)?$/.test(path);
    const heading = document.querySelector('main h1, #root h1, h1')?.textContent.replace(/\s+/g,' ').trim();
    const lead = document.querySelector('main h1 ~ p, main p, article p')?.textContent.replace(/\s+/g,' ').trim();
    const title = heading && !root ? `${heading} | ${site.name}` : (root ? initialTitle : document.title);
    const description = !root && lead && lead.length > 45 ? lead.slice(0,170) : initialDescription;
    const canonical = site.origin + (root ? '/' : path);
    if (document.title !== title) document.title = title;
    const links = [...document.head.querySelectorAll('link[rel="canonical"]')];
    const link = links.shift() || document.head.appendChild(document.createElement('link'));
    link.rel = 'canonical';
    if (link.href !== canonical) link.href = canonical;
    links.forEach(n => n.remove());
    const pageText = (heading || '') + ' ' + path.replace(/[-/]/g,' ');
    const normalize = s => s.toLocaleLowerCase('fr').normalize('NFD').replace(/[\u0300-\u036f]/g,'');
    const relevant = topics[site.key].filter(term => term.split(/\s+/).some(word => word.length > 4 && normalize(pageText).includes(normalize(word))));
    const keywords = root ? topics[site.key] : [...new Set([topics[site.key][0],...(relevant.length ? relevant : topics[site.key].slice(1,5))])];
    meta('description', description);
    meta('keywords', keywords.join(', '));
    meta('og:title',title,true); meta('og:description',description,true); meta('og:url',canonical,true);
    meta('og:locale','fr_FR',true); meta('og:site_name',site.name,true);
    meta('twitter:title',title); meta('twitter:description',description);
    let schema = document.getElementById('page-seo-20261012');
    if (!schema) { schema=document.createElement('script');schema.type='application/ld+json';schema.id='page-seo-20261012';document.head.appendChild(schema); }
    const data = {'@context':'https://schema.org','@type':'WebPage','@id':canonical+'#webpage',url:canonical,name:title,description,inLanguage:'fr-FR',isPartOf:{'@type':'WebSite','@id':site.origin+'/#website',name:site.name,url:site.origin+'/'},keywords:keywords.join(', ')};
    const content=JSON.stringify(data);
    if(schema.textContent!==content)schema.textContent=content;
  }
  let pending=false;
  const schedule=()=>{if(!pending){pending=true;requestAnimationFrame(()=>{pending=false;update();});}};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',schedule,{once:true});else schedule();
  new MutationObserver(schedule).observe(document.body || document.documentElement,{childList:true,subtree:true,characterData:true});
  addEventListener('popstate',schedule);
})();
