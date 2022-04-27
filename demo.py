from commitfetch import\
	get_repo_commits,\
	GitHubCredentials

repository = "scottyab/rootbeer" # 191 commits
#repository = "mendhak/gpslogger" # 2233 commits

tokens = (
	"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",
	"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")

credentials = GitHubCredentials("GRV96", tokens)

commits = get_repo_commits(repository, credentials, False)

first_commit = commits[0]

print(f"SHA: {first_commit.sha}")
print(f"Repository: {first_commit.repository}")
print(f"Author: {first_commit.author}")
print(f"Moment: {first_commit.moment_to_str()}")
print("Files:")
for file in first_commit.files:
	print(f"\t{file}")
