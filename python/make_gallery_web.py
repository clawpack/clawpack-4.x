"""
Create gallery files for the documentation on the Clawpack website.

OBSOLETE... instead use make_gallery.py and then webify.py.

These tools assume that the examples have already been run and the plots
produced using "make .plots".  

You should use the script python/make_all.py to do this first.
"""

import gallery as G
import os

G.claw_html_root='http://kingkong.amath.washington.edu/clawpack/trunk'
G.gallery_dir_default = os.path.join(G.clawdir_default,'doc','gallery')  
G.remake = True

G.make_all()

