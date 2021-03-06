# -*- coding: utf-8 -*-
# Copyright (C) 2006-2010  Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# License: MIT (see COPYING file)

from __future__ import division
import numpy as np

__all__ = ['thin']

def thin(binimg):
    """
    skel = thin(binimg)

    Skeletonisation by thinning

    Parameters
    ----------
    binimg : Binary input image

    Returns
    -------
    skel : Skeletonised version of `binimg`
    """
    from .bbox import bbox
    from ._thin import thin as _thin

    res = np.zeros_like(binimg)
    min0,max0,min1,max1 = bbox(binimg)
    r,c = (max0-min0,max1-min1)

    image_exp = np.zeros((r+2, c+2), bool)
    image_exp[1:r+1, 1:c+1] = binimg[min0:max0,min1:max1]
    imagebuf = np.empty((r+2,c+2), bool)

    _thin(image_exp, imagebuf)
    res[min0:max0,min1:max1] = image_exp[1:r+1, 1:c+1]
    return res

