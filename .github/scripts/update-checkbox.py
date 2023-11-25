import os
import re
from github import Github

def update_checkbox(token, repo_name, pr_number):
    # Create a GitHub API client
    g = Github(token)

    # Get the repository
    repo = g.get_repo(repo_name)

    # Get the pull request
    pr = repo.get_pull(int(pr_number))

    # Get the timeline events on the pull request
    events = pr.as_issue().get_timeline()

    # Loop through the events
    for event in events:
        if event.event == "cross-referenced":
            # Found a cross-reference
            mentioned_pr = event.source.issue
            comments = mentioned_pr.get_comments()
            # Search for checkbox and ticks it
            for comment in comments:
                if f"[ ] PR #{pr_number}" in comment.body:
                    updated_body = comment.body.replace(f"[ ] PR #{pr_number}", f"[x] PR #{pr_number}")
                    comment.edit(body=updated_body)

if __name__ == "__main__":
    repo_name = os.getenv('REPO_NAME')
    pr_number = os.getenv('PR_NUMBER')
    token = os.getenv('GITHUB_TOKEN')

    update_checkbox(token, repo_name, pr_number)
