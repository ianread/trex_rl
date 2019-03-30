import mss as _mss
import numpy as _np

class ScreenCapture(object):
    def __init__(self):
        self._regions = {}
        self._sct = _mss.mss()

    def create_new_region(self, label, bounding):
        self._regions[label] = bounding

    def get_regions(self):
        return self._regions

    def delete_region(self, label):
        del self._regions[label]
    
    def get_labels(self):
        return self._region.keys()

    def get_next(self):
        regions_returned = {}
        for label in self._regions:
            regions_returned[label] = _np.array(self._sct.grab(self._region[label]))
        return regions_returned
