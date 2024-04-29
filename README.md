# miniprojet
Programmation hétérogène (C et python) : logiciel multiplatform

# L'objectif 
L'objectif du logiciel que vous développez est de créer une solution qui intègre des codes écrits en langages de programmation hétérogènes (C et Python) pour réaliser des tâches complémentaires. Voici un rappel des principaux objectifs et fonctionnalités du logiciel :

## Articulation des Langages de Programmation Hétérogènes :
Le logiciel combine le code écrit en C et en Python pour tirer parti des forces spécifiques de chaque langage.
Le C est utilisé pour des opérations de bas niveau, comme le traitement initial des données, qui nécessitent une exécution rapide et efficace.
Python est employé pour des tâches de haut niveau, notamment l'analyse de données, le calcul de statistiques (moyenne et écart type) et la visualisation des résultats.

## Traitement et Analyse de Données :
Le programme en C lit et filtre les données à partir d'un fichier (par exemple, MesNotes.txt), en s'assurant de la validité des données et en respectant une limite de taille de tableau fixée (512 entrées).
Les données valides sont ensuite écrites dans un nouveau fichier (par exemple, FilteredNotes.txt), qui est utilisé par le script Python pour des analyses ultérieures.

## Calcul et Visualisation Statistiques :
Le script Python lit les données filtrées, calcule des mesures statistiques telles que la moyenne et l'écart type, et produit des visualisations graphiques pour aider à l'interprétation des données.
Ces visualisations peuvent inclure des histogrammes et des graphiques 3D utilisant des bibliothèques comme matplotlib.

## Gestion des Erreurs et Interopérabilité :
Le logiciel inclut une gestion robuste des erreurs pour s'assurer que tous les aspects du traitement des fichiers et des données sont sécurisés et efficaces.
Les commandes system() en C et os.system() en Python sont utilisées pour orchestrer l'exécution de tâches entre les deux langages, en assurant une communication fluide et une interopérabilité entre les composants du logiciel.
Fonctionnement Multiplateforme :
Le logiciel est conçu pour fonctionner de manière transparente sur plusieurs systèmes d'exploitation, y compris Windows, macOS, et Linux, sans nécessiter de modifications spécifiques à la plateforme.
Les utilisateurs peuvent lancer le logiciel à partir d'une simple commande dans l'invite de commande ou le terminal, rendant son utilisation accessible et pratique.
