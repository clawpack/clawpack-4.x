begin_html  [use: doc/doc.css]
<!--   For a more readable version of this file, execute
                  unix>  make .htmls
       in this directory and then point your browser to README.html 
     --------------------------------------------------------------  -->

<h2>
GeoClaw Sample Code
</h2>

Sample earthquake-generated tsunami based on the 2010 Chile event.
Primarily to illustrate how set up topo and dtopo files.

See [http://www.clawpack.org/users/topo.html] for more information.

See [code: maketopo.py].  This downloads topography data from the 
[http://www.clawpack.org/geoclaw/topo/ GeoClaw topography database]
that originally came from the
NOAA National Geophysical Data Center (NGDC)
using [http://www.ngdc.noaa.gov/mgg/gdas/gd_designagrid.html Design-a-grid].


USGS site for earthquake data:
[http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us2010tfan]

This example uses the final earthquake model from:
[http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us2010tfan/finite_fault.php Finite Fault model]
Click on "SUBFAULT MODEL" to find the data stored here in 
[link: Chile2010_USGS.txt].

This is converted to Chile2010_USGS.tt3 by running 
[code: maketopo.py] or by "make topo".
This uses an improved version of the Okada model, new in 4.6.3.

Two gauges are included at the locations of DART Buoy 32412 and 51406, see
[http://www.ndbc.noaa.gov/station_page.php?station=32412]
and
[http://www.ndbc.noaa.gov/station_page.php?station=51406]

To download other DART buoy data, see
[http://www.ndbc.noaa.gov/dart.shtml]


See also the NOAA/PMEL Center for Tsunami Research
site for this tsunami, containing DART data, tide gauges, MOST simulations:
[http://nctr.pmel.noaa.gov/chile20100227/]


<h4>
Plots of results
</h4>

After running this code and creating plots via "make .plots", you should be
able to view the plots in [link: _plots/_PlotIndex.html].

The gauge data will be plotted along with de-tided observations from the
DART buoys, stored in files
[link:32412_notide.txt] and [link:51406_notide.txt].

<h4>
Fortran files
</h4>


<dl>
<dt>[code: Makefile]
<dd> Determines which version of fortran files
are used when compiling the code with make and specifies where output and
plots should be directed.  Type "make .help" at the Unix prompt for options.


<dt>[code: setprob.f]
<dd>
Standard for for GeoClaw


</dl>

<h4>
Python files
</h4>
<dl>

<dt>[code: maketopo.py]
<dd> Used to create topo file and dtopo data file.

<dt>[code: setrun.py]
<dd> This file contains a function that 
specifies what run-time parameters will be used.

<dt>[code: setplot.py]
<dd> This file contains a function that 
specifies what plots will be done and
sets various plotting parameters. 

</dl>


<h4>
Data files
</h4>

The .data files are automatically generated using the information in 
[code: setrun.py].


<h4>
Instructions
</h4>


To make topo and dtopo data files:
{{{
  $ make topo
}}}

To make all data files, edit setrun.py and then
{{{
  $ make .data
}}}

To run code:
{{{
  $ make .output
}}}

To plot results, either generate html pages via:
{{{
  $ make .plots
}}}
or view interactively using ipython and Iplotclaw.

All of this can be done with:

{{{
  $ source make_all.py
}}}

For more documentation, see
[http://www.clawpack.org/users].

end_html

