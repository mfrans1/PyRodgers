import numpy as np


class Inversion:
    def __init__(self, altitude, wavelength, weighting_functions):
        self.altitude = np.asarray(altitude)
        self.wavelength = wavelength
        self.weighting_functions = np.asarray(weighting_functions)

    def basis_functions(self, basis_type="polynomial"):

        n_basis = len(self.weighting_functions)
        
        z = self.altitude / self.altitude[-1]

        if basis_type == "polynomial":
            self.basis = np.array([
                z**i for i in range(n_basis)
            ])

        elif basis_type == "sin":
            self.basis = np.array([
                np.sin(2 * np.pi * i * z)
                for i in range(1, n_basis + 1)
            ])

        elif basis_type == "cos":
            self.basis = np.array([
                np.cos(2 * np.pi * i * z)
                for i in range(n_basis)
            ])

        else:
            raise ValueError(f"Unknown basis function type: {basis_type}")

    def construct_C(self):
        C = np.empty((
            self.weighting_functions.shape[0],
            self.basis.shape[0]
        ))

        for i, K in enumerate(self.weighting_functions):
            for j, W in enumerate(self.basis):
                C[i, j] = np.trapezoid(K * W, self.altitude)

        self.C = C


    def reconstruct_signal(self, L):
        signal_recon = self.basis.T @ np.linalg.inv(self.C) @ L

        return signal_recon

