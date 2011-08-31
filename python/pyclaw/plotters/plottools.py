
def fix_long_tick_labels():
    """
    Utility to stop matplotlib from only displaying part of long
    tickmark labels.
    """
    from pylab import figure, xticks, yticks
    kwargs = {}
    #kwargs = {'fontsize' : 15}
    locs,labels = xticks()
    xticks(locs, [str(loc) for loc in locs], rotation=20, **kwargs)
    locs,labels = yticks()
    yticks(locs, [str(loc) for loc in locs], **kwargs)

