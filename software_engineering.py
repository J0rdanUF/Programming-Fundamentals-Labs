
echo "# Programming-Fundamentals-Labs" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/J0rdanUF/Programming-Fundamentals-Labs.git
git push -u origin main

input1 = int(input('Pick a number to add: '))
input2 = int(input('Pick another number to add: '))
result = input1 + input2
