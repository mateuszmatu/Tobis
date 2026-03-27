#!/bin/bash
#$ -S /bin/bash
#$ -l h_rt=3:00:00
#$ -q bigmem-r8.q
#$ -l h_rss=60G
#$ -l mem_free=60G 
#$ -l h_data=60G
#$ -o /lustre/storeB/users/mateuszm/thredds/Tobis/cronlog/output/
#$ -e /lustre/storeB/users/mateuszm/thredds/Tobis/cronlog/error/

source /home/mateuszm/.bashrc
conda activate opendrift
python /home/mateuszm/Tobis/cronjobs/cronjob_tobis.py
