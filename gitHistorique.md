# Historique linéaire

Pour rappel, la commande status décrit en effet toujours l’état de l’index et du répertoire de travail par rapport à la dernière version enregistrée (HEAD).

Comme la plupart des gestionnaires de version, git distingue les changements apportés à des fichiers sous gestion de version des créations de nouveaux fichiers dans le répertoire de travail.

Pour visualiser le premier type de changement, on peut utiliser git diff :
```bash
git diff
```

Cette commande décrit les différences entre le répertoire de travail et l’index, selon un format similaire à celui de l’utilitaire diff des systèmes Unix. Attention elle ne tient compte que des fichiers qui ont précédemment été mis sous gestion de version avec git add. Un fichier nouvellement créé dans le répertoire de travail ne sera pas mentionné par la sortie de git diff.

Il est donc important de prendre l’habitude de toujours vérifier la sortie de **git status** avant de créer un commit et de ne pas se baser que sur celle de git diff qui donne une vision incomplète des changements du répertoire de travail.

**git add** combine deux fonctions qui sont en général distinctes dans d’autres outils :

- Mettre des fichiers sous gestion de version
- Ajouter des changements survenus dans un fichier à la prochaine version

Dans le modèle de git, ces deux opérations sont unifiées par la notion d’index, qui rend redondante celle de fichier sous gestion de version. .

## Exploration de l’historique

Visualisation interactive

Nous avons maintenant créé quelques commits, et il est possible d’afficher l’historique de ces derniers avec git log :

```bash
git log
```
Pour étudier un commit précis de la liste, nous pouvons demander à git d’afficher des informations détaillées sur ce dernier avec git show <commit>, où le commit peut être identifié par son hash.

Cet historique peut être aussi affiché via une interface graphique :

```bash
gitk
```
Il est possible d’afficher les changements survenus dans le répertoire de travail depuis une ancienne version avec git diff <commit>. Il est également possible d’afficher la différence entre deux versions enregistrées du projet avec git diff <commit1> <commit2>.

Vous aurez remarqué que l’identifiant HEAD désigne le dernier commit enregistré, celui dit aussi « commit actif ».

Pour étudier les parents d'un commit, il sont indéxés. À tout identifiant de commit, nous pouvons ajouter le suffixe ~[N] pour désigner le (N-ième) parent de ce commit. Ainsi, HEAD~ est le parent du commit actif, et HEAD~2 est son grand-parent.

Avec cette syntaxe, nous pouvons demander à git la différence entre le répertoire de travail et le parent du commit actif

```bash
git diff HEAD~
```
…ou bien les changements du commit actif par rapport à son parent :

```bash
git diff HEAD~ HEAD
```
## Nommer un commit
Désigner des commits par des hashes absolus ou par des chemins relatifs à base de HEAD est fastidieux, et le risque d’erreur est élevé. Lorsqu’on doit souvent faire référence à un commit, il est préférable de lui donner une étiquette (tag) via la commande **git tag <étiquette> [<commit>]** :

```bash
git tag important
git tag papa HEAD~
git tag maman important~
git tag ancetre HEAD~2
git log
```

Contrairement à HEAD et à la branche active, les étiquettes ne bougent pas. Si vous créez de nouveaux commits par la suite, important pointera toujours vers le même commit.

Si vous le souhaitez, vous pouvez ajouter une description à votre étiquette, avec l’option --annotate de git tag. Ces annotations sont souvent utilisées pour indiquer les points du développement d’un logiciel auxquels une version publique a été distribuée, et documenter les nouveautés de cette version.

Par défaut, git tag --annotate ouvre un éditeur de texte comme git commit. Et comme avec git commit, on peut utiliser l’option -m pour saisir l’annotation dans la ligne de commande :

```bash
git tag --annotate -m "Ma super v1" v1.0 HEAD~
git show v1.0
git tag --list
```
**git show** permet de visualiser la description de l'étiquette v1.0, **git tag -- list** La liste des étiquettes présentes dans le dépôt.

```bash
git tag --delete v1.0 important maman papa ancetre
```
**git tag -- delete <nom>** permet de supprimer une étiquette.

## Revenir dans le passé

git nous permet aussi de remonter le temps, et de charger le contenu d’une version préalablement enregistrée dans le répertoire de travail.

Pour que les choses se passent bien, il faut au préalable s’assurer que le dit répertoire de travail soit propre à vérifier avec git status

```bash
git status
git add --all
git commit -m 'La version ultime'
git status
```
Nous avons créé un nouveau commit et nous souhaitons revenir au précédent :
```bash
git checkout HEAD~
```

git affiche alors un message pour vous avertir que vous n’êtes plus sur une branche, et que si vous créez des commits quand le dépôt est dans cet état, vous ne pourrez pas facilement les retrouver par la suite. En terminologie git, on désigne cet état par le nom morbide de HEAD détachée.

Le reste du message vous explique comment vous pourriez préserver vos changements en créant une autre branche. Nous reviendrons sur tout ça quand nous aurons abordé les branches, mais ici nous ne souhaitons pas créer de nouveaux commits donc vous pouvez ignorer cette suggestion.

Quoi qu’il en soit, si vous regardez les fichiers de votre dépôt, vous pouvez constater que leur contenu a changé pour reprendre la valeur qu’ils avaient dans la version précédente. Une vraie machine à voyager dans le temps !

N’hésitez pas à revenir en différents points de votre historique avec git checkout, en utilisant gitg pour retrouver les identifiants de vos commits. Par défaut, gitg affiche l’historique relativement au commit actif, mais vous pouvez lui faire afficher l’ensemble des commits du dépôt en sélectionnant l’option « Tous les commits » dans le menu de gauche.


Pour revenir à la fin de l’historique principal en rebasculant sur la branche master :

```bash
git checkout master
```

## Annuler un jeu de commits

Il est possible d’annuler l’effet d’un jeu de commits de façon non-destructive (il est possible de revenir à l’état avant annulation par la suite) avec la commande git revert. Cette commande modifie l’effet du répertoire de travail, ne pas oublier de vériifier l'état et corriger si nécessaire.

```bash
git status
git revert HEAD
```

À plus grande échelle, il est aussi possible d’annuler l’effet de plusieurs commits avec la variante git revert <commit1> <commit2>, ou celui d’une série de commits avec la variante git revert <commit1>..<commitN> (notez les deux points entre les deux identifiants de commit spécifiant le début et la fin du jeu de changement à annuler).

Puisque git revert fonctionne en créant un nouveau commit, c’est une commande sans risque : l’ancien commit n’est pas perdu, il reste facilement accessible au sein de l’historique. On ne peut donc pas perdre accidentellement des données en utilisant revert.

Pour collaborer facilement avec d’autres personnes, il va falloir introduire un outil qui permet à git de représenter la notion d’évolution parallèle : la branche. 
