

.. _convert:

*********************************************************
Converting an application directory from old to new form
*********************************************************

.. _convert43to46:

Converting from 4.3 to 4.6 
--------------------------------

Some of the `Clawpack 4.3 applications
<http://www.clawpack.org/clawpack-4.3/apps.html>`_
have not yet been converted to the form required by Clawpack 4.4 thru 4.6.
This section describes how to convert from 4.3 form (before we used Python at
all) to 4.6:

Note: Clawpack 5.0 will soon be available and require a new conversion.
Several things are expected to substantially change.

Converting by hand
^^^^^^^^^^^^^^^^^^

The minimal change needed to make a 4.3 application run in 4.4 (or 4.5)
is to rename
the *clawNez.data* file as *claw.data* and add a line to the top with a
single value *N*, the number of space dimensions.

To take full advantage of new features available in Clawpack 4.4 you may
also want to:

 * Create a *setrun.py* file to automatically generate *claw.data*,

 * Modify *setrun.py* to also create  *setprob.data* or other data files you
   read in. In this case you must alse modify *setprob.f* to use the 
   library routine *opendatafile* instead of the f77 function *open* as 
   illustrated in examples.  This routine skips over the warning message
   generated at the top of data files.

 * Switch to Python graphics by creating an appropriate *setplot.py* file,

 * Rewrite the Makefile to give options 'make .output', 'make .plots', etc.

 * Create a README.txt file that has links to the various other files in
   this directory, that will be converted to README.html by 'make .htmls'

Converting by script
^^^^^^^^^^^^^^^^^^^^

A first pass can be done with the Python script `$CLAW/python/convert43to44.py`
that can be found in versions of Clawpack from 4.4 to 4.6, or in
the new Clawpack github repository 
`clawpack-4.x <https://github.com/clawpack/clawpack-4.x>`_
Make sure this file is somewhere in your `PYTHONPATH`.

Download a copy of the the directory you want to convert (or make a copy of
your own 4.3 application directory).

Go into this directory and type::

    python convert43to44.py

This should do most of the work for you.  In particular it will create:

* `setrun.py` that uses the parameters found in the old `clawNez.data` file. 
* `setplot.py` that creates a basic set of plots, one for each component of
  the system.  This does **not** use the old Matlab `setplotN.m` script (if
  there is one in this directory) to try to mimic the plots that were
  originally made.
* `Makefile` with appropriate pointers to the new source code locations.
* `README.txt` with some pointers to the files, suitable for use with the
    `make .htmls` command.

Some things to watch out for:

* This only works for classic Clawpack, not for AMR or GeoClaw applications.

* If there is a file `setprob.data` that is read in by `setprob.f`, this
  file will still be here but will not be generated automatically by what's
  in `setrun.py`.   If you want it to be, you should modify the section of
  `setrun.py` that starts with::

    probdata = rundata.new_UserData(...)

  Call `probdata.add_param` for each parameter in the `setprob.data` file.
  This currently only works if there is one parameter per line, so
  `setprob.f` might need to be rewritten.

* If you want to make fancier plots, you will need to modify `setplot.py`
  appropriately.

* The file `README.txt` has been created based on a basic template but may
  not have pointers to the actual `*.f` files in this directory.  It also
  has not taken into account any old `README` file that might have been in
  the directory.

