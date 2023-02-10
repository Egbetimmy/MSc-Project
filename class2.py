import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class petrophysics:
    """
        Need to test the outcomes
        """

    def __init__(self, df):
        self.df = df

    def shale_volume(self):
        gamma_ray = self.df[self.df.columns[1]]
        gamma_ray_max = gamma_ray.quantile(q=0.99)
        gamma_ray_min = gamma_ray.quantile(q=0.01)
        self.df['vshale'] = round(
            (gamma_ray - gamma_ray_min) / (gamma_ray_max - gamma_ray_min), 4)
        return self.df

    def density_porosity(self, matrix_density, fluid_density):
        density = self.df[self.df.columns[2]]
        self.df['PHI'] = round((matrix_density - density) / (matrix_density - fluid_density), 4)
        return self.df

    def sw_archie(self, archieA, archieM, archieN):
        porosity = self.df[self.df['PHI']]
        self.df['SW'] = ((archieA /
                          (porosity ** archieM)) * (self.df['rw'] / self.df['rt'])) ** (1 / archieN)
        return self.df

    def porosity_effective(self, phitclay):
        porosity = self.df[self.df['PHI']]
        self.df['effective porosity'] = porosity - self.shale_volume() * phitclay
        return self.df

    def slowness_to_velocity(self):
        sonic = self.df[self.df.columns[4]]
        self.df['velocity'] = 1000000 / sonic
        return self.df

    def formation_factor(self, arch_a, arch_m):
        porosity = self.df[self.df['PHI']]
        formaton_factor = []
        for por in porosity:
            form = arch_a / (por ** arch_m)
            formaton_factor.append(form)
        self.df['formation_factor'] = formaton_factor
        return self.df

    def ro(self):
        rw = self.df[self.df['PHI']]
        formation_factor = self.df[self.df['formation_factor']]
        ro = []
        for res, form in zip(rw, formation_factor):
            rr = form * res
            ro.append(rr)
        self.df['ro'] = ro
        return self.df

    def swirr(self):
        formation_factor = self.df[self.df['formation_factor']]
        swirr = []
        for form in formation_factor:
            swr = (form / 2000) ** (1 / 2)
            swirr.append(swr)
        self.df['swirr'] = swirr
        return self.df

    def permeability(self):
        porosity = self.df[self.df['PHI']]
        swirr = self.df[self.df['swirr']]
        permeability = []
        for por, swr in zip(porosity, swirr):
            perm = 307 + (26552 * (por ** 2)) - (3450 * (por * swr) ** 2)
            permeability.append(perm)
        self.df['permeability'] = permeability
        return self.df
