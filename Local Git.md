# Streamlining Git For Introduction to Python

This will be a simple guide for Mac/Linux. I don't use PC, so won't be able to help much on that platform, but the principles will be similar.

**Before you follow any of the following commands in your terminal, you should know exactly what it will do. Blindly running commands in your terminal can be dangerous.**

## Terminal Package Manager

There are programs called package managers. They help download free, open source software for your use. I use Homebrew. It works on Mac and Linux. I don't do any programming on PC. To install is run this command in your terminal:

```
 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This command will install the Homebrew package manager.

## Packages that are helpful (but not necessary)

- [pyenvi](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

The 'pyenv' package and the plugin 'pyenv-virtualenv' are designed to help download and manage python versions, and then to create virtual environments using those different versions. They require some learning, and a some setup in your terminal configuration file. If this feels like to much, you can ignore these and still get things to work for you.

## Create a local git repository (repo)

I created a parent directory for the class somewhere convenient (like under Documents). The following commands moves to your Documents folder, creates a directory called "6018 Intro to Python" and then changes directory to that folder. If you already have a folder for the class just 'cd' into that one.

```
cd ~/Documents/
mkdir "6018 Intro to Python"
cd "6018 Intro to Python"
```

In this folder you can create a local git repository. Git is software that tracks all file changes in a folder and its subfolders.

```
git init
```

This command initializes a git repository locally. If you already have a git repository here you should see an error saying that. We need a file to commit though. You could make a readme file like this and then add it to your git repository.

```
touch Readme.md
git add .
```

This will create a new empty file called "Readme.md" and then add all the files/folders inside the current directory. Then you need to commit the files to your git repository.

```
git commit -m "First Commit"
git branch -M main
```

These commands commit all changes added in the previous step and give a message called "First Commit." It then makes sure your current branch is the "main" branch. Don't spend too much time now worrying about "branches."

Once you have a git repository locally, you need to make one on [GitHub.](https://www.github.com) Go to your account, create a new repository, name it something meaningful (like 6018 Intro to Python) and click next. You will see a screen which shows your repo name, and a box with "Quick setup - if you've done this kind of thing before."

Further down you'll see some instructions. The section "... or create a new repository from the command line". You'll notice that we've done most of the commands from this section already. All that's left to do is "push" our git repository to GitHub.

```
git remote add origin https://github.com/{your_github_username}/{your_repo_name}.git
git push -u origin main
```

These commands tie your local git repository to the newly made GitHub repository. It will then "push" all your local files/folder to Github. Make sure to replace {your_github_username} and {your_repo_name} with whatever your user name and repo are.

WARNING: Do not commit any files that contain sensitive information, ever!

## Uploading new assignments

Now that you have your local repo connected with your GitHub, all you have to do is commit locally, and push to GitHub whenever you finish an assignment. For example, in your 6018 folder, you've made a subfolder called "assignments", and within that folder you have your file 'assignment_3.ipynb'. You've just finished all the questions, saved it, and now want to get it to GitHub.

```
cd ~/Documents/'6018 Intro to Python'
git add .
git commit -m "My newest commit"
git push -u origin main
```

These commands first change directory to the parent directory of your git repo. You then add all files inside. Git figures out what's new and changes and adds them to get ready to commit the changes, and the does that with a short message describing the changes since last time. You then push these changed to GitHub.

Now all you have to do is navigate in your web browser to your GitHub repo and the file you want. Copy the URL in the top bar, paste that into Canvas for submission. You don't have to manage anything through the GitHub repo. You don't have to fiddle with the GitHub desktop application (which I find more annoying than helpful).

## Automate

If you're tired of typing all those lines over and over again, you could create a short bash script to do it for you. If you know how to edit your .zshrc file (and now what that even is) you could define a small function there to do it for you.

```zsh
dbmi_commit() {
 cd ~/Documents/'6018 Intro to Python'
 git add .
 git commit -m "$(date +"%Y-%m-%d %H:%M:%S")"
 git push -u origin main
}
```

All you would need to type is "dbmi_commit" and then you it will run that function, run those commands, commit with a date for the commit message, and the push to GitHub for you.
