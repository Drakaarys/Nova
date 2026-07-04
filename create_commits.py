import os
import random
import subprocess
from datetime import datetime, timedelta

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)

# 1. Get all untracked and modified files
# Untracked files
untracked = run_cmd("git ls-files --others --exclude-standard").strip().split('\n')
# Modified files
modified = run_cmd("git ls-files -m").strip().split('\n')

all_files = list(set([f for f in untracked + modified if f]))

# Ensure we have files to commit
if not all_files:
    print("No files to commit.")
    exit()

print(f"Total files to commit: {len(all_files)}")

# 2. Assign files to 58 commits
total_commits = 58
commits = [[] for _ in range(total_commits)]

# Distribute 1 file to each commit, if we have enough files
if len(all_files) >= total_commits:
    for i in range(total_commits):
        commits[i].append(all_files[i])
    for i in range(total_commits, len(all_files)):
        idx = random.randint(0, total_commits - 1)
        commits[idx].append(all_files[i])
else:
    # If fewer files than 58, put 1 file in as many commits as possible
    for i in range(len(all_files)):
        commits[i].append(all_files[i])

# 3. Determine number of commits per day (June 24 to July 7, 2026)
year = 2026
start_date = datetime(year, 6, 24, 12, 0, 0)
num_days = 14

commits_per_day = [1] * num_days
remaining = total_commits - num_days

while remaining > 0:
    idx = random.randint(0, num_days - 1)
    commits_per_day[idx] += 1
    remaining -= 1

print(f"Commits per day: {commits_per_day}")
print(f"Total commits: {sum(commits_per_day)}")

# 4. Create commits
commit_idx = 0
for i, num_commits in enumerate(commits_per_day):
    current_date = start_date + timedelta(days=i)
    
    for j in range(num_commits):
        commit_time = current_date + timedelta(minutes=random.randint(1, 400))
        date_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        files_to_commit = commits[commit_idx]
        
        if files_to_commit:
            for f in files_to_commit:
                # Need to use quotes for files with spaces
                run_cmd(f'git add "{f}"')
            msg = f"Automated commit for {len(files_to_commit)} files"
        else:
            msg = "Automated empty commit"
            
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        cmd = ["git", "commit", "-m", msg]
        if not files_to_commit:
            cmd.append("--allow-empty")
            
        subprocess.run(cmd, env=env, check=True)
        
        commit_idx += 1

print("Done making commits.")
