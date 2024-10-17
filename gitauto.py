from github import Github
import os

#Replace 'your_access_token' with your GitHub personal access token
g = Github("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")

#Replace 'repo_owner' and 'repo_name' with the owner and name of the repository
repo_owner = 'JMojicaR'
repo_name = 'gitautotest'
repo = g.get_repo(f"{repo_owner}/{repo_name}")
pwd = os.getcwd()

#Iterate through all open pull requests in the repository
for pull_request in repo.get_pulls(state='open'):
    print(f"Checking Pull Request #{pull_request.number} - {pull_request.title}")

    #Get the list of files changed in the pull request
    files = pull_request.get_files()

   #Iterate through each file and print the added lines
    for file in files:
        print(f"File: {file.filename}")

        #Fetch the content of the patch for the file
        patch_content = file.patch

        #Split the patch content into lines
        patch_lines = patch_content.split('\n')

        #Identify and print added lines
        added_lines = [line[2:] for line in patch_lines if line.startswith('+ ') and not line.startswith('+++')]
        print("Added Lines:")
        file = open(f'{pwd}/{repo_owner}/{repo_name}/changed_lines.txt', 'w')
        for added_line in added_lines:
            file.write(added_line + '\n')

        print("\n" + "=" * 50 + "\n")  # Separating each file's output
        #Identify and print deleted lines
        deleted_lines = [line[2:] for line in patch_lines if line.startswith('- ') and not line.startswith('---')]
        print("Deleted Lines:")
        for deleted_line in deleted_lines:
            print(deleted_line)

        print("\n" + "=" * 50 + "\n")  # Separating each file's output

    print("\n" + "=" * 50 + "\n")  # Separating each pull request's output