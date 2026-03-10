from run_opendrift import run_opendrift
import numpy as np
from datetime import datetime, timedelta

lon, lat = 10.241, 59.738 # drammenselva
lon, lat = 6.118, 62.195  # ørstaelva
start_date = datetime(2025,11,18,6)
end_date = datetime(2025,11,22,23)

times = np.arange(start_date, end_date, timedelta(minutes=30)).astype(datetime)
start_time='2025-11-18T06:00:00'

def one_depth():
    run_opendrift(
        file = '/home/mateuszm/FOCCUS/applications/drift/symlink_m71/',
        lon = lon,
        lat = lat,
        z=-0.5,
        start_time=times,
        duration=100,
        time_step=15,
        time_step_output=15,
        outfile=f'#/lustre/storeB/users/mateuszm/RiverPlume/drammen/river_plume_{start_time}.nc',
        horizontal_diffusivity=0,
        coastline='Model',
        N=100,
        radius=30,
        depth_type='s',
        track_vars=['sea_water_temperature', 'sea_water_salinity'],
        density_grid=200
    )

def multi_depth():
    run_opendrift(
        #file = '/home/mateuszm/FOCCUS/applications/drift/symlink_m70/',
        file = 'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_160m_m70_be',
        lon = lon,
        lat = lat,
        z=np.linspace(-0.5,-10,5),
        start_time=times,
        duration=100,
        time_step=15,
        time_step_output=15,
        outfile=f'/lustre/storeB/users/mateuszm/RiverPlume/orsta/z_multi_depth_river_plume_{start_time}.nc',
        horizontal_diffusivity=0,
        coastline='Model',
        N=100,
        radius=30,
        depth_type='s',
        track_vars=['sea_water_temperature', 'sea_water_salinity'],
        density_grid=200
    )

def multi_depth_vertical():
    run_opendrift(
        #file = '/home/mateuszm/FOCCUS/applications/drift/symlink_m70/',
        file = 'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_160m_m70_be',
        lon = lon,
        lat = lat,
        z=np.linspace(-0.5,-10,5),
        start_time=times,
        duration=100,
        time_step=15,
        time_step_output=15,
        outfile=f'/lustre/storeB/users/mateuszm/RiverPlume/orsta/z_multi_depth_vertical_river_plume_{start_time}.nc',
        horizontal_diffusivity=0,
        coastline='Model',
        N=100,
        radius=30,
        depth_type='z',
        track_vars=['sea_water_temperature', 'sea_water_salinity'],
        density_grid=200,
        vertical_mixing=True
    )

if __name__ == '__main__':
    #multi_depth()
    multi_depth_vertical()
