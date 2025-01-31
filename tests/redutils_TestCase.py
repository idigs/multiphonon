#!/usr/bin/env python
#

import pytest
from functools import reduce
# pytestmark = pytest.mark.skipif(False, reason="only run mannually")
pytestmark = pytest.mark.needs_mantid

interactive = False

import os
here = os.path.dirname(__file__)
datadir = os.path.join(here, "data")

import imp
dataurls = imp.load_source('dataurls', os.path.join(datadir, 'dataurls.py'))

import numpy as np, histogram.hdf as hh
from multiphonon.getdos import getDOS

import unittest
class TestCase(unittest.TestCase):

    def setUp(self):
        dest = os.path.join(datadir, 'ARCS_V_annulus.nxs')
        if os.path.exists(dest): return
        url = dataurls.ARCS_V_annulus
        cmd = 'wget --quiet %r -O %r' % (url, dest)
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return

    def test1(self):
        "multiphonon.redutils"
        from multiphonon.redutils import reduce
        Qaxis = 0, 0.1, 14
        reduce(os.path.join(datadir, 'ARCS_V_annulus.nxs'), Qaxis, 'iqe.nxs')
        return
    
    def test2(self):
        "multiphonon.redutils"
        from multiphonon.redutils import reduce
        Qaxis = -0.05, 0.1, 14.95001
        Eaxis = -100.5, 1., 99.5001
        reduce(os.path.join(datadir, 'ARCS_V_annulus.nxs'), Qaxis, 'iqe.nxs', eaxis=Eaxis)
        return
    pass  # end of TestCase


if __name__ == "__main__":
    interactive = True
    unittest.main()
    
# End of file 
