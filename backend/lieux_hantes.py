"""Lieux réputés hantés — attestés dans les traditions locales,
avec toujours la distinction : histoire attestée du lieu / tradition de hantise / témoignages sourcés.
"""

LIEUX_UNIVERSE = {
    "id": "lieux-hantes",
    "title": "Les lieux hantés",
    "subtitle": "Fiches techniques et témoignages sourcés",
    "description": "Châteaux, cimetières, forêts, abbayes réputés hantés. On documente d'abord l'histoire attestée du lieu, puis on rassemble les traditions de hantise et les témoignages publiés — sans jamais présenter une légende comme un fait.",
    "image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg"
}

LIEUX_DOSSIERS = [
    {"id": "france", "label": "En France"},
    {"id": "monde", "label": "Dans le monde"},
]


LIEUX_STORIES = [
    # ============ FRANCE ============
    {
        "id": "lieu-brissac",
        "universe": "lieux-hantes",
        "dossier": "france",
        "title": "Château de Brissac : la Dame Verte",
        "subtitle": "Le plus haut château habitable de France, réputé le plus hanté",
        "status": "tradition",
        "era": "moyen-age",
        "era_label": "XIe siècle",
        "year": 1050,
        "region": "Maine-et-Loire, France",
        "coords": [47.3557, -0.4432],
        "hero_image": "https://images.unsplash.com/photo-1786341540187-4ee121cecc67",
        "place_type": "Château",
        "excerpt": "Sept étages, 204 pièces, 900 ans d'histoire. Et une dame en robe verte, aperçue depuis le XVe siècle dans la tour du chapelet.",
        "specs": [
            {"label": "Type", "value": "Château fort remanié en résidence"},
            {"label": "Bâti", "value": "XIe siècle, transformé au XVIIe"},
            {"label": "Statut", "value": "Monument historique, propriété privée, visitable"},
            {"label": "Phénomène rapporté", "value": "La Dame Verte, gémissements dans la tour"},
            {"label": "Première mention écrite", "value": "XVIIe siècle (chroniques familiales)"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "Brissac est bâti au XIe siècle par Foulques Nerra, comte d'Anjou. Racheté au XVe siècle par Pierre de Brézé, sénéchal du roi, puis passé à la famille de Cossé-Brissac qui le possède toujours.",
                    "Fait historique attesté : Jacques de Brézé, fils de Pierre, découvre en 1462 sa femme **Charlotte de France** (fille illégitime légitimée du roi Charles VII) au lit avec son écuyer Pierre de Lavergne. Il les tue tous les deux sur place. Le crime est jugé, Jacques est incarcéré, la lignée est déshéritée. Ce meurtre est documenté par les archives judiciaires."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "Depuis au moins le XVIIe siècle, la famille de Cossé-Brissac transmet la tradition de la « Dame Verte » — Charlotte de France, aperçue vêtue de sa robe verte, marchant dans la tour du chapelet où elle aurait été tuée. Elle serait particulièrement visible les nuits d'orage.",
                    "Des visiteurs rapportent également des gémissements et des bruits de chaînes provenant de la même tour."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "La marquise de Brissac (années 1950) a plusieurs fois évoqué publiquement la présence, sans en faire spectacle : *« C'est une habitante comme une autre. »*",
                    "Le château est aujourd'hui ouvert aux visites nocturnes thématiques — reconnaissons que cela alimente l'industrie de la légende autant que la légende elle-même. La distinction entre témoignage sincère et récit touristique est ici particulièrement mince."
                ]
            }
        ],
        "sources": [
            "Archives départementales du Maine-et-Loire, série B (procès Brézé)",
            "Château de Brissac — visite officielle et livret édité",
            "Édouard Brasey, Guide des lieux hantés de France, 2003"
        ],
        "tags": ["château", "dame verte", "brissac", "france"]
    },
    {
        "id": "lieu-mortemer",
        "universe": "lieux-hantes",
        "dossier": "france",
        "title": "Abbaye de Mortemer : quatre fantômes recensés",
        "subtitle": "La plus ancienne abbaye cistercienne de Normandie",
        "status": "tradition",
        "era": "moyen-age",
        "era_label": "XIIe siècle",
        "year": 1134,
        "region": "Eure, Normandie, France",
        "coords": [49.3536, 1.5286],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "place_type": "Abbaye (ruines)",
        "excerpt": "Fondée en 1134 par Henri Ier d'Angleterre. Ravagée à la Révolution. Depuis, quatre apparitions récurrentes selon la tradition locale — dont une reine.",
        "specs": [
            {"label": "Type", "value": "Ruines d'abbaye cistercienne"},
            {"label": "Bâti", "value": "1134 (Henri Ier Beauclerc)"},
            {"label": "Statut", "value": "Monument historique, visitable"},
            {"label": "Phénomène rapporté", "value": "4 fantômes : Mathilde, moine blanc, moines rouges, loup-garou"},
            {"label": "Étang associé", "value": "Étang Sainte-Catherine"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "L'abbaye est fondée en 1134 par le roi Henri Ier d'Angleterre, dit Beauclerc, qui y installe une communauté cistercienne. Elle prospère jusqu'à la guerre de Cent Ans, puis décline. Elle est vendue comme bien national en 1791 et démantelée. Il n'en reste aujourd'hui que des ruines, un colombier, et le logis abbatial du XVIIe.",
                    "Fait attesté également : **l'impératrice Mathilde**, fille d'Henri Ier, aurait effectivement fréquenté Mortemer et y a peut-être été inhumée temporairement — les sources divergent. Elle est morte en 1167."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "La tradition normande recense quatre apparitions distinctes à Mortemer :",
                    "**Mathilde l'Emperesse** — apparue en robe blanche, elle chercherait la sépulture de son fils, Henri II Plantagenêt. Voir sa robe blanche annoncerait un mariage à venir ; sa robe rouge, un deuil ; sa robe noire, la trahison.",
                    "**Le moine blanc** — un cistercien qui erre dans la nef en ruine, priant.",
                    "**Les quatre moines rouges** — condamnés à errer pour avoir accueilli des révolutionnaires venus piller l'abbaye en 1792.",
                    "**Le loup-garou** — apparu dans les bois environnants à la pleine lune, associé à un moine du XVIIe qui aurait sombré dans la folie."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "L'abbaye organise depuis les années 1990 des visites nocturnes qui recueillent les témoignages des visiteurs. Un fonds photographique et un livre d'or existent sur place.",
                    "L'historien local Édouard Brasey y a mené plusieurs enquêtes documentaires (années 2000). Il classe Mortemer parmi les cas français où la tradition orale est la plus stable et la mieux transmise — sans que cela signifie qu'elle soit factuelle."
                ]
            }
        ],
        "sources": [
            "Édouard Brasey, La France mystérieuse, 2000",
            "Abbaye de Mortemer — dossier de visite (association gestionnaire)",
            "Musée normand des traditions populaires, Rouen"
        ],
        "tags": ["abbaye", "mortemer", "normandie", "mathilde"]
    },
    {
        "id": "lieu-broceliande",
        "universe": "lieux-hantes",
        "dossier": "france",
        "title": "Forêt de Brocéliande : Merlin, Viviane et les portes du monde",
        "subtitle": "La forêt de Paimpont, cœur de la matière de Bretagne",
        "status": "legende",
        "era": "moyen-age",
        "era_label": "XIIe siècle",
        "year": 1180,
        "region": "Ille-et-Vilaine, Bretagne, France",
        "coords": [48.0125, -2.1731],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "place_type": "Forêt",
        "excerpt": "9000 hectares de forêt, autour du village de Paimpont. Depuis Chrétien de Troyes, on y localise le tombeau de Merlin, la fontaine de Barenton et le Val sans retour.",
        "specs": [
            {"label": "Type", "value": "Forêt de 9000 hectares"},
            {"label": "Nom moderne", "value": "Forêt de Paimpont"},
            {"label": "Statut", "value": "Espace naturel, sentiers balisés"},
            {"label": "Lieux mythiques", "value": "Tombeau de Merlin, Fontaine de Barenton, Val sans retour, Hotié de Viviane"},
            {"label": "Première mention", "value": "Roman de Rou, Wace, 1160"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "L'existence physique de la forêt de Paimpont est bien sûr attestée. Elle est mentionnée dès le VIe siècle sous le nom de *silva Broceliandis* dans plusieurs chartes.",
                    "Ce qui est également attesté : c'est **Chrétien de Troyes**, dans son *Yvain ou le Chevalier au Lion* (v. 1180), qui installe littérairement les aventures arthuriennes dans cette forêt bretonne précise. Wace, avant lui, avait mentionné la fontaine merveilleuse dans le *Roman de Rou* (1160), avouant qu'il y était allé chercher les merveilles… sans les trouver."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "Attention : la « hantise » de Brocéliande relève de la **mythologie littéraire médiévale**, pas de témoignages de fantômes au sens moderne. La forêt est peuplée, dans les récits, par :",
                    "**Merlin l'Enchanteur**, emprisonné pour l'éternité par la fée Viviane dans le *Hotié de Viviane*, un dolmen néolithique associé à la légende.",
                    "**Le Val sans Retour**, où Morgane retiendrait les chevaliers infidèles. Le site existe, c'est un vallon rocheux à l'entrée de la forêt.",
                    "**La fontaine de Barenton**, dont on dit que verser son eau sur le *perron* voisin déclenche un orage. Sites archéologiques néolithiques réels, connotations magiques anciennes."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "Contrairement aux châteaux hantés, Brocéliande produit surtout des **récits de traversée** : promeneurs racontant s'être perdus dans une clairière qui n'existait pas la fois d'avant, sensations d'être observés, sons de flûte inexplicables. Ces récits sont rassemblés depuis le XIXe siècle par les folkloristes bretons (Jean-Pierre Le Scouëzec, Yann Brekilien).",
                    "La forêt reste un site touristique majeur. Il est difficile de démêler l'expérience réelle d'une forêt dense et de l'anticipation nourrie par les récits. Beaucoup de visiteurs viennent *pour* vivre ce qu'ils ont lu."
                ]
            }
        ],
        "sources": [
            "Chrétien de Troyes, Yvain ou le Chevalier au Lion, 1180",
            "Yann Brekilien, La Bretagne des mystères, 1970",
            "Jean Markale, Brocéliande et l'énigme du Graal, 2000"
        ],
        "tags": ["brocéliande", "bretagne", "merlin", "forêt"]
    },
    {
        "id": "lieu-pere-lachaise",
        "universe": "lieux-hantes",
        "dossier": "france",
        "title": "Père-Lachaise : la tombe qu'on touche pour retrouver l'amour",
        "subtitle": "Le plus grand cimetière de Paris et ses pèlerinages secrets",
        "status": "tradition",
        "era": "xixe",
        "era_label": "XIXe siècle",
        "year": 1804,
        "region": "Paris, France",
        "coords": [48.8619, 2.3939],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "place_type": "Cimetière",
        "excerpt": "43 hectares, 70 000 sépultures, un million de visiteurs par an. Certaines tombes reçoivent chaque jour des offrandes précises — pour l'amour, pour la chance, pour parler aux morts.",
        "specs": [
            {"label": "Type", "value": "Cimetière municipal parisien"},
            {"label": "Fondé", "value": "1804 par Napoléon Ier"},
            {"label": "Statut", "value": "Ouvert au public, tombes protégées"},
            {"label": "Phénomènes rapportés", "value": "Kardec (spiritisme), Victor Noir (fertilité), Jim Morrison (offrandes)"},
            {"label": "Visiteurs annuels", "value": "~3 millions"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "Le Père-Lachaise est créé en 1804 par Napoléon. Difficulté initiale : les Parisiens n'y viennent pas (trop excentré). Pour l'accréditer, l'administration y fait transférer solennellement les restes de La Fontaine, Molière, Héloïse et Abélard en 1817. Le succès est immédiat.",
                    "Attesté également : le cimetière abrite les tombes d'Alan Kardec (codificateur du spiritisme, mort 1869), de Victor Noir (journaliste tué en duel par le prince Pierre Bonaparte en 1870, sculpture en bronze allongé), et de Jim Morrison (chanteur des Doors, mort 1971 à Paris)."
                ]
            },
            {
                "title": "Les traditions de pèlerinage",
                "paragraphs": [
                    "**Tombe d'Allan Kardec** : chaque jour, des dizaines de spirites y déposent fleurs et messages. Certains pratiquent l'imposition des mains sur le buste. La tombe est aujourd'hui la plus visitée du cimetière — plus que celle de Morrison. C'est un fait mesurable : les gardiens l'attestent.",
                    "**Tombe de Victor Noir** : la sculpture d'Aimé-Jules Dalou représente le journaliste étendu, avec une bosse au niveau de l'entrejambe qui est devenue objet de rituel. Les femmes qui souhaitent tomber enceintes, ou trouver l'amour, y déposent un baiser et une fleur dans le chapeau à côté. La zone est visiblement polie par l'usage — le bronze y a la couleur du neuf.",
                    "**Tombe de Jim Morrison** : longtemps vandalisée par ses fans, elle est aujourd'hui protégée par un cordon. Les visiteurs y déposent bouteilles, joints, poèmes."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "Ce ne sont pas ici des témoignages de fantômes, mais de rituels vivants. Le Père-Lachaise n'est pas « hanté » au sens gothique. Il est **traversé** par des pratiques spirites, superstitieuses et amoureuses, transmises depuis un siècle et demi. C'est un des rares cimetières au monde où le rapport aux morts est aussi tactile, aussi présent."
                ]
            }
        ],
        "sources": [
            "Conservation du cimetière du Père-Lachaise — mairie de Paris",
            "Bertrand Beyern, Guide des tombes d'hommes célèbres, 2010",
            "Musée Carnavalet — collection sur le spiritisme parisien"
        ],
        "tags": ["père-lachaise", "cimetière", "paris", "spiritisme"]
    },
    {
        "id": "lieu-combourg",
        "universe": "lieux-hantes",
        "dossier": "france",
        "title": "Château de Combourg : le chat noir dans l'escalier",
        "subtitle": "Le château d'enfance de Chateaubriand — et son ancêtre à la jambe de bois",
        "status": "tradition",
        "era": "moyen-age",
        "era_label": "XIe siècle, remanié XIVe",
        "year": 1050,
        "region": "Ille-et-Vilaine, Bretagne, France",
        "coords": [48.4108, -1.7472],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "place_type": "Château",
        "excerpt": "Chateaubriand a passé son enfance dans ce château breton. Il en a raconté la solitude, la peur nocturne, et le chat noir qui, dit-il, était son ancêtre.",
        "specs": [
            {"label": "Type", "value": "Château fort médiéval"},
            {"label": "Bâti", "value": "XIe siècle, tours ajoutées XIVe-XVe"},
            {"label": "Statut", "value": "Monument historique, visitable"},
            {"label": "Résident célèbre", "value": "Chateaubriand (enfance)"},
            {"label": "Phénomène rapporté", "value": "Chat noir de l'escalier, comte à la jambe de bois"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "Combourg est construit au XIe siècle par les Guitté, tenu ensuite par plusieurs familles avant d'être acheté en 1761 par **René de Chateaubriand**, comte, corsaire malouin enrichi dans le commerce (esclavagiste également, il faut le dire), père du futur écrivain François-René.",
                    "François-René de Chateaubriand y a effectivement passé les années 1777-1786, adolescence puis jeunesse. Il en a laissé une description magnifique dans les *Mémoires d'outre-tombe* : silence pesant, dîners glacés en famille, escaliers hantés par les *ombres du passé*. Le château est toujours propriété de la famille."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "Deux apparitions récurrentes selon la tradition familiale et locale :",
                    "**Le comte à la jambe de bois** — un ancêtre Chateaubriand mort au combat, dont on entendrait la jambe de bois heurter les dalles dans les couloirs. Le comte serait particulièrement visible dans la tour du Chat.",
                    "**Le chat noir** — un chat noir qui hante l'escalier de la tour, réputé être l'ancêtre transformé. Chateaubriand lui-même mentionne l'histoire dans ses *Mémoires d'outre-tombe*, en la présentant comme une plaisanterie familiale — mais une plaisanterie qui ne le fait pas rire quand il est seul, la nuit."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "Le témoignage central est celui de Chateaubriand lui-même, dans les *Mémoires d'outre-tombe* (livre III) : *« La tour du Chat, qu'habitait le fantôme d'un comte de Chateaubriand à la jambe de bois, avait tellement effrayé une bonne des dames de Bourdeaux, chargée de garder les petits enfants, qu'elle se sauva de nuit, et resta convalescente huit jours. »*",
                    "Il n'y a pas de raison de douter que Chateaubriand a vraiment senti la peur — mais pour l'existence effective du fantôme, on est dans la même situation que pour toute légende familiale : la tradition existe, le fait ne peut être vérifié."
                ]
            }
        ],
        "sources": [
            "Chateaubriand, Mémoires d'outre-tombe, éd. de la Pléiade",
            "Château de Combourg — livret officiel",
            "Jean-Paul Clément, Chateaubriand, biographie, 2003"
        ],
        "tags": ["combourg", "chateaubriand", "bretagne", "chat noir"]
    },

    # ============ MONDE ============
    {
        "id": "lieu-tour-londres",
        "universe": "lieux-hantes",
        "dossier": "monde",
        "title": "La Tour de Londres : Anne Boleyn tient sa tête",
        "subtitle": "Neuf siècles de captifs, une des concentrations d'apparitions les plus documentées d'Europe",
        "status": "tradition",
        "era": "moyen-age",
        "era_label": "1078",
        "year": 1078,
        "region": "Londres, Royaume-Uni",
        "coords": [51.5081, -0.0759],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "place_type": "Forteresse royale",
        "excerpt": "Bâtie par Guillaume le Conquérant. Prison royale pendant sept siècles. Des dizaines d'exécutions, plusieurs enquêtes officielles de garde sur des apparitions.",
        "specs": [
            {"label": "Type", "value": "Forteresse royale et ancienne prison"},
            {"label": "Bâtie", "value": "1078 (Guillaume le Conquérant)"},
            {"label": "Statut", "value": "Palais royal, joyaux de la Couronne, UNESCO"},
            {"label": "Phénomènes rapportés", "value": "Anne Boleyn, Lady Jane Grey, deux princes, Thomas Becket, ours spectral"},
            {"label": "Enquête interne", "value": "Rapports d'incidents tenus par les Yeomen Warders"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "Guillaume le Conquérant bâtit la White Tower en 1078. La forteresse sert de palais royal, arsenal, ménagerie, prison, lieu d'exécution pendant plus de huit siècles.",
                    "**Exécutions attestées sur le site** : Anne Boleyn (1536, deuxième femme d'Henri VIII, décapitée), Catherine Howard (1542, cinquième femme d'Henri VIII), Lady Jane Grey (1554, reine pendant neuf jours), Thomas Cromwell, Guy Fawkes… Plus les deux **Princes de la Tour** (Édouard V et Richard, disparus en 1483 — leurs restes ont peut-être été retrouvés en 1674, l'analyse ADN reste refusée par la Couronne)."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "**Anne Boleyn** — l'apparition la mieux documentée. Décrite comme marchant, tête sous le bras, dans la Chapelle Royale de Saint-Pierre-aux-Liens et le corridor voisin. Signalée régulièrement depuis le XIXe siècle par les Yeomen Warders.",
                    "**Les deux Princes** — silhouettes d'enfants aperçues main dans la main dans les couloirs de la Bloody Tower.",
                    "**Lady Jane Grey** — apparaîtrait sur le mur d'enceinte le jour anniversaire de son exécution (12 février).",
                    "**L'ours spectral** — reste de l'ancienne ménagerie royale, aurait causé la mort d'un garde en 1815 selon un rapport de la Tour."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "La Tour tient un registre officiel des incidents étranges, en usage depuis le XIXe siècle. Il est consultable sous conditions. Les Yeomen Warders, qui vivent avec leur famille dans l'enceinte, sont sélectionnés parmi les vétérans de l'armée britannique et sont notoirement peu portés à l'affabulation.",
                    "Cas emblématique : en 1817, le gardien-major Edmund Lenthal Swifte affirme avoir vu, avec sa famille, une forme cylindrique lumineuse traverser leur salle à manger avant de disparaître dans un mur. Le témoignage est publié dans *Notes and Queries* en 1860."
                ]
            }
        ],
        "sources": [
            "Historic Royal Palaces — Tower of London incident logs",
            "Edmund Lenthal Swifte, letter to Notes and Queries, 1860",
            "Peter Underwood, Ghosts of the Tower of London, 1970"
        ],
        "tags": ["tour de londres", "anne boleyn", "angleterre", "royauté"]
    },
    {
        "id": "lieu-glamis",
        "universe": "lieux-hantes",
        "dossier": "monde",
        "title": "Château de Glamis : la chambre secrète des Bowes-Lyon",
        "subtitle": "Le château le plus mystérieux d'Écosse, résidence de la Reine Mère",
        "status": "tradition",
        "era": "moyen-age",
        "era_label": "XIVe siècle",
        "year": 1372,
        "region": "Angus, Écosse",
        "coords": [56.6167, -3.0],
        "hero_image": "https://images.unsplash.com/photo-1535905557558-afc4877a26fc",
        "place_type": "Château",
        "excerpt": "La reine Élisabeth II y a passé son enfance. Sa mère y est née. Et depuis des siècles, la famille Bowes-Lyon garde le secret d'une chambre murée que seuls trois hommes vivants connaîtraient.",
        "specs": [
            {"label": "Type", "value": "Château médiéval remanié"},
            {"label": "Bâti", "value": "XIVe siècle, modifications jusqu'au XVIIe"},
            {"label": "Famille", "value": "Bowes-Lyon (comtes de Strathmore)"},
            {"label": "Lien royal", "value": "Enfance de la Reine Mère (1900-2002)"},
            {"label": "Phénomènes rapportés", "value": "Chambre secrète, monstre de Glamis, dame grise"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "Glamis appartient à la famille Lyon (devenue Bowes-Lyon en 1767) depuis 1372. C'est le lieu de naissance d'Élisabeth Bowes-Lyon (1900-2002), future Reine Mère du Royaume-Uni. La princesse Margaret y est également née (1930). La reine Élisabeth II y a passé de longs séjours d'enfance.",
                    "Le château apparaît dans *Macbeth* de Shakespeare (Macbeth est baron de Glamis). Historiquement, le vrai Macbeth n'y a jamais vécu — la pièce a fusionné des lieux."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "**La chambre secrète** — la tradition affirme qu'une chambre existe quelque part dans le château, murée depuis le début du XIXe siècle. Seuls **le comte régnant, son héritier et le majordome familial** en connaîtraient l'emplacement, transmise le jour de la majorité de l'héritier. Motif : elle abriterait le secret d'un enfant né monstrueux au début du XIXe, gardé caché.",
                    "**Le monstre de Glamis** — versions multiples : premier-né des Bowes-Lyon vers 1821, difforme, gardé enfermé, ayant vécu jusqu'à un âge très avancé. Le récit apparaît dans la presse à sensation britannique dès les années 1880.",
                    "**La Dame Grise** — apparaîtrait dans la chapelle. Serait Janet Douglas, veuve du 6e Lord Glamis, brûlée pour sorcellerie en 1537 sur ordre de Jacques V d'Écosse. Fait attesté : Janet Douglas a effectivement été exécutée."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "Sur la chambre secrète : les comtes de Strathmore ont plusieurs fois été interrogés à ce sujet. Le 13e comte, Claude Bowes-Lyon (père de la Reine Mère), a répondu à une invitée : *« Si vous saviez la vérité, vous vous mettriez à genoux et remercieriez Dieu que ce ne soit pas la vôtre. »* Cette phrase, rapportée par plusieurs sources concordantes, est probablement authentique. Elle ne prouve rien de son contenu.",
                    "Sur la Dame Grise : plusieurs invités du château au XXe siècle rapportent l'avoir vue dans la chapelle, y compris Mrs. Wingfield, cousine de la Reine Mère, dans les années 1950."
                ]
            }
        ],
        "sources": [
            "Peter Underwood, A Gazetteer of Scottish and Irish Ghosts, 1973",
            "Correspondance privée de Claude Bowes-Lyon (fonds Glamis)",
            "The Times, 1898 — article sur les Strathmore"
        ],
        "tags": ["glamis", "écosse", "royauté", "chambre secrète"]
    },
    {
        "id": "lieu-poveglia",
        "universe": "lieux-hantes",
        "dossier": "monde",
        "title": "Poveglia : l'île fermée au public de Venise",
        "subtitle": "Lazaret, asile psychiatrique, dépotoir de la peste. Personne n'y débarque plus.",
        "status": "tradition",
        "era": "renaissance",
        "era_label": "XVe-XXe siècle",
        "year": 1500,
        "region": "Lagune de Venise, Italie",
        "coords": [45.3811, 12.3319],
        "hero_image": "https://images.pexels.com/photos/16811482/pexels-photo-16811482.jpeg",
        "place_type": "Île",
        "excerpt": "7 hectares dans la lagune de Venise. Utilisée comme lazaret pendant les grandes épidémies, puis asile psychiatrique jusqu'en 1968. Depuis, fermée au public.",
        "specs": [
            {"label": "Type", "value": "Île de lagune"},
            {"label": "Superficie", "value": "7 hectares"},
            {"label": "Usages historiques", "value": "Lazaret (XIVe-XVIIIe), asile (1922-1968)"},
            {"label": "Statut", "value": "Propriété d'État italien, accès interdit"},
            {"label": "Phénomènes rapportés", "value": "Cris, ombres, refus des marins locaux d'y débarquer"},
        ],
        "sections": [
            {
                "title": "Les faits historiques attestés",
                "paragraphs": [
                    "Poveglia est habitée depuis le IXe siècle, puis désertée. À partir du XIVe siècle, la République de Venise l'utilise comme **lazaret** — poste de quarantaine pour les navires suspects de porter la peste. Les malades y sont débarqués, souvent y meurent, y sont enterrés dans des fosses communes.",
                    "L'usage se prolonge sporadiquement jusqu'au XVIIIe siècle. En 1922, l'île accueille un **hôpital psychiatrique** pour malades chroniques, fermé en 1968 après des scandales sur les traitements. Depuis, l'île appartient à l'État italien, qui interdit l'accès pour raisons de sécurité (bâtiments en ruine).",
                    "Une estimation prudente évalue à plusieurs milliers le nombre de morts inhumés à Poveglia sur six siècles. Les carottages géologiques confirment des couches de cendres humaines dans le sol."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "Les pêcheurs de la lagune évitent traditionnellement Poveglia. La tradition orale vénitienne rapporte que les filets qui accrochent le sol de l'île en remontent des ossements. C'est probablement vrai — géologiquement, l'île est effectivement un ossuaire.",
                    "Les récits centraux évoquent le fantôme d'un médecin de l'asile, qui se serait suicidé dans le clocher, en jetant par la fenêtre après avoir été « attaqué par les esprits ». L'événement est mentionné dans plusieurs rapports d'époque mais reste flou."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "Poveglia est régulièrement classée dans les palmarès des « lieux les plus hantés du monde » par la presse anglo-saxonne. Il faut le dire clairement : ces classements relèvent davantage du tourisme sombre que de l'enquête documentée.",
                    "Ce qui est réel : le refus persistant des Vénitiens locaux d'y débarquer, et l'interdiction officielle qui, à défaut d'attester une hantise, préserve son mystère."
                ]
            }
        ],
        "sources": [
            "Archivio di Stato di Venezia — registres sanitaires XVIe-XVIIIe",
            "Nelli-Elena Vanzan Marchini, I mali e i rimedi della Serenissima, 1995",
            "RAI, documentaires sur les lazarets vénitiens"
        ],
        "tags": ["poveglia", "venise", "peste", "asile"]
    },
    {
        "id": "lieu-aokigahara",
        "universe": "lieux-hantes",
        "dossier": "monde",
        "title": "Aokigahara : la forêt au pied du Fuji",
        "subtitle": "35 km² de forêt sur coulée de lave, au silence anormal",
        "status": "tradition",
        "era": "antiquite",
        "era_label": "après 864",
        "year": 864,
        "region": "Yamanashi, Japon",
        "coords": [35.4691, 138.6867],
        "hero_image": "https://images.pexels.com/photos/37246081/pexels-photo-37246081.jpeg",
        "place_type": "Forêt",
        "excerpt": "Formée il y a 1200 ans sur une coulée de lave du mont Fuji. Sol volcanique dense, boussoles perturbées, silence acoustique surprenant. Et une tradition sombre.",
        "specs": [
            {"label": "Type", "value": "Forêt sur coulée de lave"},
            {"label": "Superficie", "value": "~35 km²"},
            {"label": "Sol", "value": "Basalte poreux — absorbe le son, perturbe les boussoles"},
            {"label": "Origine", "value": "Éruption du Fuji, 864 après J.-C."},
            {"label": "Tradition", "value": "Territoire des yūrei (esprits errants)"},
        ],
        "sections": [
            {
                "title": "Les faits attestés",
                "paragraphs": [
                    "Aokigahara — littéralement « la plaine des arbres bleus » — s'étend sur environ 35 km² à la base nord-ouest du mont Fuji. La forêt s'est établie sur une coulée de lave issue de l'éruption majeure de 864.",
                    "**Fait naturel attesté** : le sol basaltique poreux a des propriétés acoustiques particulières. Il absorbe une grande partie des sons ambiants, ce qui produit une impression de silence anormal à l'intérieur de la forêt, souvent notée par les visiteurs. **Le magnétisme naturel des roches volcaniques perturbe également les boussoles**, ce qui est vrai et documenté (fait par plusieurs études géologiques japonaises).",
                    "La densité végétale rend la navigation difficile même en plein jour. Il est facile de s'y perdre."
                ]
            },
            {
                "title": "La tradition de hantise",
                "paragraphs": [
                    "Dans la tradition folklorique japonaise, Aokigahara est le territoire des **yūrei** — esprits des morts qui n'ont pas pu accéder au repos, souvent ceux qui sont morts violemment ou seuls. La forêt aurait été historiquement le lieu d'*ubasute*, cette pratique légendaire (probablement plus mythique qu'attestée) d'abandon des vieillards dans les périodes de famine.",
                    "Le lien avec les suicides — plus contemporain — a été amplifié par un roman à succès de Seichō Matsumoto, *Tour de vagues* (1960), dont un personnage s'y donne la mort. Depuis, la forêt attire un flux tragique. Les autorités japonaises tiennent désormais des chiffres qu'elles cessent de publier depuis 2010, précisément pour rompre le cycle."
                ]
            },
            {
                "title": "Témoignages rapportés",
                "paragraphs": [
                    "Les gardes forestiers et bénévoles qui patrouillent Aokigahara — pour prévenir les suicides et retrouver les personnes perdues — rapportent régulièrement des sensations d'oppression, d'être suivis, d'entendre des voix. Ces témoignages sont recueillis dans plusieurs documentaires japonais et occidentaux.",
                    "Il faut préciser : les conditions objectives (silence anormal, désorientation, boussole défaillante, vue limitée) suffiraient à créer chez tout marcheur non préparé un état psychologique inconfortable. La tradition surnaturelle vient donner un cadre à cette expérience, elle ne la produit pas nécessairement."
                ]
            }
        ],
        "sources": [
            "Yamanashi Prefecture — géologie du Fuji-Hakone-Izu",
            "Seichō Matsumoto, Tour de vagues, 1960",
            "Rob Gilhooly, articles sur Aokigahara dans The Japan Times"
        ],
        "tags": ["aokigahara", "japon", "fuji", "yūrei"]
    }
]
