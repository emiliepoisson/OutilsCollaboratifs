---
title: "TP3 - travail commun sur git"
author: "Emilie Poisson Caillault"
date: "24/02/2025"
output:
  pdf_document: default
  html_document: default
---

**TP : Collaboration sur un fichier commun avec Git et GitHub**

Objectif : Un binôme ou trinôme d'étudiants collaborera sur un même fichier texte en utilisant Git et GitHub. 

Chaque étudiant travaillera sur une branche séparée et fusionnera ses modifications dans la branche principale.

Vous reprendrez le texte issu de cet partage que vous segmenterez : (VillageJuridque)[https://www.village-justice.com/articles/controler-incontrolable-intelligence-artificielle-coeur-des-enjeux-ethiques,51284.html]

Recommencez le TP pour que chaque étudiant prenne le rôle de l'étudiant1.

# Instructions :

Création du dépôt et ajout des collaborateurs par l'étudiant 1 (Créateur du dépôt) :

Créez un nouveau dépôt sur GitHub nommé projet-collaboratif.

Ajoutez les deux autres étudiants comme collaborateurs dans les paramètres du dépôt.

Créez un fichier initial texte_commun.txt dans la branche main.

Commandes Git :


# Cloner le dépôt localement

```bash
git clone https://github.com/votre-utilisateur/projet-collaboratif.git
cd projet-collaboratif
```

Création de branches individuelles :

Chaque étudiant doit créer sa propre branche pour travailler sur le projet.

Commandes Git :

```bash
# Créer une nouvelle branche (remplacez 'votre-nom' par votre nom)
git checkout -b votre-nom
```
Travail sur le fichier commun :

Chaque étudiant doit ajouter son texte dans le fichier texte_commun.txt.

Commandes Git :

```bash
# Ajouter le fichier modifié à l'index
git add texte_commun.txt

# Faire un commit des modifications
git commit -m "Ajout du texte pour etudiant1"

# Pousser la branche vers le dépôt distant
git push origin votre-nom
```

Création d'une Pull Request :

Chaque étudiant doit créer une Pull Request (PR) sur GitHub pour fusionner sa branche dans la branche main.

Instructions :

Allez sur la page du dépôt sur GitHub.

Cliquez sur "Compare & pull request".

Remplissez le formulaire et soumettez la PR.

Revue et fusion des Pull Requests :

Étudiant 1 :

Passez en revue les PR des autres étudiants.

Si tout est correct, fusionnez les PR dans la branche main.
Commandes Git (après fusion) :

```bash
# Mettre à jour la branche locale main
git checkout main
git pull origin main
```

Résolution des conflits (si nécessaire) :

Si des conflits surviennent lors de la fusion, les étudiants doivent les résoudre en discutant et en modifiant le fichier texte_commun.txt.

Commandes Git :

```bash
# Résoudre les conflits dans le fichier
# Ajouter le fichier résolu à l'index
git add texte_commun.txt

# Faire un commit pour finaliser la résolution
git commit -m "Résolution des conflits"

# Pousser les modifications vers le dépôt distant
git push origin main
```

# Suite du TP (un seul étudiant Etudiant1). 

Ensuite travailler sur les outils de génération de site web à partir de prompt ou d'IA.

Pour construire une présentation commune des potentialités offertes.

Voici des exemples d'outils : 

- HubSpot AI Website Generator [https://www.hubspot.fr/products/cms/ai-website-generator]
- Durable [https://fr.durable.co/]
- Zoho monopage (gratuit) https://www.zoho.com/fr/sites/pricing.html
- Hostinger Website Builder [https://www.hostinger.fr/]
- Wix ADI [https://fr.wix.com/ai-website-builder]
- Weblium
- Localo
- ...






