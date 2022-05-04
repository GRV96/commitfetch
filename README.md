# commitfetch

## Français

Cette bibliothèque aide à obtenir les données des commits d'un dépôt au moyen
de l'API de GitHub. L'utilisateur doit fournir ses informations
d'authentification.

### Contenu

**`Commit`**

Cette classe contient des données d'un commit de GitHub.

**`GitHubCredentials`**

Cette classe contient le nom d'un utilisateur de GitHub et des jetons
d'authentification qu'il possède. Elle aide à effectuer des requêtes
authentifiées à l'API de GitHub. Chaque jeton permet 2000 requêtes par heure.

**`RepoIdentity`**

Cette classe identifie un dépôt GitHub par le nom de son propriétaire et le nom
du dépôt. L'identité est souvent écrite sous le format `propriétaire`/`nom`.

**`extract_text_lines`**

Cette fonction lit le fichier texte spécifié et renvoie ses lignes dans une
liste. Elle permet par exemple d'accéder à des jetons enregistrés dans un
fichier texte, un par ligne.

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

### Démos

Exécutez cette commande pour installer les dépendances.

```
pip install -r requirements.txt
```

Consultez les scripts `demo_write_commits.py` et `demo_read_commits.py` dans le
dépôt de code pour savoir comment utiliser la bibliothèque `commitfetch`.

`demo_write_commits.py` obtient les commits d'un dépôt GitHub et enregistre
leur représentation dans un fichier texte. Il a besoin d'un fichier listant les
jetons d'authentification de l'utilisateur un par ligne pour effectuer des
requêtes à l'API GitHub. Pour que ce dépôt ignore les fichiers de jetons, leur
nom devrait contenir la chaîne «token».

Exemple d'exécution:

```
python demo_write_commits.py -u GRV96 -t tokens.txt -r scottyab/rootbeer
```

Pour essayer `demo_write_commits.py` avec des nombres de commits variés,
utilisez les dépôts ci-dessous.

| Dépôt                     | Nombre de commits |
|---------------------------|:-----------------:|
| k9mail/k-9                | 10 985            |
| Skyscanner/backpack       | 7075              |
| mendhak/gpslogger         | 2239              |
| PeterIJia/android_xlight  | 397               |
| scottyab/rootbeer         | 191               |

`demo_read_commits.py` montre comment lire les représentations de commits
enregistrées par `demo_write_commits.py`. Pour confirmer que la lecture a
fonctionné, il affiche les données d'un commit dans la console.

Exemple d'exécution:

```
python demo_read_commits.py -c scottyab_rootbeer_commits.txt
```

# English

This library helps obtaining the data of a repository's commits through the
GitHub API. Authentication with GitHub credentials is required.

### Content

**`Commit`**

This class contains data of a GitHub commit.

**`GitHubCredentials`**

This class contains the name of a GitHub user and authentication tokens that
they own. It helps making authenticated requests to the GitHub API. Each token
allows 2000 requests per hour.

**`RepoIdentity`**

This class identifies a GitHub repository by its owner's name and the
repository's name. The identity is often written in the format `owner`/`name`.

**`extract_text_lines`**

This function reads the specified text file and returns its lines in a list. It
allows for example to access tokens stored in a text file, one per line.

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

### Demos

Execute this command to install the dependecies.

```
pip install -r requirements.txt
```

See scripts `demo_write_commits.py` and `demo_read_commits.py` in the source
code repository to know how to use library `commitfetch`.

`demo_write_commits.py` obtains a GitHub repository's commits and writes their
representation in a text file. It needs a file that lists the user's
authentication tokens one per line to perform requests to the GitHub API. This
repository will ignore the token files if their name contains the string
"token".

Execution example:

```
python demo_write_commits.py -u GRV96 -t tokens.txt -r scottyab/rootbeer
```
To try `demo_write_commits.py` with varied numbers of commits, use the
repositories below.

| Repository                | Number of commits |
|---------------------------|:-----------------:|
| k9mail/k-9                | 10 985            |
| Skyscanner/backpack       | 7075              |
| mendhak/gpslogger         | 2239              |
| PeterIJia/android_xlight  | 397               |
| scottyab/rootbeer         | 191               |

`demo_read_commits.py` shows how to read the commit representations recorded by
`demo_write_commits.py`. It confirms that the reading was successful by
displaying a commit's data in the console.

Execution example:

```
python demo_read_commits.py -c scottyab_rootbeer_commits.txt
```
