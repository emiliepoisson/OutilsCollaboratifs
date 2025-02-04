# Pratiques Git

## Utilitaires

Outils complémentaires à git

- le git biensûr : [https://git-scm.com/], par défaut sous linux
- gitk, git-gui : ses interfaces graphiques
- tout éditeur de texte est bienvenu qui colore vos codes, pensez à rajouter les extensions.
- vscode - Editeur et lien git, GitHub
- GitHub, GitLab, Bitbucket pour avoir un serveur distant
- [https://github.com/apps/desktop] : interface locale GitHub
- [https://www.sourcetreeapp.com/] Sourcetree est une interface graphique gratuite pour Git
- Meld - comparaison de fichiers [https://meldmerge.org/]

Nous utiliserons principalement ici le terminal Windows (console WIN + R / powershell). Les commandes seront à adapter à votre système (Linux/osX).

```bash
cls #console effacée
cd #pour connaître votre répertoire courant
D: #modifier en fonction de votre partition
cd Téléchargements
mkdir TP1Git
cd TP1Git
git help git -a #aide
```

### Exemple

Pour la suite de cette section, nous nous créons l’arborescence suivante dans le dossier TP1Git:

 +- fig
 | +- image.png
 +- contenus
 | exemple.md
 principal.md

```bash
cls #console effacée (linux: clear)
cd #vérifier votre répertoire courant (pwd)
mkdir fig
mkdir contenus
echo 'premier ecrit dans le fichier'>> principal.md
echo 'second ecrit dans le deuxieme fichier'>> ./contenus/exemple.md
dir (linux:ls)
```

 Nous allons **créer un dépôt git local**. Il suffit de se placer dans le dossier dans lequel un veut initialiser le dépôt et exécuter

```bash
 git init
```

 Cela initialise un dépôt vide dans ce dossier. Les données de git sont stockées dans le fichier
 caché nommé .git :
 ```bash
 dir /a # linux: ls -a
 git status
 ```

 La commande **git status** est à user SANS modération. Elle permet de connaître l'état de son dépôt local et d'analyser si celui est potentiellement à jour avec un dépôt distant.

 A ce stade vous remarquez que votre dépôt distant contient une branche dite **master** et que des répertoires et fichiers ne sont pas suivis. Historiquement, la branche par défaut s’appelle master qu'il convient parfois de renommer en main pour une principale pour certains dépôt distant comme Github.  A noter le répertoire fig étant sans fichier, il n'est pas considéré.

```bash
 git status
 git config --list #verifier le nom de la branche par defaut et autre parametre
 ```

git propose des commentaires notamment la commande **add** qui permet d'ajouter des noms de fichiers à suivre.

```bash
 git add principal.md
 git status
 ```

Pour déposer plusieurs fichiers sans passer par leur nom (fastidieux), on peut passer par l'ajout d'une directive -A pour le diminutif anglais all.

```bash
git add contenus/ #ajout repertoire
git add -A #ajout de tout
git status
```

Afin d'enregistrer vos modifications et les sauvegarder pour revenir sur un état précédent, il faut enregistrer des états associés au moyen de la commande **commit** en y ajoutant un message permettant à vous-même ou vos collaborateurs de comprendre l'intérêt des modifications apportées par rapport aux précédentes.

```bash
git commit
```
**git commit** ouvre un éditeur vous demandant d'écrire et enregistrer un message. Dans une console classique taper echap : wq. Ceci sont les commandes nécessaires pour sauvegarder l'écriture - w:write- et quitter - q:quit

ou insérer directement votre message en console

```bash
echo "fichier inutile" >> Aretirer.txt
git add Aretirer.txt
git commit -m "ajout fichier A retirer.txt" #ajout dun point d'enregistrement
git status
```

**Rappel des concepts associés au commit**

- Commit : Une version du projet / ses changements. Chaque commit est identifiable par un __hash__,  Le premier commit est spécial (pas de parents).
- A force de commit, on crée ainsi un historique. Chaque commit a un antécédent.
- Une branche = Une extrémité de l’historique
- HEAD : La version sur laquelle on base notre travail
- Index/staging area : La version en cours de création
- Répertoire de travail : Les fichiers que l’on manipule

```bash
git Log
gitk
git-gui
```

### Déplacement et suppression de fichier

À partir du moment où un fichier est sous gestion de version, il est préférable d’informer le gestionnaire de version quand on effectue un déplacement ou une suppression, en utilisant respectivement git mv et git rm .

Exemple de renommage de fichier
```bash
echo "blabla" >> Monfichier.txt
ren Monfichier.txt MonsuperFichier.txt
git status
git add --all
git commit -m 'modifications de nom de fichier'
git rm MonFichier.txt
git status
```
Une commande pratique pour se tirer de ce genre de mauvais pas est git add --all , qui intègre à la gestion de version tous les changements d’un répertoire passé en paramètre.

### Annulation de modifications

Pour annuler des modifications deux solutions, reset ou reverse.

Deux manières d’annuler un commit : vous pouvez créer un nouveau commit qui annule les modifications ou simplement revenir au commit précédent et recommencer les modifications depuis ce commit.

Pour créer un nouveau commit qui annule les modifications, vous pouvez utiliser

```bash
 git reverse HEAD
```
ou

sans création de nouveau commit ,pour revenir à un enregistrement précédent,

Avec une version moderne de git, il suffit d’utiliser la variante de git reset qui prend un fichier en argument pour annuler cette opération :

```bash
 git reset Aretirer.txt
 git status
```

Sur d'anciennes versions de git, il est possible que vous soyez obligés d'utiliser la commande spécifique **git rm --cached <fichier>** cached évite tout destruction dans le dépôt local.

```bash
git reset --hard
git status
```

Attention, utiliser l’option **--hard** détruit totalement l’historique du commit, n’utilisez cette option que si c’est c’est absolument nécessaire de ne pas avoir l’historique de l’action

### Ignorer des fichiers dans les enregistrements

Tout contenu n'est pas utile à versionner. Trois raisons classiques :

1- Ils contiennent des données que l’on ne souhaite pas partager avec autrui (ex : mots de passe, configurations d’outils relevant du goût personnel)

2- Ils peuvent être régénérés à partir des fichiers restants (ex : résultats d’une compilation de code source, journaux d’exécution) et représentent donc une information redondante.

3- Ils sont trop lourds pour qu’on puisse se permettre d’en conserver chaque version historique

Git détecte tout nouveau fichier et incite à les suivre. Il faut donc l'informer des fichiers à ne pas suivre.

Pour éviter ça, on peut créer un fichier **.gitignore** à la racine du dépôt, qui indique que certains fichiers doivent être ignorés par git :

A Exécuter à la racine de dépôt, sinon l'effet est limité au sous-dossier actuel

```bash
echo '*.txt' > .gitignore
git status
```
Il est en général pertinent de mettre .gitignore sous gestion de version car si un fichier vous gêne, il a de fortes chances de gêner vos collègues aussi.

On le fait avec git add , comme précédemment :
```bash
git add .gitignore
```
.gitignore supporte les motifs usuels du shell Unix, comme l’étoile (wildcard), et sa configuration s’applique à chaque sous-dossier du dépôt. Pour gérer des situations plus complexes, des syntaxes
plus sophistiquées sont disponibles, consultez git help gitignore pour plus de détails.
