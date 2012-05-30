
.. _plotting:

***************************************
Plotting options in Python
***************************************

.. contents::

Clawpack 4.4 includes utilities for plotting using Python.  Most of these
are defined in the file 
`$CLAW/python/pyclaw/plotters/frametools.py <claw/python/pyclaw/plotters/frametools.py>`_
In order to use these you will need to insure that you have the required
modules installed (see :ref:`python-install`).

Clawpack 4.4 also includes the Matlab plotting tools from 4.3 and before,
see :ref:`matlabplots`.

The advantages of using the Python options are:

 * Python and the graphics modules used in Clawpack are open source.  Since
   Clawpack itself is open source we find it desirable to also have an open
   source plotting open for viewing the results.

 * The Python tools developed so far (mostly for 1d and 2d data sets) are
   more powerful than the Matlab versions they replace, and can be used for
   example to automatically generate html versions of multiple plots each
   frame over all frames of a computation, to generate latex versions of the
   output, as well as to step through the frames one by one as with the
   Matlab tools.  It is easier to specify a set of multiple plots to be
   produced for each frame.

 * Matlab graphics are somewhat limited for 3d data sets, whereas several
   open source visualization tools such as `VisIt
   <https://wci.llnl.gov/codes/visit>`_ (developed at Lawrence Livermore
   National Laboratory) are much better for dealing
   with large data sets, AMR grids, etc.  VisIt has Python bindings and 
   we are currently extending our tools to work with VisIt.  If you are
   already a VisIt user, note that VisIt has a Claw reader that can be used to
   import data from Clawpack, see `Application Toolkit Formats
   <http://www.visitusers.org/index.php?title=Detailed_list_of_file_formats_VisIt_supports#Application_Toolkit_Formats>`_.

   We are also considering developing tools for use with
   `Mayavi <http://code.enthought.com/projects/mayavi>`_.

 * Python is a powerful language that can be scripted to perform multiple
   runs, such as in a convergence test, and collect the results in tables or
   plots.  We are developing tools to simplify this process.


See :ref:`python` for more information on Python and pointers to many tutorials.

.. plotting_makeplots:

Producing html plots from the command line
==========================================


In most Clawpack directories, typing::

  $  make .plots

will compile the code and run it (if necessary) and then
produce a set of html files that can be
used to view the resulting plots.  These will be in a subdirectory
of the current directory as specified by CLAW_PLOTDIR in the Makefile.


Viewing plots via a local web server
====================================

The best way to view the plots and associated web pages for each example is
to first start a python web server in your main $CLAW directory with the
commands:: 
 
  $ cd $CLAW
  $ xterm -e python python/startserver.py & # to start server in new X window

The main $CLAW directory will then be available at http://localhost:50005
and jsMath should work properly to display latex on the webpages (once you've
downloaded the required fonts, see
`<http://www.math.union.edu/locate/jsMath/users/fonts.html>`_).  

Producing a latex file with plots from the command line
=======================================================

A latex file with all the plots can also be produced by :ref:`printframes`,
and is also typically controlled by options set in the file setplot.py.

Setting plot parameters with a setplot function
===============================================

Typically each applications directory contains a file :file:`setplot.py`, see for
example :ref:`plotexamples`.
This file should define a function `setplot(plotdata)` that sets various
attributes of an object plotdata of class :ref:`ClawPlotData`.

Documentation on how to create a setplot function and the various plotting
parameters that can be set can be found in the section :ref:`setplot`.

Examples can be found at :ref:`plotexamples`.

.. _plotting_Iplotclaw:

Interactive plotting with ``Iplotclaw``
=======================================

For interactive plotting we suggest using `IPython
<http://ipython.org>`_, which is a nicer shell
than the pure python shell, with things like command completion and history.
See the `IPython Documentation
<http://ipython.org/documentation.html>`_ for more information and
:ref:`ipython_config` for information on configuring it to use with Clawpack.

Note that to use interactive plotting must give the `--pylab` flag in
order for plotting to work properly, and that this automatically imports
numpy and matplotlib commands into your namespace, so you can use, for
example, `linspace` or `pcolor` without further imports.

Here's an example::

    $ ipython --pylab

    In [1]: from pyclaw.plotters.Iplotclaw import Iplotclaw
    In [2]: ip = Iplotclaw() 
    In [3]: ip.plotloop()
    Executing setplot ... 

    Interactive plotclaw with ndim = 1 ... 
    Type ? at PLOTCLAW prompt for list of commands

	Start at which frame [default=0] ? 
	Plotting frame 0 ... 
    PLOTCLAW >  n
	Plotting frame 1 ... 
    PLOTCLAW > q
    quitting...
    In [4]: 

Type ? at the PLOTCLAW prompt or ?command-name for more
information.  Most commonly used are n for next frame, p for previous frame
and j to jump to a different frame.  Hitting return at the prompt repeats
the previous command.

By default `Iplotclaw` attempts to determine the directory where output can
be found by examining the file `.output` that is automatically created by
the `make .output` command.  If not found, the default is to look in the
current directory.  Instead you can provide an argument `outdir` to specify
the directory for output.  

By default `Iplotclaw` attempts to execute a `setplot` function from a file
`setplot.py`.  Instead you can provide an argument `setplot` to specify the
file name.

Example::

    In [2]: ip = Iplotclaw(setplot='setplot_special.py', outdir='_output2')


You can restart the plotloop later by doing::

    In [4]: ip.plotloop()

    Interactive plotting for Clawpack output...
    Plotting data from outdir =  _output
    Type ? at PLOTCLAW prompt for list of commands

	Start at which frame [default=1] ? 
	Replot data for frame 1 [no] ? 
    PLOTCLAW > 


By default it starts at the frame where you previously left off.

If you want to change plot parameters, the easiest way is to edit the file
setplot.py, either in a different window or, if you use vi, by::

    PLOTCLAW > vi setplot.py

and then re-execute the setplot function using::

    PLOTCLAW > resetplot

If you recompute results by running the fortran code again and want to plot
the new results (from this same directory), you may have to clear the frames
that have already been viewed using::

    PLOTCLAW > clearframes

Or you can redraw the frame you're currently looking at without clearing the
rest of the cached frame data by doing::

    PLOTCLAW > rr

To see what figures, axes, and items have been defined by *setplot*::

    PLOTCLAW > show
    
    Current plot figures, axes, and items:
    ---------------------------------------
      figname = Pressure, figno = 1
         axesname = AXES1, axescmd = subplot(1,1,1)
            itemname = ITEM1,  plot_type = 1d_plot
     
      figname = Velocity, figno = 2
         axesname = AXES1, axescmd = subplot(1,1,1)
            itemname = ITEM1,  plot_type = 1d_plot
 


Type "help" or "help command-name" at the prompt for more options.

Access to current_data
----------------------

If you are viewing plots in using Iplotclaw and want to explore the data for
some frame or make plots directly in your Python shell, the data that is
being plotted is available to you in attributes of the Iplotclaw instance.
For example::

    >>> ip = Iplotclaw();  ip.plotloop()

    Interactive plotting for Clawpack output... 

    Plotting data from outdir =  _output
        ...
        Plotting Frame 0 at t = 0.0
    PLOTCLAW > q
    quitting...

    >>> pd = ip.plotdata
    >>> current_data = ip.current_data

The *current_data* object contains the :ref:`current_data` used for the most recent
plot, while *pd* is the :ref:`ClawPlotData` object that
gives access to all the plotting parameters currently being used as well as
to methods such as *getframe* for retrieving other frames of data from this
computation.  

If you want to change the directory *outdir* where the frame data is coming
from, you could do, for example::

    >>> pd.outdir = "_output2"
    >>> ip.plotloop()
    ...
    PLOTCLAW > clearframes    # to remove old frames from cache
    PLOTCLAW > rr             # to redraw current frame number but with new data


.. _ipython_config:

IPython configuration
=====================

The IPython configuration system changed substantially in IPython
Version 0.11 and Clawpack no longer contains the configuration files
that used to be found in `$CLAW/python/ipythondir`.

See the `documentation <http://ipython.org/documentation.html>`_ 
for the version of IPython you are using. 

The instructions below are for recent versions.
See `IPython Configuration Overview
<http://ipython.org/ipython-doc/dev/config/index.html>`_  and
`Configuring IPython
<http://ipython.org/ipython-doc/dev/config/ipython.html#configuring-ipython>`_
for more complete details.

It is suggested that you create a directory `.ipython` in your home
directory if you do not already have one, and set the `IPYTHONDIR`
environment variable to point here, e.g. in bash::

    $ export IPYTHONDIR=$HOME/.ipython

If you haven't created a default profile in the past you might want to do
so::

    $ ipython profile create 

Then create an IPython configuration for Clawpack via the command::

    $ ipython profile create clawpack

There will now be a directory `$HOME/.ipython/profile_clawpack`
containing a file `ipython_config.py` with the default configuration.
Replace this file with the version in `$CLAW/python/ipython_config.py`.
This doesn't do anything fancy, but does execute the command ::

    from pyclaw.plotters.Iplotclaw import Iplotclaw

whenever you start IPython with this configuration, saving you one line of
typing.  You can of course modify this profile to add anything else you
wish, as described in the IPython documentation.

Now you can start IPython via::

    $ ipython --pylab --profile=clawpack

to use this profile.  

You might want to define an alias in your `.bashrc` file for the above
invocation, e.g. ::

    alias ipyclaw='ipython --pylab --profile=clawpack'

so then you can just do::

    $ ipyclaw

to start IPython.


.. _printframes:

printframes 
===========

The function pyclaw.plotters.frametools.printframes can be used to produce html and
latex versions of the plots::

   >>> from pyclaw.plotters.data import ClawPlotData
   >>> from pyclaw.plotters import frametools
   >>> plotclaw = ClawPlotData()
   >>> # set attributes as desired
   >>> frametools.printframes(plotclaw)

A convenience method of ClawPlotData is defined to apply this function,
e.g.::

   >>> plotclaw.printframes()

This function is automatically called by the "make .plots" option available
in most examples.
   

.. _plot_files:

Specifying what and how to plot
===============================

The first step in specifying how to plot is to create a :ref:`ClawPlotData`
object to hold all the data required for plotting.  This is generally done
one of two ways:

 1. In a script such as the plotclaw.py script included in most example
    directories, e.g.,  
    `<claw/examples/acoustics/1d/example1/plotclaw.py.html>`_.

 2. By creating an instance of Iplotclaw to do interactive plotting, e.g.::

       >>> ip = Iplotclaw()

    Then ip will have an attribute plotdata that is a :ref:`ClawPlotData` 
    object.  This object will have attribute setplot initialized to
    'setplot.py', indicating that other attributes should be set by
    executing the setplot function defined in the file 'setplot.py' in this
    directory.

Once you have a :ref:`ClawPlotData` object you can set various attributes to
control what is plotted.  For example,::

      >>> plotdata.plotdir = '_plots'
      >>> plotdata.setplot = 'my_setplot_file.py'

will cause hardcopy to go to subdirectory _plots of the current directory and
will cause the plotting routines to execute::

      >>> from my_setplot_file import setplot
      >>> plotdata = setplot(plotdata)

before doing the plotting.

There are many other :ref:`ClawPlotData` attributes and methods.

Most example directories contain a file setplot.py that contains a
function setplot(). This function
sets various attributes of the :ref:`ClawPlotData`
object to control what figures, axes, and items should be plotted for each
frame of the solution.

For an outline of how a typical set of plots is specified, see
:ref:`setplot`.



