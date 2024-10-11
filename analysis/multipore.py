import prody
import .msd_pf
import .permeation_events
import .axial_loads
import .survival_time

from datetime import datetime

class Multipore:
    def __init__(self, dcd=list()):
        self._dcd = dcd

    @property
    def dcd(self):
        return self._dcd

    @dcd.setter
    def dcd(self, dcd):
        if isinstance(dcd, list):
            if all([type(element) == str for element in dcd]):
                self._dcd += dcd
            else:
                raise TypeError('The elements of the list must all be strings, i.e. paths to the .dcd files')
        elif isinstance(dcd, str):
            self._dcd.append(dcd)
        else:
            raise TypeError('Must be a string pointing to the .dcd file')

    def pf(self, ):

    def permeation_events(self, ):

    def axial_loads(self, ):

    def survival_time(self, ):

    def run_analysis(self, ):



