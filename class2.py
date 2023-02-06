import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class petrophysics:
    """
        Need to test the outcomes
        """

    def __init__(self, df):
        self.df = df
        self.gamma_ray = self.df[self.df.columns[1]]
        self.input_density = self.df[self.df.columns[2]]
        self.porosity = self.df[self.df.columns[3]]
        self.gamma_ray_max = self.gamma_ray.quantile(q=0.99),
        self.gamma_ray_min = self.gamma_ray.quantile(q=0.01)

    def shale_volume(self):
        self.df['vshale'] = round(
            (self.gamma_ray - self.gamma_ray_min) / (self.gamma_ray_max - self.gamma_ray_min), 4)
        return self.df

    def density_porosity(self, matrix_density, fluid_density):
        self.df['PHI'] = round((matrix_density - self) / (matrix_density - fluid_density), 4)
        return self.df

    def sw_archie(self, archieA, archieM, archieN):
        self.df['SW'] = ((archieA / (self.porosity ** archieM)) * (self.df['rw'] / self.df['rt'])) ** (1 / archieN)
        return self.df

    def porosity_effective(phit, vclay, phitclay):
        """
        Converts total porosity to effective porosity
        Parameters
        ----------
        phit : float
            Total porosity (decima)
        vclay : float
            Volume of clay (decimal)
        phitclay : float
            Clay porosity - taken from a shale interval (decimal)
        Returns
        -------
        float
            Returns effective porosity (decimal)
        """
        return phit - vclay * phitclay
