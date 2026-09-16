"""Extension : L'Histoire secrète + formats signature.
Nouveaux univers, nouveaux dossiers, nouvelles chroniques.
"""

EXTRA_UNIVERSES = [
    {
        "id": "histoire-secrete",
        "title": "L'Histoire secrète",
        "subtitle": "Ce que les archives murmurent",
        "description": "Occultistes de cour, mystiques auprès des rois, poisons, sociétés initiatiques, phénomènes collectifs, symboles oubliés. Toujours : ce qui est attesté versus ce que la légende a rajouté.",
        "image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc"
    },
    {
        "id": "ils-y-croyaient",
        "title": "Ils y croyaient vraiment",
        "subtitle": "Se mettre dans la tête d'une autre époque",
        "description": "Pas pour se moquer : pour comprendre pourquoi une décision royale, une consultation médicale ou une pierre glissée dans un cercueil avaient parfaitement du sens à leur époque.",
        "image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67"
    },
    {
        "id": "legende-vs-archives",
        "title": "La légende contre les archives",
        "subtitle": "La version que tout le monde connaît, puis les archives",
        "description": "On raconte d'abord la légende telle qu'elle circule. Puis on ouvre les dossiers, un par un : attesté, probable, contesté, légende tardive. Notre format préféré.",
        "image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg"
    }
]

DOSSIERS = {
    "histoire-secrete": [
        {"id": "occultistes-enigmatiques", "label": "Occultistes et personnages énigmatiques"},
        {"id": "mystiques-pouvoir", "label": "Mystiques auprès du pouvoir"},
        {"id": "rois-sorciers", "label": "Rois entourés d'occultisme"},
        {"id": "apothicaires-alchimie", "label": "Apothicaires, alchimistes, médecine ancienne"},
        {"id": "poisons-scandales", "label": "Poisons, sorcières et scandales de cour"},
        {"id": "societes-secretes", "label": "Sociétés secrètes et initiatiques"},
        {"id": "phenomenes-collectifs", "label": "Phénomènes collectifs étranges"},
        {"id": "mort-au-dela", "label": "Mort, au-delà et rites funéraires"},
        {"id": "artistes-occulte", "label": "Artistes et écrivains fascinés par l'occulte"},
        {"id": "symboles-oublies", "label": "Symboles dont on a oublié l'histoire"},
    ]
}

EXTRA_STORIES = [
    # ========== OCCULTISTES ÉNIGMATIQUES ==========
    {
        "id": "saint-germain",
        "universe": "histoire-secrete",
        "dossier": "occultistes-enigmatiques",
        "title": "Le comte de Saint-Germain : l'homme qui ne vieillissait pas",
        "subtitle": "Aventurier, musicien, chimiste, et sujet de tous les fantasmes",
        "status": "hypothese",
        "era": "moderne",
        "era_label": "XVIIIe siècle",
        "year": 1750,
        "region": "Cours d'Europe",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Un homme apparaît dans les salons de Louis XV. Il parle six langues, joue du violon, discute peinture, chimie et histoire ancienne comme s'il y avait assisté.",
        "content": [
            "Le comte de Saint-Germain apparaît dans les cours européennes vers 1740. Personne ne sait d'où il vient exactement. Il parle français, allemand, anglais, italien, espagnol et portugais sans accent. Il joue du violon, peint, connaît la chimie, discute Antiquité et histoire médiévale avec une aisance troublante.",
            "Il ne semble pas vieillir. Ceux qui l'ont vu à trente ans le retrouvent, vingt ans plus tard, apparemment identique. Il laisse entendre — sans jamais l'affirmer clairement — qu'il a connu François Ier, ou vu de ses yeux la reine de Saba. Casanova, qui l'a rencontré, écrit qu'il « ne pouvait s'empêcher d'être charmé, tout en soupçonnant l'imposteur ».",
            "**Ce que l'on sait de manière assez fiable** : il travaille pour Louis XV comme chimiste et diplomate secret. Il met au point des teintures textiles très recherchées. Il compose de la musique — plusieurs partitions ont été retrouvées. Il fréquente Frédéric II de Prusse, la cour de Russie, le landgrave de Hesse-Cassel qui le loge à la fin de sa vie.",
            "**Ce que l'on ne sait pas** : son vrai nom, sa vraie date de naissance, l'origine de sa fortune. Il meurt officiellement en 1784 à Eckernförde, en Allemagne. Officiellement. Car les rumeurs de « réapparitions » commencent aussitôt, s'amplifient au XIXe siècle avec les théosophes qui font de lui un Maître ascensionné, et n'ont plus jamais cessé.",
            "L'homme historique est déjà fascinant. La légende, elle, appartient au XIXe siècle."
        ],
        "sources": [
            "Isabel Cooper-Oakley, The Comte de St. Germain, 1912",
            "Archives d'État de Hesse — dossier Saint-Germain",
            "Mémoires de Casanova, tome 5"
        ],
        "tags": ["saint-germain", "xviiie", "cour de france", "immortalité"]
    },
    {
        "id": "nicolas-flamel",
        "universe": "histoire-secrete",
        "dossier": "occultistes-enigmatiques",
        "title": "Nicolas Flamel : le libraire qui n'a jamais dit avoir découvert la pierre",
        "subtitle": "Un couple bourgeois du Paris médiéval, une postérité totalement inventée",
        "status": "hypothese",
        "era": "moyen-age",
        "era_label": "XIVe siècle",
        "year": 1400,
        "region": "Paris",
        "coords": [48.8629, 2.353],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Le vrai Nicolas Flamel était libraire-juré à Paris, marié à Pernelle, et généreux donateur d'églises. La pierre philosophale ? Elle n'est jamais mentionnée de son vivant.",
        "content": [
            "Nicolas Flamel a réellement existé. Il naît vers 1330, est écrivain-juré (une profession officielle : copiste et libraire agréé par l'université) à Paris rue des Écrivains, aujourd'hui rue de Marivaux. Il épouse Pernelle, une riche veuve, ce qui explique en grande partie leur aisance financière.",
            "Les archives montrent que Flamel finance de nombreuses œuvres charitables : sept maisons, quatorze hôpitaux, trois chapelles, dont celle de Saint-Jacques-aux-Pèlerins et son enfeu à l'église Saint-Jacques-la-Boucherie. Sa maison rue de Montmorency, construite en 1407, est **le plus vieil édifice de Paris encore debout**. Il meurt vers 1418.",
            "**Ce qu'il n'a jamais mentionné de son vivant** : aucune découverte alchimique, aucun voyage initiatique à Saint-Jacques-de-Compostelle, aucune pierre philosophale. Absolument rien de tout cela n'apparaît dans les documents authentifiés de sa main.",
            "L'invention date de 1612. Un mystérieux « Arnauld de la Chevallerie » publie *Le Livre des figures hiéroglyphiques*, prétendument œuvre de Flamel, avec le récit complet : le vieux livre acheté chez un bouquiniste, le voyage en Espagne, la rencontre avec Maître Canches, la transmutation réussie en 1382. Aucun manuscrit antérieur à 1612 ne contient ce texte.",
            "Voilà. La générosité de Flamel a été si spectaculaire qu'elle a paru surnaturelle — comment un simple libraire pouvait-il fonder autant d'œuvres ? — et deux siècles plus tard, on lui a fabriqué une explication alchimique. C'est cette version-là que J. K. Rowling, Umberto Eco et Paulo Coelho ont réutilisée."
        ],
        "sources": [
            "Archives nationales, minutier central",
            "Nigel Wilkins, Nicolas Flamel : des livres et de l'or, 1993",
            "Musée de Cluny, épitaphe de Flamel"
        ],
        "tags": ["flamel", "alchimie", "paris médiéval"]
    },
    {
        "id": "eliphas-levi",
        "universe": "histoire-secrete",
        "dossier": "occultistes-enigmatiques",
        "title": "Éliphas Lévi : l'ancien abbé qui a inventé l'occultisme moderne",
        "subtitle": "Fils d'un cordonnier parisien, il forge en 1855 le mot « occultisme »",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "XIXe siècle",
        "year": 1855,
        "region": "Paris",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Alphonse-Louis Constant, ex-séminariste, journaliste politique, révolutionnaire de 1848, réinvente sa vie en publiant « Dogme et rituel de la haute magie ».",
        "content": [
            "Alphonse-Louis Constant naît en 1810 à Paris, fils d'un modeste cordonnier. Il entre au séminaire, se destine à la prêtrise, mais quitte tout à quelques mois de l'ordination — probablement pour une histoire d'amour.",
            "Sa vie oscille alors : professeur, journaliste, militant socialiste emprisonné plusieurs fois pour ses écrits républicains en 1841 et 1848. Rien, à ce moment, ne le prédispose à l'occulte.",
            "Le tournant a lieu vers 1852, quand il fréquente le mathématicien polonais Hoene-Wroński, un mystique messianique. À cinquante ans, il se réinvente : il adopte le nom d'Éliphas Lévi (traduction hébraïque de ses deux premiers prénoms) et publie en 1855-1856 le *Dogme et rituel de la haute magie*.",
            "C'est un livre-somme, à la fois séduisant et confus, qui synthétise Kabbale, tarot, alchimie, mesmerisme et rites cérémoniels. Lévi y forge le mot **« occultisme »** dans son sens moderne. Il y trace pour la première fois un pentagramme codifié comme protection. Il y associe explicitement les 22 arcanes majeurs du tarot aux 22 lettres de l'alphabet hébreu.",
            "Peu importe la solidité érudite : le succès est colossal. Toute l'occultisme du XXe siècle — Papus, Aleister Crowley, la Golden Dawn — hérite de lui. Il meurt en 1875, à Paris, dans une pauvreté quasi totale. Son influence, elle, ne fait alors que commencer."
        ],
        "sources": [
            "Éliphas Lévi, Dogme et rituel de la haute magie, 1855-1856",
            "Christopher McIntosh, Éliphas Lévi and the French Occult Revival, 1972",
            "BNF, fonds Alphonse-Louis Constant"
        ],
        "tags": ["éliphas lévi", "occultisme", "xixe", "kabbale"]
    },

    # ========== MYSTIQUES AUPRÈS DU POUVOIR ==========
    {
        "id": "catherine-medicis-astrologues",
        "universe": "histoire-secrete",
        "dossier": "mystiques-pouvoir",
        "title": "Catherine de Médicis et ses astrologues : une reine très bien conseillée",
        "subtitle": "Consulter les étoiles était, à son époque, une décision politique rationnelle",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe siècle",
        "year": 1560,
        "region": "Cour de France",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "La reine mère consulte Nostradamus, Cosimo Ruggieri, Luca Gaurico. Pas par superstition secondaire : c'est ainsi qu'on gouverne à la Renaissance.",
        "content": [
            "Catherine de Médicis (1519-1589) est la fille des Médicis, cette famille florentine qui a fait de l'astrologie et de la philosophie néoplatonicienne un instrument de pouvoir depuis Cosme l'Ancien. Elle arrive en France en 1533 avec cet héritage.",
            "Ce qui est attesté : elle consulte régulièrement plusieurs astrologues. Le Napolitain Luca Gaurico avait dressé le thème d'Henri II et prédit sa mort violente lors d'un tournoi — prédiction que la reine prendra très au sérieux le jour du drame en 1559. Elle emploie ensuite le Florentin Cosimo Ruggieri, qui la suivra jusqu'à sa mort. Elle rencontre Nostradamus, qu'elle invite en 1555 et à qui elle confie l'établissement de thèmes pour ses enfants.",
            "**Ce que la légende noire a ajouté** : messes noires, envoûtements, meurtres par sortilège, cristal de divination dans lequel elle aurait vu défiler les rois futurs. Cette version — largement diffusée par ses adversaires huguenots — n'est pas soutenue par les archives.",
            "**La vraie question historique** est plus intéressante : pourquoi une souveraine intelligente prend-elle ces avis au sérieux ? Réponse : parce qu'à la Renaissance, l'astrologie est une science universitaire, enseignée à Bologne, Paris, Salamanque, à côté des mathématiques et de la médecine. La consulter n'est pas plus étrange, à l'époque, que consulter aujourd'hui un économiste ou un sondage.",
            "Catherine n'était pas superstitieuse dans un monde rationnel : elle était rationnelle dans son monde à elle."
        ],
        "sources": [
            "Denis Crouzet, Le Haut Cœur de Catherine de Médicis, 2005",
            "Ivan Cloulas, Catherine de Médicis, 1979",
            "BNF — correspondance de Cosimo Ruggieri"
        ],
        "tags": ["catherine de médicis", "astrologie", "cour de france"]
    },
    {
        "id": "raspoutine-romanov",
        "universe": "histoire-secrete",
        "dossier": "mystiques-pouvoir",
        "title": "Raspoutine et les Romanov : moine errant, tsarine désespérée",
        "subtitle": "Un guérisseur sibérien, un enfant hémophile, une famille impériale au bord du gouffre",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "Début XXe siècle",
        "year": 1907,
        "region": "Saint-Pétersbourg",
        "coords": [59.9343, 30.3351],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Alexis, l'héritier, est hémophile — un secret d'État. Raspoutine, quand il est présent, semble arrêter les crises. Le reste tient à ce fait précis.",
        "content": [
            "Grigori Raspoutine naît en 1869 en Sibérie, dans le village de Pokrovskoïe. Paysan, marié, père de trois enfants, il connaît vers trente ans une conversion religieuse et devient *starets* — moine errant, guide spirituel populaire. Il n'a jamais été prêtre orthodoxe ordonné.",
            "En 1905, il arrive à Saint-Pétersbourg. En 1907, il est présenté à la tsarine Alexandra. À cette date, la famille impériale garde un secret : le tsarévitch Alexis, trois ans, est hémophile. Toute contusion peut être fatale. Aucun médecin ne sait faire.",
            "**Ce qui est attesté** : les crises d'Alexis semblent effectivement s'atténuer quand Raspoutine est présent ou envoie ses messages. Les explications historiques modernes convergent : effet calmant sur la mère (donc sur l'enfant) ; peut-être conseils pratiques (interdire l'aspirine, un anticoagulant méconnu à l'époque comme tel) ; et peut-être hasard heureux répété.",
            "**Ce qui est très amplifié par la légende** : ses pouvoirs surnaturels, sa débauche pittoresque, sa mainmise sur le tsar. Il avait une réelle influence sur Alexandra, oui, et par elle sur des nominations. Il n'était pas l'homme d'État caché que les pamphlets ont dessiné.",
            "Son assassinat en décembre 1916 par le prince Youssoupov et un cousin du tsar est romanesque : poison, balles, noyade dans la Neva. Là aussi, les récits contradictoires des tueurs ont fabriqué un « Raspoutine impossible à tuer » qui ne résiste pas à l'analyse. La révolution éclatera trois mois plus tard."
        ],
        "sources": [
            "Douglas Smith, Rasputin: Faith, Power, and the Twilight of the Romanovs, 2016",
            "Archives d'État de la Fédération de Russie (GARF)",
            "Journal de la tsarine Alexandra"
        ],
        "tags": ["raspoutine", "romanov", "russie"]
    },

    # ========== ROIS SORCIERS ==========
    {
        "id": "rodolphe-ii-prague",
        "universe": "histoire-secrete",
        "dossier": "rois-sorciers",
        "title": "Rodolphe II à Prague : la cour la plus étrange de la Renaissance",
        "subtitle": "Un empereur mélancolique fait de son château le laboratoire de l'Europe",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "Fin XVIe siècle",
        "year": 1583,
        "region": "Prague",
        "coords": [50.0906, 14.4004],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Alchimistes, astronomes, peintres maniéristes, kabbalistes, faussaires. Tout ce monde travaille sous le même toit. Le résultat est unique dans l'histoire.",
        "content": [
            "Rodolphe II de Habsbourg (1552-1612), empereur du Saint-Empire, transfère en 1583 sa capitale à Prague. Solitaire, mélancolique, passionné d'art et de sciences, il rassemble sur la colline du Hradschin une des cours les plus singulières de l'histoire européenne.",
            "S'y croisent en même temps, sur quelques décennies : les astronomes **Tycho Brahe** puis **Johannes Kepler** (les vrais fondateurs de l'astronomie moderne), les peintres maniéristes Bartholomeus Spranger et Giuseppe Arcimboldo, l'alchimiste-charlatan Edward Kelley, le kabbaliste supposé Rabbi Loew (à qui la légende attribue le Golem), le graveur Aegidius Sadeler, une foule de faussaires en pierres précieuses, et John Dee de passage.",
            "Rodolphe finance leurs recherches. Il constitue un cabinet d'art et de curiosités qui compte, à sa mort, environ 3 000 tableaux et plusieurs milliers d'objets rares. Il commande des horloges astronomiques et alchimiques. Il traite ses savants comme des artistes de cour.",
            "**Ce qui est réel** : cette cour a produit des découvertes scientifiques majeures. Les *Tables rudolphines* de Kepler, publiées en 1627 grâce au patronage de Rodolphe, calculent les positions planétaires avec une précision inédite et resteront la référence pendant un siècle. Le maniérisme praguois marque durablement l'histoire de l'art.",
            "**Ce que la légende a ajouté** : l'empereur « occultiste », affilié à des rites secrets, à moitié fou. Il était en réalité un mécène fatigué, dépressif, passionnément curieux — et si extraordinairement bien entouré qu'il a laissé la science moderne quelques pas plus loin qu'il ne l'avait trouvée."
        ],
        "sources": [
            "Robert J. W. Evans, Rudolf II and His World, 1973",
            "Kunsthistorisches Museum, Vienne — Kunstkammer",
            "Národní galerie, Prague"
        ],
        "tags": ["rodolphe ii", "prague", "kepler", "maniérisme"]
    },

    # ========== APOTHICAIRES / ALCHIMIE ==========
    {
        "id": "theorie-signatures",
        "universe": "histoire-secrete",
        "dossier": "apothicaires-alchimie",
        "title": "La théorie des signatures : la plante qui ressemble au malade",
        "subtitle": "Le principe qui a guidé la pharmacopée européenne pendant deux mille ans",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "Antiquité jusqu'au XVIIIe",
        "year": 1500,
        "region": "Europe",
        "coords": [46.2276, 2.2137],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Une plante en forme de cœur soignerait le cœur. Une racine jaune, la jaunisse. Cette idée a organisé la médecine occidentale jusqu'à l'apparition de la chimie moderne.",
        "content": [
            "L'idée est simple, tellement simple qu'elle semble aujourd'hui absurde : Dieu (ou la Nature) aurait marqué chaque plante d'un signe indiquant à quoi elle sert. Une plante qui ressemble à une oreille — comme la *Cymbalaire des murs* — serait bonne pour les otites. Une racine rouge, pour le sang. Une plante à fleurs jaunes, pour le foie.",
            "Cette **théorie des signatures** est très ancienne. On la retrouve chez Dioscoride au Ier siècle, mais elle est formalisée surtout par Paracelse au XVIe siècle et par Giambattista della Porta dans son *Phytognomonica* (1588). Elle inspire toute la pharmacopée européenne jusqu'à la fin du XVIIIe.",
            "Absurde ? Oui et non. La signature elle-même est une superstition. Mais elle a donné aux apothicaires une **méthode mnémotechnique** utile pour organiser un savoir empirique par ailleurs très concret. La pulmonaire (feuilles tachées comme des poumons) contient effectivement des mucilages adoucissants utiles pour la toux. La millepertuis (fleurs perforées « comme des blessures ») était utilisée sur les plaies, et on sait aujourd'hui qu'elle a des propriétés antibactériennes.",
            "**Ce qui est attesté** : le savoir empirique des herboristes médiévaux, souvent des femmes, était réel. Beaucoup de remèdes fonctionnaient — sans qu'on sache pourquoi.",
            "**Ce qui est une reconstruction romantique** : l'image de l'apothicaire « ésotériste ». La plupart étaient de solides commerçants soumis à des règlements corporatifs stricts, tenant registres et payant taxes. La magie était au fond de la boutique, la comptabilité devant."
        ],
        "sources": [
            "Giambattista della Porta, Phytognomonica, 1588",
            "Paracelse, De Natura Rerum",
            "Musée de la pharmacie, Paris"
        ],
        "tags": ["théorie des signatures", "plantes médicinales", "paracelse"]
    },
    {
        "id": "theriaque",
        "universe": "histoire-secrete",
        "dossier": "apothicaires-alchimie",
        "title": "La thériaque : le médicament miracle qui a duré deux mille ans",
        "subtitle": "Une préparation à 60 ingrédients, dont de la chair de vipère",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "-100 → XIXe siècle",
        "year": -100,
        "region": "Bassin méditerranéen",
        "coords": [40.4168, -3.7038],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Inventée par le médecin de Mithridate au Ier siècle avant J.-C., elle est encore vendue dans les pharmacies parisiennes en 1884.",
        "content": [
            "La thériaque est le médicament le plus prescrit et le plus prestigieux de l'histoire européenne. Elle est censée protéger de tous les poisons, guérir la peste, la rage, les morsures venimeuses, et à peu près tout le reste.",
            "L'origine remonte à Mithridate VI du Pont, roi qui craignait tellement l'empoisonnement qu'il aurait pris quotidiennement un antidote composite. Son médecin Cratueas met au point la formule. Elle est reprise et complétée par Andromaque, médecin de Néron, au Ier siècle après J.-C. La recette contient alors une soixantaine d'ingrédients : opium, myrrhe, safran, cannelle, castoréum, poudres de gemmes, et surtout de la chair de vipère.",
            "La préparation est un événement public. À Venise, Montpellier, Lyon, Paris, la fabrication de thériaque se fait sous serment, en présence de médecins, apothicaires et magistrats. Les ingrédients sont exposés au public plusieurs jours avant. La composition est ensuite triturée pendant des semaines, puis mise à vieillir plusieurs années.",
            "Elle est vendue extrêmement cher, à toute l'Europe. Les rois s'en font offrir. On la donne aux mourants, aux femmes en couches, aux soldats blessés.",
            "**Ce qui est attesté sur son efficacité réelle** : l'opium et le safran ont des effets sédatifs et anti-inflammatoires modérés. Le reste, non. Mais l'effet placebo, sur un médicament vieux de deux millénaires et associé au prestige royal, était probablement considérable.",
            "Elle disparaît des pharmacopées officielles françaises en 1884. Elle avait tenu deux mille ans."
        ],
        "sources": [
            "Galien, Sur les antidotes",
            "Christiane Bange, La thériaque, Persée",
            "Musée de la pharmacie, Montpellier"
        ],
        "tags": ["thériaque", "pharmacie", "mithridate"]
    },

    # ========== POISONS ET SCANDALES DE COUR ==========
    {
        "id": "affaire-poisons",
        "universe": "histoire-secrete",
        "dossier": "poisons-scandales",
        "title": "L'Affaire des Poisons : quand la cour de Louis XIV bascule",
        "subtitle": "Une devineresse, une chambre de justice secrète, et Madame de Montespan",
        "status": "fait_historique",
        "era": "moderne",
        "era_label": "1679-1682",
        "year": 1679,
        "region": "Paris",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Trois ans d'enquête, 442 accusés, 36 exécutions, une commission spéciale dissoute par le roi lorsque l'enquête frôle sa favorite.",
        "content": [
            "En 1679, la police de Paris arrête Catherine Monvoisin, dite **La Voisin**, devineresse et avorteuse installée dans le quartier de la Villeneuve. On l'accuse d'avoir vendu des poisons et pratiqué des messes noires. L'enquête va durer trois ans et ébranler la cour.",
            "Louis XIV, alerté par son ministre Louvois, crée en 1680 une **chambre de justice** secrète, la Chambre ardente, qui siégera à l'Arsenal. Elle instruit à huis clos les cas les plus lourds. Quatre-cent-quarante-deux personnes sont interrogées, cent-quatre condamnées, trente-six exécutées, dont La Voisin brûlée vive le 22 février 1680.",
            "**Ce que les dossiers judiciaires racontent réellement** : un réseau parisien de devineresses, avorteuses et vendeuses de poudres opérant sur une clientèle mêlant petit peuple, bourgeoisie et grands seigneurs. Beaucoup d'escroquerie, quelques empoisonnements avérés, et un fond de pratiques rituelles douteuses.",
            "**Ce qui est amplifié** : les récits de messes noires célébrées sur le ventre d'aristocrates, avec sacrifices de nourrissons. Ces témoignages viennent essentiellement d'Étienne Guibourg, prêtre défroqué, obtenus sous des interrogatoires très pressants. Les historiens modernes considèrent qu'une partie relève d'aveux extorqués.",
            "**Le vrai scandale** : le nom de la marquise de Montespan, favorite officielle du roi, apparaît dans les dépositions. Aurait-elle consulté La Voisin pour retenir Louis XIV ? Peut-être. Aurait-elle participé à des messes noires ? Rien de solidement prouvé. En 1682, le roi ordonne de sceller les archives les plus compromettantes et fait dissoudre la Chambre ardente. Certains dossiers ne seront rouverts qu'au XIXe siècle."
        ],
        "sources": [
            "Arlette Lebigre, L'Affaire des Poisons, 1989",
            "Archives de la Bastille, éd. François Ravaisson",
            "Anne Somerset, The Affair of the Poisons, 2003"
        ],
        "tags": ["affaire des poisons", "louis xiv", "la voisin"]
    },

    # ========== SOCIÉTÉS SECRÈTES ==========
    {
        "id": "rose-croix-origines",
        "universe": "histoire-secrete",
        "dossier": "societes-secretes",
        "title": "La Rose-Croix : une société qui n'a peut-être jamais existé",
        "subtitle": "Trois manifestes anonymes en 1614-1616 annoncent un ordre qui reste introuvable",
        "status": "hypothese",
        "era": "moderne",
        "era_label": "Début XVIIe siècle",
        "year": 1614,
        "region": "Allemagne",
        "coords": [49.0069, 8.4037],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Entre 1614 et 1616, trois textes anonymes annoncent une confraternité secrète, sage et invisible. Toute l'Europe cherche à la rejoindre. Personne ne la trouve.",
        "content": [
            "Entre 1614 et 1616, trois textes paraissent en Allemagne : la *Fama Fraternitatis*, la *Confessio Fraternitatis*, et *Les Noces chymiques de Christian Rosenkreutz*. Ils racontent la vie d'un mystérieux Christian Rosenkreutz, fondateur d'une confraternité invisible dédiée à la réforme spirituelle et scientifique du monde.",
            "L'effet est phénoménal. Pendant les dix années suivantes, des centaines d'ouvrages sont publiés en Europe pour rejoindre la confraternité, la dénoncer, la défendre, la parodier. Descartes, Comenius, Robert Fludd s'y intéressent. À Paris, en 1623, des affiches proclament : *« Nous, députés du collège principal des Frères de la Rose-Croix, faisons séjour visible et invisible en cette ville. »* La ville s'affole.",
            "**Le problème** : personne, jamais, ne trouve la confraternité. Aucun membre initial ne se déclare. Aucune archive, aucun lieu, aucun rituel authentifié.",
            "L'hypothèse la mieux étayée aujourd'hui : les manifestes seraient l'œuvre d'un petit groupe de théologiens luthériens de Tübingen, dont **Johann Valentin Andreae** (qui reconnaîtra tardivement avoir écrit les *Noces*, en la présentant comme un « jeu littéraire de jeunesse »). Objectif : provoquer une réforme intellectuelle en instrumentalisant la fiction d'une confrérie invisible.",
            "La postérité, elle, a créé de véritables ordres rosicruciens à partir du XVIIIe siècle — mais ces ordres modernes n'ont aucune filiation prouvée avec les auteurs des manifestes originaux. La Rose-Croix historique reste peut-être la plus fascinante société secrète qui n'ait jamais existé."
        ],
        "sources": [
            "Frances Yates, La Lumière des Rose-Croix, 1972",
            "Roland Edighoffer, Rose-Croix et société idéale selon Johann Valentin Andreae, 1987",
            "Manifestes originaux (Fama, Confessio, Noces), éd. critique Neugebauer 2003"
        ],
        "tags": ["rose-croix", "andreae", "manifestes"]
    },
    {
        "id": "golden-dawn",
        "universe": "histoire-secrete",
        "dossier": "societes-secretes",
        "title": "La Golden Dawn : la fabrique de l'occultisme britannique",
        "subtitle": "Trois francs-maçons, un manuscrit codé, et une génération d'artistes envoûtés",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "1888-1910",
        "year": 1888,
        "region": "Londres",
        "coords": [51.5074, -0.1278],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "L'Ordre hermétique de l'Aube dorée n'a duré qu'une vingtaine d'années. Il a formé Yeats, Aleister Crowley, Arthur Machen et l'imaginaire occulte moderne.",
        "content": [
            "En 1887, un pasteur anglican, William Wynn Westcott, tombe entre les mains d'un manuscrit codé — probablement acheté à un bouquiniste londonien. Il le déchiffre : ce sont les rituels d'une prétendue société initiatique, avec l'adresse d'une contactrice allemande, « Anna Sprengel ». Westcott écrit. Sprengel répond, donne l'autorisation de fonder une loge anglaise, puis « disparaît ». Les lettres sont probablement fausses.",
            "En 1888, Westcott, Mathers et Woodman fondent à Londres **l'Ordre hermétique de l'Aube dorée**. Le système est syncrétique : kabbale hébraïque, tarot, alchimie, magie cérémonielle, astrologie, alphabet énochien de John Dee, rituels égyptiens reconstitués. Chaque membre progresse à travers des grades.",
            "Le succès est fulgurant. En dix ans, l'ordre attire l'élite culturelle : le poète **W. B. Yeats** (fondamental — sa poésie tardive en dépend), l'écrivain **Arthur Machen**, l'actrice Florence Farr, Bram Stoker (l'auteur de *Dracula*) selon certains, et l'inévitable **Aleister Crowley**.",
            "L'ordre implose en 1900-1903 : conflit de leadership entre Mathers (à Paris) et une fronde londonienne menée par Yeats, scandales d'inconduite, apparition de Crowley qui fait basculer les dissensions dans le chaos. Plusieurs schismes suivent.",
            "**Ce qui reste** : les rituels et les documents de l'ordre, publiés dans les années 1930 par Israel Regardie, sont devenus la base de presque toute la magie cérémonielle moderne. La Golden Dawn a inventé, en une génération, le vocabulaire de l'occultisme du XXe siècle."
        ],
        "sources": [
            "Israel Regardie, The Golden Dawn, 1937-1940",
            "Ellic Howe, The Magicians of the Golden Dawn, 1972",
            "R. A. Gilbert, The Golden Dawn Companion, 1986"
        ],
        "tags": ["golden dawn", "yeats", "crowley", "occultisme"]
    },

    # ========== PHÉNOMÈNES COLLECTIFS ==========
    {
        "id": "danse-strasbourg-1518",
        "universe": "histoire-secrete",
        "dossier": "phenomenes-collectifs",
        "title": "Strasbourg, 1518 : la ville qui a dansé jusqu'à en mourir",
        "subtitle": "Environ 400 personnes prises d'une danse compulsive pendant plusieurs semaines",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "Été 1518",
        "year": 1518,
        "region": "Alsace",
        "coords": [48.5734, 7.7521],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Une femme, Frau Troffea, se met à danser dans la rue. Une semaine plus tard, une trentaine de personnes dansent avec elle. Un mois plus tard, ils sont quatre cents. Certains ne s'arrêteront qu'en mourant.",
        "content": [
            "En juillet 1518, à Strasbourg, une femme dénommée Frau Troffea sort dans la rue et se met à danser, seule, sans musique. Elle danse une journée, puis une nuit, puis une autre journée. Au bout de six jours, une trentaine de personnes ont commencé à danser avec elle. Au bout d'un mois, elles seraient environ quatre cents.",
            "Ce n'est pas de la joie. Ce n'est pas un rite. Les danseurs ont l'air épuisé, hagard. Certains s'effondrent. Plusieurs meurent — de crises cardiaques, d'accidents vasculaires, d'épuisement. Les autorités municipales sont dépassées.",
            "Les documents contemporains — registres du conseil de la ville, chroniques, notes du médecin municipal — attestent tous du phénomène. Il n'y a aucun doute historique : cela s'est réellement produit.",
            "**Les tentatives d'explication de l'époque** : possession démoniaque, colère divine, malédiction de saint Guy (les autorités finiront par envoyer les danseurs en pèlerinage à la chapelle de saint Guy, ce qui semble avoir clos la crise).",
            "**Les hypothèses modernes** : ergotisme (le seigle de l'été 1518 aurait pu être contaminé par un champignon hallucinogène — mais l'ergotisme provoque plutôt des convulsions et des gangrènes) ; **hystérie collective** dans une population traumatisée par la famine, la peste et l'angoisse religieuse. Cette dernière hypothèse, défendue par l'historien John Waller, est aujourd'hui la mieux étayée.",
            "Il ne s'agirait donc pas d'une folie individuelle contagieuse au sens médical, mais d'un effet de stress collectif catastrophique dans une culture où on savait qu'une malédiction pouvait vous faire danser à mort."
        ],
        "sources": [
            "John Waller, A Time to Dance, a Time to Die, 2008",
            "Chroniques de Strasbourg, éd. Reuss",
            "Archives municipales de Strasbourg — registres 1518"
        ],
        "tags": ["danse", "strasbourg", "hystérie collective", "1518"]
    },

    # ========== MORT / SPIRITISME ==========
    {
        "id": "bijoux-deuil-spiritisme",
        "universe": "histoire-secrete",
        "dossier": "mort-au-dela",
        "title": "Bijoux de deuil et naissance du spiritisme",
        "subtitle": "Comment le XIXe siècle a réinventé le rapport aux morts",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "XIXe siècle",
        "year": 1848,
        "region": "États-Unis / Europe",
        "coords": [43.0356, -77.4197],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Bagues avec les cheveux du défunt, photographies post-mortem, tables tournantes : le XIXe siècle transforme le deuil en communication.",
        "content": [
            "Le XIXe siècle est le siècle du deuil visible. Après la mort du prince Albert en 1861, la reine Victoria porte le noir jusqu'à sa propre mort en 1901 — quarante ans de veuvage affiché. La mode suit. Les bijoutiers s'emparent du marché : bagues, broches, colliers contenant des mèches de cheveux du défunt sont produits massivement.",
            "En parallèle, une invention révolutionnaire arrive : la **photographie post-mortem**. Faire tirer le portrait d'un défunt — souvent un enfant, dans les familles où c'était la seule image que l'on aurait jamais de lui — devient courant entre 1840 et 1900. Ce n'est pas du morbide : c'est un usage rationnel d'une technologie encore chère.",
            "Et puis, le 31 mars 1848, à Hydesville, dans l'État de New York, deux fillettes, Maggie et Kate Fox, disent entendre des « coups » dans leur ferme. Elles disent que c'est un esprit qui répond à leurs questions. C'est le début officiel du **spiritisme moderne**.",
            "En dix ans, le spiritisme conquiert l'Amérique et l'Europe. Tables tournantes, écritures automatiques, séances chez les Hugo à Jersey, chez Napoléon III aux Tuileries. Allan Kardec, en France, publie *Le Livre des esprits* en 1857 et structure la doctrine.",
            "**Ce qui est attesté** : Maggie Fox avouera publiquement en 1888 avoir produit les coups en faisant craquer les articulations de ses orteils. Trop tard : le spiritisme est devenu une religion mondiale, comptant à son apogée plusieurs millions d'adeptes.",
            "**Le contexte qui l'explique** : au XIXe siècle, on meurt beaucoup, jeune, souvent. Un ménage sur deux perd un enfant. Le spiritisme offre l'espoir d'un contact maintenu. La science elle-même semble crédibiliser l'invisible : électricité, ondes, rayons X, radio."
        ],
        "sources": [
            "Ann Braude, Radical Spirits, 1989",
            "Allan Kardec, Le Livre des esprits, 1857",
            "Musée d'Orsay — photographies post-mortem"
        ],
        "tags": ["spiritisme", "bijoux de deuil", "photographie post-mortem"]
    },

    # ========== ARTISTES OCCULTE ==========
    {
        "id": "hugo-tables-tournantes",
        "universe": "histoire-secrete",
        "dossier": "artistes-occulte",
        "title": "Victor Hugo, les tables tournantes de Jersey",
        "subtitle": "Deux années où l'un des plus grands écrivains de langue française prend des dictées de l'au-delà",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "1853-1855",
        "year": 1853,
        "region": "Jersey",
        "coords": [49.2144, -2.1312],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Exilé politique à Jersey, Hugo assiste à des séances de tables tournantes. Il note tout. Il dialogue avec Shakespeare, Molière, sa fille Léopoldine, et un « Ombre du sépulcre ».",
        "content": [
            "En 1853, Victor Hugo, exilé politique de la France de Napoléon III, s'installe à Jersey avec sa famille. En septembre, la femme d'un ami, madame de Girardin, arrive de Paris avec la dernière mode parisienne : les tables tournantes.",
            "Hugo, la famille et quelques proches organisent des séances. Le procédé est classique : on pose les mains sur un guéridon, on interroge, la table frappe le sol pour désigner des lettres. Les séances dureront deux ans, de septembre 1853 à octobre 1855.",
            "**Ce qui est attesté** : Hugo prend les dictées consciencieusement. Charles, son fils, sert souvent de médium (main sur la table). Les manuscrits, environ 4 000 pages, sont conservés à la BNF. Les « esprits » dictent en alexandrins, en prose, en dialogues.",
            "Se présentent : Shakespeare, Molière, Racine, Dante, Marat, Jésus, la Mort, l'Ombre du sépulcre, la fille perdue de Hugo, Léopoldine (noyée en 1843). Le contenu est stylistiquement… hugolien, jusque dans les tournures.",
            "**Comment interpréter ça** ? Hugo n'a jamais publié ces textes, mais ne les a pas non plus reniés. Les historiens de la littérature y voient un cas fascinant d'**écriture automatique collective** : les participants, tout en croyant vraiment à la médiumnité, produisaient ensemble une littérature qui reflétait leurs préoccupations conscientes et inconscientes. Le style ressemble à Hugo parce que c'est Hugo qui, en dernière analyse, tenait la plume.",
            "L'affaire s'arrête brutalement en octobre 1855, quand un des participants a une crise de folie. Hugo comprend le risque. Il ne participera plus jamais à une séance."
        ],
        "sources": [
            "Victor Hugo, Le Livre des Tables, éd. Jean Gaudon",
            "BNF, département des Manuscrits — NAF 13438-13440",
            "Maison de Victor Hugo, Guernesey"
        ],
        "tags": ["victor hugo", "tables tournantes", "spiritisme"]
    },

    # ========== SYMBOLES OUBLIÉS ==========
    {
        "id": "ouroboros-origines",
        "universe": "histoire-secrete",
        "dossier": "symboles-oublies",
        "title": "L'ouroboros : le serpent qui se mord la queue",
        "subtitle": "Égypte, Grèce, alchimie, psychanalyse — trois mille cinq cents ans de reprises",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "XIVe s. av. J.-C. → aujourd'hui",
        "year": -1400,
        "region": "Égypte puis monde",
        "coords": [25.7402, 32.6014],
        "hero_image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67",
        "excerpt": "Sa première représentation connue est peinte sur un sarcophage de Toutankhamon. Il n'a jamais cessé d'être réutilisé depuis.",
        "content": [
            "La plus ancienne représentation connue de l'ouroboros — un serpent qui se mord la queue, formant un cercle — est peinte sur l'un des sanctuaires en bois dorés placés autour du sarcophage de Toutankhamon, vers -1325. Deux ouroboros y entourent une figure divine.",
            "Il resurgit dans l'Égypte hellénistique, dans le *Chrysopée de Cléopâtre* (un traité d'alchimie du IIIe siècle), avec la légende « Hen to Pan » — *l'Un est le Tout*. Il devient alors le symbole alchimique par excellence de la matière qui se transforme sans jamais se perdre, du cycle éternel de la vie et de la mort.",
            "Il traverse le Moyen Âge dans les manuscrits alchimiques, puis la Renaissance. Au XIXe siècle, il est adopté par les théosophes et Éliphas Lévi. Au XXe, Carl Gustav Jung en fait un archétype central de son analyse : symbole de l'inconscient, de l'intégration des opposés, du Soi.",
            "**Ce qui est réel** : ce symbole a une continuité documentée d'environ 3 400 ans. Il traverse toutes les grandes traditions ésotériques occidentales.",
            "**Ce qui est reconstruit** : les significations très spécifiques qu'on lui attribue aujourd'hui (« équilibre », « recommencement », etc.) sont souvent des lectures modernes. Le vrai fil rouge, presque tout le monde le partage : l'idée que l'univers est cyclique, et que le vivant se nourrit de sa propre fin.",
            "Une petite anecdote : le chimiste August Kekulé raconte avoir découvert la structure cyclique du benzène en 1865 après avoir vu en rêve un serpent se mordant la queue. Vrai ou reconstruction poétique tardive ? On en débat toujours."
        ],
        "sources": [
            "Musée du Caire — sarcophage de Toutankhamon",
            "Cleopatra, Chrysopée, IIIe siècle (papyrus Leiden)",
            "Carl Gustav Jung, Psychology and Alchemy, 1944"
        ],
        "tags": ["ouroboros", "alchimie", "égypte", "jung"]
    },
    {
        "id": "pentagramme-histoire",
        "universe": "histoire-secrete",
        "dossier": "symboles-oublies",
        "title": "Le pentagramme : de Pythagore aux films d'horreur",
        "subtitle": "Deux mille cinq cents ans, cinq branches, plusieurs sens successifs",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "-500 → aujourd'hui",
        "year": -500,
        "region": "Grèce puis monde",
        "coords": [37.9838, 23.7275],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Symbole de reconnaissance des pythagoriciens, puis emblème chrétien des cinq plaies, puis pentacle magique, puis symbole des satanistes du XXe. Le même dessin. Cinq siècles de sens successifs.",
        "content": [
            "Le pentagramme — étoile à cinq branches tracée d'un seul trait — est probablement l'un des symboles les plus détournés de l'histoire.",
            "**Grèce antique** : les pythagoriciens (VIe-Ve s. avant J.-C.) l'utilisent comme signe de reconnaissance secret. Il représente pour eux l'harmonie mathématique, à cause du nombre d'or que dessinent ses segments intérieurs. On l'appelle *pentalpha*.",
            "**Moyen Âge chrétien** : le pentagramme devient un symbole des cinq plaies du Christ, ou des cinq sens du chevalier vertueux. Sir Gauvain, dans le roman arthurien *Sir Gawain and the Green Knight* (XIVe siècle), porte un pentagramme d'or sur son bouclier — symbole de perfection chevaleresque.",
            "**Renaissance et occultisme** : Agrippa de Nettesheim et Paracelse en font un pentacle magique. Éliphas Lévi, en 1854, code l'interprétation qui restera : pentagramme pointe en haut = bien, homme spirituel ; pointe en bas = mal, bouc de Mendès. C'est **Lévi**, pas les satanistes, qui invente cette distinction moderne.",
            "**XXe siècle** : en 1966, Anton LaVey fonde à San Francisco l'Église de Satan et adopte le pentagramme inversé comme emblème officiel — reprenant directement le dessin de Lévi. Le cinéma d'horreur s'en empare. Une génération oublie complètement les cinq plaies du Christ et les pythagoriciens.",
            "Le même signe, cinq contextes, cinq significations totalement différentes. Voilà ce que la mémoire fait aux symboles."
        ],
        "sources": [
            "Sir Gawain and the Green Knight, éd. Tolkien 1925",
            "Éliphas Lévi, Dogme et rituel de la haute magie, 1855",
            "Anton LaVey, The Satanic Bible, 1969"
        ],
        "tags": ["pentagramme", "pythagore", "éliphas lévi"]
    },

    # ========== ILS Y CROYAIENT VRAIMENT ==========
    {
        "id": "ils-astrologue-du-roi",
        "universe": "ils-y-croyaient",
        "title": "1560 : pourquoi le roi consulte un astrologue avant d'attaquer",
        "subtitle": "Se mettre dans la tête d'un souverain de la Renaissance",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe siècle",
        "year": 1560,
        "region": "Cours européennes",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "En 1560, l'astrologie n'est pas une superstition parallèle. C'est une discipline universitaire, enseignée à côté des mathématiques.",
        "format": "ils-y-croyaient",
        "sections": [
            {
                "title": "Le décor",
                "paragraphs": [
                    "Nous sommes en 1560. Vous êtes un roi ou une reine régente. Vous devez décider : signer la paix, ou attaquer maintenant. Une décision qui engage des milliers de vies et l'avenir de votre lignée. Vous convoquez vos conseillers, oui — et parmi eux, vos astrologues."
                ]
            },
            {
                "title": "Ce que vous considérez comme normal",
                "paragraphs": [
                    "Vous demandez à votre astrologue un thème horaire — la carte du ciel à l'instant même où vous prenez la décision. Vous croisez avec le thème natal de votre ennemi. Vous regardez si Mars et Saturne sont bien placés. Vous fixez la date de l'attaque en fonction.",
                    "C'est une procédure encadrée, technique, coûteuse. Votre astrologue a fait des études universitaires. Il a payé un doctorat à Bologne ou à Salamanque, où l'astrologie est enseignée à côté de la médecine, des mathématiques et du droit."
                ]
            },
            {
                "title": "Pourquoi ça avait du sens",
                "paragraphs": [
                    "À votre époque, la conception dominante du monde repose sur une chaîne d'influences allant du plus haut (les astres, les sphères célestes) au plus bas (les métaux, les plantes, les corps). C'est cohérent avec l'astronomie ptoléméenne. Aristote lui-même l'avait posé.",
                    "Consulter un astrologue, c'est utiliser le savoir le plus avancé de votre siècle. Ce n'est pas plus étrange que consulter aujourd'hui un économiste avant une décision budgétaire — vous savez que les modèles ont leurs limites, mais vous ne prendriez pas de décision majeure sans les avoir consultés."
                ]
            },
            {
                "title": "Ce qui a fini par changer",
                "paragraphs": [
                    "Entre 1610 et 1690, tout bascule. Galilée démontre que les planètes ne sont pas des sphères parfaites. Kepler leur donne des trajectoires elliptiques. Newton explique la gravité. Le monde ptoléméen s'effondre — et avec lui, la justification théorique de l'astrologie.",
                    "Elle sort alors des universités. En 1700, plus aucun roi européen ne consulte officiellement un astrologue avant une bataille. Ce n'est pas devenu « faux ». C'est devenu impensable dans le nouveau cadre scientifique."
                ]
            }
        ],
        "sources": [
            "Nick Campion, A History of Western Astrology, 2008",
            "Anthony Grafton, Cardano's Cosmos, 1999"
        ],
        "tags": ["astrologie", "renaissance", "pouvoir royal"]
    },
    {
        "id": "ils-medecin-astral",
        "universe": "ils-y-croyaient",
        "title": "Renaissance : pourquoi votre médecin dresse d'abord votre thème astral",
        "subtitle": "La médecine astrologique n'était pas de la charlatanerie",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe siècle",
        "year": 1550,
        "region": "Europe",
        "coords": [43.6108, 3.8767],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Vous êtes malade. Vous appelez le médecin. Il vous demande votre heure de naissance avant de vous ausculter. Pourquoi ?",
        "format": "ils-y-croyaient",
        "sections": [
            {
                "title": "Le décor",
                "paragraphs": [
                    "1550. Vous vivez à Montpellier ou à Padoue. Vous êtes fiévreux. Le médecin arrive avec sa canne, son long manteau, et — chose banale à l'époque — il vous demande votre date, votre heure et votre lieu de naissance avant de vous toucher."
                ]
            },
            {
                "title": "Ce que vous considérez comme normal",
                "paragraphs": [
                    "Le médecin part de votre thème natal pour déterminer votre « complexion » — votre équilibre naturel entre les quatre humeurs (sang, phlegme, bile jaune, bile noire), lui-même lié à votre configuration astrale de naissance. Il regarde ensuite le ciel du jour pour savoir quels organes sont « affaiblis » par les positions actuelles.",
                    "Il vous prescrit alors une plante, un aliment, un moment précis de la journée pour agir. Les saignées, s'il y en a, seront calculées sur des jours favorables. Toute la médecine occidentale fonctionne comme ça, du XIIIe au XVIIe."
                ]
            },
            {
                "title": "Pourquoi ça avait du sens",
                "paragraphs": [
                    "Parce que la théorie humorale de Galien (IIe siècle) régnait sans partage. Elle offrait un cadre cohérent : chaque humeur avait sa planète, chaque planète son organe, chaque organe son remède. C'était la médecine officielle, enseignée à l'université, encadrée par des ordres professionnels.",
                    "Et parfois, ça marchait ! Non pour la raison invoquée, mais parce que le repos, les plantes, la diète et l'effet placebo produisaient de vrais résultats. Un patient guéri est un patient qui recommande le médecin."
                ]
            },
            {
                "title": "Ce qui a fini par changer",
                "paragraphs": [
                    "Au XVIIe siècle, Harvey découvre la circulation sanguine (1628). Au XVIIIe, Lavoisier fonde la chimie moderne. Au XIXe, Pasteur démontre le rôle des microorganismes. Chaque étape sape la théorie humorale sans qu'aucune n'ait été spécifiquement dirigée contre elle.",
                    "En 1900, plus aucune faculté de médecine occidentale n'enseigne l'astrologie médicale. La transition a duré deux siècles. Elle s'est faite sans révolution : par accumulation silencieuse d'observations que le vieux modèle ne pouvait plus expliquer."
                ]
            }
        ],
        "sources": [
            "Nancy Siraisi, Medieval and Early Renaissance Medicine, 1990",
            "Bibliothèque interuniversitaire de médecine, Paris"
        ],
        "tags": ["médecine astrologique", "humeurs", "renaissance"]
    },
    {
        "id": "ils-pierres-du-roi",
        "universe": "ils-y-croyaient",
        "title": "Moyen Âge : pourquoi la couronne d'un roi est cousue de pierres",
        "subtitle": "Chaque gemme travaille, littéralement, pour le souverain",
        "status": "fait_historique",
        "era": "moyen-age",
        "era_label": "Moyen Âge",
        "year": 1200,
        "region": "Europe médiévale",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Le rubis rend courageux, le saphir garde la chasteté, l'améthyste protège de l'ivresse. Une couronne médiévale n'est pas un ornement : c'est une armure invisible.",
        "format": "ils-y-croyaient",
        "sections": [
            {
                "title": "Le décor",
                "paragraphs": [
                    "Vous êtes couronné roi ou reine. Le regalia qu'on pose sur vous — couronne, sceptre, anneau — est incrusté de pierres précieuses. Ce n'est pas une décoration. C'est un dispositif fonctionnel."
                ]
            },
            {
                "title": "Ce que vous considérez comme normal",
                "paragraphs": [
                    "Vous savez, parce que vous l'avez lu ou entendu, que le **rubis** rend courageux au combat et repousse le venin. Le **saphir**, associé au ciel, garde la chasteté et discerne les mensonges. Le **grenat** protège des voyages nocturnes. L'**améthyste** empêche l'ivresse — d'où son usage dans les coupes.",
                    "Pour un roi, porter ces pierres n'est pas de la superstition esthétique. C'est un investissement de sécurité au sens le plus concret."
                ]
            },
            {
                "title": "Pourquoi ça avait du sens",
                "paragraphs": [
                    "Parce que la source de ce savoir est **Pline l'Ancien** (Ier siècle), autorité inattaquable au Moyen Âge. Parce que les **lapidaires** — des traités listant les propriétés des pierres — sont rédigés par des évêques comme Marbode de Rennes (1035-1123), dont l'ouvrage est enseigné dans les écoles cathédrales.",
                    "Ce n'est pas une croyance marginale. C'est le savoir standard d'un homme cultivé du Moyen Âge, adossé à des autorités anciennes et à l'Église."
                ]
            },
            {
                "title": "Ce qui a fini par changer",
                "paragraphs": [
                    "La minéralogie moderne — Agricola au XVIe siècle, puis la classification cristallographique au XVIIIe — vide progressivement les pierres de leurs propriétés magiques. Elles deviennent des combinaisons chimiques mesurables.",
                    "Mais le prestige, lui, ne disparaît jamais. Aujourd'hui encore, la couronne impériale britannique est incrustée du Cullinan II. Personne ne pense qu'il repousse le venin. Tout le monde sent quand même qu'il change quelque chose. C'est peut-être ça, la vraie survie de l'ancien savoir."
                ]
            }
        ],
        "sources": [
            "Marbode de Rennes, Liber lapidum, XIe siècle",
            "Pline l'Ancien, Histoire naturelle, livre XXXVII",
            "Musée du Louvre — département des Objets d'art"
        ],
        "tags": ["pierres", "moyen-âge", "regalia"]
    },

    # ========== LA LÉGENDE CONTRE LES ARCHIVES ==========
    {
        "id": "archives-flamel",
        "universe": "legende-vs-archives",
        "title": "Nicolas Flamel a-t-il vraiment trouvé la pierre philosophale ?",
        "subtitle": "La légende contre les archives",
        "status": "fait_historique",
        "era": "moyen-age",
        "era_label": "XIVe siècle",
        "year": 1400,
        "region": "Paris",
        "coords": [48.8629, 2.353],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Version connue : un libraire parisien découvre un livre mystérieux, part en Espagne, décrypte, transmute. Version des archives : rien de tout ça n'est mentionné avant 1612.",
        "format": "legende-vs-archives",
        "sections": [
            {
                "title": "La version que tout le monde connaît",
                "paragraphs": [
                    "Nicolas Flamel, libraire à Paris, achète un jour à un bouquiniste un vieux livre écrit en caractères mystérieux : le *Livre d'Abraham le Juif*. Ne comprenant pas, il part en pèlerinage à Saint-Jacques-de-Compostelle. En chemin, il rencontre un certain Maître Canches, un juif converti, qui accepte de traduire.",
                    "Revenu à Paris, Flamel, aidé de sa femme Pernelle, met en pratique les instructions. Le 17 janvier 1382 à midi, il transmute une demi-livre de mercure en pur argent. Le 25 avril suivant, il transmute en or fin. Immensément riche, il consacre sa fortune à des œuvres charitables. Certains disent qu'il n'est jamais mort — qu'on l'aurait revu à Istanbul au XVIIe."
                ]
            },
            {
                "title": "Maintenant, ouvrons les archives",
                "paragraphs": [
                    "**Ce que les archives disent réellement** : Flamel a existé. Il est écrivain-juré à Paris de 1370 environ à sa mort vers 1418. Il vit rue des Écrivains. Il épouse en 1368 Pernelle, une riche veuve qui a hérité deux fois. C'est elle qui apporte la fortune initiale.",
                    "**Ses œuvres charitables sont attestées** : quatorze hôpitaux, sept maisons, trois chapelles, mentionnés dans des donations authentifiées. Sa maison rue de Montmorency existe toujours (c'est le plus vieil édifice de Paris).",
                    "**Absolument aucun document du vivant de Flamel** ne mentionne d'alchimie, de voyage à Compostelle, de rencontre avec Maître Canches, ou de transmutation. Son testament, conservé, est purement religieux et bourgeois.",
                    "**Le récit alchimique** apparaît pour la première fois dans *Le Livre des figures hiéroglyphiques*, publié à Paris en **1612** — soit deux siècles après la mort de Flamel — par un certain « Arnauld de la Chevallerie ». Aucun manuscrit antérieur à 1612 ne contient ce texte. La plupart des historiens y voient une fabrication du XVIIe siècle, à un moment où l'alchimie est de nouveau à la mode."
                ]
            }
        ],
        "verdict": [
            {"label": "Attesté", "text": "Flamel a existé. Il était écrivain-juré. Il a fait de nombreux dons charitables. Sa maison existe."},
            {"label": "Attesté", "text": "Sa fortune vient très probablement de son mariage avec Pernelle, qui héritait de deux veuvages précédents."},
            {"label": "Contesté", "text": "Le voyage à Compostelle : aucune trace documentaire."},
            {"label": "Légende tardive", "text": "La rencontre avec Maître Canches, le déchiffrement du Livre d'Abraham, les transmutations de 1382 : tout provient d'un texte de 1612."},
            {"label": "Légende tardive", "text": "L'immortalité de Flamel : c'est de la littérature du XVIIe et XIXe siècle."}
        ],
        "sources": [
            "Nigel Wilkins, Nicolas Flamel : des livres et de l'or, 1993",
            "Didier Kahn, Le fixe et le volatil, 2016",
            "Archives nationales, série AB (donations Flamel)"
        ],
        "tags": ["flamel", "pierre philosophale", "légende"]
    },
    {
        "id": "archives-saint-germain",
        "universe": "legende-vs-archives",
        "title": "Le comte de Saint-Germain était-il immortel ?",
        "subtitle": "La légende contre les archives",
        "status": "hypothese",
        "era": "moderne",
        "era_label": "XVIIIe siècle",
        "year": 1760,
        "region": "Europe",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Version connue : un homme immortel qui traverse les siècles. Version des archives : un aventurier très doué, mort en 1784.",
        "format": "legende-vs-archives",
        "sections": [
            {
                "title": "La version que tout le monde connaît",
                "paragraphs": [
                    "Un aristocrate mystérieux traverse le XVIIIe siècle sans jamais vieillir. Il aurait connu François Ier, dansé avec la reine de Saba, croisé Cléopâtre. Il possède le secret de la pierre philosophale et de la fontaine de Jouvence. Il ne mange presque rien. On le reverra plusieurs fois après sa mort officielle : au Congrès de Vienne en 1815, dans Paris de 1840, en Inde en 1900."
                ]
            },
            {
                "title": "Maintenant, ouvrons les archives",
                "paragraphs": [
                    "**Origines** : totalement inconnues. Il apparaît à Londres vers 1743-1745, arrêté brièvement pour espionnage jacobite (les rebelles écossais fidèles aux Stuart). Il se dit « comte de Saint-Germain » sans qu'aucun titre légitime ne le confirme. Les hypothèses sur son origine réelle vont du fils d'un percepteur d'impôts espagnol au fils illégitime du roi de Portugal.",
                    "**Vie active** : documentée entre 1745 et 1784. Il fréquente Louis XV, Frédéric II, la Russie de Catherine II, la Hollande, l'Allemagne. Il est effectivement chimiste (teintures textiles), musicien (partitions retrouvées), diplomate secret. Il parle plusieurs langues sans accent — mais Casanova, qui l'a rencontré, note quand même quelques imprécisions.",
                    "**Sa non-vieillissement** : légende alimentée par lui-même. Il faisait des remarques du type « quand j'étais en Perse il y a quelques siècles… », probablement avec le sourire ironique. Il apparaissait toujours d'âge indéfini, entre 40 et 50 ans, selon les témoins.",
                    "**Sa mort** : registres paroissiaux d'Eckernförde, dans le duché de Schleswig, 27 février 1784. Enterrement le 2 mars. Documents notariaux du landgrave de Hesse-Cassel confirmant. Il n'y a pas de doute historique sérieux sur ce point.",
                    "**Ses réapparitions** : elles commencent aussitôt. Elles sont toutes rapportées par des personnages liés au milieu théosophique et occultiste. Aucune n'est corroborée par un document indépendant."
                ]
            }
        ],
        "verdict": [
            {"label": "Attesté", "text": "Personnage réel, actif entre 1743 et 1784."},
            {"label": "Attesté", "text": "Talents multiples réels : chimie, musique, diplomatie, langues."},
            {"label": "Attesté", "text": "Mort à Eckernförde en 1784, funérailles documentées."},
            {"label": "Probable", "text": "Origine sociale bien plus modeste que ce qu'il affichait."},
            {"label": "Contesté", "text": "Certaines de ses missions diplomatiques secrètes : partiellement documentées."},
            {"label": "Légende tardive", "text": "Son immortalité, ses vies antérieures, ses réapparitions post-mortem : construites au XIXe siècle par Blavatsky et les théosophes."}
        ],
        "sources": [
            "Isabel Cooper-Oakley, The Comte de St. Germain, 1912",
            "Jean Overton Fuller, The Comte de Saint-Germain, 1988",
            "Registres paroissiaux d'Eckernförde, Landesarchiv Schleswig"
        ],
        "tags": ["saint-germain", "immortalité", "xviiie"]
    },
    {
        "id": "archives-raspoutine",
        "universe": "legende-vs-archives",
        "title": "Que faisait vraiment Raspoutine auprès des Romanov ?",
        "subtitle": "La légende contre les archives",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "1905-1916",
        "year": 1910,
        "region": "Russie impériale",
        "coords": [59.9343, 30.3351],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Version connue : un moine débauché aux pouvoirs hypnotiques qui gouvernait la Russie. Version des archives : un guérisseur autour d'un enfant hémophile, dont l'influence a été considérablement gonflée.",
        "format": "legende-vs-archives",
        "sections": [
            {
                "title": "La version que tout le monde connaît",
                "paragraphs": [
                    "Un moine paysan sibérien s'introduit à la cour de Nicolas II. Il hypnotise la tsarine, séduit toutes les femmes qu'il croise, participe à des orgies, dicte les nominations du gouvernement, précipite la Russie à sa perte. Empoisonné, poignardé, tiré à balles, il refuse de mourir. On finit par le jeter dans la Néva glacée. Trois mois plus tard, la révolution éclate — et c'est un peu de sa faute."
                ]
            },
            {
                "title": "Maintenant, ouvrons les archives",
                "paragraphs": [
                    "**Le contexte central** : le tsarévitch Alexis est hémophile. C'est un secret d'État. Toute contusion peut le tuer. Les médecins officiels sont impuissants. La tsarine Alexandra vit dans l'angoisse permanente depuis 1904.",
                    "**Raspoutine, arrivé à Saint-Pétersbourg en 1905, présenté à la famille impériale en 1907**. Ce qui est attesté : les crises d'Alexis paraissent plus supportables quand il est présent, ou même quand il envoie des télégrammes. Les explications les plus probables aujourd'hui : effet apaisant sur la tsarine (donc sur l'enfant), suggestion hypnotique modérée, peut-être conseil d'éviter certains médicaments (l'aspirine, alors nouvellement introduite, est un anticoagulant dangereux pour un hémophile).",
                    "**Sa débauche** : elle a existé, elle a été très visible dans les cabarets de la capitale. Mais elle a aussi été considérablement amplifiée par la presse et par la police politique (l'Okhrana), qui le surveillait constamment. Beaucoup de rapports « anti-Raspoutine » ont été rédigés par des ennemis politiques.",
                    "**Son influence politique réelle** : forte sur la tsarine, indirecte sur le tsar, réelle mais surestimée. Il fait effectivement obtenir des postes à des proches. Mais il n'a jamais gouverné.",
                    "**Son assassinat en décembre 1916** : perpétré par le prince Youssoupov et le grand-duc Dmitri Pavlovitch, avec quelques complices. Les récits du meurtre sont contradictoires : Youssoupov a réécrit sa version plusieurs fois. Le rapport d'autopsie officiel, retrouvé dans les années 1990, indique une mort par balle à courte portée — sans mention d'empoisonnement ni de noyade."
                ]
            }
        ],
        "verdict": [
            {"label": "Attesté", "text": "Guérisseur ayant réellement soulagé Alexis, sans qu'on sache pleinement expliquer comment."},
            {"label": "Attesté", "text": "Influence réelle sur la tsarine, plus indirecte sur le tsar."},
            {"label": "Attesté", "text": "Débauche publique réelle, mais amplifiée par la presse."},
            {"label": "Probable", "text": "Rôle mineur dans la déstabilisation générale du régime, très surestimé par la propagande post-révolutionnaire."},
            {"label": "Contesté", "text": "Version des tueurs sur l'assassinat (poison, résistance surnaturelle) : partiellement démentie par le rapport d'autopsie."},
            {"label": "Légende tardive", "text": "Raspoutine « occultiste » ou « satanique » : construction posthume, notamment par le cinéma américain des années 1930."}
        ],
        "sources": [
            "Douglas Smith, Rasputin, 2016",
            "Rapport d'autopsie n°55/2, Archives d'État de la Fédération de Russie",
            "Journal du tsar Nicolas II"
        ],
        "tags": ["raspoutine", "romanov", "russie"]
    },
    {
        "id": "archives-catherine-medicis",
        "universe": "legende-vs-archives",
        "title": "Catherine de Médicis pratiquait-elle vraiment la magie noire ?",
        "subtitle": "La légende contre les archives",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe siècle",
        "year": 1570,
        "region": "France",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Version connue : la reine noire, sorcière florentine, empoisonneuse, ordonnatrice de la Saint-Barthélemy. Version des archives : une politique pragmatique et cultivée, victime d'une légende noire monumentale.",
        "format": "legende-vs-archives",
        "sections": [
            {
                "title": "La version que tout le monde connaît",
                "paragraphs": [
                    "Catherine de Médicis empoisonne ses ennemis, consulte les astres pour tout, organise des messes noires, envoûte les mannequins de cire de ses adversaires, garde Nostradamus prisonnier, et déclenche personnellement le massacre de la Saint-Barthélemy en 1572. C'est la « reine noire », l'Italienne machiavélique, l'incarnation de la cour corrompue."
                ]
            },
            {
                "title": "Maintenant, ouvrons les archives",
                "paragraphs": [
                    "**Consultations astrologiques** : oui, largement attestées. Elle consulte régulièrement Luca Gaurico, Cosimo Ruggieri, et rencontre Nostradamus. Elle croit à l'astrologie comme la quasi-totalité de sa génération éduquée. Elle établit des thèmes pour ses enfants et pour ses ennemis. Ce n'est pas de la « magie noire », c'est la science universitaire de son temps.",
                    "**Empoisonnements** : aucun n'est prouvé. La rumeur d'empoisonnement de Jeanne d'Albret en 1572 (via une paire de gants parfumés) est démontée par les médecins de l'époque qui documentent une tuberculose ancienne. Les autres accusations sont politiques.",
                    "**Messes noires et envoûtements** : accusations issues des pamphlets huguenots pendant les guerres de religion, ne reposant sur aucune source documentaire. La cour la plus surveillée d'Europe n'aurait pas laissé un tel rite passer inaperçu.",
                    "**Saint-Barthélemy** : les historiens débattent depuis un siècle du rôle exact de Catherine. La thèse d'une préméditation méthodique par la reine seule est aujourd'hui minoritaire. La thèse dominante : une décision d'urgence collective, prise par le conseil royal (Catherine incluse) après l'échec de l'attentat contre Coligny, dans un contexte de peur d'un contre-coup huguenot. Sanglant. Responsable, oui. Mais pas la sorcière au chaudron.",
                    "**L'origine de la légende noire** : les pamphlets huguenots publiés à partir de 1572, notamment le *Discours merveilleux de la vie, actions et déportements de Catherine de Médicis*, un chef-d'œuvre de propagande politique.  Michelet, au XIXe siècle, popularisera cette version, qui hantera l'imaginaire français depuis."
                ]
            }
        ],
        "verdict": [
            {"label": "Attesté", "text": "Recours régulier à des astrologues, comme la plupart des souverains de sa génération."},
            {"label": "Attesté", "text": "Politique de compromis religieux avec les huguenots pendant les années 1560."},
            {"label": "Contesté", "text": "Rôle exact dans le déclenchement de la Saint-Barthélemy : décision collective en urgence plutôt que préméditation."},
            {"label": "Non prouvé", "text": "Aucun empoisonnement politique n'a été documenté malgré des enquêtes."},
            {"label": "Légende tardive", "text": "Messes noires, envoûtements, meurtres par sortilège : accusations de pamphlets huguenots, sans source archivistique."}
        ],
        "sources": [
            "Denis Crouzet, Le Haut Cœur de Catherine de Médicis, 2005",
            "Discours merveilleux… (pamphlet, 1575), éd. critique Wilson",
            "Ivan Cloulas, Catherine de Médicis, 1979"
        ],
        "tags": ["catherine de médicis", "saint-barthélemy", "légende noire"]
    }
]
