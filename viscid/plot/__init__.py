"""Package of modules that make it convinient to plot fields using
other libraries (Matplotlib / Mayavi)

Note:
    mpl and mvi are not imported by default since these import
    pylab and mlab, which has side-effects. To use them, you
    must use the imports explicitly,

    >>> from viscid.plot import mpl
    >>> from viscid.plot import mvi
"""

from viscid import import_injector

__all__ = ["mpl_extra",
           "mpl_style",
           "vseaborn"
          ]

import_injector(__all__, globals(), package="viscid.plot")
