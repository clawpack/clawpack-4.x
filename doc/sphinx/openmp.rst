.. _openmp:

==========================
Using openmp
==========================

The AMRClaw and GeoClaw codes now have openmp directives so that some of the
work can be done in parallel on multicore machines.

To compile with openmp
----------------------

To use openmp, first go into each of the directories `$CLAW/amrclaw/2d/lib`
and `$CLAW/geoclaw/2d/lib` and modify the `Makefile` to add the flag
`-fopenmp` to the `FFLAGS =` line.  To also turn on optimization, you might
want to use::

    FFLAGS ?=  -O2 -fopenmp

Then do the following::

    make clean
    make .objs

Now go into your application directory and make the same modification to the
Makefile as above.  Then::

    make clean
    make .exe

should make a new version of the executable that uses openmp.

Note that if you want to later turn off openmp, you must change the
Makefiles to remove `-fopenmp` from the `FFLAGS` line and then recompile
as above.  In particular, if you want to run an example that does not have
`-fopenmp` in the local Makefile then you will have to recompile the
appropriate library routines first or you will get error messages when you
compile such as::

    Undefined symbols:
      "_omp_get_max_threads_", referenced from:
          _MAIN__ in amr2ez.o
          _MAIN__ in amr2ez.o


To run the code
---------------

To specify the number of threads that openmp should use, 
first set the environment variable `OMP_NUM_THREADS`.  For example, in bash::

    $ export OMP_NUM_THREADS=2

to use 2 threads.  You should set this to at most the number of cores in
your machine.  If this environment variable is not set, then by default
it will probably use the number of cores available, 
but this may be compiler dependent.  

You can put this export statement in your `.bashrc` file if you want it to
be set everytime you open a new shell.

Once the code compiles properly with the `-fopenmp` flags and you have set
the environment variable `OMP_NUM_THREADS`, you should be
able to run it as usual, e.g. ::

    $ make .output

