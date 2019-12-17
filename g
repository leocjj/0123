#!/bin/bash
#./g 'File_to_push' 'Commit message'
git add $1
git commit -m $2
git push origin master
