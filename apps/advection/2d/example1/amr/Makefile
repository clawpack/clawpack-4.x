
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
AMR_LIB = $(CLAW)/amrclaw/2d/lib

# Add AMR_LIB to list of library paths
LIB_PATHS = $(AMR_LIB)

# List all modules in either local or library directories.
# List them in the order they must be compiled, remembering that if
# a module is "used" in another module it must be compiled first.
# It is suggested that module names be of the form fname_module.f90
# but this is not required.

MODULES = \
  $(AMR_LIB)/mem_storage.f90

# Source files (other than modules):

SOURCES = \
  ../qinit.f \
  ../setprob.f \
  ../rpn2.f \
  ../rpt2.f \
  $(AMR_LIB)/amr2ez.f \
  $(AMR_LIB)/bc2amr.f \
  $(AMR_LIB)/setaux.f \
  $(AMR_LIB)/b4step2.f \
  $(AMR_LIB)/qad.f \
  $(AMR_LIB)/src2.f \
  $(AMR_LIB)/src1d.f \
  $(AMR_LIB)/advanc.f \
  $(AMR_LIB)/bound.f \
  $(AMR_LIB)/stepgrid.f \
  $(AMR_LIB)/auxcoarsen.f \
  $(AMR_LIB)/fixcapaq.f \
  $(AMR_LIB)/estdt.f \
  $(AMR_LIB)/igetsp.f \
  $(AMR_LIB)/reclam.f \
  $(AMR_LIB)/birect.f \
  $(AMR_LIB)/cleanup.f \
  $(AMR_LIB)/colate.f \
  $(AMR_LIB)/bufnst.f \
  $(AMR_LIB)/spest.f \
  $(AMR_LIB)/flag2refine.f \
  $(AMR_LIB)/allowflag.f \
  $(AMR_LIB)/errest.f \
  $(AMR_LIB)/errf1.f \
  $(AMR_LIB)/gfixup.f \
  $(AMR_LIB)/filval.f \
  $(AMR_LIB)/filpatch.f \
  $(AMR_LIB)/prefilp.f \
  $(AMR_LIB)/flglvl.f \
  $(AMR_LIB)/fluxad.f \
  $(AMR_LIB)/fluxsv.f \
  $(AMR_LIB)/ginit.f \
  $(AMR_LIB)/grdfit.f \
  $(AMR_LIB)/intfil.f \
  $(AMR_LIB)/moment.f \
  $(AMR_LIB)/nestck.f \
  $(AMR_LIB)/prepf.f \
  $(AMR_LIB)/prepc.f \
  $(AMR_LIB)/projec.f \
  $(AMR_LIB)/signs.f \
  $(AMR_LIB)/findcut.f \
  $(AMR_LIB)/smartbis.f \
  $(AMR_LIB)/putnod.f \
  $(AMR_LIB)/putsp.f \
  $(AMR_LIB)/regrid.f \
  $(AMR_LIB)/setgrd.f \
  $(AMR_LIB)/setuse.f \
  $(AMR_LIB)/stst1.f \
  $(AMR_LIB)/tick.f \
  $(AMR_LIB)/trimbd.f \
  $(AMR_LIB)/update.f \
  $(AMR_LIB)/nodget.f \
  $(AMR_LIB)/upbnd.f  \
  $(AMR_LIB)/basic.f \
  $(AMR_LIB)/outval.f \
  $(AMR_LIB)/copysol.f \
  $(AMR_LIB)/outvar.f \
  $(AMR_LIB)/outmsh.f \
  $(AMR_LIB)/outtre.f \
  $(AMR_LIB)/domain.f  \
  $(AMR_LIB)/setflags.f \
  $(AMR_LIB)/shiftset.f \
  $(AMR_LIB)/conck.f \
  $(AMR_LIB)/domshrink.f \
  $(AMR_LIB)/domprep.f \
  $(AMR_LIB)/domup.f \
  $(AMR_LIB)/domcopy.f \
  $(AMR_LIB)/coarsen.f \
  $(AMR_LIB)/intcopy.f \
  $(AMR_LIB)/preintcopy.f \
  $(AMR_LIB)/icall.f \
  $(AMR_LIB)/preicall.f \
  $(AMR_LIB)/step2.f \
  $(AMR_LIB)/flux2.f \
  $(AMR_LIB)/limiter.f \
  $(AMR_LIB)/philim.f \
  $(AMR_LIB)/cstore.f \
  $(AMR_LIB)/saveqc.f \
  $(AMR_LIB)/valout.f \
  $(AMR_LIB)/check.f \
  $(AMR_LIB)/restrt.f \
  $(AMR_LIB)/setgauges.f \
  $(AMR_LIB)/dumpgauge.f \
  $(AMR_LIB)/quick_sort1.f \
  $(AMR_LIB)/opendatafile.f \
  $(AMR_LIB)/restrt_alloc.f90 \
  $(AMR_LIB)/resize_alloc.f90 \
# $(AMR_LIB)/resize_alloc_static.f90 \

#-------------------------------------------------------------------
# Include Makefile containing standard definitions and make options:
include $(CLAWMAKE)


### DO NOT remove this line - make depends on it ###
    
