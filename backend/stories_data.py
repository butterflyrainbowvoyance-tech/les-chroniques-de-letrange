"""Seed content for La Bibliothèque Secrète.
All stories have a clearly labeled 'status' so readers know what they are reading.
"""

STORIES = [
    # ============ ÉSOTÉRISME ============
    {
        "id": "hermes-trismegiste",
        "universe": "esoterisme",
        "title": "Hermès Trismégiste, le trois fois grand",
        "subtitle": "Une figure à mi-chemin entre le mythe et la philosophie",
        "status": "hypothese",
        "era": "antiquite",
        "era_label": "Antiquité tardive",
        "year": -100,
        "region": "Égypte",
        "coords": [30.0444, 31.2357],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "On l'a présenté comme un pharaon oublié, un contemporain de Moïse, un dieu grec déguisé... Hermès Trismégiste n'a probablement jamais existé, et pourtant il a inspiré toute la pensée ésotérique occidentale.",
        "content": [
            "Imagine : tu ouvres un vieux livre du XVIe siècle, et l'auteur cite très sérieusement un sage égyptien qui aurait vécu avant les pyramides, aurait enseigné à Pythagore, prédit la venue du Christ, et rédigé au passage une trentaine de traités sur l'univers. Ce sage, c'est Hermès Trismégiste, littéralement « Hermès trois fois grand ».",
            "Le problème, c'est que les historiens sont à peu près certains d'une chose : ce personnage n'a jamais existé.",
            "Ce que l'on sait vraiment, c'est qu'au IIe et IIIe siècle après J.-C., en Égypte hellénistique, des auteurs anonymes de langue grecque commencent à faire circuler des textes philosophiques et religieux. Pour donner du poids à leurs idées, ils les attribuent à un maître mythique, un mélange du dieu grec Hermès et du dieu égyptien Thot. Ce collage divin, c'est notre fameux Trismégiste.",
            "Ces textes, regroupés plus tard sous le nom de *Corpus Hermeticum*, parlent de l'âme, du destin, de l'univers, du salut. Rien de très occulte à l'origine : c'est de la philosophie religieuse de l'époque, cousine du néoplatonisme et du gnosticisme.",
            "Le vrai tournant arrive à la Renaissance. En 1462, Cosme de Médicis reçoit un manuscrit grec ramené de Macédoine. Il demande au philosophe Marsile Ficin d'interrompre sa traduction de Platon (rien que ça) pour traduire d'urgence ces textes attribués à Hermès. Pourquoi tant d'empressement ? Parce qu'à l'époque, on croit dur comme fer que ce sage est plus ancien que Moïse. Le lire, c'est presque toucher à la sagesse originelle de l'humanité.",
            "Sauf qu'en 1614, un érudit protestant du nom d'Isaac Casaubon démolit tout : par analyse linguistique, il prouve que les textes ont été écrits en grec tardif, bien après Moïse. Le mythe s'effondre… chez les savants. Mais dans l'imaginaire ésotérique, il ne bougera plus jamais. Alchimistes, francs-maçons, occultistes du XIXe siècle continueront de citer Hermès comme s'il avait bel et bien tenu la plume."
        ],
        "sources": [
            "Corpus Hermeticum, traduction de A.-J. Festugière (Les Belles Lettres)",
            "Frances Yates, Giordano Bruno et la tradition hermétique, 1964",
            "Isaac Casaubon, De rebus sacris et ecclesiasticis exercitationes XVI, 1614"
        ],
        "tags": ["hermétisme", "renaissance", "alchimie", "philosophie"]
    },
    {
        "id": "societe-theosophique",
        "universe": "esoterisme",
        "title": "Madame Blavatsky et la Société théosophique",
        "subtitle": "Comment une aventurière russe a réinventé la spiritualité au XIXe siècle",
        "status": "fait_historique",
        "era": "xixe",
        "era_label": "XIXe siècle",
        "year": 1875,
        "region": "États-Unis / Inde",
        "coords": [40.7128, -74.006],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Fondée à New York en 1875, la Société théosophique voulait réconcilier science, religion et occultisme. Elle a produit autant de génies que d'imposteurs, et façonné le New Age à venir.",
        "content": [
            "Helena Petrovna Blavatsky, dite « HPB », est un personnage impossible à inventer. Née en 1831 en Ukraine russe, mariée à seize ans à un général qu'elle plaque presque aussitôt, elle passe les années suivantes à voyager – ou à raconter qu'elle voyage – en Égypte, en Inde, au Tibet, aux États-Unis. Elle prétend avoir étudié auprès de « Maîtres » cachés dans l'Himalaya.",
            "En 1875, à New York, elle fonde avec le colonel Henry Steel Olcott et l'avocat William Quan Judge la Société théosophique. L'ambition est modeste : rien de moins qu'une religion universelle, une fraternité humaine sans distinction de race ou de croyance, et l'étude comparée des sagesses anciennes.",
            "Ses livres, notamment *Isis dévoilée* (1877) et *La Doctrine secrète* (1888), sont des monuments touffus mêlant hindouisme, bouddhisme, gnose, kabbale, science victorienne et… beaucoup d'invention.",
            "En 1884, la Société de recherche psychique de Londres publie un rapport accablant : les lettres soi-disant matérialisées par les Maîtres seraient des faux. Blavatsky est traitée d'imposteur. Elle continuera pourtant à écrire jusqu'à sa mort en 1891, entourée d'une aura à la fois d'admiration et de scandale.",
            "Peu importe la controverse : l'influence est immense. Le mot « karma » entre dans le langage occidental grâce à elle. Kandinsky, Mondrian, Yeats, Gandhi (jeune) et bien d'autres liront ses ouvrages. Toute la nébuleuse New Age, avec ses maîtres ascensionnés, ses chakras et ses réincarnations, descend en droite ligne de ce salon new-yorkais de 1875."
        ],
        "sources": [
            "Marion Meade, Madame Blavatsky, the Woman Behind the Myth, 1980",
            "Rapport Hodgson, Society for Psychical Research, 1885",
            "H. P. Blavatsky, The Secret Doctrine, 1888"
        ],
        "tags": ["théosophie", "new age", "spiritisme"]
    },
    {
        "id": "alchimie-medievale",
        "universe": "esoterisme",
        "title": "L'alchimie : bien plus qu'une chasse à l'or",
        "subtitle": "Une science-religion oubliée, ancêtre discrète de la chimie moderne",
        "status": "fait_historique",
        "era": "moyen-age",
        "era_label": "Moyen Âge & Renaissance",
        "year": 1200,
        "region": "Europe et monde arabe",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "L'alchimiste n'était pas un charlatan qui essayait de tricher avec la matière. C'était souvent un homme cultivé, croyant, à la fois chimiste, philosophe et mystique.",
        "content": [
            "On imagine l'alchimiste comme un vieil homme crasseux, penché sur un chaudron fumant, cherchant à changer le plomb en or pour devenir riche. La réalité est infiniment plus intéressante.",
            "L'alchimie naît vers le IIIe siècle à Alexandrie, dans le grand melting-pot de la pensée grecque, égyptienne et juive. Elle se transmet ensuite dans le monde arabo-musulman (l'Espagne d'Al-Andalus est un carrefour majeur) avant d'être traduite en latin à partir du XIIe siècle, notamment à Tolède.",
            "Ce que cherche vraiment l'alchimiste, c'est un *opus*, une œuvre. Transformer une matière brute (la « materia prima ») en pierre philosophale, à la fois substance concrète capable de guérir les maladies et transmuer les métaux, et symbole d'une purification intérieure. En clair : perfectionner la matière et l'âme en même temps.",
            "Cela ne l'empêche pas de faire de la chimie très concrète. On lui doit la découverte de l'alcool, de l'acide nitrique, la mise au point de nombreux instruments (alambic, bain-marie – oui, du nom de Marie la Juive, alchimiste du IIIe siècle), et une méthode expérimentale rigoureuse.",
            "Isaac Newton, oui, celui de la gravitation, a passé plus de temps sur ses cornues alchimiques que sur son fameux traité *Principia*. Il n'y a rien de honteux à cela : la frontière entre science et magie n'existait pas encore telle qu'on la conçoit aujourd'hui."
        ],
        "sources": [
            "Serge Hutin, L'alchimie, PUF « Que sais-je ? »",
            "Bernard Joly, Rationalité de l'alchimie au XVIIe siècle",
            "Betty Jo Teeter Dobbs, The Foundations of Newton's Alchemy, 1975"
        ],
        "tags": ["alchimie", "moyen-âge", "chimie", "transmutation"]
    },

    # ============ ARTS DIVINATOIRES ============
    {
        "id": "tarot-histoire",
        "universe": "arts-divinatoires",
        "title": "Le tarot : d'un jeu de cartes italien à l'oracle universel",
        "subtitle": "Non, le tarot n'a pas été inventé par les prêtres égyptiens.",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVe siècle",
        "year": 1440,
        "region": "Italie du Nord",
        "coords": [45.4642, 9.19],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Milan, vers 1440 : à la cour des Visconti, on commande un magnifique jeu de cartes peintes à la main. Pas un instrument de divination — juste un jeu. Le reste ? Une longue histoire de récupération.",
        "content": [
            "Quand quelqu'un te dit « le tarot vient des prêtres égyptiens », tu peux lui répondre : Milan, XVe siècle, cour des Visconti-Sforza.",
            "Les plus anciens tarots connus sont italiens, peints à la main entre 1440 et 1470 pour les grandes familles d'Italie du Nord. Ils servent à jouer à un jeu de plis appelé *tarocchi*, ancêtre du bridge, où les cartes de « triomphes » (le Bateleur, l'Impératrice, la Mort, etc.) coupent les autres. Aucune trace, à cette époque, d'usage divinatoire.",
            "L'invention du tarot ésotérique date de 1781. Un ancien pasteur protestant nommé Antoine Court de Gébelin publie *Le Monde primitif*, une encyclopédie fantaisiste dans laquelle il affirme, sans la moindre preuve, que le tarot serait le *Livre de Thot*, un livre sacré égyptien miraculeusement conservé sous forme de cartes.",
            "Un contemporain, Jean-Baptiste Alliette, dit **Etteilla** (son nom de famille à l'envers), s'engouffre dans la brèche : il devient le premier cartomancien professionnel de l'histoire moderne, publie des méthodes, et invente pratiquement le métier.",
            "Puis vient le XIXe siècle avec Éliphas Lévi, qui associe le tarot à la kabbale hébraïque, et surtout, en 1909, la publication du **Rider-Waite-Smith** en Angleterre. Illustré par Pamela Colman Smith sous la direction d'Arthur Edward Waite, c'est ce tarot – aux images narratives, où même les cartes numérales racontent une scène – qui inspirera 90 % des jeux modernes.",
            "**Ce que l'on peut dire sans mentir :** le tarot est un magnifique support de projection et de narration. Ce qu'il n'est pas : un livre sacré remontant à Thot."
        ],
        "sources": [
            "Michael Dummett & Ronald Decker, A History of the Occult Tarot",
            "Antoine Court de Gébelin, Le Monde primitif, 1781",
            "Musée français de la carte à jouer, Issy-les-Moulineaux"
        ],
        "tags": ["tarot", "cartomancie", "renaissance", "occultisme"]
    },
    {
        "id": "astrologie-occidentale",
        "universe": "arts-divinatoires",
        "title": "L'astrologie : de Babylone à ton horoscope hebdomadaire",
        "subtitle": "Quatre mille ans d'histoire, entre observation du ciel et lecture du destin",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "Antiquité",
        "year": -2000,
        "region": "Mésopotamie",
        "coords": [32.5355, 44.4275],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Les premiers astrologues étaient les astronomes du roi. Leur mission : prédire les guerres et les récoltes en scrutant le ciel de Babylone.",
        "content": [
            "L'astrologie occidentale, celle avec les douze signes du zodiaque, remonte au minimum au IIe millénaire avant notre ère. À Babylone, une caste de scribes-prêtres note méticuleusement les positions des planètes et des étoiles sur des tablettes d'argile. Objectif : prévoir ce qui va arriver au roi et au royaume.",
            "À ce moment-là, il n'y a pas de « thème natal » individuel. On lit les présages collectifs, pour la nation. Les Grecs, au IVe siècle avant J.-C., importent ce savoir, y ajoutent la philosophie (Ptolémée, Alexandrie, IIe siècle) et surtout inventent l'astrologie *personnelle* : chaque être humain aurait son ciel de naissance.",
            "Au Moyen Âge chrétien, l'astrologie est enseignée dans les universités. On l'utilise en médecine (« signature » des plantes selon les planètes), en politique (le pape Sixte IV consulte des astrologues), en agriculture.",
            "La rupture arrive au XVIIe siècle, avec Galilée, Kepler et surtout la révolution scientifique. On cesse de considérer que les astres influencent physiquement nos destins. L'astrologie sort du champ universitaire, mais ne disparaît pas.",
            "Le XXe siècle lui offre un second souffle inattendu, via la presse. En 1930, l'astrologue britannique R. H. Naylor rédige un article sur la naissance de la princesse Margaret dans le *Sunday Express*. Immense succès. Deux ans plus tard, le concept d'« horoscope quotidien par signe solaire » est né. Douze paragraphes, un pour chacun : c'est un format éditorial génial, mais ce n'est plus vraiment de l'astrologie savante."
        ],
        "sources": [
            "Ptolémée, Tetrabiblos, IIe siècle",
            "Nick Campion, A History of Western Astrology (2 vol.), 2008",
            "Musée du Louvre, département des Antiquités orientales — tablettes MUL.APIN"
        ],
        "tags": ["astrologie", "zodiaque", "antiquité", "babylone"]
    },
    {
        "id": "chiromancie",
        "universe": "arts-divinatoires",
        "title": "La chiromancie : lire les lignes de la main",
        "subtitle": "Une pratique attestée depuis l'Inde antique, longtemps combattue par l'Église",
        "status": "tradition",
        "era": "antiquite",
        "era_label": "Antiquité indienne",
        "year": -500,
        "region": "Inde puis Europe",
        "coords": [28.6139, 77.209],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Ligne de vie, mont de Vénus, ligne de tête… La chiromancie a son vocabulaire, ses règles, ses maîtres. Et une histoire mouvementée.",
        "content": [
            "Regarde la paume de ta main. Tu y vois trois grandes lignes (vie, tête, cœur), quelques lignes secondaires, des « monts » (petits renflements sous chaque doigt). Toute la chiromancie tient dans cette carte miniature.",
            "Les plus anciennes mentions écrites remontent aux traités indiens en sanskrit, autour du Ve siècle avant J.-C. On la retrouve chez les Grecs (Aristote lui consacre un texte, ou plus probablement un pseudo-Aristote), chez les Romains, puis dans le monde arabe médiéval.",
            "En Europe, la chiromancie est régulièrement condamnée par l'Église. Le concile de Trente (1545-1563) la classe parmi les arts divinatoires suspects. Cela n'empêche pas les traités de se multiplier : *La Chiromance* de Jean Belot (1619) est un classique du XVIIe.",
            "Au XIXe siècle, un capitaine irlandais, William John Warner, alias **Cheiro**, en fait une célébrité mondaine. Il lit la main de Mark Twain, d'Oscar Wilde, du roi Édouard VII. Vraies prédictions ou coup de bluff élégant ? Chacun jugera.",
            "**La méthode traditionnelle** distingue toujours : la ligne de vie (partant entre le pouce et l'index, contournant le mont de Vénus), la ligne de tête (traversant horizontalement le milieu), et la ligne de cœur (au-dessus de la précédente). Puis vient l'analyse des monts, associés chacun à une planète, écho direct de l'astrologie."
        ],
        "sources": [
            "Cheiro, Cheiro's Language of the Hand, 1900",
            "Jean Belot, Œuvres, 1619",
            "Musée de la Main, université de Lausanne"
        ],
        "tags": ["chiromancie", "main", "divination"]
    },
    {
        "id": "runes-nordiques",
        "universe": "arts-divinatoires",
        "title": "Les runes : d'un alphabet à un oracle",
        "subtitle": "Attention : la « lecture des runes » telle qu'on la connaît est très récente",
        "status": "hypothese",
        "era": "antiquite",
        "era_label": "Ier siècle après J.-C.",
        "year": 100,
        "region": "Scandinavie / Germanie",
        "coords": [59.3293, 18.0686],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Oui, les Germains utilisaient des runes pour l'écriture et sans doute pour tirer au sort. Non, il n'existe pas de « tirage de runes » complet remontant aux Vikings.",
        "content": [
            "L'alphabet runique le plus ancien, le *Futhark ancien*, est utilisé entre le Ier et le VIIIe siècle après J.-C. dans les régions germaniques. Il compte 24 caractères, chacun ayant un nom (Fehu, Uruz, Thurisaz…) et une valeur phonétique.",
            "Tacite, dans son *Germania* (98 après J.-C.), décrit chez les peuples germaniques une pratique de tirage au sort : on grave des signes sur des baguettes taillées dans un arbre, on les répand sur un tissu blanc, et un prêtre en tire trois pour interpréter la volonté des dieux. C'est probablement l'ancêtre d'un usage divinatoire — mais la description est brève.",
            "Le problème, c'est qu'entre cette description et les manuels modernes de tirage de runes, il y a un gouffre d'un millénaire. Aucun texte médiéval ne détaille une « méthode » de divination runique. Les Islandais racontent des mythes où Odin obtient la connaissance des runes par sacrifice, mais rien sur un rituel opérationnel.",
            "Ce qu'on appelle aujourd'hui « lecture des runes », avec sa vingtaine de significations symboliques figées et son tirage à trois ou neuf pierres, a été codifié essentiellement dans les années 1980 par des auteurs comme Ralph Blum, dont le livre *The Book of Runes* (1982) est un immense succès commercial. Ralph Blum lui-même l'assumait : il avait « rêvé » ses significations.",
            "Cela n'enlève rien à la puissance symbolique des runes, mais il faut savoir qu'entre le tirage viking et le kit de runes qu'on trouve dans une boutique aujourd'hui, il y a surtout de la reconstitution poétique du XXe siècle."
        ],
        "sources": [
            "Tacite, Germania, chapitre 10",
            "R. I. Page, Runes, British Museum Press, 1987",
            "Ralph Blum, The Book of Runes, 1982"
        ],
        "tags": ["runes", "vikings", "nordique"]
    },
    {
        "id": "marc-de-cafe",
        "universe": "arts-divinatoires",
        "title": "La cafédomancie : lire l'avenir dans le fond d'une tasse",
        "subtitle": "Une pratique populaire née dans l'Empire ottoman",
        "status": "tradition",
        "era": "moderne",
        "era_label": "XVIIe siècle",
        "year": 1650,
        "region": "Turquie et Balkans",
        "coords": [41.0082, 28.9784],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Café turc, tasse retournée, motifs dans le marc… La cafédomancie est jeune, colorée, et très codifiée.",
        "content": [
            "Le café arrive en Europe via l'Empire ottoman au XVIIe siècle. Avec lui, une tradition purement domestique : quand on a fini son petit café bien épais, on retourne la tasse sur la soucoupe, on attend qu'elle refroidisse, et on lit les formes que le marc a dessinées à l'intérieur.",
            "En Turquie, en Grèce, en Bosnie, dans les Balkans et jusqu'en Arménie et au Liban, cette pratique est une véritable coutume familiale, essentiellement transmise entre femmes. Pas besoin d'être « voyante » : n'importe quelle grand-mère peut te lire ta tasse.",
            "La méthode est simple mais rigoureuse. On boit le café (turc, non filtré). On ajoute la soucoupe sur la tasse, on retourne le tout, on attend. On soulève la tasse et on examine les motifs sur les parois : un oiseau (une nouvelle), un poisson (de la chance), une montagne (un obstacle), un serpent (attention à quelqu'un)…",
            "L'intérieur de la tasse représenterait l'avenir proche, la soucoupe le passé ou les émotions. Certains lecteurs ajoutent une étape : ils demandent à la personne de tremper son doigt dans le marc de la soucoupe pour « signer » sa tasse.",
            "Rien de particulièrement mystérieux : c'est un art de la conversation, du regard, et de la mémoire familiale. On ne pratique jamais la cafédomancie seul — c'est toujours un moment partagé."
        ],
        "sources": [
            "Musée du café, Istanbul (Türk Kahvesi Müzesi)",
            "Angela Stewart, Coffee Culture in Eastern Europe, 2019"
        ],
        "tags": ["cafédomancie", "café", "ottoman", "tradition"]
    },
    {
        "id": "yi-jing",
        "universe": "arts-divinatoires",
        "title": "Le Yi Jing : le plus vieux livre divinatoire du monde",
        "subtitle": "Trois mille ans d'usage continu, en Chine puis dans le monde entier",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "IXe siècle avant J.-C.",
        "year": -800,
        "region": "Chine",
        "coords": [34.7472, 113.6249],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Le *Livre des Mutations* est à la fois un manuel de divination, un traité philosophique, et l'un des piliers de la pensée chinoise.",
        "content": [
            "Le Yi Jing, ou *Livre des Mutations*, est un texte chinois dont les couches les plus anciennes remontent au IXe siècle avant J.-C. Il repose sur un système de 64 « hexagrammes », chaque hexagramme étant composé de six traits, pleins ou brisés, qui symbolisent le yin et le yang.",
            "À l'origine, on tirait ces hexagrammes en manipulant des tiges d'achillée (une plante). Aujourd'hui, la méthode courante utilise trois pièces de monnaie qu'on jette six fois de suite : pile ou face décide de chaque trait.",
            "Une fois l'hexagramme obtenu, on lit dans le livre le commentaire correspondant. Chaque hexagramme a un titre poétique (« Le Créateur », « La Puissance du grand », « L'Attente ») et un texte souvent énigmatique — c'est justement l'énigme qui déclenche la réflexion.",
            "Le Yi Jing est un outil de méditation autant qu'un oracle. Confucius, dit la tradition, aurait usé sa reliure à force de le consulter. Le psychiatre C. G. Jung a préfacé la traduction allemande de Richard Wilhelm en 1949, y voyant une illustration de son concept de synchronicité.",
            "Ce qui est intéressant, c'est que même dans la Chine ancienne, le Yi Jing n'était pas seulement pour les devins. Les lettrés le consultaient pour prendre des décisions politiques, militaires, personnelles. C'est un livre-conseil autant qu'un livre-oracle."
        ],
        "sources": [
            "Richard Wilhelm, I Ging: Das Buch der Wandlungen, 1924",
            "Cyrille Javary, Le Yi Jing, PUF « Que sais-je ? »",
            "Musée national du Palais, Taipei — pièces archéologiques"
        ],
        "tags": ["yi jing", "chine", "hexagrammes", "confucianisme"]
    },

    # ============ MYSTÈRES ============
    {
        "id": "voynich",
        "universe": "mysteres",
        "title": "Le manuscrit de Voynich : le livre que personne n'a jamais lu",
        "subtitle": "Un codex du XVe siècle, illustré, rédigé dans une écriture inconnue",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "Début XVe siècle",
        "year": 1420,
        "region": "Europe centrale",
        "coords": [50.0755, 14.4378],
        "hero_image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67",
        "excerpt": "Datation carbone : entre 1404 et 1438. Écriture : totalement inconnue. Contenu : indéterminé. Depuis un siècle, cryptographes et linguistes s'y cassent les dents.",
        "content": [
            "Il existe, à l'université Yale, un livre de 240 pages qu'aucun être humain n'a réussi à lire depuis probablement six siècles. Il s'appelle le manuscrit de Voynich, du nom du libraire polonais qui l'a acheté en 1912 à des jésuites italiens.",
            "La datation au carbone 14, réalisée en 2009, situe le parchemin entre 1404 et 1438. Ce n'est donc pas un canular moderne — sur ce point au moins, on est sûr.",
            "L'écriture est cursive, élégante, régulière. Elle utilise environ 25 à 30 caractères récurrents. Elle se comporte statistiquement comme une vraie langue (fréquences, répétitions, structure). Mais aucun linguiste, aucun cryptographe (y compris ceux qui ont cassé Enigma pendant la guerre) n'a réussi à en tirer un sens.",
            "Les illustrations sont fascinantes. Une section « botanique » montre des plantes qui ne correspondent à aucune espèce connue. Une section « astronomique » présente des roues zodiacales étranges. Une section « biologique » représente des femmes nues baignant dans des tuyauteries. Et une section « pharmaceutique » aligne des bocaux mystérieux.",
            "Les hypothèses ne manquent pas. Certains y voient un canular médiéval très élaboré (l'astronome Gordon Rugg a montré qu'on pouvait générer un texte de ce type avec une méthode simple). D'autres, une langue construite naturelle mais aujourd'hui perdue. D'autres encore, un code personnel d'un érudit isolé. La vérité, à ce jour : personne ne sait.",
            "Le manuscrit est numérisé intégralement et consultable gratuitement en ligne sur le site de la Beinecke Rare Book & Manuscript Library. Si tu veux tenter ta chance, tu es le bienvenu."
        ],
        "sources": [
            "Beinecke Rare Book & Manuscript Library, Yale — cote MS 408",
            "Gordon Rugg, The Mystery of the Voynich Manuscript, 2004",
            "Datation carbone 14, université d'Arizona, 2009"
        ],
        "tags": ["manuscrit", "cryptographie", "mystère", "moyen-âge"]
    },
    {
        "id": "proces-sorcieres-salem",
        "universe": "mysteres",
        "title": "Les procès de sorcières de Salem",
        "subtitle": "1692 : quand une petite ville puritaine sombre dans la panique collective",
        "status": "fait_historique",
        "era": "moderne",
        "era_label": "1692",
        "year": 1692,
        "region": "Massachusetts",
        "coords": [42.5195, -70.8967],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "En quelques mois, une trentaine de personnes sont accusées, dix-neuf sont pendues, une est écrasée sous des pierres. Comment un tel emballement a-t-il pu se produire ?",
        "content": [
            "Salem, Massachusetts, hiver 1691-1692. La communauté puritaine vit sous tension : conflits fonciers, épidémies, guerres avec les tribus autochtones, hivers rigoureux. Chacun sent que quelque chose « ne va pas ».",
            "En janvier 1692, deux fillettes de la maison du révérend Samuel Parris — sa fille Betty, 9 ans, et sa nièce Abigail, 11 ans — se mettent à avoir des crises étranges : convulsions, cris, contorsions. Le médecin diagnostique, faute de mieux : « ensorcellement ».",
            "Les fillettes désignent trois femmes. L'une d'elles, Tituba, une esclave caraïbe, avoue sous pression toute une série de choses fantastiques : elle vole dans les airs, elle a signé un pacte avec le Diable, elle a vu d'autres sorcières… La machine s'emballe.",
            "En quelques mois, plus de 150 personnes sont accusées. Un tribunal spécial est convoqué. Il accepte comme preuve les « témoignages spectraux » : le simple fait qu'une accusatrice dise qu'un « spectre » de l'accusée est venu la tourmenter suffit à condamner. C'est une aberration juridique majeure.",
            "Résultat : 19 personnes sont pendues sur Gallows Hill, un homme (Giles Corey) est écrasé sous des pierres parce qu'il refuse de plaider, cinq meurent en prison. Puis, à l'automne, le gouverneur Phips interdit les témoignages spectraux. Les acquittements suivent. Fin de la crise.",
            "Aujourd'hui, les historiens n'invoquent plus une seule cause. On combine plusieurs facteurs : tensions sociales et foncières, oppression puritaine des femmes, hystérie collective, jalousies villageoises, hypothèse (contestée) d'un ergotisme du seigle. Le procès de Salem reste le cas d'école de ce que produit la peur quand elle rencontre un système judiciaire qui accepte l'invisible comme preuve."
        ],
        "sources": [
            "Stacy Schiff, The Witches: Salem, 1692, 2015",
            "Archives du procès, Peabody Essex Museum",
            "Elaine G. Breslaw, Tituba, Reluctant Witch of Salem, 1996"
        ],
        "tags": ["sorcières", "salem", "puritains", "procès"]
    },
    {
        "id": "cabinets-curiosites",
        "universe": "mysteres",
        "title": "Les cabinets de curiosités : l'ancêtre du musée",
        "subtitle": "Corne de licorne, momie, coquillages géants et fœtus dans le formol",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe-XVIIIe siècle",
        "year": 1550,
        "region": "Europe",
        "coords": [50.0755, 14.4378],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Une pièce sombre, remplie du sol au plafond d'objets improbables. Un savant montre sa « collection » à des visiteurs choisis. Nous sommes au XVIIe siècle, et ces pièces ont fondé la science moderne.",
        "content": [
            "Imagine une pièce, souvent dans le palais d'un prince ou la maison d'un érudit fortuné. Sur les étagères : une momie égyptienne, un pied de rhinocéros, une « corne de licorne » (en réalité une défense de narval), des coquillages exotiques rapportés des Indes, un crâne difforme, un livre de sortilèges, une pierre soi-disant tombée du ciel.",
            "Les cabinets de curiosités apparaissent à la Renaissance, quand les grandes découvertes mettent en circulation un flot d'objets étranges venus de partout. Rassembler ces choses, c'est prétendre embrasser du regard tout le savoir du monde.",
            "On y mélange trois catégories : les *naturalia* (produits de la nature — pierres, animaux, plantes), les *artificialia* (produits de la main humaine — armes exotiques, sculptures, montres), et les *mirabilia* (les curiosités pures, l'étrange et le monstrueux).",
            "Certains cabinets sont célèbres. Celui de l'apothicaire copenhagois Ole Worm au XVIIe siècle est représenté dans une gravure iconique : on y voit un jeune homme regardant un narval accroché au plafond. Celui d'Athanasius Kircher à Rome mélange automates, obélisques miniatures et vestiges antiques.",
            "L'astuce, c'est que ces cabinets sont les ancêtres directs des musées d'histoire naturelle. Le British Museum s'ouvre en 1759 sur la base de la collection privée du médecin Hans Sloane. Le Muséum de Paris naît en 1793. La grande différence : on trie, on classe, on ne mélange plus la corne de licorne avec le coquillage."
        ],
        "sources": [
            "Ole Worm, Museum Wormianum, 1655",
            "Krzysztof Pomian, Collectionneurs, amateurs et curieux, 1987",
            "Museum d'histoire naturelle de Paris"
        ],
        "tags": ["cabinet", "curiosités", "musée", "renaissance"]
    },

    # ============ LÉGENDES ============
    {
        "id": "dame-blanche",
        "universe": "legendes",
        "title": "Les dames blanches : une figure européenne millénaire",
        "subtitle": "Légende — non historiquement démontrée",
        "status": "legende",
        "era": "moyen-age",
        "era_label": "Depuis le Moyen Âge",
        "year": 1200,
        "region": "France, Allemagne, Îles britanniques",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Elle apparaît près d'un pont, d'une fontaine, d'un manoir. Elle est belle, silencieuse, toute vêtue de blanc. Puis elle disparaît.",
        "content": [
            "**Précisons d'entrée** : la dame blanche est une figure légendaire. Aucune source historique fiable n'atteste qu'elle « existe » en un lieu précis. Ce qui est réel, en revanche, c'est la persistance et l'universalité de cette figure dans le folklore européen.",
            "La dame blanche est un fantôme féminin, généralement lié à un lieu (un pont, une fontaine, un carrefour, une chapelle) ou à une famille noble. Elle apparaît la nuit ou au crépuscule, silencieuse, sereine ou mélancolique. Parfois elle prévient d'un malheur ; parfois elle demande de l'aide ; parfois elle disparaît simplement.",
            "En Bourgogne, la Dame Blanche de Puiseaux hante un vieux château. Dans les Vosges, la Dame Blanche de la Kunkel apparaît près d'une fontaine. En Bretagne, on parle des « Lavandières de la nuit ». En Allemagne, la *Weiße Frau* est associée à la maison de Hohenzollern et à celle de Habsbourg : elle apparaîtrait avant la mort d'un membre de la famille.",
            "Origine probable ? Les folkloristes proposent plusieurs pistes qui s'additionnent : christianisation de divinités féminines païennes liées à l'eau et aux passages, croyances sur les morts « en couche » (les femmes mortes en couches deviendraient des revenantes), figures d'ancêtres protectrices d'une lignée. Rien de tout cela n'est *la* réponse : c'est le mille-feuille des siècles.",
            "La légende urbaine de la « dame blanche sur la route » (auto-stoppeuse qui monte dans une voiture et disparaît) est, elle, un développement du XXe siècle, très bien étudié par les folkloristes contemporains. On en retrouve des versions strictement identiques aux États-Unis (« The Vanishing Hitchhiker »), au Japon, et en Amérique latine. Exactement les mêmes lieux, exactement les mêmes détails, sans qu'aucun cas ait jamais pu être documenté."
        ],
        "sources": [
            "Claude Lecouteux, Fantômes et revenants au Moyen Âge, 1986",
            "Jan Harold Brunvand, The Vanishing Hitchhiker, 1981",
            "Musée national des arts et traditions populaires (fonds numérisés)"
        ],
        "tags": ["fantômes", "légende", "folklore", "france"]
    },
    {
        "id": "melusine",
        "universe": "legendes",
        "title": "Mélusine, la fée-serpente du Poitou",
        "subtitle": "Légende médiévale ancrée dans l'histoire des Lusignan",
        "status": "legende",
        "era": "moyen-age",
        "era_label": "XIVe siècle",
        "year": 1392,
        "region": "Poitou, France",
        "coords": [46.5802, 0.3404],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "excerpt": "Un chevalier surprend son épouse dans son bain. Il découvre qu'elle a une queue de serpent. Elle s'envole en poussant un cri terrible.",
        "content": [
            "**Attention** : Mélusine est une légende, ce qui ne l'empêche pas d'avoir été prise très au sérieux, notamment par la famille de Lusignan qui la revendiquait comme ancêtre fondatrice.",
            "L'histoire, dans sa version la plus complète, est mise par écrit vers 1392-1394 par un certain Jean d'Arras, à la demande du duc Jean de Berry. Elle raconte les aventures de Mélusine, fille d'une fée et d'un roi humain, condamnée à devenir serpent de la taille aux pieds chaque samedi.",
            "Elle rencontre le chevalier Raymondin et l'épouse à une condition non négociable : il ne devra jamais chercher à la voir le samedi. Le mariage est magnifique, Mélusine bâtit en une nuit le château de Lusignan (et plusieurs autres, dit-elle), donne dix fils à son mari.",
            "Un jour, un frère de Raymondin lui glisse à l'oreille que sa femme le trompe peut-être ces samedis-là. Raymondin cède à la curiosité, perce un trou dans la porte de la chambre… et découvre Mélusine dans son bain, avec sa queue de serpent. Il se tait. Mais lorsque, plus tard, il la traite publiquement de « très fausse serpente », elle s'envole en cri déchirant. Elle reviendra, dit la légende, à chaque mort d'un seigneur de Lusignan, pour l'annoncer.",
            "La légende a une fonction politique claire : donner aux Lusignan (une maison féodale importante, qui régna aussi sur Chypre et Jérusalem) une ascendance surnaturelle et donc légitime. On retrouve ce schéma partout en Europe : les grandes familles avaient besoin d'un « fondateur mythique ».",
            "Ce qui est réel, en revanche : les ruines du château de Lusignan, en Poitou, existent bel et bien. Et la sirène-fée à double queue est devenue un motif décoratif immensément diffusé — jusqu'au logo de Starbucks."
        ],
        "sources": [
            "Jean d'Arras, Le roman de Mélusine, 1393",
            "Coudrette, Le roman de Mélusine, vers 1401",
            "Jacques Le Goff, « Mélusine maternelle et défricheuse », Annales ESC, 1971"
        ],
        "tags": ["mélusine", "fée", "moyen-âge", "lusignan"]
    },
    {
        "id": "loch-ness",
        "universe": "legendes",
        "title": "Le monstre du Loch Ness : histoire d'une légende moderne",
        "subtitle": "Une créature ancienne, une célébrité mondiale née en 1933",
        "status": "legende",
        "era": "contemporain",
        "era_label": "XXe siècle",
        "year": 1933,
        "region": "Écosse",
        "coords": [57.3229, -4.4244],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Une créature aquatique dans un lac écossais. La première mention remonte au VIe siècle. La célébrité mondiale, à un article du *Inverness Courier* en 1933.",
        "content": [
            "**Rappel du statut** : Nessie appartient à la légende. Aucun spécimen n'a jamais été capturé, aucune analyse ADN d'un lac écossais n'a livré de trace de reptile marin géant. Ce qui est *réel*, c'est la fascination.",
            "La toute première mention d'une créature dans le Loch Ness date du VIe siècle : dans la *Vie de saint Colomba* écrite par Adomnán vers 700, le saint irlandais aurait chassé un « monstre » dans la rivière Ness (pas le lac). Après ça… silence pendant plus de mille ans.",
            "Puis, le 2 mai 1933, le journal *Inverness Courier* publie un article intitulé « Étrange spectacle sur le Loch Ness ». Un couple, les Mackay, aurait vu une créature « énorme » se déplacer dans l'eau. L'article devient viral (avant même que ce mot n'existe). Le tourisme afflue. Une industrie naît.",
            "En 1934, le chirurgien Kenneth Wilson publie *la* photo mythique, dite « photo du chirurgien » : un long cou émergeant de l'eau, comme un plésiosaure. En 1994, on apprend que c'était un faux : une figurine en bois de 30 centimètres flottant sur un sous-marin jouet. Wilson avait participé à la supercherie avec Marmaduke Wetherell, un chasseur humilié par le *Daily Mail*.",
            "Rien de tout cela n'a arrêté la légende. Le loch Ness fait 39 km de long, 230 m de profondeur, son eau est extrêmement sombre à cause de la tourbe. Il reste un fantastique projeteur d'imaginaire. Une étude ADN environnementale menée par l'université d'Otago en 2019 a listé toutes les espèces présentes : beaucoup d'anguilles, aucun reptile géant."
        ],
        "sources": [
            "Adomnán, Vita Columbae, VIIe siècle",
            "Ronald Binns, The Loch Ness Mystery Solved, 1983",
            "Neil Gemmell et al., étude ADN environnemental, université d'Otago, 2019"
        ],
        "tags": ["nessie", "écosse", "cryptide", "légende moderne"]
    },

    # ============ REGALIA ============
    {
        "id": "cullinan-diamants-couronne",
        "universe": "regalia",
        "title": "Le Cullinan : le plus gros diamant brut jamais trouvé",
        "subtitle": "3 106 carats, découverts en 1905 en Afrique du Sud, offerts au roi Édouard VII",
        "status": "fait_historique",
        "era": "contemporain",
        "era_label": "XXe siècle",
        "year": 1905,
        "region": "Afrique du Sud / Royaume-Uni",
        "coords": [-25.6866, 28.0783],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Un caillou de 621 grammes, la taille d'un poing. On l'a taillé en 9 grandes pierres et 96 petites. La plus grosse, Cullinan I, orne aujourd'hui le sceptre du souverain britannique.",
        "content": [
            "Le 26 janvier 1905, dans la mine Premier près de Pretoria, un contremaître nommé Frederick Wells aperçoit un éclat inhabituel dans la paroi. C'est un diamant brut de 3 106,75 carats, environ 621 grammes. À ce jour, aucun autre diamant de gemme de cette taille n'a jamais été extrait de la terre.",
            "Le gouvernement du Transvaal l'achète et l'offre en 1907 au roi Édouard VII pour son 66e anniversaire. Le voyage vers Londres est une opération digne d'un roman : la pierre part par la poste ordinaire dans une simple boîte, tandis qu'un faux Cullinan escorté d'une armée de gardes voyage à bord d'un navire. Personne n'y prête attention. La vraie pierre arrive intacte.",
            "En 1908, Édouard VII confie la taille à la maison Asscher d'Amsterdam. Joseph Asscher étudie la pierre pendant six mois avant de risquer le premier coup. Le premier essai brise sa lame. Le second réussit, mais Asscher, dit-on, s'évanouit sous le coup de l'émotion. On en tirera 9 grandes pierres numérotées I à IX, et 96 petites.",
            "Le Cullinan I, également appelé *Great Star of Africa*, 530,4 carats, est serti dans le sceptre royal. Le Cullinan II, 317,4 carats, orne la couronne impériale. Les autres sont dispersés dans les bijoux personnels de la Couronne : broches, colliers, bagues.",
            "La légitimité de cette « offrande » de 1907, faite deux ans après la fin d'une guerre coloniale, reste un sujet de débat vif en Afrique du Sud. Depuis 2023, plusieurs voix officielles demandent le retour du Cullinan I. Le dossier est ouvert."
        ],
        "sources": [
            "Royal Collection Trust, Londres — inventaire des joyaux de la Couronne",
            "Ian Balfour, Famous Diamonds, 5e édition, 2009",
            "Archives de la mine Premier, De Beers"
        ],
        "tags": ["cullinan", "diamant", "couronne", "afrique du sud"]
    },
    {
        "id": "couronne-charlemagne",
        "universe": "regalia",
        "title": "La couronne dite « de Charlemagne » : une histoire de nom",
        "subtitle": "Un chef-d'œuvre du Xe siècle attribué (à tort) à l'empereur du VIIIe",
        "status": "fait_historique",
        "era": "moyen-age",
        "era_label": "Fin du Xe siècle",
        "year": 980,
        "region": "Saint-Empire romain germanique",
        "coords": [47.7959, 13.0405],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "On l'appelle « couronne de Charlemagne ». Elle a été fabriquée près de deux siècles après la mort de Charlemagne. Elle n'en est pas moins un chef-d'œuvre.",
        "content": [
            "Charlemagne meurt en 814. La couronne qu'on associe à son nom, conservée aujourd'hui au Trésor impérial de la Hofburg à Vienne, a probablement été réalisée à la fin du Xe siècle, sans doute pour le couronnement d'Otton Ier en 962 ou celui d'Otton II en 967. Le lien avec Charlemagne est un lien symbolique, pas historique.",
            "Elle est constituée de huit plaques d'or, quatre plus grandes ornées de pierres précieuses (améthystes, saphirs, émeraudes, perles), et quatre plus petites décorées d'émaux cloisonnés représentant le roi David, Salomon, Ézéchias et le Christ. Tout un programme politico-religieux : le souverain, comme les rois d'Israël, tient son pouvoir de Dieu.",
            "Une croix ornée de pierres a été ajoutée à l'avant, sans doute par Conrad II au XIe siècle. Un arceau frontal a été ajouté encore plus tard, portant l'inscription CHVONRADVS DEI GRATIA ROMANORVM IMPERATOR AVGVSTVS.",
            "Elle a servi au couronnement de la plupart des empereurs du Saint-Empire romain germanique jusqu'à sa dissolution en 1806. François II d'Autriche, dernier empereur, l'emporte à Vienne, où elle est conservée depuis.",
            "Anecdote : Adolf Hitler, obsédé par le prestige impérial, la fait transférer à Nuremberg en 1938. À la fin de la guerre, les Américains la retrouvent cachée dans un bunker sous le château de Nuremberg. Elle est rendue à l'Autriche en 1946."
        ],
        "sources": [
            "Kunsthistorisches Museum, Vienne — Weltliche Schatzkammer",
            "Hermann Fillitz, Die Insignien und Kleinodien des Heiligen Römischen Reiches, 1954"
        ],
        "tags": ["couronne", "charlemagne", "saint-empire", "vienne"]
    },

    # ============ PIERRES ============
    {
        "id": "ambre-histoire",
        "universe": "pierres",
        "title": "L'ambre : la résine qui a traversé les âges",
        "subtitle": "Une « pierre » qui n'en est pas une, adorée depuis la Préhistoire",
        "status": "fait_historique",
        "era": "prehistoire",
        "era_label": "Depuis le Paléolithique",
        "year": -30000,
        "region": "Mer Baltique",
        "coords": [54.6872, 25.28],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Une résine fossilisée depuis 30 à 90 millions d'années, dans laquelle on retrouve parfois des insectes intacts.",
        "content": [
            "L'ambre n'est pas une pierre au sens minéralogique : c'est une résine de conifères, fossilisée sur des dizaines de millions d'années. La plupart de l'ambre européen provient de la mer Baltique et date d'environ 44 millions d'années.",
            "Les hommes préhistoriques l'utilisaient déjà. On a retrouvé des perles d'ambre dans des tombes du Paléolithique supérieur, il y a plus de 30 000 ans. À l'époque néolithique, il devient un objet d'échange à longue distance.",
            "Les Grecs l'appellent *êlektron*. Fait crucial : Thalès de Milet, au VIe siècle avant J.-C., remarque qu'en frottant un morceau d'ambre avec de la laine, celui-ci attire de petits fétus. Il ne le sait pas, mais il vient d'observer l'électricité statique. Le mot « électricité » vient directement de l'ambre.",
            "Les Romains payaient l'ambre à prix d'or. Pline l'Ancien raconte que Néron avait envoyé un chevalier spécial jusqu'à la Baltique pour en rapporter des quantités phénoménales : les combats de gladiateurs de son grand jeu ont vu chaque filet, chaque arme, décoré d'ambre.",
            "Côté croyances, l'ambre a été considéré comme protecteur (surtout pour les enfants), curatif (contre les maux de gorge, les maladies articulaires), et magique. **À distinguer clairement des faits** : la « lithothérapie » moderne prête à l'ambre de nombreuses propriétés thérapeutiques qui ne sont pas confirmées par la science. Ce qui est réel, c'est l'acide succinique qu'il contient — mais à des doses beaucoup trop faibles pour un effet mesuré sur le corps humain porté en collier."
        ],
        "sources": [
            "Pline l'Ancien, Histoire naturelle, livre XXXVII",
            "Musée de l'ambre, Palanga (Lituanie)",
            "Michael Ganzelewski & Rainer Slotta, Bernstein — Tränen der Götter, 1996"
        ],
        "tags": ["ambre", "baltique", "résine", "antiquité"]
    },
    {
        "id": "lapis-lazuli",
        "universe": "pierres",
        "title": "Le lapis-lazuli : le bleu des rois",
        "subtitle": "Six mille ans d'histoire, une seule route d'approvisionnement",
        "status": "fait_historique",
        "era": "antiquite",
        "era_label": "Depuis le IVe millénaire avant J.-C.",
        "year": -3500,
        "region": "Afghanistan",
        "coords": [36.6511, 71.1178],
        "hero_image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67",
        "excerpt": "Le bleu profond du lapis-lazuli fut, pendant des millénaires, la couleur la plus chère du monde. Il ne venait que d'un seul endroit.",
        "content": [
            "Il y a un lieu, un seul, qui a fourni pendant plus de six mille ans la majorité du lapis-lazuli utilisé dans le monde antique : les mines de Sar-e Sang, dans la vallée du Kokcha, au nord-est de l'Afghanistan. Ces mines sont toujours en activité aujourd'hui.",
            "De là, la pierre voyage. On la retrouve dans les tombes royales d'Ur en Mésopotamie (2600 avant J.-C.), sur le masque de Toutânkhamon (1323 avant J.-C.), en Chine sur la route de la soie, en Grèce et à Rome.",
            "Le lapis-lazuli n'est pas une pierre monominérale, contrairement au rubis ou au diamant : c'est un agrégat, où domine la *lazurite* bleue, mais dans lequel on distingue à l'œil nu des pyrites (paillettes dorées) et de la calcite (veines blanches).",
            "Réduit en poudre, il donne un pigment bleu extraordinaire : **l'outremer véritable**. Au Moyen Âge et à la Renaissance, ce pigment était plus cher que l'or au poids. Il était réservé aux commandes les plus prestigieuses. C'est pour cela que les peintres médiévaux réservaient le lapis-lazuli au manteau de la Vierge Marie : plus la robe est bleue, plus le commanditaire a payé cher.",
            "Vermeer, dans *La Jeune Fille à la perle*, utilise l'outremer de lapis pour le turban. Michel-Ange, à la fin de sa vie, laissera inachevée son *Ensevelissement* faute d'avoir les moyens de commander l'outremer.",
            "En 1826, un chimiste français, Jean-Baptiste Guimet, met au point un procédé pour synthétiser un outremer artificiel équivalent. Le lapis perd son monopole du bleu. Mais pas son aura."
        ],
        "sources": [
            "British Museum, Londres — collection mésopotamienne",
            "Musée du Louvre — trésors d'Ur",
            "Michael Price, The Chemistry of Colour, Nature Chemistry, 2015"
        ],
        "tags": ["lapis-lazuli", "afghanistan", "pigment", "outremer"]
    },

    # ============ PERSONNAGES ============
    {
        "id": "nostradamus",
        "universe": "personnages",
        "title": "Nostradamus : médecin, astrologue, superstar posthume",
        "subtitle": "Un vrai médecin, un vrai astrologue, mais une postérité largement gonflée",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe siècle",
        "year": 1555,
        "region": "Provence",
        "coords": [43.9493, 4.8055],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Médecin de la peste, apothicaire, astrologue de la reine Catherine de Médicis. Auteur des « Prophéties ». On lui fait dire beaucoup plus qu'il n'a jamais écrit.",
        "content": [
            "Michel de Nostredame naît en 1503 à Saint-Rémy-de-Provence, dans une famille de juifs convertis. Il étudie la médecine à Montpellier, sans doute autour de 1521-1529, à une époque de grandes épidémies de peste.",
            "Il gagne sa réputation en travaillant sur les foyers de peste à Aix-en-Provence et Salon-de-Provence. Ses méthodes (privilégier l'air propre, l'eau propre, des « pilules aromatiques ») ne guérissent pas la peste, personne ne le pouvait, mais elles évitent probablement d'aggraver la situation par des saignées à outrance.",
            "En 1550, il commence à publier des almanachs annuels, mélange de prévisions météorologiques, astrologiques et politiques. Le succès est immédiat.",
            "En 1555 paraît la première édition des *Prophéties*, un recueil de quatrains obscurs numérotés par « Centuries ». Le style est volontairement énigmatique : anagrammes, latinismes, symboles. Impossible d'en tirer un sens univoque à la lecture. C'est précisément ce qui a permis à ses lecteurs, depuis 470 ans, de « retrouver » a posteriori la mort d'Henri II, la Révolution française, Hitler, le 11 septembre 2001, la guerre en Ukraine…",
            "Ce qui est vrai : Catherine de Médicis, veuve d'Henri II, le fait venir à la cour en 1555 et l'estime. Il meurt à Salon en 1566, à 62 ans. Il est enterré dans l'église Saint-Laurent, où sa tombe existe toujours.",
            "Ce qui est faux ou reconstruit : la plupart des « prédictions vérifiées » ont été fabriquées après coup, souvent en modifiant légèrement le quatrain original, ou en interprétant de façon abusive un texte volontairement flou. Aucune n'est prouvable comme prédiction avant l'événement."
        ],
        "sources": [
            "Denis Crouzet, Nostradamus, une médecine des âmes à la Renaissance, 2011",
            "Nostradamus, Les Prophéties, édition Lyon 1568",
            "Musée Nostradamus, Salon-de-Provence"
        ],
        "tags": ["nostradamus", "prophétie", "renaissance", "provence"]
    },
    {
        "id": "john-dee",
        "universe": "personnages",
        "title": "John Dee : mathématicien de la reine Élisabeth Ire, invocateur d'anges",
        "subtitle": "Le savant complet de la Renaissance anglaise, entre science et occulte",
        "status": "fait_historique",
        "era": "renaissance",
        "era_label": "XVIe siècle",
        "year": 1580,
        "region": "Angleterre",
        "coords": [51.4934, -0.1074],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "excerpt": "Cartographe, astronome, cryptographe, conseiller royal, alchimiste — et candidat crédible au titre de « personnage historique le plus étonnant de la Renaissance anglaise ».",
        "content": [
            "John Dee (1527-1608) est né à Londres, brillant élève à Cambridge dès l'âge de 15 ans. À 20 ans, il est déjà l'un des plus grands mathématiciens de son pays.",
            "Il joue un rôle discret mais central dans le programme maritime anglais. C'est lui qui dessine les cartes qui permettront les expéditions vers le Nouveau Monde. Il conseille Élisabeth Ire sur les questions de navigation, de dates, d'astrologie. On lui attribue la formule « British Empire » — il aurait été le premier à l'écrire.",
            "Sa bibliothèque, à Mortlake, est la plus grande d'Angleterre : environ 4 000 livres, quand la bibliothèque de Cambridge n'en compte que 450. C'est un laboratoire intellectuel où passent tous les grands esprits du royaume.",
            "À partir de 1582, Dee bascule dans une autre dimension. Convaincu de pouvoir communiquer avec des anges, il s'associe à un médium douteux, Edward Kelley, qui prétend voir et entendre des entités dans un miroir d'obsidienne. Ensemble, ils passent des années à noter les « conversations angéliques » qui produiront la fameuse langue « énochienne », un système linguistique complet, extrêmement structuré, dont l'origine réelle reste débattue.",
            "En 1583, ils partent pour la Bohême, invités par des nobles fascinés par l'alchimie. Dee revient huit ans plus tard, ruiné, sa maison de Mortlake pillée pendant son absence, sa bibliothèque en partie brûlée. Il mourra dans la pauvreté en 1608.",
            "Aujourd'hui, on redécouvre Dee comme un cas fascinant : un des savants les plus rigoureux de son époque a passé une partie de sa vie à essayer d'invoquer des anges. C'est ce qui rend la Renaissance si passionnante : la ligne entre science et magie n'était pas là où nous la traçons."
        ],
        "sources": [
            "British Museum — miroir d'obsidienne aztèque ayant appartenu à Dee",
            "Benjamin Woolley, The Queen's Conjurer, 2001",
            "John Dee, Monas Hieroglyphica, 1564"
        ],
        "tags": ["john dee", "élisabeth", "occultisme", "renaissance"]
    },
    {
        "id": "cagliostro",
        "universe": "personnages",
        "title": "Cagliostro : le comte imposteur qui a fait chuter Marie-Antoinette",
        "subtitle": "Aventurier européen, alchimiste autoproclamé, mêlé à l'affaire du collier",
        "status": "fait_historique",
        "era": "moderne",
        "era_label": "XVIIIe siècle",
        "year": 1785,
        "region": "France et Europe",
        "coords": [48.8566, 2.3522],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "excerpt": "Il se disait comte, immortel, guérisseur, mage égyptien. Il était en fait Giuseppe Balsamo, fils d'un modeste marchand palermitain.",
        "content": [
            "Giuseppe Balsamo naît en 1743 à Palerme, dans une famille très modeste. À 25 ans, il quitte la Sicile, s'invente un nom noble — comte Alexandre de Cagliostro — et commence une itinérance européenne qui va durer vingt ans.",
            "Sa méthode : arriver dans une ville, se faire présenter comme un mage égyptien maîtrisant l'alchimie, la médecine et la « magie divine », séduire les élites locales, organiser des séances spectaculaires, encaisser beaucoup d'argent, puis repartir avant que les ennuis n'arrivent. Il opère à Londres, Strasbourg, Naples, Saint-Pétersbourg, Varsovie.",
            "En 1785, il est à Paris quand éclate l'affaire du Collier de la Reine. Une aventurière, Jeanne de La Motte, orchestre une escroquerie monumentale : elle fait croire à un cardinal, Rohan, que Marie-Antoinette souhaite acheter en secret un collier de diamants fabuleux. Le cardinal avance l'argent, on lui remet le collier « pour la reine », le collier est démonté, revendu à Londres pièce par pièce. Marie-Antoinette n'était au courant de rien.",
            "Quand tout éclate, Cagliostro, qui fréquente Rohan, est embarqué dans le scandale. Il passe neuf mois à la Bastille, avant d'être acquitté. Il en tire une célébrité paradoxale : le mage devient une figure publique, ses *Lettres au peuple français* rédigées depuis l'Angleterre sont lues partout.",
            "L'affaire discrédite pour longtemps Marie-Antoinette, alors qu'elle en est en réalité victime. Napoléon écrira plus tard : « L'affaire du Collier a été la cause première de la Révolution française. »",
            "Cagliostro finit mal. Arrêté à Rome en 1789 par l'Inquisition pour franc-maçonnerie et hérésie, il est condamné à mort, peine commuée en prison à vie. Il meurt dans la forteresse de San Leo en 1795. Ses dernières années auront été aussi obscures que ses années de gloire avaient été spectaculaires."
        ],
        "sources": [
            "Frantz Funck-Brentano, L'Affaire du Collier, 1901",
            "Élise Goodman-Soellner, Cagliostro, 1994",
            "Archives de la Bastille — dossier Cagliostro"
        ],
        "tags": ["cagliostro", "collier de la reine", "imposteur", "xviiie"]
    }
]

UNIVERSES = [
    {
        "id": "esoterisme",
        "title": "Histoire de l'ésotérisme",
        "subtitle": "De l'Antiquité aux mouvements contemporains",
        "description": "Explorer les époques, civilisations, mouvements et pratiques qui ont façonné la pensée ésotérique occidentale.",
        "image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc"
    },
    {
        "id": "arts-divinatoires",
        "title": "Arts divinatoires",
        "subtitle": "Tarot, astrologie, chiromancie, runes…",
        "description": "L'histoire réelle de chaque pratique : origine documentée, transformations, protocoles anciens et idées reçues.",
        "image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg"
    },
    {
        "id": "mysteres",
        "title": "Mystères et bizarreries",
        "subtitle": "Événements étranges mais documentés",
        "description": "Objets énigmatiques, procès de sorcières, cabinets de curiosités, prophéties historiques et phénomènes inexpliqués à leur époque.",
        "image": "https://images.pexels.com/photos/1786341540187-4ee121cecc67"
    },
    {
        "id": "legendes",
        "title": "Contes, mythes et légendes",
        "subtitle": "Créatures, revenants, folklore",
        "description": "Les grandes légendes françaises et internationales, leurs origines et leurs transformations au fil des siècles.",
        "image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg"
    },
    {
        "id": "regalia",
        "title": "Rois, reines, couronnes et pierres",
        "subtitle": "Les bijoux du pouvoir",
        "description": "Couronnes, sceptres, regalia et pierres associés aux souverains et grandes dynasties. Histoire attestée, vols, disparitions et légendes.",
        "image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg"
    },
    {
        "id": "pierres",
        "title": "Pierres, symboles et croyances",
        "subtitle": "L'histoire avant la signification",
        "description": "Pour chaque pierre, son parcours historique — Antiquité, médecine ancienne, royauté, folklore — avant les significations contemporaines.",
        "image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67"
    },
    {
        "id": "personnages",
        "title": "Les personnages",
        "subtitle": "Portraits narratifs",
        "description": "Occultistes, astrologues, alchimistes, souverains, écrivains — les figures réelles qui ont façonné cette histoire, et celles que la légende a ensuite entourées.",
        "image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc"
    }
]

ERAS = [
    {"id": "prehistoire", "label": "Préhistoire", "range": "avant -3000"},
    {"id": "antiquite", "label": "Antiquité", "range": "-3000 → 476"},
    {"id": "moyen-age", "label": "Moyen Âge", "range": "476 → 1492"},
    {"id": "renaissance", "label": "Renaissance", "range": "1400 → 1650"},
    {"id": "moderne", "label": "Époque moderne", "range": "1650 → 1789"},
    {"id": "xixe", "label": "XIXe siècle", "range": "1789 → 1914"},
    {"id": "contemporain", "label": "Époque contemporaine", "range": "1914 → aujourd'hui"}
]

STATUS_LABELS = {
    "fait_historique": {"label": "Fait historique attesté", "description": "Sources historiques sérieuses"},
    "tradition": {"label": "Tradition ou croyance", "description": "Pratique ou interprétation culturelle"},
    "legende": {"label": "Conte ou légende", "description": "Non historiquement démontré"},
    "hypothese": {"label": "Hypothèse ou controverse", "description": "Les sources divergent"}
}
