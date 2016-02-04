# aeri-108-plots
When the script "plot_sgpc1_metadata.py" is ran the matplotlib "figure_1.png" is created. Test code used to create the script is containted in the IPython Notebook "codetest.ipynb".

Script plots data found in .cdf files that were too large to add to this repo. Plots were made in order to troubleshoot a power outage.
Official filed report for power outage:
>Upon power being restored the laser signal was low and below the critical threshold so the interferometer went into open loop mode.  This is to prevent the instrument from trying to find the correct alignment when the laser is dead.  When that happens the white light or mechanical arm get broken.  I logged on and did some checks on the laser level and they looked fine.  After those checks I restarted it it started working. A DQR should be filed for when the instrument was in open loop mode. We were down from the power outage starting at 12/28/2015 @ 2:57 UTC.  The system was up but with unusable data 12/31/2015 @ 15:16 UTC to 01/04/2016 @ 16:23:39 UTC.

First time using the Python packages netCDF4 and matplotlib. Things could have been done more efficiently in many places.
