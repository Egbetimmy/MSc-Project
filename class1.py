# check effectiveness

class Volumetrics:
    """
    Need to test the outcomes
    """

    def __init__(self, df, area, fvf):
        self.df = df
        self.area = area
        self.fvf = fvf

    def bulk_volume(self, thickness_col):
        """
        Calculates the bulk volume of each data point in the dataframe based on a given thickness column.

        Args:
            thickness_col (str): The name of the column containing the thickness values.

        Returns:
            pandas.DataFrame: The input dataframe with a new column called 'Bulk Volume' containing the
            calculated bulk volume values.
        """

        # Get the thickness values of the reservoir
        thickness = self.df.iloc[:, thickness_col]

        # Calculate the thickness values of hydrocarbons in each cell
        bulk_volume = thickness * self.area

        # Add the calculated thickness values to the dataframe and return
        self.df['Bulk Volume'] = bulk_volume
        return self.df

    def net_volume(self, ntg_col_index):
        """
        Calculate the net volume of hydrocarbons in each cell of the reservoir.

        Parameters:
        -----------
        ntg_col_index: int
            Index of the column in the dataframe containing the net-to-gross ratio.

        Returns:
        --------
        pandas.DataFrame:
            The updated dataframe with a new column 'Net Volume' containing the calculated net volume.
        """

        # Get the net-to-gross ratio and bulk volume of the reservoir
        net_to_gross = self.df.iloc[:, ntg_col_index]
        bulk_volume = self.df['Bulk Volume']

        # Calculate the net volume of hydrocarbons in each cell
        net_volume = bulk_volume * net_to_gross

        # Add the calculated net volume to the dataframe and return
        self.df['Net Volume'] = net_volume
        return self.df

    def pore_volume(self, por_col, net_vol_col):
        """
        Calculates pore volume from porosity and net volume.

        Args:
            por_col (str): Name of the column containing porosity data.
            net_vol_col (str): Name of the column containing net volume data.

        Returns:
            pandas.DataFrame: Updated dataframe with a new 'Pore Volume' column.

        """
        porosity = self.df[por_col]
        net_volume = self.df[net_vol_col]
        pore_volume = porosity * net_volume
        self.df['Pore Volume'] = pore_volume
        return self.df

    def hydrocarbon_pore_volume(self, column_index):
        """
        Calculates the hydrocarbon pore volume in a reservoir zone.

        Args:
        column_index (int): Index of the column containing the hydrocarbon saturation data.

        Returns:
        pandas.DataFrame: DataFrame with a new column containing the hydrocarbon pore volume values.
        """
        # Get required data from DataFrame
        Hsaturation = self.df.iloc[:, column_index]
        pore_volume = self.df['Pore Volume']

        # Calculate hydrocarbon pore volume for each row
        hydrocarbon_pore_volume = pore_volume * Hsaturation

        # Add hydrocarbon pore volume column to DataFrame
        self.df['Hydrocarbon Pore Volume'] = hydrocarbon_pore_volume

        return self.df

    def calculate_oiip(self, net_pay_col, porosity_col, Hsaturation_col):
        """
        Calculates Original Oil in Place (OOIP) using net pay, porosity, and hydrocarbon saturation columns.

        Args:
        net_pay_col (str): Name of column containing net pay values.
        porosity_col (str): Name of column containing porosity values.
        Hsaturation_col (str): Name of column containing hydrocarbon saturation values.

        Returns:
        pandas.DataFrame: Original dataframe with a new column for calculated oiip values.
        """

        # Get required data from DataFrame
        net_pay = self.df[net_pay_col]
        porosity = self.df[porosity_col]
        Hsaturation = self.df[Hsaturation_col]

        # Calculate oiip values for each row
        oiip_value = porosity * net_pay * Hsaturation * 7758

        # Add hydrocarbon pore volume column to DataFrame
        self.df['oiip'] = oiip_value
        return self.df

    def calculate_giip(self, x, y, z):
        """
        Calculates the Gas Initially In Place (GIIP) of a reservoir.

        Parameters:
        x (int): Index of the net pay column in the dataframe
        y (int): Index of the porosity column in the dataframe
        z (int): Index of the gas saturation column in the dataframe

        Returns:
        pandas.DataFrame: A modified version of the input dataframe with a new 'giip' column added, containing
        the calculated GIIP values.

        """

        # Get required data from DataFrame
        net_pay = self.df[x]
        porosity = self.df[y]
        Hsaturation = self.df[z]

        # Calculate GIIP values for each row
        gas = porosity * net_pay * Hsaturation * 43560

        # Add GIIP values column to DataFrame
        self.df['giip'] = gas
        return self.df

    def calculate_stoiip(self, x, y, z):
        """
        Calculates the stock tank oil initially in place (STOIIP) based on net pay, porosity, and hydrocarbon
        saturation.

        Parameters:
        x (int): index of the column containing the net pay data
        y (int): index of the column containing the porosity data
        z (int): index of the column containing the hydrocarbon saturation data

        Returns:
        stoiip (list): list containing STOIIP values
        """

        # Get required data from DataFrame
        net_pay = self.df.iloc[:, x]
        porosity = self.df.iloc[:, y]
        hsaturation = self.df.iloc[:, z]

        # Calculate STOIIP values for each row
        hc_volume = porosity * net_pay * hsaturation

        stoiip = hc_volume.sum() * 7758  # convert from acre-ft to barrels
        return stoiip

    """
    need to create a function to plot for proper visualization

    well.replace(-999.00, np.nan, inplace=True)

    """
