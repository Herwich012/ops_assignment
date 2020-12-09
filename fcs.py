import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs #conda install cartopy
import cartopy.feature as cfeature

#%% Data acquisition
def aploc(APlist):
    """
    AIRPORT LAT&LONG data,
    FIRST AIRPORT SHOULD BE THE HUB!\n
    This function requires airports.csv 
    to be in the same folder!\n
    APlist = list of strings:
    3-letter IATA codes of requested airports\n
    Returns: Numpy array with size [[# of airports][3]]
    Row example: ['OAK', 37.721298, -122.221001]
    """
    df = pd.read_csv('airports.csv', header=None, usecols=[4,6,7])
    df.columns = ["IATA","lat","long"]
    
    apl = np.empty((len(APlist),2))                 #airport locs
    apn = np.empty((len(APlist),1), dtype=object)   #column with airport names
    for i in range(len(APlist)):
        dfi = df[df['IATA'].str.match(APlist[i])]
        apl[i,0] = dfi.to_numpy()[0,1]
        apl[i,1] = dfi.to_numpy()[0,2]
        apn[i,0] = str(dfi.to_numpy()[0,0])
    aps = np.hstack((apn,apl))                      #add column of names to lat&long data
    return aps


#%% Plotting
def solplot(aplocs,solarcs):
    """
    Parameters
    ----------
    aplocs : np.array
        output of the aploc function
    solarcs : list
        list of arcs beloning to the solution

    Returns
    -------
    Figure of solution

    """
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal(),frameon=False)
    ax.patch.set_visible(False)
    ax.set_extent([-120, -70, 22, 50], ccrs.Geodetic())
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.STATES)
    for i,j in solarcs: #plot lines of solution
        plt.plot([aplocs[i,2],aplocs[j,2]], [aplocs[i,1],aplocs[j,1]],
                 transform=ccrs.Geodetic(), c='b', alpha=0.5)
    ax.scatter(aplocs[1:,2],aplocs[1:,1],transform=ccrs.PlateCarree(), 
               zorder=2) #plot clients
    ax.plot(aplocs[0,2], aplocs[0,1], c='r', marker='s',
            transform=ccrs.PlateCarree(), zorder=2) #plot hub
    for i in range(len(aplocs)): #annotate locations
        ax.text(aplocs[i,2]+0.5, aplocs[i,1]-0.5, str(aplocs[i,0]),
                weight='bold', transform=ccrs.Geodetic(), zorder=2)
    plt.show()

#%% Plotting with time windows
def solplottw(aplocs,solarcs,twb,twe,tau):
    """
    Parameters
    ----------
    aplocs : np.array
        output of the aploc function
    solarcs : list
        list of arcs beloning to the solution

    Returns
    -------
    Figure of solution

    """
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal(),frameon=False)
    ax.patch.set_visible(False)
    ax.set_extent([-120, -70, 22, 50], ccrs.Geodetic())
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.STATES)
    for i,j in solarcs: #plot lines of solution
        plt.plot([aplocs[i,2],aplocs[j,2]], [aplocs[i,1],aplocs[j,1]],
                 transform=ccrs.Geodetic(), c='b', alpha=0.5)
    ax.scatter(aplocs[1:,2],aplocs[1:,1],transform=ccrs.PlateCarree(), 
               zorder=2) #plot clients
    ax.plot(aplocs[0,2], aplocs[0,1], c='r', marker='s',
            transform=ccrs.PlateCarree(), zorder=2) #plot hub
    for i in range(1, len(aplocs)): #annotate locations
        anntxt = str(aplocs[i,0]) + '-' + str(twb[i]) + '-' + str(twe[i]) + '-' + '%0.1f' % (tau[i])
        ax.text(aplocs[i,2]+0.5, aplocs[i,1]-0.5, anntxt, weight='bold', transform=ccrs.Geodetic(), zorder=2)
    plt.show()


def hubplot(aplocs):
    """Plot the locations without solution for validation"""
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal(),frameon=False)
    ax.patch.set_visible(False)
    ax.set_extent([-120, -70, 22, 50], ccrs.Geodetic())
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.STATES)
    ax.scatter(aplocs[1:,2],aplocs[1:,1],transform=ccrs.PlateCarree(), zorder=2)
    ax.plot(aplocs[0,2], aplocs[0,1], c='r', marker='s',
            transform=ccrs.PlateCarree(), zorder=2)
    for i in range(len(aplocs)):
        ax.text(aplocs[i,2]+0.5, aplocs[i,1]-0.5, str(aplocs[i,0]), color='black',
                weight='bold', transform=ccrs.Geodetic(), zorder=2)
    plt.show()