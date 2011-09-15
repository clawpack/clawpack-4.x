
# Makefile for Clawpack code in this directory.
# This version only sets the local files and frequently changed
# options, and then includes the standard makefile pointed to by CLAWMAKE.
CLAWMAKE = $(CLAW)/util/Makefile.common

# See the above file for details and a list of make options, or type
#   make .help
# at the unix prompt.


# Adjust these variables if desired:
# ----------------------------------
CLAW_PKG = amrclaw                  # Clawpack package to use
EXECUTABLE = xamr                     # Executable to create
SETRUN_FILE = setrun.py        # File containing function to make data
OUT_DIR = _output               # Directory for output
SETPLOT_FILE = setplot.py      # File containing function to set plots
PLOT_DIR = _plots               # Directory for plots

# Environment variable FC should be set to fortran compiler, e.g. gfortran
FC ?= gfortran   # default if not set as environment variable
# Add any desired compiler flags such as -g here:
FFLAGS ?=  -O2 



# ---------------------------------
# List of sources for this program:
# ---------------------------------

# Clawpack library to be used:
AMR_LIB_PATH = $(CLAW)/amrclaw/2d/lib

# List all modules in either local or library directories.
# List them in the order they must be compiled, remembering that if
# a module is "used" in another module it must be compiled first.
# It is suggested that module names be of the form fname_module.f90
# but this is not required.

MODULES = \
  $(AMR_LIB_PATH)/mem_storage.f90

# Source files (other than modules):

SOURCES = \
  ../qinit.f \
  ../setprob.f \
  ../rpn2.f \
  ../rpt2.f \
  $(AMR_LIB_PATH)/amr2ez.f \
  $(AMR_LIB_PATH)/bc2amr.f \
  $(AMR_LIB_PATH)/setaux.f \
  $(AMR_LIB_PATH)/b4step2.f \
  $(AMR_LIB_PATH)/qad.f \
  $(AMR_LIB_PATH)/src2.f \
  $(AMR_LIB_PATH)/src1d.f \
  $(AMR_LIB_PATH)/advanc.f \
  $(AMR_LIB_PATH)/bound.f \
  $(AMR_LIB_PATH)/stepgrid.f \
  $(AMR_LIB_PATH)/auxcoarsen.f \
  $(AMR_LIB_PATH)/fixcapaq.f \
  $(AMR_LIB_PATH)/estdt.f \
  $(AMR_LIB_PATH)/igetsp.f \
  $(AMR_LIB_PATH)/reclam.f \
  $(AMR_LIB_PATH)/birect.f \
  $(AMR_LIB_PATH)/cleanup.f \
  $(AMR_LIB_PATH)/colate.f \
  $(AMR_LIB_PATH)/bufnst.f \
  $(AMR_LIB_PATH)/spest.f \
  $(AMR_LIB_PATH)/flag2refine.f \
  $(AMR_LIB_PATH)/allowflag.f \
  $(AMR_LIB_PATH)/errest.f \
  $(AMR_LIB_PATH)/errf1.f \
  $(AMR_LIB_PATH)/gfixup.f \
  $(AMR_LIB_PATH)/filval.f \
  $(AMR_LIB_PATH)/filpatch.f \
  $(AMR_LIB_PATH)/prefilp.f \
  $(AMR_LIB_PATH)/flglvl.f \
  $(AMR_LIB_PATH)/fluxad.f \
  $(AMR_LIB_PATH)/fluxsv.f \
  $(AMR_LIB_PATH)/ginit.f \
  $(AMR_LIB_PATH)/grdfit.f \
  $(AMR_LIB_PATH)/intfil.f \
  $(AMR_LIB_PATH)/moment.f \
  $(AMR_LIB_PATH)/nestck.f \
  $(AMR_LIB_PATH)/prepf.f \
  $(AMR_LIB_PATH)/prepc.f \
  $(AMR_LIB_PATH)/projec.f \
  $(AMR_LIB_PATH)/signs.f \
  $(AMR_LIB_PATH)/findcut.f \
  $(AMR_LIB_PATH)/smartbis.f \
  $(AMR_LIB_PATH)/putnod.f \
  $(AMR_LIB_PATH)/putsp.f \
  $(AMR_LIB_PATH)/regrid.f \
  $(AMR_LIB_PATH)/setgrd.f \
  $(AMR_LIB_PATH)/setuse.f \
  $(AMR_LIB_PATH)/stst1.f \
  $(AMR_LIB_PATH)/tick.f \
  $(AMR_LIB_PATH)/trimbd.f \
  $(AMR_LIB_PATH)/update.f \
  $(AMR_LIB_PATH)/nodget.f \
  $(AMR_LIB_PATH)/upbnd.f  \
  $(AMR_LIB_PATH)/basic.f \
  $(AMR_LIB_PATH)/outval.f \
  $(AMR_LIB_PATH)/copysol.f \
  $(AMR_LIB_PATH)/outvar.f \
  $(AMR_LIB_PATH)/outmsh.f \
  $(AMR_LIB_PATH)/outtre.f \
  $(AMR_LIB_PATH)/domain.f  \
  $(AMR_LIB_PATH)/setflags.f \
  $(AMR_LIB_PATH)/shiftset.f \
  $(AMR_LIB_PATH)/conck.f \
  $(AMR_LIB_PATH)/domshrink.f \
  $(AMR_LIB_PATH)/domprep.f \
  $(AMR_LIB_PATH)/domup.f \
  $(AMR_LIB_PATH)/domcopy.f \
  $(AMR_LIB_PATH)/coarsen.f \
  $(AMR_LIB_PATH)/intcopy.f \
  $(AMR_LIB_PATH)/preintcopy.f \
  $(AMR_LIB_PATH)/icall.f \
  $(AMR_LIB_PATH)/preicall.f \
  $(AMR_LIB_PATH)/step2.f \
  $(AMR_LIB_PATH)/flux2.f \
  $(AMR_LIB_PATH)/limiter.f \
  $(AMR_LIB_PATH)/philim.f \
  $(AMR_LIB_PATH)/cstore.f \
  $(AMR_LIB_PATH)/saveqc.f \
  $(AMR_LIB_PATH)/valout.f \
  $(AMR_LIB_PATH)/check.f \
  $(AMR_LIB_PATH)/restrt.f \
  $(AMR_LIB_PATH)/setgauges.f \
  $(AMR_LIB_PATH)/dumpgauge.f \
  $(AMR_LIB_PATH)/quick_sort1.f \
  $(AMR_LIB_PATH)/opendatafile.f \
  $(AMR_LIB_PATH)/restrt_alloc.f90 \
  $(AMR_LIB_PATH)/resize_alloc.f90 \
# $(AMR_LIB_PATH)/resize_alloc_static.f90 \

# Add AMR_LIB_PATH to list of library paths
LIB_PATHS = $(AMR_LIB_PATH)

#-------------------------------------------------------------------
# Include Makefile containing standard definitions and make options:
include $(CLAWMAKE)


### DO NOT remove this line - make depends on it ###
    
