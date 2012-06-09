begin_html [use: jsMath] [use: doc/doc.css]
<!--   For a more readable version of this file, execute
                  unix>  make .htmls
       in this directory and then point your browser to README.html 
     --------------------------------------------------------------  -->

<h2>
CLAWPACK Sample Code
</h2>

1d acoustics in a constant medium.
          \[   q_t + A q_x = 0  \]
where
          \[   q(x,t) = \vector{ p(x,t)\\ u(x,t)}           \]
and the coefficient matrix is
          \[   A = \begin{matrix}
                        0         & K\\
                        1/\rho & 0
                        \end{matrix}.
          \]

The parameters rho and K are specified in [code: setrun.py], along with data
used to specify the initial conditions (a Gaussian pressure pulse).

Boundary conditions: outflow at both boundaries.

See [link: #instructions Instructions]

<h4>
Plots of results
</h4>
After running this code and creating plots via "make .plots", you should be
able to view the plots in [link: _plots/_PlotIndex.html].


<h4>
Fortran files
</h4>


<dl>
<dt>[code: Makefile]
<dd> Determines which version of fortran files
are used when compiling the code with make.



<dt>[code: setprob.f]
<dd>
A routine by this name is called by the library routine 
[clawcode: clawpack/1d/lib/claw1ez.f]
and is generally used to set any values needed for the specific problem
being solved. 


<dt>[code: rp1.f]
<dd>
This is the Riemann solver, which takes the $q$ values stored in the
arrays <tt>ql</tt> and <tt>qr</tt> and returns the waves in the array
<tt>wave</tt> and speeds in the array <tt>s</tt> that result in solving the
Riemann problem at each cell interface, and the fluctuations <tt>amdq</tt>
and <tt>apdq</tt>.  See [claw:doc/rp1.html] for more information about 1d
Riemann solvers.



<dt>[code: qinit.f]
<dd>
This subroutine sets the initial data $q(x,0)$ at time $t=0$.

</dl>

<h4>
Python files
</h4>
<dl>

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

<font color='red'>Warning:</font> These files are generally changed
when setting up a run and the versions here may not be the ones actually
used.


<dl>
<dt>[code: claw.data]
<dd> This file contains a number of
parameter values that are used by CLAWPACK.  
The values in this file are read by the library routine
[clawcode: clawpack/1d/lib/claw1ez.f].  
Each line contains one or more values to be read
in, followed by comments that are ignored by the Fortran code but
may be used by Pythons scripts.


Some parameters that you might want to modify are described in the
[http://www.clawpack.org/users documentation].


<dt> [code: setprob.data]
<dd> This file contains the advection velocity $u$ and various other
parameters used in setting the initial conditions.  
Values in this file are read  in by the
subroutine [code: setprob.f95].


</dl>


<h4>Library routines</h3>

In addition to the Fortran routines in this library, several library
routines from [claw:clawpack/1d/lib] are used.  See the [code: Makefile]
to determine which ones are used.

[name:  instructions]
<h4>Instructions</h4> 

To run code:

{{{
    $ make .output
}}}

View plots interactively with Iplotclaw or use "make .plots" to create html
files.

end_html
