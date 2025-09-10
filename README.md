# Task Manager

Un gestionnaire de tâches simple en ligne de commande écrit en Python.

## Fonctionnalités

- Ajouter des tâches
- Modifier des tâches existantes  
- Supprimer des tâches
- Afficher toutes les tâches dans un tableau formaté

## Installation

1. Clonez ce repository
2. Assurez-vous d'avoir Python 3.10+ installé
3. Aucune dépendance externe requise

## Utilisation

```bash
python main.py <chemin_fichier> <commande> [arguments]
```

### Commandes disponibles

#### Ajouter une tâche
```bash
python main.py lestaches.txt add "Description de la tâche"
```

#### Modifier une tâche
```bash
python main.py lestaches.txt modify <id_tache> "Nouvelle description"
```

#### Supprimer une tâche
```bash
python main.py lestaches.txt rm <id_tache>
```

#### Afficher toutes les tâches
```bash
python main.py lestaches.txt show
```

## Exemples

```bash
# Ajouter une tâche
python main.py lestaches.txt add "Faire les courses"

# Afficher les tâches
python main.py lestaches.txt show

# Modifier la tâche avec l'ID 1
python main.py lestaches.txt modify 1 "Faire les courses au supermarché"

# Supprimer la tâche avec l'ID 1
python main.py lestaches.txt rm 1
```

## Structure du projet

```
.
├── main.py           # Point d'entrée principal
├── task.py           # Classe Task
├── commands.py       # Implémentation des commandes
└── utils/
    ├── __init__.py
    ├── parser.py     # Parser d'arguments
    ├── io.py         # Lecture/écriture des fichiers
    └── print.py      # Affichage formaté
```

## Format des données

Les tâches sont stockées dans un fichier texte avec le format :
```
id|description
```

Exemple :
```
1|Faire les courses
2|Réviser pour l'examen
3|Nettoyer la chambre
```