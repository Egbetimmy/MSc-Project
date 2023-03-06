import math


class WellMetrics:
    """
    Conversion functions
    """

    def __int__(self, df):
        self.df = df

    def true_vertical_depth(self, x, y):
        measured_depth = self.df[self.df.columns[x]]
        angle_of_inclination = self.df[self.df.columns[y]]
        tvd = measured_depth * math.cos(math.radians(angle_of_inclination))
        return tvd

    # Depth and length conversions
    def ft_to_m(self, x):
        """
        Converts feet to metres.
        Parameters
        ----------
        self.df : float
            Input value in feet.
        Returns
        -------
        float
            Returns value in metres.
        """
        depth = self.df[self.df.columns[x]]
        depth_m = []
        for dept in depth:
            dept_m = round((dept * 0.3048), 1)
            depth_m.append(dept_m)
        self.df['Depth_m'] = depth_m
        return self.df

    def m_to_ft(self, x):
        """
        Converts metres to feet.
        Parameters
        ----------
        self.df : float
            Input value in metres.
        Returns
        -------
        float
            Returns value in feet.
        """
        depth = self.df[self.df.columns[x]]
        depth_ft = []
        for dept in depth:
            dept_ft = round((dept * 3.28084), 1)
            depth_ft.append(dept_ft)
        self.df['Depth_ft'] = depth_ft
        return self.df

    def ft_to_in(self, x):
        """
        Converts feet to inches.
        Parameters
        ----------
        self.df : float
            Input value in feet.
        Returns
        -------
        float
            Returns value in inches.
        """
        depth = self.df[self.df.columns[x]]
        depth_in = []
        for dept in depth:
            dept_in = round((dept * 12), 1)
            depth_in.append(dept_in)
        self.df['Depth_in'] = depth_in
        return self.df

    def in_to_ft(self, x):
        """
        Converts inches to feet.
        Parameters
        ----------
        self.df : float
            Input value in inches.
        Returns
        -------
        float
            Returns value in feet.
        """
        depth = self.df[self.df.columns[x]]
        depth_ft = []
        for dept in depth:
            dept_ft = round((dept / 12), 1)
            depth_ft.append(dept_ft)
        self.df['Depth_ft'] = depth_ft
        return self.df

    # Velocity / Slowness conversions
    def velocity_to_slowness(self, x):
        """
        Converts velocity to slowness.
        Parameters
        ----------
        self.df : float
            Input value in velocity units.
        Returns
        -------
        float
            Returns value in slowness units.
        """
        velocity = self.df[self.df.columns[x]]
        slowness = []
        for vel in velocity:
            dept_ft = round((1000000 / vel), 1)
            slowness.append(dept_ft)
        self.df['slowness'] = slowness
        return self.df

    def slowness_to_velocity(self, x):
        """
        Converts slowness to velocity.
        Parameters
        ----------
        self.df : float
            Input value in slowness units.
        Returns
        -------
        float
            Returns value in velocity units.
        """
        sonic = self.df[self.df.columns[x]]
        velocity = []
        for vel in sonic:
            son = 1000000 / vel
            velocity.append(son)
        self.df['velocity'] = velocity
        return self.df

    # Temperature conversions
    def temperature_convert(self, inputunits, outputunits, x):
        """
        Converts temperature from one unit to another.
        Parameters
        ----------
        self.df : float
            Input temperature value
        x: int
            Index of the column in the dataframe containing the temperature.
        inputunits : string
            Input temperature units:
                c = celsius
                f = fahrenheit
                k = kelvin
        outputunits : string
            Output temperature units:
                c = celsius
                f = fahrenheit
                k = kelvin
        Returns
        -------
        float
            Returns temperature value in required units.
        """
        temp = self.df[self.df.columns[x]]
        if inputunits.lower() == "c":
            if outputunits.lower() == "f":
                return (9 / 5) * temp + 32
            elif outputunits.lower() == "k":
                return temp + 273.15
            elif outputunits.lower() == "c":
                return self.df

        if inputunits.lower() == "f":
            if outputunits.lower() == "c":
                return (5 / 9) * temp - 32
            elif outputunits.lower() == "k":
                return (temp - 32) * (5 / 9) + 273.15
            elif outputunits.lower() == "f":
                return self.df

        if inputunits.lower() == "k":
            if outputunits.lower() == "c":
                return temp - 273.15
            elif outputunits.lower() == "f":
                return (temp - 273.15) * (9 / 5) + 32
            elif outputunits.lower() == "k":
                return self.df
        units = ["k", "c", "f"]

        if inputunits.lower() not in units or outputunits.lower() not in units:
            raise Exception("Enter a valid temperature inputunit or outputunit value. Must be: c, f or k")
