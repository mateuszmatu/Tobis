from run_opendrift import run_opendrift
import numpy as np
from datetime import datetime, timedelta

time = datetime.now()
run_opendrift(
    file = 'https://thredds.met.no/thredds/dodsC/fou-hi/norkystv3_800m_m00_be',
    start_time=time,
    geojson='/home/mateuszm/Tobis/tobis_singlepart.geojson',
    z = -5,
    duration=48,
    time_step=30,
    time_step_output=60,
    outfile=f'/home/mateuszm/Tobis/netcdf/{time}.nc',
    horizontal_diffusivity=0,
    coastline='Model',
    vertical_mixing=False,
    N=1000
)