"""Les morts étranges — décès historiquement attestés de personnages
entourés d'une aura d'ésotérisme, d'occultisme ou de mysticisme.
Toujours : ce que les archives disent réellement + ce que la légende a rajouté.
"""

MORTS_UNIVERSE = {
    "id": "morts-etranges",
    "title": "Les morts étranges",
    "subtitle": "Décès attestés, halo d'ésotérisme",
    "description": "Empoisonnements, disparitions, agonies inexpliquées. Des morts réelles, documentées, mais qui traînent depuis un siècle une odeur d'occulte. On dit ce que l'on sait, on démêle ce que la légende a rajouté.",
    "image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg"
}

MORTS_STORIES = [
    {
        "id": "mort-mozart",
        "universe": "morts-etranges",
        "title": "Mozart : empoisonné par Salieri ? Par la franc-maçonnerie ?",
        "subtitle": "Une agonie fulgurante à 35 ans, deux siècles de théories",
        "status": "fait_historique",
        "era": "moderne",
        "era_label": "1791",
        "year": 1791,
        "region": "Vienne",
        "coords": [48.2082, 16.3738],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Décembre 1791. Mozart est terrassé en quinze jours par une maladie qui gonfle le corps et déchire l'esprit. Il vient de composer un Requiem qu'il croit dédié à sa propre mort.",
        "content": [
            "**Ce que les archives disent avec certitude** : Wolfgang Amadeus Mozart tombe malade le 20 novembre 1791. Il meurt le 5 décembre à 0h55, à Vienne, dans son appartement de la Rauhensteingasse. Il a 35 ans.",
            "Les symptômes rapportés par les proches et son beau-frère Nikolaus Nissen : fièvre élevée, gonflement du corps (œdème), douleurs articulaires, éruption cutanée, vomissements. La conscience alterne entre lucidité extraordinaire et délire. Il travaille au *Requiem* jusqu'à quelques heures avant la mort.",
            "**Le halo mystique** commence immédiatement. Mozart lui-même, dans ses dernières semaines, aurait confié à sa femme Constance : *« Je suis en train d'écrire ce Requiem pour moi. »* Il pense à un mystérieux commanditaire vêtu de gris — c'était en réalité un émissaire du comte Walsegg, qui voulait faire passer l'œuvre pour la sienne. Rien de surnaturel.",
            "**Les théories du poison** apparaissent aussitôt. Les journaux allemands de 1791 lancent la rumeur d'un empoisonnement. Une piste : Antonio Salieri, compositeur officiel de la cour. En 1823, un Salieri âgé, hospitalisé, atteint de démence, aurait avoué avoir empoisonné Mozart — puis nié. Rien ne le prouve, et les archives médicales de Salieri décrivent un état confusionnel.",
            "**Autre piste, la franc-maçonnerie** : Mozart, franc-maçon convaincu, venait de composer *La Flûte enchantée*, qui met en scène des rites initiatiques. Une frange de commentateurs (surtout au XIXe) verra dans sa mort la vengeance de loges offensées par la divulgation. Aucun document maçonnique ne l'atteste.",
            "**Le diagnostic médical actuel**, appuyé sur une étude néerlandaise de 2009 (Zegers et al., *Annals of Internal Medicine*), pointe la piste la plus probable : une **infection streptococcique** ayant dégénéré en glomérulonéphrite aiguë avec insuffisance rénale. Compatible avec tous les symptômes documentés. Aucun besoin de poison."
        ],
        "sources": [
            "Nikolaus Nissen, Biographie W. A. Mozarts, 1828",
            "Zegers et al., 'The Death of Wolfgang Amadeus Mozart', Annals of Internal Medicine, 2009",
            "Musée Mozart, Salzbourg"
        ],
        "tags": ["mozart", "empoisonnement", "requiem", "franc-maçonnerie"]
    },
    {
        "id": "mort-hendrick-jeanne-albret",
        "universe": "morts-etranges",
        "title": "Jeanne d'Albret : les gants empoisonnés de Catherine de Médicis ?",
        "subtitle": "1572, trois mois avant la Saint-Barthélemy",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "1572",
        "year": 1572,
        "region": "Paris",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "La reine de Navarre, cheffe protestante, meurt à Paris deux mois avant le massacre de la Saint-Barthélemy. Tout de suite, on accuse une paire de gants parfumés.",
        "content": [
            "**Ce qui est attesté** : Jeanne d'Albret, reine de Navarre, mère du futur Henri IV, arrive à Paris en mai 1572 pour négocier le mariage de son fils avec Marguerite de Valois. Elle est logée dans les appartements royaux du Louvre. Elle meurt le 9 juin 1572, à 43 ans, après une maladie de deux semaines.",
            "**Le halo occulte** est immédiat. Les huguenots accusent : Catherine de Médicis, la reine mère, aurait offert à Jeanne une paire de gants parfumés préparés par son astrologue-empoisonneur florentin René Bianchi, dit *René le Florentin*. Le poison, absorbé par la peau, aurait tué en deux semaines. La rumeur est reprise par Voltaire, Alexandre Dumas, et fait aujourd'hui partie du folklore national.",
            "**Ce que les archives disent réellement** : Jeanne d'Albret avait une santé fragile depuis des années. Les rapports médicaux du docteur Desneux, son médecin personnel, décrivent une **tuberculose évolutive** documentée depuis au moins 1568 : toux persistante, fièvre, amaigrissement, hémoptysies. À sa mort, l'autopsie révèle des poumons ravagés et un abcès pleural.",
            "**Il n'existe aucune trace archivistique** d'un cadeau de gants parfumés — ni chez Catherine, ni chez Jeanne, ni chez leurs entourages respectifs. La rumeur naît dans les mois qui suivent, en pleine propagande post-Saint-Barthélemy.",
            "**Le paradoxe** : Catherine de Médicis a fait beaucoup de choses discutables dans sa vie politique. Empoisonner Jeanne d'Albret avec des gants n'en fait pas partie — cette accusation-là est presque à coup sûr fausse. La reine mère était plus intelligente que ça, et surtout Jeanne mourait déjà."
        ],
        "sources": [
            "Nancy Roelker, Queen of Navarre: Jeanne d'Albret, 1968",
            "Denis Crouzet, Le Haut Cœur de Catherine de Médicis, 2005",
            "Rapport d'autopsie, BNF, Fonds français 3237"
        ],
        "tags": ["jeanne d'albret", "empoisonnement", "gants", "renaissance"]
    },
    {
        "id": "mort-poe",
        "universe": "morts-etranges",
        "title": "Edgar Allan Poe : trouvé délirant, vêtu des habits d'un autre",
        "subtitle": "Baltimore, octobre 1849, quatre jours de mystère",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "1849",
        "year": 1849,
        "region": "Baltimore",
        "coords": [39.2904, -76.6122],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Le 3 octobre, on retrouve Poe dans une taverne de Baltimore, incohérent, trempé, portant les vêtements d'un inconnu. Quatre jours plus tard, il meurt à l'hôpital, sans qu'on ait pu tirer un mot cohérent de lui.",
        "content": [
            "**Ce que les archives disent** : Edgar Allan Poe quitte Richmond le 27 septembre 1849 en direction de Philadelphie. Il ne l'atteint jamais. Le 3 octobre, un typographe le retrouve à Baltimore, devant la taverne Ryan's, qui sert aussi de bureau de vote — c'est un jour d'élection. Il est délirant, sale, trempé, vêtu de vêtements qui ne sont pas les siens : costume de laine bon marché et chapeau de paille cabossé.",
            "Il est transporté à l'hôpital Washington College. Le docteur John Moran le soigne pendant quatre jours. Poe alterne délires et lucidité brève. Il appelle à plusieurs reprises un certain **Reynolds** — personne ne sait qui c'est. Il meurt le 7 octobre 1849 à 5 heures du matin, à 40 ans, en murmurant : *« Lord, help my poor soul. »*",
            "**Le halo mystique** est immédiat, alimenté par un ennemi de Poe : Rufus Griswold, journaliste littéraire, qui publie une nécrologie calomnieuse le lendemain, décrivant Poe comme alcoolique, drogué, suicidaire. Cette version, largement démentie depuis, a colonisé la légende.",
            "**Les théories** se sont multipliées : delirium tremens, rage (Poe s'était plaint de morsures récentes), tumeur au cerveau, encéphalite, empoisonnement au mercure ou à l'oxyde de carbone. La théorie la plus étayée aujourd'hui est celle du **cooping** : à l'époque, les gangs politiques de Baltimore kidnappaient des passants, les droguaient à l'alcool ou à l'opium, les faisaient revêtir plusieurs déguisements pour voter plusieurs fois dans différents bureaux. Cela expliquerait les vêtements changés, la localisation près d'un bureau de vote, l'état comateux.",
            "**L'étrange dans tout ça** : Poe écrivait depuis vingt ans des histoires de mort violente, d'enterré vivant, d'empoisonnement, de manipulation mentale. Il est mort dans des circonstances qui auraient pu être une de ses nouvelles. Le mystère de sa fin est peut-être ce que l'histoire littéraire pouvait lui offrir de plus digne."
        ],
        "sources": [
            "John J. Moran, A Defense of Edgar Allan Poe, 1885",
            "Matthew Pearl, The Poe Shadow, 2006",
            "Poe Museum, Richmond — dossier médical original"
        ],
        "tags": ["poe", "baltimore", "cooping", "mort mystérieuse"]
    },
    {
        "id": "mort-cesare-borgia",
        "universe": "morts-etranges",
        "title": "César Borgia : celui qui empoisonnait s'est empoisonné lui-même",
        "subtitle": "La *cantarella*, poison légendaire des Borgia",
        "status": "hypothese",
        "era": "renaissance",
        "era_label": "1503",
        "year": 1503,
        "region": "Rome",
        "coords": [41.9028, 12.4964],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Août 1503. À une table romaine, cardinaux et famille Borgia dînent ensemble. Trois jours plus tard, le pape Alexandre VI est mort, et son fils César se bat contre la même agonie.",
        "content": [
            "**Le décor** : les Borgia règnent sur la Rome papale. Alexandre VI (Rodrigo), son fils César (le modèle du *Prince* de Machiavel), sa fille Lucrèce. On leur prête l'usage d'un poison de leur invention, la *cantarella* — un mélange à base d'arsenic, très lent, indétectable. Personne n'a jamais retrouvé la recette. Beaucoup d'historiens pensent que ce poison n'a jamais existé.",
            "**Ce qui est attesté** : le 12 août 1503, le pape et son fils dînent chez le cardinal Adriano da Corneto. Une semaine plus tard, Alexandre VI est fiévreux. Il meurt le 18 août, à 72 ans. César tombe malade le même soir, souffre atrocement pendant plusieurs semaines, mais survit.",
            "**Les théories immédiates** : les rumeurs affirment que César comptait empoisonner le cardinal Corneto pour hériter, mais qu'un serviteur aurait échangé les verres. Les Borgia se seraient empoisonnés eux-mêmes. Version dramatique, colportée par les diplomates vénitiens dès la fin août 1503.",
            "**Les diagnostics rétrospectifs modernes** privilégient une autre piste : **la malaria**. Rome est en été 1503 traversée par une épidémie de fièvres particulièrement virulente. Les symptômes rapportés (fièvre récurrente, vomissements, faiblesse extrême, teint jaunâtre) correspondent à une malaria pernicieuse plus qu'à un empoisonnement à l'arsenic.",
            "**L'ironie historique** : c'est la médecine moderne qui innocente les Borgia du crime dont on les accuse depuis cinq cents ans. Ce qui les a tués n'était pas leur propre poison — c'était un moustique. César, plus jeune et plus robuste, y a survécu. Il mourra finalement en 1507 en Navarre, tué au combat, à 31 ans."
        ],
        "sources": [
            "Sarah Bradford, Cesare Borgia: His Life and Times, 1976",
            "Machiavel, Le Prince, 1513",
            "Diarii de Marino Sanudo (vol. V), édition vénitienne"
        ],
        "tags": ["borgia", "cantarella", "arsenic", "malaria"]
    },
    {
        "id": "mort-tycho-brahe",
        "universe": "morts-etranges",
        "title": "Tycho Brahe : mort d'avoir été trop poli",
        "subtitle": "1601. La vessie éclatée, ou l'empoisonnement au mercure ?",
        "status": "hypothese",
        "era": "renaissance",
        "era_label": "1601",
        "year": 1601,
        "region": "Prague",
        "coords": [50.0755, 14.4378],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "L'astronome danois avait un nez en argent, un élan apprivoisé et une santé de fer. Il meurt en 1601 après onze jours d'agonie. Diagnostic officiel : vessie éclatée pour avoir voulu tenir sa politesse jusqu'à la fin d'un banquet.",
        "content": [
            "**Le personnage** : Tycho Brahe (1546-1601) est l'astronome le plus précis du monde avant l'invention du télescope. Il a produit des tables planétaires que Kepler exploitera pour formuler ses lois. Il porte un nez en métal (le vrai perdu dans un duel étudiant). Il est riche, capricieux, et vit à Prague sous la protection de l'empereur Rodolphe II.",
            "**Ce qui est attesté** : le 13 octobre 1601, Brahe assiste à un banquet à la cour de Rodolphe II. Selon la coutume, on ne quitte pas la table avant l'empereur. Brahe, qui a beaucoup bu, aurait souffert d'une envie pressante qu'il n'a pas osé assouvir. Onze jours plus tard, le 24 octobre, il meurt à Prague dans des douleurs abdominales atroces.",
            "**Le diagnostic officiel de l'époque** : rupture de la vessie ou infection urinaire aiguë, provoquée par la rétention. Kepler, son assistant, rapporte la version dans son journal. Brahe aurait murmuré sur son lit de mort : *« Ne laissez pas dire que j'ai vécu en vain. »*",
            "**Le halo occulte** : Brahe fréquentait Rodolphe II, empereur alchimiste qui pratiquait la manipulation du mercure — supposé prolonger la vie. Brahe lui-même avait mené des expériences alchimiques à Uraniborg. En 1991, une analyse de ses cheveux (conservés dans un musée danois) révèle des taux anormalement élevés de mercure. Théorie : empoisonnement lent, volontaire ou accidentel.",
            "**Rebondissement en 2010** : le corps est exhumé une seconde fois pour une analyse plus poussée. Résultat : le mercure est bien présent, mais à des doses trop faibles pour être fatales. La théorie de l'empoisonnement est écartée. La rupture urinaire — combinée sans doute à une infection — reste l'explication la plus probable.",
            "**Le paradoxe** : Tycho Brahe, l'homme qui a mesuré le ciel plus précisément que quiconque, est vraisemblablement mort d'un excès de politesse à table. Cela reste la mort la plus étrange de l'histoire de la science."
        ],
        "sources": [
            "Kepler, Journal astronomique, 1601",
            "Jens Vellev, exhumation report, National Museum of Denmark, 2010",
            "Chapelle Tycho Brahe, Notre-Dame-du-Týn, Prague"
        ],
        "tags": ["tycho brahe", "prague", "mercure", "vessie"]
    },
    {
        "id": "mort-crowley",
        "universe": "morts-etranges",
        "title": "Aleister Crowley : « la Bête » meurt dans une pension anglaise",
        "subtitle": "1947. Une agonie très ordinaire pour l'homme le plus scandaleux du XXe siècle",
        "status": "fait_historique",
        "era": "contemporain",
        "era_label": "1947",
        "year": 1947,
        "region": "Hastings, Angleterre",
        "coords": [50.8543, 0.5728],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Il s'était proclamé « la Bête 666 », avait fondé une religion, terrifié l'Angleterre, ruiné trois épouses. Il meurt le 1er décembre 1947, dans une chambre à cinq shillings la nuit, d'une bronchite.",
        "content": [
            "**Aleister Crowley** (1875-1947) est le personnage le plus controversé de l'occultisme du XXe siècle. Alpiniste, poète, franc-maçon, membre puis dissident de la Golden Dawn, fondateur d'une religion (*Thelema*) et d'un ordre (l'A∴A∴), il s'est autoproclamé « la Bête 666 » et a passé sa vie à choquer.",
            "**Ce qui est attesté sur sa fin** : après une vie flamboyante et coûteuse, Crowley est ruiné dès les années 1930. Héroïnomane depuis longtemps — la drogue lui avait d'abord été prescrite contre l'asthme —, il vit ses dernières années dans une pension modeste à Hastings, sur la côte sud de l'Angleterre. Il tient un journal jusqu'à la fin. Le 1er décembre 1947, à 72 ans, il meurt d'une bronchite aiguë compliquée par un état cardiaque défaillant. Un décès banal.",
            "**Le halo occulte** entoure surtout ses funérailles. Le 5 décembre 1947, à Brighton, une cérémonie funéraire est organisée en présence d'une trentaine de personnes. Le poète Louis Wilkinson lit à haute voix l'*Hymne à Pan* de Crowley — un poème délibérément païen. La presse britannique titre : *« Black Mass Funeral »*. Le maire de Brighton exige que jamais une telle chose ne se reproduise. Rien de « satanique » ne s'y était pourtant passé : c'était l'hommage littéraire d'un ami à un poète.",
            "**La légende posthume** enfle. On raconte que ses dernières paroles auraient été : *« I am perplexed »* — je suis perplexe. Version contestée. On raconte aussi qu'il aurait maudit son médecin, qui serait mort peu après. Le docteur William Brown Thomson est en effet décédé dans les mois suivants — mais il était âgé et malade.",
            "**Ce qui reste vrai** : Crowley, qui a passé sa vie à cultiver le scandale, a eu une mort d'un ennui absolu. C'est sans doute la plus grande ironie de sa biographie."
        ],
        "sources": [
            "John Symonds, The Great Beast, 1951",
            "Aleister Crowley, Diary, entrées 1946-1947",
            "Warburg Institute, Londres — Fonds Crowley"
        ],
        "tags": ["crowley", "thelema", "occultisme", "xxe"]
    },
    {
        "id": "mort-jeanne-arc",
        "universe": "morts-etranges",
        "title": "Jeanne d'Arc : brûlée trois fois, pour que rien ne reste",
        "subtitle": "Rouen, 30 mai 1431",
        "status": "fait_historique",
        "era": "moyen-age",
        "era_label": "1431",
        "year": 1431,
        "region": "Rouen",
        "coords": [49.4432, 1.0993],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "On l'a brûlée. Puis on a écarté les braises pour montrer son corps. Puis on l'a brûlée encore. Puis à nouveau. Enfin, on a jeté les cendres dans la Seine. Trois brûlages pour être sûr.",
        "content": [
            "**Ce que les archives disent** : le 30 mai 1431, sur la place du Vieux-Marché à Rouen, Jeanne d'Arc est brûlée vive à 19 ans, condamnée pour hérésie et récidive après un procès de sept mois mené par l'évêque Pierre Cauchon. Les minutes du procès et du procès en réhabilitation (1456) sont conservées et publiées.",
            "**Le rituel de sa mort est exceptionnellement documenté**. Deux témoins présents, Isambart de La Pierre (moine dominicain) et Guillaume Manchon (greffier), décrivent trois brûlages successifs. Après le premier, le bourreau Geoffroy Thérage écarte les braises et **exhibe le corps carbonisé aux spectateurs** — les Anglais craignent qu'on ne dise plus tard qu'elle s'est échappée. Puis on rallume. Puis on écrase les os. Puis on brûle encore.",
            "**Ce qui est très inhabituel** : les cendres sont ramassées, mises dans un sac, portées jusqu'au pont Mathilde, et jetées dans la Seine. Le bourreau, dit-on, en pleure. Ce protocole n'était pas la routine des exécutions médiévales. On voulait, littéralement, que rien ne reste.",
            "**Le halo mystique** est immédiat. Les rumeurs affirment qu'un cœur n'aurait pas brûlé — trouvé intact dans les cendres. Le bourreau aurait déclaré, selon des sources tardives : *« Nous sommes tous perdus, nous avons brûlé une sainte. »* Ces phrases apparaissent dans les archives du procès en réhabilitation, 25 ans plus tard, avec toutes les précautions à prendre.",
            "**La question ésotérique** qui traînera après elle : Jeanne était-elle une visionnaire au sens religieux médiéval (elle-même parlait de « voix » de saintes Catherine, Marguerite et de l'archange Michel), une manipulée politique, une hallucinée, une hystérique ? Le procès de canonisation en 1920 tranchera pour la première hypothèse. La médecine du XXe siècle a proposé plusieurs diagnostics — épilepsie du lobe temporal, schizophrénie légère — qui n'expliquent pas grand-chose.",
            "**Ce qui reste** : une jeune femme de 19 ans, qui n'avait jamais vu de bataille avant 17 ans, a mené des armées et a été brûlée trois fois pour être sûr qu'elle ne revienne pas. C'est déjà, historiquement, assez inexplicable."
        ],
        "sources": [
            "Procès de condamnation de Jeanne d'Arc, éd. Champion, 5 vol.",
            "Procès en nullité (1456), Bibliothèque nationale",
            "Régine Pernoud, Jeanne d'Arc, 1981"
        ],
        "tags": ["jeanne d'arc", "bûcher", "moyen-âge", "visions"]
    },
    {
        "id": "mort-alexandre-le-grand",
        "universe": "morts-etranges",
        "title": "Alexandre le Grand : douze jours d'agonie à 32 ans",
        "subtitle": "Babylone, juin 323 avant J.-C.",
        "status": "hypothese",
        "era": "antiquite",
        "era_label": "-323",
        "year": -323,
        "region": "Babylone",
        "coords": [32.5416, 44.4211],
        "hero_image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67",
        "excerpt": "Il avait conquis un empire de l'Adriatique à l'Indus. À 32 ans, un banquet à Babylone. Une coupe de vin. Douze jours de fièvre. Il meurt.",
        "content": [
            "**Ce qui est attesté (autant que possible)** : Alexandre III de Macédoine (356-323 av. J.-C.) meurt à Babylone début juin 323, après onze ou douze jours de maladie. Les sources — Arrien, Plutarque, Diodore, Justin — décrivent une fièvre élevée continue, des douleurs abdominales, un affaiblissement progressif, la perte de la parole à la fin. Il a 32 ans, marié depuis peu, sans héritier reconnu. Son empire va imploser en trois ans.",
            "**Le halo occulte** commence de son vivant. Alexandre lui-même croyait être fils du dieu Ammon — la prêtresse de l'oasis de Siwa lui aurait confirmé. Il avait accumulé les prophéties : oracles de Delphes, de Milet, chaldéens de Babylone. Les Chaldéens lui déconseillaient précisément d'entrer dans Babylone en 323, disant qu'il y trouverait la mort. Il y entra quand même.",
            "**Les théories antiques d'empoisonnement** apparaissent tout de suite. Plutarque rapporte l'accusation contre Antipater, régent de Macédoine, dont les fils Iolas (l'échanson d'Alexandre) et Cassandre auraient administré un poison importé du Styx dans un sabot d'âne. La légende du poison magique du Styx est un classique antique : censé être si corrosif qu'il ne pouvait être transporté que dans cette matière particulière. Version merveilleuse, non prouvée.",
            "**Les diagnostics modernes** ne s'accordent pas. Les principales pistes crédibles : malaria compliquée (typhoïde d'Ellemann-Jensen 1998), fièvre typhoïde (Oldach 1998), pancréatite alcoolique — Alexandre buvait immodérément —, ou syndrome de Guillain-Barré (Hall 2018) suivi d'une paralysie ascendante qui aurait donné l'illusion de la mort avant qu'elle ne survienne vraiment. Cette dernière théorie explique un détail troublant : Plutarque rapporte que son corps ne se serait pas décomposé pendant plusieurs jours après sa mort, ce qui aurait pu être interprété comme un signe divin mais pourrait signifier qu'il n'était pas mort au moment où on le crut mort.",
            "**L'étrange dernier détail** : Alexandre, mourant, aurait été interrogé sur son successeur. Il aurait répondu : *« Au plus fort »*. La phrase est répétée par toutes les sources antiques, ce qui est rare. Ses officiers se déchireront pendant quarante ans pour départager les prétendants. L'empire ne survivra pas à son fondateur."
        ],
        "sources": [
            "Plutarque, Vie d'Alexandre",
            "Arrien, Anabase d'Alexandre, livre VII",
            "David W. Oldach et al., 'A Mysterious Death', New England Journal of Medicine, 1998"
        ],
        "tags": ["alexandre", "babylone", "antiquité", "empoisonnement"]
    }
]
