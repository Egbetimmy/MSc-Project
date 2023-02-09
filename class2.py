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
        self.density = self.df[self.df.columns[2]]
        self.porosity = self.df[self.df.columns[3]]
        self.sonic = self.df[self.df.columns[4]]
        self.gamma_ray_max = self.gamma_ray.quantile(q=0.99),
        self.gamma_ray_min = self.gamma_ray.quantile(q=0.01)

    def shale_volume(self):
        self.df['vshale'] = round(
            (self.gamma_ray - self.gamma_ray_min) / (self.gamma_ray_max - self.gamma_ray_min), 4)
        return self.df

    def density_porosity(self, matrix_density, fluid_density):
        self.df['PHI'] = round((matrix_density - self.density) / (matrix_density - fluid_density), 4)
        return self.df

    def sw_archie(self, archieA, archieM, archieN):
        self.df['SW'] = ((archieA / (self.porosity ** archieM)) * (self.df['rw'] / self.df['rt'])) ** (1 / archieN)
        return self.df

    def porosity_effective(self, phitclay):
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
        self.df['effective porosity'] = self.porosity - self.shale_volume() * phitclay
        return self.df

    def slowness_to_velocity(self):
        """
        Converts slowness to velocity.
        Parameters
        ----------
        inputvalue : float
            Input value in slowness units.
        Returns
        -------
        float
            Returns value in velocity units.
        """

        self.df['velocity'] = 1000000 / self.sonic
        return self.df

    def formation_factor(self, arch_a, arch_m):
        """
        Computes Archie Formation Factor (F)
        Parameters
        ----------
        arch_a : float
            Archie Tortuosity Factor - a
        phi : [type]
            Porosity (decimal)
        arch_m : float
            Archie Cementation Exponent - m
        Returns
        -------
        float
            Returns Archie Formation Factor
        """
        self.df['formation_factor'] = arch_a / (self.porosity ** arch_m)
        return self.df

    def ro(self, formation_factor, rw):
        """
        Archie Ro - Resistivity of water saturation formation (ohm.m)
        Parameters
        ----------
        formation_factor : float
            Archie Formation Factor
        rw : float
            Resistivity of formation water (ohm.m)
        Returns
        -------
        float
            Returns resistivity of water saturation formation (ohm.m)
        """
        ro = formation_factor * rw
        return ro

    def swirr(self, formation_factor):
        swirr = (formation_factor / 2000) ** (1/2)

        return swirr
    # nothing


    def permeability(self, swirr):
        permeability = 307 + (26552 * (self.porosity ** 2)) - (3450 * (self.porosity * swirr)**2)

        return permeability
