
import sys
sys.path.append('/home/mateuszm/Tobis/')
from run_opendrift import run_opendrift
import numpy as np
from datetime import datetime, timedelta
import pandas as pd

rivers = pd.read_csv('/home/mateuszm/Tobis/rivers/rivers_adjusted.csv')

start = datetime.now()
end = start+timedelta(days=3)

times = np.arange(datetime(start.year,start.month,start.day,0), datetime(end.year,end.month,end.day,23), timedelta(minutes=60)).astype(datetime)

path = f'/lustre/storeB/project/fou/hi/oper/norkyst_v3/forecast/his/{start.year}/{start.month:02d}/{start.day:02d}/'
file_list = [
    path+f'norkyst160_his_sdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m71_AN.nc',
    path+f'norkyst160_his_sdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m71_FC_0001.nc',
    path+f'norkyst160_his_sdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m71_FC_0002.nc',
    path+f'norkyst800_his_sdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_AN.nc',
    path+f'norkyst800_his_sdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0001.nc',
    path+f'norkyst800_his_sdepth_{start.year}{start.month:02d}{start.day:02d}T00Z_m00_FC_0002.nc'
]

for index, river in rivers.iterrows():
    print(river['river'], river['lon'], river['lat'])
    run_opendrift(
    file = file_list,
    lon = river['lon'],
    lat = river['lat'],
    z=-0.5,
    start_time=times,
    duration=24 * 3, # 3 days
    time_step=15,
    time_step_output=60,
    outfile=f'/lustre/storeB/users/mateuszm/thredds/oper/{river['river']}/{river['river']}_{start.year}{start.month:02d}{start.day:02d}.nc',
    horizontal_diffusivity=0,
    coastline='Model',
    N=50,
    radius=30,
    depth_type='s',
    track_vars=['sea_water_temperature', 'sea_water_salinity'],
    density_grid=200,
    vertical_mixing=True,
    vertical_advection=True
    )