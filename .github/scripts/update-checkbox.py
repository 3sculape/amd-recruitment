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

    # Get the comments on the pull request
    comments = pr.get_issue_comments()

    # Regular expression to match the mentioned pull request format
    pr_mention_pattern = re.compile(r'#(\d+)')

    # Loop through the comments
    for comment in comments:
        # Check if the comment contains a mentioned pull request
        matches = pr_mention_pattern.findall(comment.body)
        for match in matches:
            mentioned_pr_number = int(match)
            print(mentioned_pr_number)

            # Check if the mentioned pull request is closed
            mentioned_pr = repo.get_pull(mentioned_pr_number)
            if mentioned_pr.state == 'closed':
                # Update the original comment with a checked checkbox
                updated_body = comment.body.replace(f"[ ] PR #{pr_number}", f"[x] PR #{pr_number}")
                comment.edit(body=updated_body)

if __name__ == "__main__":
    repo_name = os.getenv('REPO_NAME')
    pr_number = os.getenv('PR_NUMBER')
    token = os.getenv('GITHUB_TOKEN')

    update_checkbox(token, repo_name, pr_number)
