#!/bin/bash

git config --global user.name "HYEZ"
git config --global user.email oohyejioo@gmail.com

message=""

if [ "$1" = "" ]
then message="HEYZ is too busy to write commit message."
else message=$1
fi

git add .
git commit -m "$message"
git push -u origin master
