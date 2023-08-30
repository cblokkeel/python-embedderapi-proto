# Que faut-il savoir sur ChatGPT ?

Created: June 25, 2023 10:46 PM
Tags: DIGITAL
Read: Yes
URL: https://15marches.substack.com/p/que-faut-il-savoir-sur-chatgpt?utm_medium=email
Authors: 15 Marches
Durée: 30
Ranking: 4-Stars

👨‍🚀 Tous les mardis, Stéphane décrypte **l’impact des technologies sur l’économie et la société**... En savoir plus sur cette lettre : [À propos](https://15marches.substack.com/about)

Vous êtes 6 636 abonnés à recevoir cette lettre. Bienvenue aux nouvelles et nouveaux et merci aux autres pour leur fidélité.

Vous avez découvert cette lettre par un autre canal ? Abonnez-vous pour la recevoir directement dans votre boîte :

## 🧭 De quoi allons-nous parler

Je traîne souvent les pieds pour étudier les “dernières technologies à la mode”. J’ai passé mon tour sur la blockchain, les NFT et le Metaverse. J’ai à peine regardé le dernier produit Apple. Sans doute pour de mauvaises raisons, mais également car cela ne touchait pas de près ma propre activité.

Autant dire que pour ChatGPT, je ne pouvais pas passer à côté d’une solution qui 1/ met à disposition de tous une information encyclopédique

[1](https://15marches.substack.com/p/que-faut-il-savoir-sur-chatgpt?utm_medium=email#footnote-1-127127048)

2/ rédige des textes convenables dans toutes les langues 3/ est disponible gratuitement et en quelques clics 4/ attire à elle une grande quantité de développeurs. Quand votre métier est d’observer ce qui se passe, faire le lien entre des tendances et imaginer les moyens d’en tirer parti, vous ne pouvez pas rester indifférent à une telle innovation.

Je n’ai pas la prétention de comprendre dans le détail comment fonctionnent les réseaux neuronaux et parmi eux la famille des *Generative Pretrained Transformers*, appelés communément GPT. J’aimerais simplement **partager quelques éléments qu’il me semble important de saisir à ce moment précis où ces solutions, qui existent depuis des décennies à des stades moins aboutis, prennent une autre dimension**. Je parlerai ici des modèles de génération de langage, mais je m’intéresse également aux modèles de génération d’images dans le cadre de la préparation d’un [Mardi Graphique](https://www.pollenstudio.fr/identite/les-mardis-graphiques/) que j’organise avec ma femme pour la rentrée. Ce sera sans doute pour un prochain post.

J’espère que les expertes et experts du domaine pardonneront mes probables imprécisions et erreurs. Vous trouverez des ressources beaucoup plus complètes (et justes !) dans la rubrique suivante…

![Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fc1899a29-3fc0-4079-a5b6-9a8e825e73e1_708x712.png](Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fc1899a29-3fc0-4079-a5b6-9a8e825e73e1_708x712.png)

*Visualisation des tâches réalisées par un réseau de neurones entraîné pour reconnaître les chiens des chats. J’ai perdu mon chat alors je voulais mettre des photos de chat* 😢*. Source : Stephen Wolfram (lien plus bas)*

## 🎯 Cette semaine

*À chaque lettre un nouveau sujet décrypté : Comment fonctionne ChatGPT ?*

Comme le dit [Xavier de la Porte](https://www.radiofrance.fr/franceinter/podcasts/le-code-a-change/le-code-a-change-7051369) : un GPT est “une machine qui produit du texte. **Une machine mathématique qui se nourrit du langage humain et qui donne à lire du langage humain**”. C’est ce croisement entre deux disciplines - mathématiques et littérature - qui passionne les foules.

Essayons de comprendre pas à pas de quoi il s’agit avant de se demander comment s’en servir et ce que cela va changer.

### De GPT à ChatGPT

Au commencement il y a des **modèles linguistiques**, développés pour générer par exemple des traductions de texte automatiques. Les évolutions de ces modèles ont suivi celles des capacités de calcul informatique, puis ont connu récemment une croissance exponentielle avec les **modèles dits conversationnels**, qui impliquent de vrais humains pour “renforcer” leurs capacités.

Prenez un modèle mathématique et “nourrissez-le” avec des **centaines de milliards de mots provenant de textes aspirés sur le web, Wikipedia, Reddit et dans des livres numérisés**. Découpez ces textes non pas en mots mais en “tokens” et traduisez-les en suites de chiffres.

![Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2F255ed33b-78fb-435c-a410-9d4a5c817ad0_2234x1278.png](Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2F255ed33b-78fb-435c-a410-9d4a5c817ad0_2234x1278.png)

*Visuel tiré de la conférence d’Andrew Karpathy - lien plus bas.*

Laissez tourner le modèle pour qu’il distingue les infinies possibilités de “mariage” entre ces suites de chiffres. Et recommencez.

> “Chaque “mot” généré est le résultat d’une exploration spatiale qui tient à la fois compte des voisins immédiats du mot (qui vont notamment déterminer sa syntaxe), du sens général de la conversation (la fenêtre contextuelle de 3000 mots) et de tout le vaste imaginaire des mots possibles dans cette langue (…)
> 
> 
> Les réseaux de neurones peuvent réévaluer les données initiales à la lumière de nouvelles observations grâce à une boucle de rétroaction (*feedback loop*). (….)
> 
> Au lieu de se limiter à une lecture flottante de ce qui précède et d’en retirer une vague notion générale du sujet du texte, les modèles *transformers* modélisent les interactions entre les mots précédents. Ils ont une compréhension intuitive de la syntaxe et de la composition de la phrase qui fait défaut dans tous les modèles qui l’ont précédé” (Pierre-Carl Langlais, voir lien dans la rubrique suivante).
> 

Nous sommes donc face à un modèle qui **écrit des textes en calculant la probabilité que chaque mot soit le bon, probabilité basée sur des centaines de milliards de paramètres** (175 pour être précis pour GPT-3).

Formidable non ?

Le soucis est que ce modèle n’a aucune idée de ce qu’il raconte. **Il ne réfléchit pas, il ne crée pas : il assemble des mots selon leur probabilité d’être les bons mots** en utilisant sa formidable mémoire et la “mécanique” des réseaux neuronaux. En clair, il peut parfaitement écrire que Napoléon a gagné la bataille de Waterloo ou que les Bretons aiment le beurre doux si cela lui paraît la probabilité la plus sûre en fonction du contexte. Un modèle de ce type testé par Microsoft à partir des données de Twitter avait rapidement produit des textes racistes et xénophobes. Ce qui explique que ces solutions ne sont pas accessibles au public.

![Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fc7982769-631d-4de4-a625-e8ddab0d0041_2420x1302.png](Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fc7982769-631d-4de4-a625-e8ddab0d0041_2420x1302.png)

*Support de la conférence de Andrew Karpathy : lien plus bas*

D’où l’obligation pour les chercheurs de faire entrer de bons vieux humains dans le dispositif. On parle d’*alignement*, une phase indispensable pour “humaniser” ces outils. Ce sont les trois étapes représentées par les trois colonnes de droite du visuel ci-dessus : amélioration supervisée, modèle de récompense et apprentissage renforcé.

Elles représentent l’évolution des GPT vers *InstructGPT*, aussi appelé ChatGPT car il permet à l’utilisateur de converser avec la machine. Avec ce dispositif, on va **cumuler la puissance de calcul et la mémoire des GPT avec un “renforcement” humain organisé pour améliorer les résultats.** Ce renforcement deviendra à son tour une ressource intégrée aux calculs probabilistes grâce aux réseaux de neurones. C’est l’ « apprentissage renforcé par feed-back humain » ou RLHF en anglais.

Je vous renvoie aux ressources listées dans la rubrique suivante pour le détail de ces renforcements, mais retenez qu’ils mobilisent fortement de vrais humains pour leur faire :

- rédiger les “bonnes réponses” à des questions
- classer les réponses données par le modèle et éliminer les plus choquantes
- rédiger des “prompts”, des consignes ou *briefs* correspondant à certaines réponses.

**Ces éléments sont “réinjectés” dans le modèle** qui s’améliore au fur et à mesure et apprend de mieux en mieux à “imiter” les humains.

Le résultat est donc bien meilleur qu’avant le *human feedback*. Celui-ci permet aussi aux humains d’éliminer purement et simplement certains types de réponses pour éviter les contenus jugés choquants ou inappropriés. D’où certaines polémiques apparues entre fondateurs d’OpenAI, l’un des grands fournisseurs de ces solutions, autour de la **liberté d’expression** (du *transformer* dans ce cas précis). Retenez surtout que ces réponses ne sont en aucun cas « neutres » politiquement et moralement parlant.

Mais peut-on pour autant comparer ces réponses à des réponses humaines ?

Pour faire court : non.

![Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2F52e1d139-c65f-43db-868a-ebcebd4efdb4_1200x626.jpeg](Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2F52e1d139-c65f-43db-868a-ebcebd4efdb4_1200x626.jpeg)

![Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fcf3f7a90-8fcf-4db0-83d2-12e8062d9af3_1200x631.jpeg](Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fcf3f7a90-8fcf-4db0-83d2-12e8062d9af3_1200x631.jpeg)

Le modèle ne s’interroge pas sur la bonne méthode, il ne se demande pas si sa réponse a du sens, il ne va pas chercher de l’information dans des “sources sûres” pour vérifier. **Il ne se corrige pas car il ne sait pas ce qui est “vrai”.**

Le modèle se contente (même si c’est infiniment complexe) de reproduire un “comportement” c’est à dire une suite de mots en les choisissant selon leur probabilité, augmentée des “renforcements humains” c’est à dire la manière dont les humains lui ont conseillé de choisir.

### Système 1, système 2

Pour celles et ceux qui connaissent la distinction entre Système 1 et Système 2, ChatGPT fonctionnerait systématiquement comme notre Système 1 (“système cognitif qui fonctionne de manière automatique, involontaire, intuitive, rapide et demandant peu d'effort” selon [Wikipedia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_1_/_Syst%C3%A8me_2_:_Les_deux_vitesses_de_la_pens%C3%A9e)) et serait incapable de générer un raisonnement de type Système 2 ( qui “intervient dans la résolution de problèmes complexes, grâce à son approche plutôt analytique”). Pour les autres, disons que ChatGPT fonctionne comme votre cerveau quand on lui dit "4 par 3 ?”, mais il est incapable de raisonner comme votre cerveau quand on lui dit “48 par 38” ? Alors que vous vous allez prendre votre calculette poser calmement de tête 40 par 30, 8 par 30,… pour trouver le résultat. Ce que le modèle ne sait absolument pas faire.

Cette analogie avec les “deux vitesses de la pensée” génialement théorisées par Kahneman et Tversky s’arrête cependant là. En effet le Système 1 est aussi celui qui est à l’origine de la **créativité**, grâce aux associations intuitives qu’il permet. Mais pour les modèles génératifs, foin de créativité. Tout au plus notre *large langage model* est-il capable de produire des “hallucinations”, c’est à dire des résultats totalement faux mais qui “ont l’air vrais” vu qu’ils sont livrés dans une syntaxe et une rhétorique de bonne facture.

Pour éviter cela, il faut donc aider notre pauvre ChatGPT à réfléchir comme nous, un peu comme nous le ferions avec notre pré-ado de 13 ans en train de sécher devant un problème de maths ou de physique.

![Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fae55d792-d3f7-4c6b-889e-a39cc544718c_1200x630.jpeg](Que%20faut-il%20savoir%20sur%20ChatGPT%2027a2a19596614a809cc52f68e3223eea/https3A2F2Fsubstack-post-media.s3.amazonaws.com2Fpublic2Fimages2Fae55d792-d3f7-4c6b-889e-a39cc544718c_1200x630.jpeg)

Il faut lui donner du contexte - des exemples, des textes que vous déjà rédigés (surtout si vous souhaitez qu’il bosse à votre place 😎), puis lui préciser qu’il doit procéder étape par étape et enfin qu’il peut poser des questions s’il a besoin de plus d’information.

### Mes supers stagiaires

Ces modèles ont donc une capacité de mémoire très étendue mais une capacité de raisonnement très limitée. Ce qui est exactement le contraire de nous les humains.

Restons donc assez zen sur les capacités réelles de ces solutions à nous remplacer.

Comme le précise Andrew Karpathy l’un des co-fondateurs d’OpenAI : “ce sont des outils, pas des créatures. Ils effectuent des tâches, pas des emplois. **Ces modèles sont des outils pour effectuer votre travail plus efficacement**”.

Désolé de casser l’ambiance “robot blanc qui appuie sur des murs transparents couverts de chiffres” : vous n’allez pas perdre votre travail demain matin, sauf si votre travail consiste uniquement à mobiliser les capacités d’une armée d’enfants de 13 ans.

Considérez plutôt ces modèles comme vos stagiaires : jamais fatigués, capables d’aller chercher hyper vite toute l’information du monde, mais également capable de raconter n’importe quoi avec beaucoup d’assurance. Apprenez à les utiliser de la meilleure manière, en formulant clairement vos demandes, en examinant avec eux chaque étape de leur réponse, et en engageant un véritable *dialogue* constructif pour en obtenir le meilleur résultat et les aider à s’améliorer.

Les bases de la pédagogie en somme !

### Ne me parlez pas d’intelligence artificielle

Si vous êtes arrivé jusque là, vous avez peut-être remarqué que je n’ai pas utilisé une seule fois les termes “intelligence + artificielle”. C’est évidemment volontaire, car ces termes contribuent plus à entretenir des fantasmes de “robots blancs devant un mur de chiffres” qu’ils ne permettent de saisir le potentiel réel de ces modèles. Laissons là *l’intelligence*, dont l’explication reste encore largement méconnue, et parlons plus simplement de “mathématiques” ou de “statistiques” appliquées. C’est moins vendeur, mais comme disait Camus, “mal nommer les choses, c’est ajouter aux malheurs du monde”, qui n’en a pas besoin en ce moment.

Par ailleurs, les plus de 200 éditions de cette newsletter vous ont je l’espère convaincu qu’une technologie en soi n’a qu’un intérêt limité. Ce qui importe est **ce que des chercheurs et des entrepreneurs en feront**.

J’espère vous avoir donné envie d’explorer vous aussi les arcanes et le potentiel de ces solutions. Bonne exploration !

## 🧐 Et aussi

*Des ressources utiles en lien avec le sujet traité cette semaine.*

La vidéo d’Andrew Karpathy - [State of GPT - YouTube 43 minutes](https://www.youtube.com/watch?v=bZQun8Y4L2A)

Si vous souhaitez rentrer dans le détail du **fonctionnement réel de ChatGPT** en “soulevant le capot”, ces deux articles sont incontournables :

En français, par Pierre-Carles Langlais [ChatGPT : comment ça marche ?](https://scoms.hypotheses.org/1059)

En anglais, par Stephen Wolfram [What Is ChatGPT Doing … and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/?)

L’enjeu du **partage de la valeur pour les IA génératives** dans l’excellente newsletter de Louis-David Benayer - [Generative AI: how to prepare for the upcoming battle for value capture](https://www.louisdavidbenyayer.com/generative-ai-how-to-prepare-for-the-upcoming-battle-for-value-capture)

Qui est l’entreprise qui emploie les **modérateurs de ChatGPT** payés 2$ de l’heure ? [Sama, l'entreprise "éthique" derrière les scandales de modération au Kenya](https://www.france24.com/fr/%C3%A9co-tech/20230120-chatgpt-sama-l-entreprise-%C3%A9thique-derri%C3%A8re-les-scandales-de-mod%C3%A9ration-au-kenya?)

## 🤩 On a aimé

*Nos trouvailles de la semaine, en vrac et sans détour*

Écoutez mon associée Noémie Aubron répondre aux questions de Carole Méziat dans son podcast **On n’est pas des robots** (décidément). [Imaginer le futur du travail par la fiction - podcast 68 minutes](https://smartlink.ausha.co/onnestpasdesrobots/55-noemie-aubron-imaginer-le-futur-du-travail-via-la-fiction?)

Joli article sur l’**évolution effarante de la taille (et du poids) des voitures**. [Des voitures toujours plus grosses - RTBF](https://www.rtbf.be/article/11174850)

Une étude sur le fléau des **vols de vélos**. À transmettre à votre maire et au CPE du collège. [Le vol de vélos en France - ADMA](https://www.mobilites-actives.fr/etudes-techniques/8)

Pour finir, la tendance de fond qui devrait mobiliser toute notre attention - [Toujours très peu de naissances en France : moins de 1 800 bébés sont nés chaque jour - en moyenne - en avril, pour la première fois depuis le début des données en 1994](https://twitter.com/nicolasberrod/status/1662727901219807232?)

## 💬 La phrase

*“Le vrai problème de l’humanité est le suivant : nous avons des émotions paléolithiques, des institutions médiévales et des technologies de dieux”*. Edward Osborne Wilson

C’est terminé pour aujourd’hui !

À la semaine prochaine, n’hésitez pas à réagir.

*Si vous avez apprécié cette lettre, laissez-nous un* 💙 *pour nous encourager.*

Et n’oubliez pas la **seconde newsletter** de 15marches, Futur(s) :

👩🏻‍🚀 Tous les jeudis, mon associée Noémie raconte *les futurs possibles en fiction.*

[Abonnez-vous à Futur(s)](https://lamutante.substack.com/)

Stéphane

*Je suis [Stéphane Schultz](https://www.linkedin.com/in/stefschultz), de [15marches](https://15marches.fr/). Le jour je suis consultant, je prends des trains à travers les plaines. La nuit je lis et j’écris cette lettre.*

[1](https://15marches.substack.com/p/que-faut-il-savoir-sur-chatgpt?utm_medium=email#footnote-anchor-1-127127048)

En réalité cette affirmation s’avérera fausse, comme vous le découvrirez dans l’article (mise à jour)