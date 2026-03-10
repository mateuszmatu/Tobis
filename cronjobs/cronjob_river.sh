#!/bin/bash

export PATH="/usr/local/bin:/usr/bin:/bin"
source /etc/profile.d/sge.sh
/opt/sge/bin/lx-amd64/qsub /home/mateuszm/Tobis/cronjobs/submit_river.sh