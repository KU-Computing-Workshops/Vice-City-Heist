# Vice-City-Heist
An incomplete Python script that is in the form of a GTA VI Heist in Vice City. Students are supposed to fix each function and learn Git doing so. There is also a hidden key in the repo, go along with us to find out more 👀.

---
 
## Before you start
 
1. Install **Git** (git-scm.com) and **Python** (python.org).
2. Create a free **GitHub** account (github.com).
3. Open **Visual Studio**, open a terminal, and check that both work:
```
git --version
python --version
```
4. Tell Git who you are (use your GitHub name and email):
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
 
---

## The big picture
 
- **Git** tracks every change to your files (what changed, when did it change, who changed it) so you can roll back to any version. It runs **locally** on your PC It's divided into **Local** and **Remote**.
  - **Local**: The folder you are working in is called **Working Directory**, then we save changes by moving them to the **Stage**, and then we can take the staged changes by **Commit**.
  - **Remote**: you can **clone** a repository to your local machine, **push** changes to the cloud/remote repo, and **fetch** & **pull** remote changes into the local repo.
- **GitHub** stores your repo in the cloud so teammates can share work. Like OneDrive, but for code.
- A **repository (repo)** is where all your versions and their history live.

---

## Part 1: Fork and clone
 
1. On this GitHub page, click **Fork** (top right) then **Create fork**. **IMPORTANT: CHOOSE THE OWNER AS KU-COMPUTING WORKSHOP.**
2. On **your fork's page**, click the green **Code** button and copy the HTTPS link.
3. In Visual Studio terminal:
```
cd Desktop
git clone (THE LINK YOU COPIED)
cd Vice-City-Heist
dir /a
```
   `dir /a` shows the hidden `.git` folder: that's the repo. **Clone** = downloaded files + full history + a link back to GitHub.
4. Open the `Vice-City-Heist` folder in Visual Studio / VS Code (**File > Open Folder**) and open `heist.py`.
5. Run it:
```
python heist.py
```
   You should see **0/7 missions complete**. Let's fix that.
 
---

## Part 2: Mission 1: your first commit
 
In `heist.py`, finish **Mission 1** (`welcome`). Save (Ctrl+S), then:
 
```
python heist.py
git status
git diff
```
 
- `git status` says `modified: heist.py`. Git noticed your change.
- `git diff` shows the lines you changed (`-` removed, `+` added). Press `q` if it gets stuck in a scrolling view.
Now save the change as a version. **Stage** it, then **commit** it:
 
```
git add heist.py
git status
git commit -m "Fix mission 1: welcome message"
git log --oneline
```
 
- `git add heist.py` stages the changes in the file.
- See how `git status` looks now.
- A commit locks the staged changes into your project's history. Write messages that say *what* you did, not `stuff`.

---

## Part 3: Staging practice
 
Fix **Mission 2** (`show_stars`), save, and try each of these, running `git status` after every one:
 
```
git add .
git status
git reset
git status
git add --all
git reset
git add heist.py
```
 
- `git add .` stages everything in the current directory and everything inside.
- `git add --all` / `git add -A` stages everything.
- `git add heist.py` stages one file.
- `git reset` **unstages** files to working directory, but it doesn't unstage deleted files, only new and modified files.

Finish with:
 
```
git commit -m "Fix mission 2: wanted stars"
```

**Exercise:** Fix **Mission 4** (`is_wasted`) and commit it with your own message.
 
---

## Part 4: Oops! Undoing things
 
**Mess up on purpose.** In `heist.py`, delete the return statement from Mission 5 and save. Run `python heist.py`: error or broken. Don't panic.

```
git status
git diff
git reset --hard
```
 
Look at your editor: the file snapped back to your last commit.
 
> `git reset --hard` **throws away all uncommitted changes**, including deleted files. It's great for undoing everything, but it's dangerous if you have work you want to keep.
 
**Committed too early?** undo the commit but keep your work with `git reset HEAD~`:
 
```
git add .
git commit -m "Oops, too early"
git reset HEAD~1
git status
```
The commit is gone, but your change is back in the working directory.

---

## Part 5: Branching and merging
 
A **branch** is a separate line of development. `main` is the central one. You experiment on a branch and merge into `main` when it's stable.
 
```
git branch
git branch fix-split
git checkout fix-split
```
- `git branch` gives you the current branch

The `*` marks the branch you're on. **Watch your editor** when you switch branches: the file will change in front of you.

- `git branch fix-split` creates a branch with the name 'fix-split'
- `git checkout fix-split` switches to the 'fix-split'
 
On `fix-split`, fix **Mission 7** (`split_the_take`). Save, test, and commit:
 
```
git add .
git commit -m "Fix mission 7: split the take"
git checkout main
```
 
Look at `heist.py`. Your Mission 7 fix **vanished**. It's safe on the other branch.
 
Now, on `main`, fix **Mission 3** (`payout`):
 
```
git add .
git commit -m "Fix mission 3: payout"
```
 
Merge the branch into `main`:
 
```
git merge fix-split -m "Merge fix-split into main"
git log --oneline
python heist.py
```
 
Both fixes are there. Git merged two different edits in the same file by itself. 
 
**Exercise:** Create a branch `fix-car`, fix **Mission 6** (`fastest_car`), commit, merge into `main`.

### Merge conflicts

A **conflict** happens when two branches change **the same line**, so Git can't decide. Let's cause one. Lucia and Jason (Jason? JSON? Who is JSON? 👀) disagree about the `HIDEOUT` line near the top of `heist.py`.
 
```
git branch lucia
git branch jason
git checkout lucia
```
 
Change `HIDEOUT = "Leonida Keys"` to `HIDEOUT = "Vice City Beach"`. Save.
 
```
git add .
git commit -m "Lucia picks the beach"
git checkout jason
```
 
Change that **same line** to `HIDEOUT = "Grassrivers"`. Save.
 
```
git add .
git commit -m "Jason picks Grassrivers"
git merge lucia
```
 
**CONFLICT!** Open `heist.py`. The top now contains:
 
```
<<<<<<< HEAD
HIDEOUT = "Grassrivers"
=======
HIDEOUT = "Vice City Beach"
>>>>>>> lucia
```
 
- Between `<<<<<<< HEAD` and `=======` is **your branch** (`jason`).
- Between `=======` and `>>>>>>> lucia` is the **incoming** branch.
Your editor shows clickable options: **Accept Current Change**, **Accept Incoming Change**, **Accept Both**. Pick one (or edit by hand). The final file must have **only the line you want and none of the `<<<`, `===`, `>>>` marker lines**. Save, then:
 
```
git add .
git commit -m "Resolve hideout conflict"
git checkout main
git merge jason
```
 
(If you panic mid-merge: `git merge --abort`.)
 
---

## Part 6: Time travel
 
```
git log --oneline
```
 
Each line is `commit-id message`. Visit an old commit using an id from **your** log:
 
```
git checkout (PUT ID HERE)
python heist.py
```
 
Your editor shows the old version of the file, and the score is lower. Git warns about a "detached HEAD". That's fine: you're just visiting. Don't edit here. Go home:
 
```
git checkout main
```
 
Compare two commits (**older id first**):
 
```
git diff (NEW ID) (OLD ID)
```
 
Press `q` to exit.
 
**Exercise 1:** Find the commit where Mission 3 got fixed, using `git log --oneline` and `git diff`. What was the line before and after?

**Exercise 2:** There is a hidden key in the commit history of the repo. Can you use `git log --oneline` and `git checkout ID` to find it?
 
---

## Part 7: Push to GitHub
 
So far **nothing has left your computer**. Time to push:
 
```
git push origin main
```
 
- `origin` is the nickname for your GitHub repo. `main` is the branch you're pushing.
- Refresh your fork on GitHub. Your fixes are there.
Branches are pushed one at a time:
 
```
git push origin fix-split
git push origin lucia
```
 
### Fetch vs pull
 
On GitHub, open `heist.py`, click the pencil, change `CREW_NAME` to your own crew name, and click **Commit changes**. GitHub now has something your computer doesn't.
 
```
git fetch
git status
```
 
`fetch` downloads the changes **without** merging them. `git status` says you're **behind**. Your file hasn't changed yet. Now merge:
 
```
git merge
```
 
Make another change on GitHub (change `HIDEOUT`) and commit. This time:
 
```
git pull
```
 
**Pull = fetch + merge.** It's the one you'll use every day.
 
---
