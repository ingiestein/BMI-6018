#!/usr/bin/env zsh

## DBMI repo commit
dbmi_commit() {
  folder="$HOME/Library/Mobile Documents/com~apple~CloudDocs/iCloud Documents/School/Biomedical Informatics Masters Degree/"

  echo "Commiting your DBMI repo..."

  git -C "$folder" add .

  echo "Added files and folder."

  datetime=$(date +"%Y-%m-%d %H:%M:%S")

  git -C "$folder" commit -m "$datetime"

  git -C "$folder" push origin main

  echo "git commit and push completed..."

}
