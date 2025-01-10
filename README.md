# commitfetch

## FRANÇAIS

Cette bibliothèque aide à obtenir les données des commits d'un dépôt au moyen
de l'API de GitHub. Puisqu'il faut authentifier les requêtes à cette API,
l'utilisateur doit fournir des authentifications.

### Authentification des requêtes

Une authentification consiste en un nom d'utilisateur de GitHub et en un jeton
d'accès personnel (*personal access token*, *PAT*) appartenant à l'utilisateur
correspondant. Chaque authentification permet d'envoyer 5000 requêtes par heure
à l'API de GitHub. Une fois cette limite atteinte, on peut utiliser une autre
authentification pour effectuer plus de requêtes.

Cette bibliothèque représente les authentifications par des tuples contenant un
nom d'utilisateur (`str`, indice 0) et un jeton (`str`, indice 1). Les requêtes
reçoivent ces tuples en paramètre.

Il est possible d'écrire des authentifications dans un fichier texte. Le
générateur `read_github_credentials` décrit ci-dessous lit un tel fichier et
produit une authentification par itération. Pour que ce dépôt ignore les
fichiers de jetons, leur nom devrait correspondre au modèle `*cred*.txt`, où
l'astérisque (`*`) représente une chaîne de caractères quelconque.

### Contenu

**`Commit`**

Cette classe contient des données d'un commit de GitHub.

**`GitHubAPIError`**

Cette exception est levée quand une requête à l'API de GitHub échoue.

**`GitHubCredRepository`**

Cette classe conserve des authentifications sous forme de tuples. Pour
faciliter l'envoi de nombreuses requêtes dans une courte période, cette classe
permet d'itérer dans les authentifications.

**`GitHubUser`**

Cette classe contient des données d'un utilisateur de GitHub.

**`GitHubUserRepository`**

Ce singleton conserve des instances de `GitHubUser` identifiées par leur
proprité `login`. Ainsi, il aide à éviter la création de nombreuses instances
identiques de `GitHubUser`.

**`RepoIdentity`**

Cette classe identifie un dépôt GitHub par le nom de son propriétaire et le nom
du dépôt. L'identité est souvent écrite sous le format `propriétaire`/`nom`.

**`get_repo_commits`**

Ce générateur est l'élément principal de `commitfetch`. C'est lui qui effectue
les requêtes à l'API de GitHub pour obtenir les données des commits d'un dépôt.
Chaque itération produit une instance de `Commit`.

**`read_commit_reprs`**

Ce générateur lit un fichier texte contenant les représentations d'instances
de `Commit` et recrée ces objets. Chaque itération produit une instance de
`Commit`. Les représetations sont des chaînes de caractères renvoyées par la
fonction `repr`. Chaque ligne du fichier doit être une représentation d'un
`Commit`. Les lignes vides sont ignorées.

**`read_github_credentials`**

Ce générateur fournit des authentifications GitHub conservées dans un fichier
texte. Chaque ligne doit consister en un nom d'utilisateur GitHub et en un
jeton séparés par un deux-points. Les espaces sont autorisées avant et après
le deux-points. Les lignes vides sont ignorées. Chaque itération produit une
authentification sous forme de tuple.

Exemples de lignes valides dans le fichier d'authentifications:

`NomUtilisateur:ghp_a1b2c3d4e5f6`

`NomUtilisateur: ghp_a1b2c3d4e5f6`

`NomUtilisateur : ghp_a1b2c3d4e5f6`

**`write_commit_reprs`**

Cette fonction écrit les représentations d'instances de `Commit` dans un
fichier texte. Les représetations sont des chaînes de caractères renvoyées par
la fonction `repr`. Chaque ligne du fichier est une représentation. Le
générateur `read_commit_reprs` peut lire ce fichier.

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
représentation dans un fichier texte. Il a besoin d'un fichier d'authentifications
lisible par `read_github_credentials`. Ce dépôt ignore le fichier produit par
`demo_write_commits.py`.

Aide:

```
python demos/demo_write_commits.py -h
```

Exemples d'exécution:

```
python demos/demo_write_commits.py -c credentials.txt -r GRV96/commitfetch
```

```
python demos/demo_write_commits.py -c credentials.txt -r scottyab/rootbeer
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
GitHub API. The requests must be authentified with GitHub credentials.

### Request authentification

A GitHub credential consists of a GitHub username and a personal access token
(PAT) owned by the corresponding user. Each credential allows to send 5000
requests per hour to the GitHub API. After this limit is reached, another
credential can be used to make more requests.

This library represents credentials with tuples containing a username
(`str`, index 0) and a token (`str`, index 1). The requests take these tuples
as arguments.

It is possible to write credentials in a text file. Generator
`read_github_credentials` described below reads such a file and yields one
credential per iteration. For this repository to ignore credential files, their
name should match pattern `*cred*.txt`, where the asterisk (`*`) stands for any
character string.

### Content

**`Commit`**

This class contains data about a GitHub commit.

**`GitHubAPIError`**

This exception is raised when a request to the GitHub API fails.

**`GitHubCredRepository`**

This class stores credential tuples. To facilitate sending many requests in a
short period, this class allows to iterate through the credentials.

**`GitHubUser`**

This class contains data about a GitHub user.

**`GitHubUserRepository`**

This singleton stores `GitHubUser` instances identified by their property
`login`. Thus, it helps preventing the creation of many identical `GitHubUser`
instances.

**`RepoIdentity`**

This class identifies a GitHub repository by its owner's name and the
repository's name. The identity is often written in the format `owner`/`name`.

**`get_repo_commits`**

This generator is the core element of `commitfetch`. It performs requests to
the GitHub API to obtain data about a repository's commits. Each iteration
yields a `Commit` instance.

**`read_commit_reprs`**

This generator reads a text file that contains the representations of `Commit`
instances and recreates those objects. Each iteration yields a `Commit`
instance. The representations are strings returned by function `repr`. Each
line in the file must be a `Commit` representation. Empty lines are ignored.

**`read_github_credentials`**

This generator provides GitHub credentials stored in a text file. Each line
must consist of a GitHub username and a personal access token (PAT) separated
by a colon. Whitespaces are allowed before and after the colon. Empty lines are
ignored. Each iteration yields one credential tuple.

Examples of valid lines in the credential file:

`MyUsername:ghp_a1b2c3d4e5f6`

`MyUsername: ghp_a1b2c3d4e5f6`

`MyUsername : ghp_a1b2c3d4e5f6`

**`write_commit_reprs`**

This function writes the representations of `Commit` instances in a text file.
The representations are strings returned by function `repr`. Each line of the
file is a representation. Generator `read_commit_reprs` can read this file.

### Dependencies

Execute this command to install the dependecies.

```
pip install -r requirements.txt
```

### Demos

See scripts in directory `demos` to know how to use library `commitfetch`.

#### Recording commits

`demo_write_commits.py` obtains a GitHub repository's commits and writes their
representation in a text file. It needs a credential file readable by
`read_github_credentials`. This repository ignores the file produced by
`demo_write_commits.py`.

Help:

```
python demos/demo_write_commits.py -h
```

Execution examples:

```
python demos/demo_write_commits.py -c credentials.txt -r GRV96/commitfetch
```

```
python demos/demo_write_commits.py -c credentials.txt -r scottyab/rootbeer
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
