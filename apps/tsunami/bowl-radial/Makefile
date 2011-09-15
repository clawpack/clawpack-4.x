
# Makefile for Clawpack code in this directory.
# This version only sets the local files and frequently changed
# options, and then includes the standard makefile pointed to by CLAWMAKE.
CLAWMAKE = $(CLAW)/util/Makefile.common

# See the above file for details and a list of make options, or type
#   make .help
# at the unix prompt.


# Adjust these variables if desired:
# ----------------------------------

CLAW_PKG = geoclaw                  # Clawpack package to use
EXECUTABLE = xgeoclaw                 # Executable to create
SETRUN_FILE = setrun.py        # File containing function to make data
OUT_DIR = _output               # Directory for output
SETPLOT_FILE = setplot.py      # File containing function to set plots
PLOT_DIR = _plots               # Directory for plots

# Environment variable FC should be set to fortran compiler, e.g. gfortran
FC ?= gfortran   # default if not set as environment variable
# Add any desired compiler flags such as -g here:
FFLAGS ?=  -O2
# If you want to include NetCDF output add these flags
# FFLAGS ?=-I/usr/include  -lnetcdf -lnetcdff

# ---------------------------------
# List of sources for this program:
# ---------------------------------

# Clawpack libraries to be used:
AMR_LIB = $(CLAW)/amrclaw/2d/lib
GEO_LIB = $(CLAW)/geoclaw/2d/lib

# This will be the search path order for source files, make sure this
# is in the correct order!
LIB_PATHS = $(GEO_LIB) $(AMR_LIB)

# List all modules in either local or library directories.
# List them in the order they must be compiled, remembering that if
# a module is "used" in another module it must be compiled first.
# It is suggested that module names be of the form fname_module.f90
# but this is not required.

MODULES = \
  $(AMR_LIB)/mem_storage.f90 \
  $(GEO_LIB)/geoclaw_module.f90 \
  $(GEO_LIB)/topo_module.f90 \
  $(GEO_LIB)/dtopo_module.f90 \

# Source files (other than modules):

SOURCES = \
  $(GEO_LIB)/setprob_geo.f \
  $(GEO_LIB)/qinit_geo.f \
  $(GEO_LIB)/readqinit_geo.f \
  $(GEO_LIB)/movetopo_geo.f \
  $(GEO_LIB)/cellgridintegrate_geo.f \
  $(GEO_LIB)/topointegral_geo.f \
  $(GEO_LIB)/bilinearintegral_geo.f \
  $(GEO_LIB)/stepgrid_geo.f \
  $(GEO_LIB)/fgridinterp_geo.f \
  $(GEO_LIB)/fgridout_geo.f \
  $(GEO_LIB)/rpn2ez_geo.f \
  $(GEO_LIB)/riemannsolvers_geo.f \
  $(GEO_LIB)/rpt2_geo.f \
  $(GEO_LIB)/src2_geo.f \
  $(GEO_LIB)/src1d_geo.f \
  $(GEO_LIB)/step2_geo.f \
  $(GEO_LIB)/flux2fw_geo.f \
  $(GEO_LIB)/qad_geo.f \
  $(GEO_LIB)/valout_geo.f \
  $(GEO_LIB)/filval_geo.f \
  $(GEO_LIB)/filpatch_geo.f \
  $(GEO_LIB)/bc2amr_geo.f \
  $(GEO_LIB)/update_geo.f \
  $(GEO_LIB)/amr2ez_geo.f \
  $(GEO_LIB)/setaux_geo.f \
  $(GEO_LIB)/setqinit_geo.f \
  $(GEO_LIB)/setregions_geo.f \
  $(GEO_LIB)/setgauges_geo.f \
  $(GEO_LIB)/setfixedgrids_geo.f \
  $(GEO_LIB)/b4step2_geo.f \
  $(GEO_LIB)/flag2refine_geo.f  \
  $(GEO_LIB)/allowflag_geo.f  \
  $(GEO_LIB)/dumpgauge_geo.f \
  $(GEO_LIB)/upbnd_geo.f  \
  $(GEO_LIB)/tick_geo.f \
  $(GEO_LIB)/setgrd_geo.f \
  $(GEO_LIB)/gfixup_geo.f \
  $(GEO_LIB)/ginit_geo.f \
  $(GEO_LIB)/getmaxspeed_geo.f \
  $(AMR_LIB)/prefilp.f \
  $(AMR_LIB)/quick_sort1.f \
  $(AMR_LIB)/advanc.f \
  $(AMR_LIB)/estdt.f \
  $(AMR_LIB)/bound.f \
  $(AMR_LIB)/check4nans.f \
  $(AMR_LIB)/spest.f  \
  $(AMR_LIB)/igetsp.f \
  $(AMR_LIB)/reclam.f \
  $(AMR_LIB)/birect.f \
  $(AMR_LIB)/cleanup.f \
  $(AMR_LIB)/colate.f \
  $(AMR_LIB)/errest.f \
  $(AMR_LIB)/bufnst.f \
  $(AMR_LIB)/errf1.f \
  $(AMR_LIB)/fixcapaq.f \
  $(AMR_LIB)/flglvl.f \
  $(AMR_LIB)/fluxad.f \
  $(AMR_LIB)/fluxsv.f \
  $(AMR_LIB)/grdfit.f \
  $(AMR_LIB)/intfil.f \
  $(AMR_LIB)/moment.f \
  $(AMR_LIB)/nestck.f \
  $(AMR_LIB)/prepc.f \
  $(AMR_LIB)/prepf.f \
  $(AMR_LIB)/projec.f \
  $(AMR_LIB)/signs.f \
  $(AMR_LIB)/findcut.f \
  $(AMR_LIB)/smartbis.f \
  $(AMR_LIB)/putnod.f \
  $(AMR_LIB)/putsp.f \
  $(AMR_LIB)/regrid.f \
  $(AMR_LIB)/setuse.f \
  $(AMR_LIB)/stst1.f \
  $(AMR_LIB)/trimbd.f \
  $(AMR_LIB)/nodget.f \
  $(AMR_LIB)/basic.f \
  $(AMR_LIB)/outval.f \
  $(AMR_LIB)/copysol.f \
  $(AMR_LIB)/outvar.f \
  $(AMR_LIB)/outmsh.f \
  $(AMR_LIB)/outtre.f \
  $(AMR_LIB)/domain.f  \
  $(AMR_LIB)/cellave.f \
  $(AMR_LIB)/fdisc.f \
  $(AMR_LIB)/fss.f \
  $(AMR_LIB)/zeroin.f \
  $(AMR_LIB)/setflags.f \
  $(AMR_LIB)/shiftset.f \
  $(AMR_LIB)/conck.f \
  $(AMR_LIB)/domshrink.f \
  $(AMR_LIB)/domprep.f \
  $(AMR_LIB)/domup.f \
  $(AMR_LIB)/domcopy.f \
  $(AMR_LIB)/coarsen.f \
  $(AMR_LIB)/auxcoarsen.f \
  $(AMR_LIB)/intcopy.f \
  $(AMR_LIB)/preintcopy.f \
  $(AMR_LIB)/icall.f \
  $(AMR_LIB)/preicall.f \
  $(AMR_LIB)/inlinelimiter.f \
  $(AMR_LIB)/cstore.f \
  $(AMR_LIB)/saveqc.f \
  $(AMR_LIB)/check.f \
  $(AMR_LIB)/restrt.f \
  $(AMR_LIB)/opendatafile.f \
  $(AMR_LIB)/restrt_alloc.f90 \
  $(AMR_LIB)/resize_alloc.f90 \
# $(AMR_LIB)/resize_alloc_static.f90 \



#-------------------------------------------------------------------
# Include Makefile containing standard definitions and make options:
include $(CLAWMAKE)

topo: .data
	python maketopo.py


### DO NOT remove this line - make depends on it ###

