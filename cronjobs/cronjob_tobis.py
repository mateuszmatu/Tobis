import sys
sys.path.append('/home/mateuszm/Tobis/')
from run_opendrift import run_opendrift
import numpy as np
from datetime import datetime, timedelta
import os

start = datetime.now()
end = start+timedelta(days=3)

times = np.arange(datetime(start.year,start.month,start.day,0), datetime(end.year,end.month,end.day,23), timedelta(minutes=60)).astype(datetime)

path = f'/lustre/storeB/project/fou/hi/oper/norkyst_v3/forecast/his_zdepths/{start.year}/{start.month:02d}/{start.day:02d}/'
file_list = [
    path+f'norkyst800_his_zdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_AN.nc',
    path+f'norkyst800_his_zdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0001.nc',
    path+f'norkyst800_his_zdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0002.nc',
    path+f'norkyst800_his_zdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0003.nc',
    path+f'norkyst800_his_zdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0004.nc',
    path+f'norkyst800_his_zdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0005.nc',
]

previous = start - timedelta(days=1)
p_output = f'/lustre/storeB/users/mateuszm/thredds/Tobis/tobis_{previous.year}{previous.month:02d}{previous.day:02d}.nc'
output = f'/lustre/storeB/users/mateuszm/thredds/Tobis/tobis_{start.year}{start.month:02d}{start.day:02d}.nc'

if os.path.exists(p_output):
    netCDF = p_output
else:
    netCDF = None

print(netCDF)
geojson = '/home/mateuszm/Tobis/tobis/tobis_singlepart.geojson'

run_opendrift(
    file = file_list,
    start_time=times,
    geojson=geojson,
    netCDF=netCDF,
    z = -5,
    duration=24 * 3, # 3 days
    time_step=30,
    time_step_output=60,
    outfile=output,
    traj_time_index=24,
    N=10000,
    particle_type='LarvalFish',
    egg_advection=False,
    density_grid=800,
)
