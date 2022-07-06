

def set_plotparams(ax_obj, xticks=(50, 5), yticks=(2, 0.4), grid=True, legend=False, fs=14,
                   ms=1.5, facecolor="white",linewidth=0.5):
    import matplotlib as mpl
    from matplotlib.ticker import MultipleLocator
    """
    Sets plot parameters to the axes object 'ax_obj'.
    Args:
        ax_obj      : Axes object to be used for plotting and setting plot parameters
        xticks      : X-Axis Major and Minor tick intervals
        yticks      : Y-Axis Major and Minor tick intervals
        grid        : Boolean stating whether to enable Grid in the plot
        legend      : Boolean stating whether legend is to be displayed in the plot
        fs          : Font of the labels in the legend
        ms          : Scaled marker size to be used in the legend
    Returns:
    """
    mpl.rcParams['lines.linewidth']='0.5'
    mpl.rcParams['lines.markersize']='4.0'
    mpl.rcParams['errorbar.capsize']='1.0'
    mpl.rcParams['axes.linewidth']= '1.0'

    if legend:
        handles, labels = ax_obj.get_legend_handles_labels()
        handles = [h[0] if isinstance(h, container.ErrorbarContainer) else h for h in handles]
        ax_obj.legend(handles, labels, fontsize=fs, markerscale=ms, frameon=False, shadow=True)

    if grid:
        ax_obj.grid(True, which='major', ls='-', lw=0.5, alpha=0.8)
        
    if facecolor:
        ax_obj.set_facecolor(facecolor)

    ax_obj.xaxis.set_ticks_position('both')
    ax_obj.yaxis.set_ticks_position('both')
    ax_obj.xaxis.set_major_locator(MultipleLocator(xticks[0]))
    ax_obj.xaxis.set_minor_locator(MultipleLocator(xticks[1]))
    ax_obj.yaxis.set_major_locator(MultipleLocator(yticks[0]))
    ax_obj.yaxis.set_minor_locator(MultipleLocator(yticks[1]))
    ax_obj.tick_params(axis='both', which='major', direction='in', width=1.3, length=7, color='k',
                       labelcolor='k', labelsize=fs)
    ax_obj.tick_params(axis='both', which='minor', direction='in', width=0.7, length=3.5, color='k',
                       labelcolor='k', labelsize=fs)
