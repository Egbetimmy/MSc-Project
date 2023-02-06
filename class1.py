class volumetrics:
    """
    Need to test the outcomes
    """

    def __init__(self, df, area, fvf):
        self.df = df
        self.thickness = self.df[self.df.columns[1]]
        self.ntg = self.df[self.df.columns[2]]
        self.porosity = self.df[self.df.columns[3]]
        self.Hsaturation = self.df[self.df.columns[4]]
        self.area = area
        self.fvf = fvf

    def bulk_volume(self):
        bulk_volume = []
        for thickness in self.thickness:
            bulk = thickness * self.area
            bulk_volume.append(bulk)

        self.bulk_volume = bulk_volume
        self.df['Bulk Volume'] = self.bulk_volume
        return self.df

    def net_volume(self):
        net_volume = []
        for bulk_volume, ntg in zip(self.bulk_volume, self.ntg):
            net = bulk_volume * ntg
            net_volume.append(net)

        self.net_volume = net_volume
        self.df['Net Volume'] = self.net_volume
        return self.df

    def pore_volume(self):
        pore_volume = []
        for net_volume, ntg in zip(self.net_volume, self.ntg):
            pore = net_volume * ntg
            pore_volume.append(pore)

        self.pore_volume = pore_volume
        self.df['Pore Volume'] = self.pore_volume
        return self.df

    def hydrocarbon_pore_volume(self):
        hydrocarbon_pore_volume = []
        for pore_volume, ntg in zip(self.pore_volume, self.ntg):
            bulk = pore_volume * ntg
            hydrocarbon_pore_volume.append(bulk)

        self.hydrocarbon_pore_volume = hydrocarbon_pore_volume
        self.df['Hydrocarbon Pore Volume'] = self.hydrocarbon_pore_volume
        return self.df

    def oiip(self):
        """
        calculate oiip
        """
        pass

    def giip(self):
        """
        calculate giip
        """
        pass

    def stoiip(self):
        """
        calculate stoiip
        """
        pass

    def stgiip(self):
        """
        calculate stgiip
        """
        pass

    """
    need to create a function to plot for proper visualization

    well.replace(-999.00, np.nan, inplace=True)


    """
