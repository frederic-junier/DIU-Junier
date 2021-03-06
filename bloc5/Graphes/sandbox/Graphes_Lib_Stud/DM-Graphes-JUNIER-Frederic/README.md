# Activité _Notice de montage_



## Sujet choisi

Illustration du tri topologique dans un contexte et implémentation de ce tri comme méthode d'une classe d'objets graphes orientés.

L'ensemble des fichiers de cette activité sont disponibles
en ligne sur ce dépôt <https://github.com/frederic-junier/DIU-Junier/tree/master/bloc5/Graphes/sandbox/Graphes_Lib_Stud/DM-Graphes-JUNIER-Frederic>.

## Contenu de l'archive et mode d'emploi

* Une fois déballée, cette archive contient cinq fichiers :

.

├── activite-eleve.md

├── lib_graphes_junier_frederic.py

├── main_junier_frederic.py

├── Makefile

└── README.md

* `README.md` est ce fichier
* `lib_graphes_junier_frederic.py` est le fichier contenant la bibliothèque de graphes avec deux classes `Graph` et `DirectGraph` qui hérite de `Graph`. 
La documentation de la classe `DirectGraph` contient une série de tests d'exécution des différentes méthodes de classes sur quelques exemples. 
Ils peuvent être vérifiés automatiquement avec le module `doctest` lorsqu'on exécute le fichier directement `lib_graphes_junier_frederic.py`. 
* Les codes des méthodes de détection de cycle et de tri topologique pour un graphe orienté, se trouvent entre les lignes 717 et 857 de `lib_graphes_junier_frederic.py`.
* `main_junier_frederic.py` est le fichier de tests avec un jeu de tests réduit. Il peut s'exécuter avec des options qui peuvent se combiner :
  * `python3 main_junier_frederic.py` exécute le script sans générer de fichiers `pdf` et `png` pour les graphes manipulés, les sorties des tests sont affichées dans la console
  * `python3 main_junier_frederic.py h` ou `python3 main_junier_frederic.py -h` affiche l'aide (réduite) du programme
  * `python3 main_junier_frederic.py pdf` ou `python3 main_junier_frederic.py png` exécute les tests, affiche les sorties dans la console, 
  crée un sous-répertoire `images` dans le répertoire de l'archive et y stocke les fichiers `pdf` et `png` des graphes générés avec les outils de la ligne de commande `xargs` et `convert`.
  * `python main_junier_frederic.py greedy` exécute sur les  tests la méthode de tri topologique gloutonne
  * `python main_junier_frederic.py dfs` exécute sur les  tests la méthode de tri topologique avec dfs
  * Pour l'instant j'ai positionné les paramètres `greedy` et `dfs` à `True` par défaut dans la fonction `main` mais pour une utilisation 
  avec des élèves il faudrait les positionner à `False`.

* `activite-eleve.md` contient une ébauche de scénario d'activité élève en langage Markdown. 
Le contenu est plus complet que dans la partie Contexte ci-dessous avec en particulier les dessins des graphes. 
 Pour générer les versions `pdf` et `odt` de l'activité, il suffit d'ouvrir un terminal de commande dans le répertoire courant 
 et  d'exécuter la commande `make` ou `make all`. Le script `main_junier_frederic.py` est alors exécuté avec l'option `pdf`, les fichiers `pdf` et `png` des graphes 
  sont générés dans le sous-répertoire `images` et les fichiers `activite-eleve.pdf` et `activite-eleve.odt` sont générés avec `pandoc` à partir de la source `activite-eleve.md`. 
On peut nettoyer   les fichiers créés en exécutant `make clean` et si on a modifié le contenu d'un fichier source et on peut tout reconstruire avec `make fresh`. 
Pour outiller l'activité, il faudra fournir aux élèves un code à trous avec des `# TO DO` à compléter au niveau des  méthodes ciblées.


## Contexte de l'activité


Vous travaillez au service _Notice de montage_ de l'entreprise  __AEKI__ qui fabrique et commercialise des meubles en kit, _à monter soi-même_.

Pour chaque nouveau produit, le service ingénierie vous founit un schéma sous la forme d'un _graphe de contraintes_ qui est un graphe orienté :
* chaque étape de montage  est un sommet du graphe, identifié par une étiquette distincte choisie aléatoirement  parmi les  lettres minuscules
* un arc reliant deux sommets du graphe exprime une contrainte d'ordre (ou _relation de précédence_ ou _relation de dépendance_) dans le montage  : 
par exemple un arc d'origine  le sommet d'étiquette `'c'` et d'extrémité le sommet d'étiquette  `'a'`  signifie que  l'étape de montage `'c'` doit être réalisée avant l'étape `'a'`.
  
Attention, L'étiquetage étant aléatoire, l'ordre alphabétique sur les étiquettes des étapes n'est pas forcément l'ordre de montage !
À partir d'un tel graphe, vous devez définir un ordre d'exécution des étapes de montage pour la notice de montage, 
permettant à un utilisateur de monter le produit en respectant toutes les contraintes.

Voici une liste ordonnée de questions possibles :


1. Le service ingénierie vous a fourni un graphe de contraintes ci-dessous, vous devez vérifier si l'ordre de montage (voir activité élève)  respecte  les contraintes du graphe. 
Si ce n'est pas le cas, vous devez proposer une modification de  cet ordre qui  respecte les contraintes du graphe. 
Existe-t-il d'autres ordres possibles pour la notice de montage ?

2. Le service ingénierie vous a fourni un autre graphe (qui contient un cycle, voir activité élève). 

    * Pouvez-vous déterminer un ordre de montage respectant ces contraintes ?
    * Quelle condition nécessaire doit vérifier un graphe de contraintes pour qu'un ordre de montage existe ? 


3. Votre chef vous demande d'écrire en pseudo-code  un algorithme qui automatise la génération d'un ordre de montage 
à partir d'un graphe de contraintes pour lequel il existe un ordre de montage.
Ayant suivi la spécialité NSI au lycée, vous vous souvenez des algorithmes gloutons présentés en classe de première (lesquels au fait ?). 

   * Si on résout ce problème par étape, quel choix glouton optimal peut-on faire à chaque étape ? 
   * Écrivez en  pseudo-code un algorithme glouton qui permet de déterminer un ordre de montage compatible avec un graphe donné
    puis implémentez en Python en complétant le code de la  méthode `verif_topological_order`  de la classe `DirectGraph` dans le  fichier `LibGraphes.py`.
   * Testez avec le script  `main.py` , affichez d'abord l'aide avec `python3 main.py h`.
   * Complétez le code de la  méthode `verif_topological_order`  de la classe `DirectGraph` dans le  fichier `LibGraphes.py`, 
   elle droit vérifier qu'un ordre de montage donné en paramètre est bien compatible avec le graphe de contraintes.

4. Il existe un autre algorithme pour déterminer un ordre topologique sur les sommets d'un graphe, basé sur un parcours en profondeur du graphe. 
   Visionnez ce tutoriel video <https://youtu.be/eVsCO71q1L0>, puis implémentez cet algorithme 
   en complétant la méthode `topological_sort_dfs` de la classe `DirectGraph` dans le  fichier `LibGraphes.py`.
