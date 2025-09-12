# Auteurs:
<Omar AMINE, Brice PERROUT, GHARSALLI Hanine, BAKNINE Nouhaila, Xiaoyu TANG> 

# Task Manager

Un gestionnaire de tâches avancé en ligne de commande écrit en Python.

## Fonctionnalités

- Ajouter des tâches avec état et récurrence
- Modifier des tâches existantes (description, état, récurrence)
- Supprimer des tâches
- Afficher toutes les tâches dans un tableau formaté
- Gestion des états de tâches (started, suspended, completed, cancelled)
- Support de tâches récurrentes (weekly, monthly, no)
- Journalisation des actions

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
python main.py lestaches.txt add "Description de la tâche" -s <état> [-r <récurrence>]
```

**États disponibles :** started, suspended, completed, cancelled
**Récurrences disponibles :** weekly, monthly, no

#### Modifier une tâche
```bash
python main.py lestaches.txt modify <id_tache> [-d "Nouvelle description"] [-s <nouvel_état>] [-r <nouvelle_récurrence>]
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
# Ajouter une tâche avec état et récurrence
python main.py lestaches.txt add "Faire les courses" -s started -r weekly

# Ajouter une tâche simple
python main.py lestaches.txt add "Réviser pour l'examen" -s started

# Afficher les tâches
python main.py lestaches.txt show

# Modifier la description d'une tâche
python main.py lestaches.txt modify 1 -d "Faire les courses au supermarché"

# Changer l'état d'une tâche
python main.py lestaches.txt modify 1 -s completed

# Modifier la récurrence d'une tâche
python main.py lestaches.txt modify 1 -r monthly

# Modifier plusieurs paramètres à la fois
python main.py lestaches.txt modify 1 -d "Nouvelle description" -s suspended -r no

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

Les tâches sont stockées dans un fichier texte avec le format étendu incluant l'état, la date de création et la récurrence.

## États des tâches

- **started** : Tâche démarrée/en cours
- **suspended** : Tâche suspendue/en pause
- **completed** : Tâche terminée
- **cancelled** : Tâche annulée

## Récurrence

- **weekly** : Répétition hebdomadaire
- **monthly** : Répétition mensuelle  
- **no** : Aucune récurrence

## Journalisation

Le système enregistre automatiquement toutes les actions dans un fichier de logs pour traçabilité.