import numpy as np

h = 6.62607015e-34  # Planck's constant (J·s)
c = 2.998e8         # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann's constant (J/K)

class ForwardModel:
    def __init__(self, temperature, wavelength):
        self.temperature = temperature
        self.wavelength = wavelength

    def planck_function(self):
        """
        Calculate the spectral radiance using Planck's law.

        Parameters:
        temperature (float): Temperature in Kelvin.
        wavelength (float): Wavelength in meters.

        Returns:
        float: Spectral radiance in W·sr⁻¹·m⁻³.
        """

        # Calculate spectral radiance
        exponent = (h * c) / (self.wavelength * k * self.temperature)
        spectral_radiance = (2 * h * c**2) / (self.wavelength**5 * (np.exp(exponent) - 1))
        
        return spectral_radiance