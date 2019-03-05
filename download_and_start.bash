#!/bin/bash
## Script that downloads the code for doing the Artificial Intelligence course exercises
cd /home/jovyan/
	
# git reflog requires a name and email if user is not in passwd
# even if you're only cloning
export GIT_COMMITTER_NAME=anonymous
export GIT_COMMITTER_EMAIL=anon@localhost
	
git clone https://github.com/alexjungaalto/PythonPlayground.git
pip install svgwrite pymc3 hiddenlayer pytorch-pretrained-bert
	
rm PythonPlayground/README.md
rm PythonPlayground/download_and_start.sh
rm download_and_start.sh
	
	
	
	