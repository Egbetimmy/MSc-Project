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
        for net_volume, porosity in zip(self.net_volume, self.porosity):
            pore = net_volume * porosity
            pore_volume.append(pore)

        self.pore_volume = pore_volume
        self.df['Pore Volume'] = self.pore_volume
        return self.df

    def hydrocarbon_pore_volume(self):
        hydrocarbon_pore_volume = []
        for pore_volume, Hsaturation in zip(self.pore_volume, self.Hsaturation):
            bulk = pore_volume * Hsaturation
            hydrocarbon_pore_volume.append(bulk)

        self.hydrocarbon_pore_volume = hydrocarbon_pore_volume
        self.df['Hydrocarbon Pore Volume'] = self.hydrocarbon_pore_volume
        return self.df

    def calculate_oiip(self, net_pay, initial_oil_saturation):
        oiip = self.porosity * net_pay * initial_oil_saturation * 7758
        return oiip

    def calculate_giip(self, net_pay, initial_gas_saturation):
        giip = self.porosity * net_pay * initial_gas_saturation * 43560
        return giip

    def calculate_stoiip(self, net_pay, initial_oil_saturation):
        stoiip = self.porosity * net_pay * initial_oil_saturation
        return stoiip

    """
    need to create a function to plot for proper visualization

    well.replace(-999.00, np.nan, inplace=True)


    """
