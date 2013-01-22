"""
Create topo files needed for this example:
    etopo10min170W60W65S25N.asc        download from GeoClaw topo repository
    etopo1min78W68W40S30S.asc
    Chile2010_USGS.tt3                 create using Okada model 
    
"""

from pyclaw.geotools import topotools, dtopotools
import os,sys

def gettopo():
    """
    Retrieve the topo file from the GeoClaw repository.
    """
    remote_directory = 'http://www.clawpack.org/geoclaw/topo/etopo'
    topo_fname = 'etopo10min170W60W65S25N.asc'
    topotools.get_topo(topo_fname, remote_directory)
    topo_fname = 'etopo1min78W68W40S30S.asc'
    topotools.get_topo(topo_fname, remote_directory)

    
def makedtopo():
    """
    Create dtopo data file for deformation of sea floor due to earthquake.
    Uses the Okada model with fault parameters and mesh specified in the
    .cfg file.
    """
    from pyclaw.geotools import okada2
    dtopo_fname = 'Chile2010_USGS.tt3'
    subfault_fname = 'Chile2010_USGS.txt'
    if os.path.exists(dtopo_fname):
        print "*** Not regenerating dtopo file (already exists): %s" % dtopo_fname
    else:
        print "Using Okada model to create %s " % dtopo_fname
        
        columns = """latitude longitude depth slip rake strike dip""".split()
        defaults = {'latlong_location': 'top center', 'length':30, 'width':20}
        units = {'slip': 'cm', 'depth': 'km', 'length': 'km', 'width': 'km'}
        subfaults = dtopotools.read_subfault_model(subfault_fname, \
                            columns=columns, units=units, \
                            defaults = defaults, skiprows=1)

        # Needed for extent of dtopo file:
        xlower = -76.
        xupper = -69.
        ylower = -39.
        yupper = -32.
        
        # dtopo parameters for 1 min resolution:
        mx = int((xupper - xlower)*60 + 1)
        my = int((yupper - ylower)*60 + 1)
        
        # Create dtopo_params dictionary with parameters for dtopo file: 
        dtopo_params = {}
        dtopo_params['fname'] = dtopo_fname
        dtopo_params['faulttype'] = 'static'
        dtopo_params['dtopotype'] = 3
        dtopo_params['mx'] = mx
        dtopo_params['my'] = my
        dtopo_params['xlower'] = xlower
        dtopo_params['xupper'] = xupper
        dtopo_params['ylower'] = ylower
        dtopo_params['yupper'] = yupper
        dtopo_params['t0'] = 0.
        dtopo_params['tfinal'] = 1.
        dtopo_params['ntimes'] = 2
        
        dtopo = dtopotools.make_dtopo_from_subfaults(subfaults, dtopo_params)



if __name__=='__main__':
    gettopo()
    makedtopo()
