'''\
=======
Mahotas
=======

A package for computer vision in Python.

Main Features
-------------

features
    Compute global and local features (several submodules, include SURF and Haralick features)
convolve
    Convolution and wavelets
morph
    Morphological features. Most are available at the mahotas level, include erode(), dilate()...
watershed
    Seeded watershed implementation
imread/imsave
    read/write image

Citation:

    Coelho, Luis Pedro, 2013. Mahotas: Open source software for scriptable
    computer vision. Journal of Open Research Software, 1:e3, DOI:
    http://dx.doi.org/10.5334/jors.ac
'''
try:
    from .bbox import bbox, croptobbox
    from .center_of_mass import center_of_mass
    from .convolve import convolve, convolve1d, median_filter, rank_filter, template_match, gaussian_filter1d, gaussian_filter
    from .convolve import haar, ihaar, daubechies, idaubechies, wavelet_center, wavelet_decenter
    from .distance import distance
    from .edge import sobel
    from .euler import euler
    from .histogram import fullhistogram
    from .labeled import border, borders, bwperim, label, labeled_sum
    from .features.moments import moments
    from .morph import cerode, close, close_holes, get_structuring_elem, disk, dilate, cdilate, hitmiss, erode, cwatershed, majority_filter, open, regmin, regmax
    from .resize import imresize
    from .stretch import stretch, stretch_rgb, as_rgb
    from .thin import thin
    from .thresholding import otsu, rc
    from .io import imread, imsave

    from .tests import run as test

    from .mahotas_version import __version__

    from . import colors
    from . import features
    from . import morph
    from . import segmentation
except ImportError:
    import sys
    _,e,_ = sys.exc_info()
    from sys import stderr
    stderr.write('''\
Could not import submodules (exact error was: %s).

There are many reasons for this error the most common one is that you have
either not built the packages or have built (using `python setup.py build`) or
installed them (using `python setup.py install`) and then proceeded to test
mahotas **without changing the current directory**.

Try installing and then changing to another directory before importing mahotas.
''' % e)

citation_text = '''
If you use mahotas please cite

    Coelho, Luis Pedro, 2013. Mahotas: Open source software for scriptable
    computer vision. Journal of Open Research Software, 1:e3, DOI:
    http://dx.doi.org/10.5334/jors.ac


In BibTex format:

@article{coelho:mahotas,
    title = {Mahotas: Open source software for scriptable computer vision},
    author = {Luis Pedro Coelho},
    journal = {Journal of Open Research Software},
    year = {2013},
    volume = {1},
    doi = {10.5334/jors.ac},
    url = {http://dx.doi.org/10.5334/jors.ac}
}
'''

def citation(print_out=True):
    if print_out:
        # Use a Python2/3 compatible form of printing:
        from sys import stdout
        stdout.write(citation_text)
    return citation_text

__all__ = [
    'as_rgb',
    'bbox',
    'border',
    'borders',
    'bwperim',
    'cdilate',
    'center_of_mass',
    'cerode',
    'close',
    'close_holes',
    'convolve',
    'convolve1d',
    'croptobbox',
    'cwatershed',
    'daubechies',
    'dilate',
    'distance',
    'erode',
    'euler',
    'fullhistogram',
    'gaussian_filter',
    'gaussian_filter1d',
    'get_structuring_elem',
    'haar',
    'hitmiss',
    'idaubechies',
    'ihaar',
    'imread',
    'imresize',
    'imsave',
    'label',
    'labeled_sum',
    'majority_filter',
    'median_filter',
    'moments',
    'open',
    'otsu',
    'rank_filter',
    'rc',
    'regmax',
    'regmin',
    'sobel',
    'stretch',
    'template_match',
    'thin',
    'wavelet_center',
    'wavelet_decenter',

    'morph',
    'features',
    'segmentation',

    'test',

    'citation',
    'citation_text'
    '__version__',
    ]

