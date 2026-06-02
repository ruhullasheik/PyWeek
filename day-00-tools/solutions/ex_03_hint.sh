# Hints for ex_03

# Create a new repo outside PyWeek
mkdir /tmp/my-first-repo
cd /tmp/my-first-repo
git init

# Create file and make commits
echo "Once upon a time..." > story.txt
git add story.txt
git commit -m "beginning"

echo "...there was a Python programmer." >> story.txt
git add story.txt
git commit -m "middle"

echo "...who learned Git in one day. The end." >> story.txt
git add story.txt
git commit -m "end"

# View history
git log --oneline

# What if you want to see what changed between commits?
# git diff <hash1> <hash3>
