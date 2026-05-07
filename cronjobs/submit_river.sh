#!/bin/bash
#$ -S /bin/bash
#$ -l h_rt=4:00:00
#$ -q bigmem-r8.q
#$ -l h_rss=50G
#$ -l mem_free=50G 
#$ -l h_data=50G
#$ -o /lustre/storeB/users/mateuszm/thredds/oper/cronlog/output/
#$ -e /lustre/storeB/users/mateuszm/thredds/oper/cronlog/error/

source /home/mateuszm/.bashrc
conda activate opendrift
python /home/mateuszm/Tobis/cronjobs/cronjob_river.py
