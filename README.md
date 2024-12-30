# commitfetch

## FRANÇAIS

Cette bibliothèque aide à obtenir les données des commits d'un dépôt au moyen
de l'API de GitHub. L'utilisateur doit fournir ses informations
d'authentification.

### Contenu

**`Commit`**

Cette classe contient des données d'un commit de GitHub.

**`GitHubCredentials`**

Cette classe contient le nom d'un utilisateur de GitHub et des jetons
d'authentification qu'il possède. Elle aide à effectuer des requêtes
authentifiées à l'API de GitHub. Chaque jeton permet 5000 requêtes par heure.

**`GitHubUser`**

Cette classe contient des données d'un utilisateur de GitHub.

**`github_user_repository`**

Ce module conserve des instances de `GitHubUser`. Il utilise leur propriété
`login` comme une clé pour y donner accès. Ainsi, ce module aide à éviter la
création de nombreuses instances identiques de `GitHubUser`.

**`RepoIdentity`**

Cette classe identifie un dépôt GitHub par le nom de son propriétaire et le nom
du dépôt. L'identité est souvent écrite sous le format `propriétaire`/`nom`.

**`extract_text_lines`**

Ce générateur lit le fichier texte spécifié et renvoie une de ses lignes à
chaque itération. Il permet par exemple d'accéder à des jetons enregistrés
dans un fichier texte, un par ligne.

**`get_repo_commits`**

Ce générateur est l'élément principal de `commitfetch`. C'est lui qui effectue
les requêtes à l'API de GitHub pour obtenir les données des commits d'un dépôt.
Chaque itération produit une instance de `Commit`. Il faut fournir à ce
générateur des informations d'authentification dans une instance de
`GitHubCredentials`.

**`read_commit_reprs`**

Ce générateur lit un fichier texte contenant les représentations d'instances
de `Commit` et recrée ces objets. Chaque itération produit une instance de
`Commit`. Les représetations sont des chaînes de caractères renvoyées par la
fonction `repr`. Chaque ligne du fichier doit être une représentation d'un
`Commit`. Les lignes vides sont ignorées.

**`write_commit_reprs`**

Cette fonction écrit les représentations d'instances de `Commit` dans un
fichier texte. Les représetations sont des chaînes de caractères renvoyées par
la fonction `repr`. Chaque ligne du fichier est une représentation. La fonction
`read_commit_reprs` peut lire ce fichier.

### Dépendances

Exécutez cette commande pour installer les dépendances.

```
pip install -r requirements.txt
```

### Démos

Consultez les scripts dans le dossier `demos` pour savoir comment utiliser la
bibliothèque `commitfetch`.

#### Enregistrement des commits

`demo_write_commits.py` obtient les commits d'un dépôt GitHub et écrit leur
représentation dans un fichier texte. Il a besoin d'un fichier listant les
jetons d'authentification de l'utilisateur un par ligne pour effectuer des
requêtes à l'API GitHub. Pour que ce dépôt ignore les fichiers de jetons, leur
nom devrait contenir la chaîne «`token`».

Aide:

```
python demos/demo_write_commits.py -h
```

Exemples d'exécution:

```
python demos/demo_write_commits.py -u GRV96 -t tokens.txt -r GRV96/commitfetch
```

```
python demos/demo_write_commits.py -u GRV96 -t tokens.txt -r scottyab/rootbeer
```

Pour essayer `demo_write_commits.py` avec des nombres de commits variés,
utilisez les dépôts ci-dessous.

| Dépôt                     | Nombre de commits |
|---------------------------|:-----------------:|
| k9mail/k-9                | 12 840            |
| Skyscanner/backpack       | 7788              |
| mendhak/gpslogger         | 2811              |
| PeterIJia/android_xlight  | 397               |
| scottyab/rootbeer         | 191               |

#### Lecture des commits

`demo_read_commits.py` montre comment lire les représentations de commits
enregistrées dans un fichier texte. Pour confirmer que la lecture a
fonctionné, il affiche les données d'un commit dans la console.

Aide:

```
python demos/demo_read_commits.py -h
```

Exemples d'exécution:

```
python demos/demo_read_commits.py -c GRV96_commitfetch_commits.txt
```

```
python demos/demo_read_commits.py -c scottyab_rootbeer_commits.txt
```

## ENGLISH

This library helps obtaining the data of a repository's commits through the
GitHub API. Authentication with GitHub credentials is required.

### Content

**`Commit`**

This class contains data about a GitHub commit.

**`GitHubCredentials`**

This class contains the name of a GitHub user and authentication tokens that
they own. It helps making authenticated requests to the GitHub API. Each token
allows 5000 requests per hour.

**`GitHubUser`**

This class contains data about a GitHub user.

**`github_user_repository`**

This module stores `GitHubUser` instances. It uses their property `login` as a
key to grant access to them. Thus, this module helps preventing the creation of
many identical `GitHubUser` instances.

**`RepoIdentity`**

This class identifies a GitHub repository by its owner's name and the
repository's name. The identity is often written in the format `owner`/`name`.

**`extract_text_lines`**

This generator reads the specified text file and yields one of its lines at
each iteration. It allows for example to access tokens stored in a text file,
one per line.

**`get_repo_commits`**

This generator is the core element of `commitfetch`. It performs requests to
the GitHub API to obtain data about a repository's commits. Each iteration
yields a `Commit` instance. The user must provide their credentials in a
`GitHubCredentials` instance.

**`read_commit_reprs`**

This generator reads a text file that contains the representations of `Commit`
instances and recreates those objects. Each iteration yields a `Commit`
instance. The representations are strings returned by function `repr`. Each
line in the file must be a `Commit` representation. Empty lines are ignored.

**`write_commit_reprs`**

This function writes the representations of `Commit` instances in a text file.
The representations are strings returned by function `repr`. Each line of the
file is a representation. Function `read_commit_reprs` can read this file.

### Dependencies

Execute this command to install the dependecies.

```
pip install -r requirements.txt
```

### Demos

See scripts in directory `demos` to know how to use library `commitfetch`.

#### Recording commits

`demo_write_commits.py` obtains a GitHub repository's commits and writes their
representation in a text file. It needs a file that lists the user's
authentication tokens one per line to perform requests to the GitHub API. This
repository will ignore the token files if their name contains the string
"`token`".

Help:

```
python demos/demo_write_commits.py -h
```

Execution examples:

```
python demos/demo_write_commits.py -u GRV96 -t tokens.txt -r GRV96/commitfetch
```

```
python demos/demo_write_commits.py -u GRV96 -t tokens.txt -r scottyab/rootbeer
```

To try `demo_write_commits.py` with varied numbers of commits, use the
repositories below.

| Repository                | Number of commits |
|---------------------------|:-----------------:|
| k9mail/k-9                | 12 840            |
| Skyscanner/backpack       | 7788              |
| mendhak/gpslogger         | 2811              |
| PeterIJia/android_xlight  | 397               |
| scottyab/rootbeer         | 191               |

#### Reading commits

`demo_read_commits.py` shows how to read the commit representations recorded
in a text file. It confirms that the reading was successful by displaying a
commit's data in the console.

Help:

```
python demos/demo_read_commits.py -h
```

Execution examples:

```
python demos/demo_read_commits.py -c GRV96_commitfetch_commits.txt
```

```
python demos/demo_read_commits.py -c scottyab_rootbeer_commits.txt
```
