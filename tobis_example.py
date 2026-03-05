from run_opendrift import run_opendrift
import numpy as np
from datetime import datetime, timedelta
start_date = datetime(2026,3,1,6)
end_date = datetime(2026,3,1,9)

times = np.arange(start_date, end_date, timedelta(minutes=60)).astype(datetime)
#times = '2026-03-01T00:00:00'
#run_opendrift(
#    file = 'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_800m_m00_be',
#    rls = 'particles_example.rls',
#    z = -5,
#    duration=1,
#    time_step=30,
#    time_step_output=60,
#    outfile='test_rls.nc',
#    horizontal_diffusivity=0,
#    coastline='Model',
#    vertical_mixing=False
#)

run_opendrift(
    file = 'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_800m_m00_be',
    start_time=times,
    geojson='tobis_singlepart.geojson',
    z = [-5, -10],
    duration=5,
    time_step=30,
    time_step_output=60,
    outfile='test_geojson_c.nc',
    horizontal_diffusivity=0,
    coastline='Model',
    vertical_mixing=False,
    N=1
)
lon, lat = 6.118, 62.195
#run_opendrift(
#    file = 'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_800m_m00_be',
#    start_time=times,
#    lon = lon, lat = lat,
#    z = -5,
#    duration=5,
#    time_step=30,
#    time_step_output=60,
#    outfile='test_geojson.nc',
#    horizontal_diffusivity=0,
#    coastline='Model',
#    vertical_mixing=False,
#    N=1
#)