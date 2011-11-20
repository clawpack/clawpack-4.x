
def fix_long_tick_labels(xlimits='auto',ylimits='auto',kwargs={}):
    """
    Utility to stop matplotlib from only displaying part of long
    tickmark labels.

    xlimits, ylimits can be set to lists of 2 elements each since
    limits have to be set before grabbing the ticks and reformatting.

    kwargs can be a dictionary of keyword arguments to be passed
    to xticks and yticks.  For example: kwargs={'fontsize' : 15}
    for larger labels.
    
    Problem with this way of doing it:  Ticks are fixed if you zoom in on plot.
    """

    from pylab import figure, xticks, yticks, xlim, ylim
    if xlimits != 'auto':
        xlim(xlimits)
        print "+++ xlim: ",xlim()
    if ylimits != 'auto':
        ylim(ylimits)
    locs,labels = xticks()
    xticks(locs, [str(loc) for loc in locs], rotation=20, **kwargs)
    locs,labels = yticks()
    yticks(locs, [str(loc) for loc in locs], **kwargs)

def plotbox(xy, kwargs={'color':'b', 'linewidth':2}):
    """
    Add a box around a region to an existing plot.
    """
    from pylab import plot
    if type(xy)==str:
        xy=x1.split()
    x1 = float(xy[0])
    x2 = float(xy[1])
    y1 = float(xy[2])
    y2 = float(xy[3])
    plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],**kwargs)

    
def boxfg(outdir="."):
    """
    Plot boxes around all the fixed grids specified in setfixedgrids.data.
    Use to add boxes to existing plot of topo or solution.
    """

    import os
    from pylab import plot,text,hstack
    from numpy import loadtxt
    try:
        fname = os.path.join(outdir,'setfixedgrids.data')
        fgrids = loadtxt(os.path.join(outdir,'setfixedgrids.data'),skiprows=7)
    except:
        print "*** problem loading ",fname

    if fgrids.ndim == 1:
        nfgrids = 1
    else:
        nfgrids = fgrids.shape[0]

    for irow in range(nfgrids):
        if fgrids.ndim == 1:
            fgrid = fgrids
        else:
            fgrid = fgrids[irow,:]
        x1 = fgrid[3]
        x2 = fgrid[4]
        y1 = fgrid[5]
        y2 = fgrid[6]
        plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],'b-')
        text(x1-0.4*(x2-x1),y1,"FG %s" % str(irow+1))


