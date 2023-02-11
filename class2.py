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
        vshale = []
        for gamma in gamma_ray:
            vsh = round(
                (gamma - gamma_ray_min) / (gamma_ray_max - gamma_ray_min), 4)
            vshale.append(vsh)
        self.df['vshale'] = vshale
        return self.df

    def density_porosity(self, matrix_density, fluid_density):
        density = self.df[self.df.columns[2]]
        porosity = []
        for den in density:
            por = round((matrix_density - den) / (matrix_density - fluid_density), 4)
            porosity.append(por)
        self.df['PHI'] = porosity
        return self.df

    def sw_archie(self, archieA, archieM, archieN):
        porosity = self.df[self.df['PHI']]
        rw = self.df[self.df.columns[3]]
        rt = self.df[self.df.columns[4]]
        sw_archie = []
        for a, b, c in zip(porosity, rw, rt):
            sw = ((archieA /
                   (a ** archieM)) * (b / c)) ** (1 / archieN)
            sw_archie.append(sw)
        self.df['SW'] = sw_archie
        return self.df

    def porosity_effective(self):
        porosity = self.df[self.df['PHI']]
        vclay = self.df[self.df['vshale']]
        effective_porosity = []
        for por, shale_volume in zip(porosity, vclay):
            eff_por = porosity - self.shale_volume() * shale_volume
            effective_porosity.append(eff_por)
        self.df['effective porosity'] = effective_porosity
        return self.df

    def slowness_to_velocity(self):
        sonic = self.df[self.df.columns[4]]
        velocity = []
        for vel in sonic:
            son = 1000000 / vel
            velocity.append(son)
        self.df['velocity'] = velocity
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
        rw = self.df[self.df.columns[3]]
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
