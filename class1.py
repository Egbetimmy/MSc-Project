# check effectiveness

class Volumetrics:
    """
    Need to test the outcomes
    """

    def __init__(self, df, area, fvf):
        self.df = df
        self.area = area
        self.fvf = fvf

    def bulk_volume(self, x):
        bulk_volume = []
        thickness = self.df[self.df.columns[x]]
        for thick in thickness:
            bulk = thick * self.area
            bulk_volume.append(bulk)
        self.bulk_volume = bulk_volume
        self.df['Bulk Volume'] = self.bulk_volume
        return self.df

    def net_volume(self, x):
        net_to_gross = self.df[self.df.columns[x]]
        net_volume = []
        for bulk_volume, ntg in zip(self.bulk_volume, net_to_gross):
            net = bulk_volume * ntg
            net_volume.append(net)
        self.net_volume = net_volume
        self.df['Net Volume'] = self.net_volume
        return self.df

    def pore_volume(self, x):
        porosity = self.df[self.df.columns[x]]
        pore_volume = []
        for net_volume, por in zip(self.net_volume, porosity):
            pore = net_volume * por
            pore_volume.append(pore)
        self.pore_volume = pore_volume
        self.df['Pore Volume'] = self.pore_volume
        return self.df

    def hydrocarbon_pore_volume(self, x):
        Hsaturation = self.df[self.df.columns[x]]
        hydrocarbon_pore_volume = []
        for pore_volume, Hsh in zip(self.pore_volume, Hsaturation):
            bulk = pore_volume * Hsh
            hydrocarbon_pore_volume.append(bulk)
        self.hydrocarbon_pore_volume = hydrocarbon_pore_volume
        self.df['Hydrocarbon Pore Volume'] = self.hydrocarbon_pore_volume
        return self.df

    def calculate_oiip(self, x, y, z):
        net_pay = self.df[self.df.columns[x]]
        porosity = self.df[self.df.columns[y]]
        Hsaturation = self.df[self.df.columns[z]]
        oil = []
        for por, ntg, Hsh in zip(porosity, net_pay, Hsaturation):
            x = por * ntg * Hsh * 7758
            oil.append(x)
        self.df['oiip'] = oil
        return self.df

    def calculate_giip(self, x, y, z):
        net_pay = self.df[self.df.columns[x]]
        porosity = self.df[self.df.columns[y]]
        Hsaturation = self.df[self.df.columns[z]]
        gas = []
        for por, ntg, Hsh in zip(porosity, net_pay, Hsaturation):
            x = por * ntg * Hsh * 43560
            gas.append(x)
        self.df['giip'] = gas
        return self.df

    def calculate_stoiip(self, x, y, z):
        net_pay = self.df[self.df.columns[x]]
        porosity = self.df[self.df.columns[y]]
        Hsaturation = self.df[self.df.columns[z]]
        HC = []
        for por, ntg, Hsh in zip(porosity, net_pay, Hsaturation):
            Hsat = por * net_pay * Hsh
            HC.append(Hsat)
        stoiip = HC
        return stoiip

    """
    need to create a function to plot for proper visualization

    well.replace(-999.00, np.nan, inplace=True)


    """
