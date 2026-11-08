import numpy as np

h = 6.62607015e-34  # Planck's constant (J s)
c = 2.998e8         # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann's constant (J/K)


class ForwardModel:
    def __init__(self, temperature, altitude, wavelength):
        self.temperature = np.asarray(temperature)
        self.altitude = np.asarray(altitude)
        self.wavelength = wavelength

    def planck_function(self):
        """Calculate spectral radiance at each altitude."""

        exponent = (
            h * c / (self.wavelength * k * self.temperature)
        )

        spectral_radiance = (
            2 * h * c**2
            / (self.wavelength**5 * np.expm1(exponent))
        )

        return spectral_radiance

    def simulate_toa(self, weighting_functions):
        """Integrate the radiance profile against each weighting function."""

        B = self.planck_function()

        L = np.array([
            np.trapezoid(B * K, self.altitude)
            for K in weighting_functions
        ])

        return L