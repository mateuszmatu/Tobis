import os
from datetime import datetime, timedelta

start = datetime.now()
end = start+timedelta(days=4)

os.system("source /home/havis/.cmems_login")

datasets = {'3Dcurr': 'cmems_mod_nws_phy-cur_anfc_1.5km-3D_PT1H-i',
            '3Dsalt': 'cmems_mod_nws_phy-sal_anfc_1.5km-3D_PT1H-i',
            '3Dtemp': 'cmems_mod_nws_phy-tem_anfc_1.5km-3D_PT1H-i'}

for key, dataset in datasets.items():
    os.system(f"/home/ecf-prod/.conda/envs/copernicusmarine_2_0/bin/copernicusmarine subset --overwrite --dataset-id {dataset} --start-datetime {start.strftime('%Y%m%d')} --end-datetime {end.strftime('%Y%m%d')} --output-filename {key}")