#!/usr/bin/env python
# encoding: utf-8
#  ======================================================================
#  Package:     pyclaw.io
#  File:        __init__.py
#  Created:     Feb 10, 2008
#  Author:      Kyle Mandli
#  ======================================================================
"""Output package for Pyclaw"""

import logging
from ascii import read_ascii,write_ascii
from netcdf import read_netcdf, write_netcdf
__all__ = ['read_ascii','write_ascii','read_netcdf','write_netcdf']

# Check for HDF 5 support
try:
    import h5py
    from hdf5 import read_hdf5,write_hdf5
    __all__ += ['read_hdf5','write_hdf5']
except:
    logging.debug("No hdf5 support found.")
    
# Check for netcdf 4 support
try:
    import netCDF4
    from netcdf import read_netcdf, write_netcdf
    __all__ += ['read_netcdf','write_netcdf']
except(ImportError):
    logging.debug("No netcdf4 support found.")
    
# Check for netcdf 3 support
try:
    import Scientific.IO.NetCDF
    from netcdf import read_netcdf, write_netcdf
    __all__ += ['read_netcdf','write_netcdf']
except(ImportError):
    logging.debug("No netcdf3 support found.")
    
# Check for netcdf 3 support
try:
    import Scientific.IO.NetCDF
    from netcdf import read_netcdf, write_netcdf
    __all__ += ['read_netcdf','write_netcdf']
except(ImportError):
    logging.debug("No netcdf3 support found.")

