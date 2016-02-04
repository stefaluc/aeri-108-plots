#/usr/bin/env ipython
from netCDF4 import Dataset
from dateutil.parser import parse
import matplotlib.pyplot as plt
import numpy as np
import os, datetime

# Create correct file path for netCDF to use
fp = '/Users/lstefanski/aeri_data/sgp-c1/' # location of data files
fps_part = os.listdir(fp) # file names in fp directory
fps = []
for files in fps_part:
    full_fp = fp + files
    fps.append(full_fp)

# Fill list full of netCDF objects
cdfs = []
for files in fps:
    cdfs.append(Dataset(files, mode='r'))

def get_data(varstr, cdfs):
    values = []
    for x in cdfs:
        values.append(x.variables[varstr][:])
    values_all = []
    for row in values:
        for col in row:
            values_all.append(col)
    return values_all # a single dimensional list of the values of param varstr

# Converts time from CDF files from the float format "YYMMDD HHMMSS" to the datetime
# format of "YYYY-MM-DD HH:MM:SS"
def get_time(cdfs):
    dateYYMMDD = get_data('dateYYMMDD', cdfs)
    timeHHMMSS = get_data('timeHHMMSS', cdfs)
    times_fix = []
    for x,y in zip(dateYYMMDD, timeHHMMSS):
        x = str(int(x))
        y = str(int(y))
        #append 0s to end of time to complete HHMMSS
        #!HIGH COMPLEXITY. INEFFICIENT!
        if len(y) < 6:
            for i in range(6 - len(y)):
                y = '0' + y
        datestr = x + ' ' + y # "YYMMDD HHMMSS"
        times_fix.append(parse(datestr)) 
    return times_fix # single dimensional list of standardized times

# Y-var data to plot
LWresponsivity = get_data('LWresponsivity', cdfs)
SWresponsivity = get_data('SWresponsivity', cdfs)
LW_HBB_NEN = get_data('LW_HBB_NEN', cdfs)
SW_HBB_NEN = get_data('SW_HBB_NEN', cdfs)

# X-var data to plot
times = get_time(cdfs)

# Instantiate figure
fig = plt.figure()
plt.xlabel('Date')
# Add subplots to figure
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412, sharex=ax1)
ax3 = fig.add_subplot(413, sharex=ax1)
ax4 = fig.add_subplot(414, sharex=ax1)
# Plot data
ax1.plot(times, LWresponsivity)
ax2.plot(times, SWresponsivity)
ax3.plot(times, LW_HBB_NEN)
ax4.plot(times, SW_HBB_NEN)
# Label subplots
ax1.set_ylabel('LWresponsivity')
ax2.set_ylabel('SWresponsivity')
ax3.set_ylabel('LW HBB NEN')
ax4.set_ylabel('SW HBB NEN')
# Restrict axis bounds
#ax1.axis([0,31, 0, .16])
#ax2.axis([0,31, 0, 1.2])
#ax3.axis([0,31, 0, 500])
#ax4.axis([0,31, 0, 45])

# Show plot
plt.show()

