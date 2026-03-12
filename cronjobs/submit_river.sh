#!/bin/bash
#$ -S /bin/bash
#$ -l h_rt=2:00:00
#$ -q research-r8.q
#$ -l h_rss=30G
#$ -l mem_free=30G 
#$ -l h_data=30G
#$ -o /lustre/storeB/users/mateuszm/thredds/oper/cronlog/output/
#$ -e /lustre/storeB/users/mateuszm/thredds/oper/cronlog/error/

source /home/mateuszm/.bashrc
conda activate opendrift
python /home/mateuszm/Tobis/cronjobs/cronjob_river.py
