from run_opendrift import run_opendrift
import numpy as np
from datetime import datetime, timedelta
start_date = datetime(2026,3,2,0)
end_date = datetime(2026,3,4,0)

times = np.arange(start_date, end_date, timedelta(minutes=60)).astype(datetime)
#times = '2026-03-03T00:00:00'

lon = 5.35
lat = 57

files = [
    'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_800m_m00_be',
    'https://thredds.met.no/thredds/dodsC/cmems/topaz5phy_6hr_bulletins/topaz5_phy_6hr_b2025-05-01T00.ncml',
    'https://thredds.met.no/thredds/dodsC/cmems/topaz5phy_6hr_bulletins/topaz5_phy_6hr_b2025-05-02T00.ncml',
    'https://thredds.met.no/thredds/dodsC/cmems/topaz5phy_6hr_bulletins/topaz5_phy_6hr_b2025-05-03T00.ncml'
]
run_opendrift(
    file = files,
    start_time=times,
    lon=lon,
    lat=lat,
    #radius=100000,
    #geojson='tobis/tobis_singlepart.geojson',
    #rls = 'tobis/particles_example.rls',
    netCDF='test1.nc',
    z = -5,
    duration=48,
    time_step=60,
    time_step_output=60,
    outfile=f'test2.nc',
    traj_time_index=24, 
    coastline='Model',
    vertical_mixing=False,
    N=1,
    particle_type='LarvalFish',
    egg_advection=False
)