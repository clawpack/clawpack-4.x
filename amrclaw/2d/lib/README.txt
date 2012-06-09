

This directory contains the basic amrclaw files in 2d.

Execute
  make .objs
to create .o files needed in running any example or application.

Notes:

The common blocks in call.i are "included" in many of the .f files.
If you copy .f files to another directory you may also need this file.

The Clawpack 4.4 version includes a few .f90 files, in particular so that
dynamic memory allocation is now supported.  You will need to use a Fortran
compiler that supports this, such as gfortran.

