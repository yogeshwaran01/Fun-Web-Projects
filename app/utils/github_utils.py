from collections import Counter
from github import Github

gh = Github("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")

class UserStats:

    def __init__(self, username: str):
        self.user = gh.get_user()
        self.user_repos = self.user.get_repos()
        self.name = self.user.name
        self.bio = self.user.bio
        self.web = self.user.blog
        self.stars = sum([repo.stargazers_count for repo in self.user_repos])
        self.forks = sum([repo.forks_count for repo in self.user_repos])
        self.commits = sum([0 if repo.fork else repo.get_commits().totalCount for repo in self.user_repos])
        self.repos_count = len(list(self.user_repos))
        self.followers = self.user.followers


    def stats(self):
        return {
            'name': self.name,
            'bio': self.bio,
            'web': self.web,
            'stars': self.stars,
            'forks': self.forks,
            'commits': self.commits,
            'repos': self.repos_count,
            'followers': self.followers,
            'pic': self.user.avatar_url,
        }


    def repos_per_langs(self):
        data = []
        langs = [repo.language for repo in self.user_repos]
        for lang in langs:
            count = 0
            for repo in self.user_repos:
                if repo.language == lang:
                    count = count + 1
                else:
                    pass
            data.append((lang, count))
        c = Counter(data)
        return c

    def star_per_langs(self):
        star_lang_data = []
        for repo in self.user_repos:
            star = repo.stargazers_count
            name = repo.name
            star_lang_data.append((name, star))
        return star_lang_data

    def commit_per_repo(self):
        commits = []
        for repo in self.user_repos:
            commit_count = repo.get_commits().totalCount
            if repo.fork:
                pass
            else:
                name = repo.name
                commits.append((name, commit_count))
        
        return commits
    
    def star_per_repo(self):
        star = []
        for repo in self.user_repos:
            commit_count = repo.stargazers_count
            name = repo.name
            star.append((name, commit_count))

        return star
