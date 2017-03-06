import random
import utils


class PlaneSimulator(object):
    def __init__(self, initial_tilt=0, mean_tilt=0, max_correction=5, turbulance_deviation=15):
        self.current_tilt = initial_tilt
        self.mean_tilt = mean_tilt
        self.max_correction = max_correction
        self.turbulance_deviation = turbulance_deviation

    def run(self):
        while True:
            print "Current tilt %s" % self.current_tilt

            random_turbulance = self._generate_new_turbulance()
            print "Turbulance %s" % random_turbulance

            self.current_tilt += random_turbulance
            print "Current tilt with turbulance %s" % self.current_tilt

            correction = self._get_correction_value(self.current_tilt)
            print "Correction value %s" % correction

            self.current_tilt += correction
            print "Tilt with correction %s\n" % self.current_tilt

    def _generate_new_turbulance(self):
        return random.gauss(self.mean_tilt, self.turbulance_deviation)

    def _get_correction_value(self, current_tilt):
        if abs(current_tilt) < self.max_correction:
            return -current_tilt

        return -utils.signum(current_tilt) * self.max_correction
