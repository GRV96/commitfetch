# commitfetch

## Français

Cette bibliothèque aide à obtenir les données des commits d'un dépôt au moyen
de l'API de GitHub. L'utilisateur doit fournir ses informations
d'authentification.

Exécutez cette commande pour installer les dépendances.

```
pip install -r requirements.txt
```

`commitfetch` contient les classes et fonctions suivantes. Consultez les
scripts `demo_write_commits.py` et `demo_read_commits.py` pour savoir comment
les utiliser.

**`Commit`**

Cette classe contient des données extraites d'un commit de GitHub.

**`GitHubCredentials`**

Cette classe contient le nom d'un utilisateur de GitHub et des jetons
d'authentification qu'il possède.

**`RepoIdentity`**

Cette classe identifie un dépôt GitHub par le nom de son propriétaire et le nom
du dépôt. L'identité est souvent écrite sous le format `propriétaire`/`nom`.

**`extract_text_lines`**

Cette fonction lit le fichier texte spécifié et renvoie ses lignes dans une
liste. Elle permet par exemple d'accéder à des jetons enregistrés dans un
fichier texte.

**`get_repo_commits`**

Cette fonction est l'élément principal de `commitfetch`. C'est elle qui
effectue les requêtes à l'API de GitHub pour obtenir les données des commits
d'un dépôt. Il faut lui fournir des informations d'authentification dans une
instance de `GitHubCredentials`.

**`read_reprs`**

Cette fonction lit un fichier texte contenant les représentations d'objets
Python puis recrée ces objets et les renvoie dans une liste. Les représetations
sont des chaînes de caractères renvoyées par la fonction `repr`. Chaque ligne
du fichier doit contenir une représentation.

**`write_reprs`**

Cette fonction écrit les représentations d'objets Python dans un fichier texte.
Les représetations sont des chaînes de caractères renvoyées par la fonction
`repr`. Chaque ligne du fichier contient une représentation. La fonction
`read_reprs` peut lire ce fichier.

# English

This library helps obtaining the data of a repository's commits through the
GitHub API. Authentication with GitHub credentials is required.

Execute this command to install the dependecies.

```
pip install -r requirements.txt
```

`commitfetch` contains the following classes and functions. See scripts
`demo_write_commits.py` and `demo_read_commits.py` to know how to use them.

**`Commit`**

This class contains data extracted from a GitHub commit.

**`GitHubCredentials`**

This class contains the name of a GitHub user and authentication tokens that
they own.

**`RepoIdentity`**

This class identifies a GitHub repository by its owner's name and the
repository's name. The identity is often written in the format `owner`/`name`.

**`extract_text_lines`**

This function reads the specified text file and returns its lines in a list. It
allows for example to access tokens stored in a text file.

**`get_repo_commits`**

This function is the main element of `commitfetch`. It performs requests to the
GitHub API to obtain data about a repository's commits. The user must provide
their credentials in a `GitHubCredentials` instance.

**`read_reprs`**

This function reads a text file that contains the representations of Python
objects then recreates those objects and returns them in a list. The
representations are strings returned by function `repr`. Each line of the file
must contain one representation.

**`write_reprs`**

This function writes the representations of Python objects in a text file. The
representations are strings returned by function `repr`. Each line of the file
contains one representation. Function `read_reprs` can read this file.
