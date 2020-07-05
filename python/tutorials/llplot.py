""" Plot a .csv file of latitude/longitude points on a map. """
import sys
import argparse
import csv
import matplotlib.pyplot

# pip3 install --user https://github.com/matplotlib/basemap/archive/master.zip
import mpl_toolkits.basemap

def main(options):
    lon = []
    lat = []
    with open(options.points) as pf:
        reader = csv.DictReader(pf, delimiter=',')
        for row in reader:
            lon.append(float(row['longitude']))
            lat.append(float(row['latitude']))

    # Minimum default margin.
    margin = max([max(lat) - min(lat), max(lon) - min(lon)])        
    if options.margin:
        margin = options.margin
    lat_min = min(lat) - margin
    lat_max = max(lat) + margin
    lon_min = min(lon) - margin
    lon_max = max(lon) + margin

    m = mpl_toolkits.basemap.Basemap(
        llcrnrlon=lon_min,
        llcrnrlat=lat_min,
        urcrnrlon=lon_max,
        urcrnrlat=lat_max,
        lat_0=(lat_max - lat_min)/2,
        lon_0=(lon_max-lon_min)/2,
        projection='merc',
        resolution = 'h',
        area_thresh=10000.0)
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.drawparallels(range(int(lat_min), int(lat_max), 1), labels=[1,0,0,0])
    m.drawmeridians(range(int(lon_min), int(lon_max), 1), labels=[0,0,0,1])
    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color='white', lake_color='#46bcec')

    # Convert lat and lon to map projection coordinates.
    lons, lats = m(lon, lat)

    # Plot points as red dots.
    m.scatter(lons, lats, marker = '.', color='r', zorder=5)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--margin',
        dest='margin',
        type=float,
        help='Margin to add around the data (in degrees).')
    parser.add_argument(
        'points',
        help='CSV file of points to plot.  Should have columns \'latitude\' and \'longitude\` (column order unimportant).')
    options = parser.parse_args()
    sys.exit(main(options))
