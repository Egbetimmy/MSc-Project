import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker


def make_facies_log_plot(logs, facies_colors, Formation_name, top):
    logs = logs.sort_values(by='DEPT')
    cmap_facies = colors.ListedColormap(
        facies_colors[0:len(facies_colors)], 'indexed')

    ztop = logs.DEPT.min();
    zbot = logs.DEPT.max()

    cluster = np.repeat(np.expand_dims(logs['Facies_pred'].values, 1), 100, 1)

    f, ax = plt.subplots(nrows=1, ncols=7, figsize=(19, 16))
    ax[0].plot(logs.GR, logs.DEPT, '-g', linewidth=2)
    ax[1].plot(logs.NPLS, logs.DEPT, '-', linewidth=2)
    ax[2].plot(logs.RHOB, logs.DEPT, '-', color='0.5', linewidth=2)
    ax[3].plot(logs.DT, logs.DEPT, '-', color='r', linewidth=2)
    ax[4].plot(logs.PE, logs.DEPT, '-', color='black', linewidth=2)
    ax[5].plot(logs.Log_ILD, logs.DEPT, '-', color='purple', linewidth=2)
    im = ax[6].imshow(cluster, interpolation='none', aspect='auto',
                      cmap=cmap_facies, vmin=1, vmax=8)
    #     im=ax[6].imshow(cluster, interpolation='none', aspect='auto',
    #                     cmap=cmap_facies,vmin=1,vmax=6)

    divider = make_axes_locatable(ax[6])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((30 * ' ').join(['1', '2',
                                    '3', '4 ', ' 5 ', ' 6  ',
                                    ' 7 ', '8']))
    #     cbar.set_label((35*' ').join(['1', '2',
    #                                  '3', '4 ', ' 5 ', ' 6  ']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    tick_inter = [80, 10, 0.3, 20, 1.1, 1.0]

    for i in range(len(ax) - 1):
        ax[i].set_ylim(ztop, zbot)
        ax[i].invert_yaxis()
        ax[i].grid(which='minor', axis='both')
        ax[i].locator_params(axis='x', nbins=3)

    tops = len(Formation_name)

    for k in range(tops):
        ax[0].set_xlabel("GR (api)", fontsize=15)
        ax[0].set_xlim(logs.GR.min(), logs.GR.max())
        ax[0].xaxis.set_ticks(np.arange(0, int(logs.GR.max()), tick_inter[0]))
        ax[0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0i'))
        y = top[k] * np.ones((len(logs.GR), 1))
        x = logs.GR
        ax[0].plot(x, y, 'y', linewidth=1)
        ax[0].text(200, top[k] - 10, Formation_name[k], fontsize=12, bbox=dict(facecolor='yellow', alpha=0.05))

        ax[1].set_xlabel("NPLS (%)", fontsize=15)
        ax[1].set_xlim(logs.NPLS.min(), logs.NPLS.max())
        ax[1].xaxis.set_ticks(np.arange(0, int(logs.NPLS.max()), tick_inter[1]))
        ax[1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0i'))
        y = top[k] * np.ones((len(logs.NPLS), 1))
        x = logs.NPLS
        ax[1].plot(x, y, 'y', linewidth=1)

        ax[2].set_xlabel("RHOB (g/cm^{3})", fontsize=15)
        ax[2].set_xlim(logs.RHOB.min(), logs.RHOB.max())
        ax[2].xaxis.set_ticks(np.arange(logs.RHOB.min(), (logs.RHOB.max()), tick_inter[2]))
        ax[2].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
        y = top[k] * np.ones((len(logs.RHOB), 1))
        x = logs.RHOB
        ax[2].plot(x, y, 'y', linewidth=1)

        ax[3].set_xlabel("DT (μs/ft)", fontsize=15)
        ax[3].set_xlim(logs.DT.min(), logs.DT.max())
        ax[3].xaxis.set_ticks(np.arange(logs.DT.min(), int(logs.DT.max()), tick_inter[3]))
        ax[3].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0i'))
        y = top[k] * np.ones((len(logs.DT), 1))
        x = logs.DT
        ax[3].plot(x, y, 'y', linewidth=1)

        ax[4].set_xlabel("PE (b/E)", fontsize=15)
        ax[4].set_xlim(logs.PE.min(), logs.PE.max())
        ax[4].xaxis.set_ticks(np.arange(logs.PE.min(), (logs.PE.max()), tick_inter[4]))
        ax[4].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
        y = top[k] * np.ones((len(logs.PE), 1))
        x = logs.PE
        ax[4].plot(x, y, 'y', linewidth=1)

        ax[5].set_xlabel("Log_ILD (Ω/m)", fontsize=15)
        ax[5].set_xlim(logs.Log_ILD.min(), logs.PE.max())
        ax[5].xaxis.set_ticks(np.arange(logs.Log_ILD.min(), (logs.Log_ILD.max()), tick_inter[5]))
        ax[5].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
        y = top[k] * np.ones((len(logs.Log_ILD), 1))
        x = logs.Log_ILD
        ax[5].plot(x, y, 'y', linewidth=1)

        ax[6].set_xlabel('Facies', fontsize=15)

        ax[1].set_yticklabels([]);
        ax[2].set_yticklabels([]);
        ax[3].set_yticklabels([])
        ax[4].set_yticklabels([]);
        ax[5].set_yticklabels([]);
        ax[6].set_yticklabels([])
        ax[6].set_xticklabels([])
        f.suptitle('Well: %s' % logs.iloc[0]['Well name'], fontsize=14, y=0.94)

    # f.tight_layout()


def rearrange_columns(df, col_order):
    """
    Rearrange columns in a pandas dataframe based on a given list of column names.

    Parameters
    -----------
    df : pandas.DataFrame
        Input dataframe
    col_order : list
        List of column names in the order they should be arranged

    Returns
    --------
    df : pandas.DataFrame
        Dataframe with rearranged columns
    """
    # Get a list of all columns in the dataframe
    cols = df.columns.tolist()

    # Make sure all the columns in col_order are present in the dataframe
    for col in col_order:
        if col not in cols:
            raise ValueError(f"{col} not found in dataframe columns")

    # Rearrange the columns based on col_order
    df = df.reindex(columns=col_order)

    return df


def rename_columns(df, old_names, new_names):
    """
    Rename columns in a dataframe.

    Parameters
    ----------
    df (pd.DataFrame):
        the input dataframe
    old_names (list):
        a list of the current column names
    new_names (list):
        a list of the new column names, in the same order as old_names

    Returns
    ----------
    pd.DataFrame:
        the renamed dataframe
    """
    renamed_df = df.rename(columns=dict(zip(old_names, new_names)))
    return renamed_df


def facies_classification(column):
    """
        Classify lithofacies based on gamma ray values.

        Parameters
        ----------
        df (pd.DataFrame):
            Dataframe containing gamma ray values.

        Returns
        ----------
        pd.DataFrame:
            Dataframe with facies classification.
        """

    facies = []
    for value in column:
        if np.isnan(value):
            facies.append('None')
        elif value < 66:
            facies.append('sand')
        elif 66 <= value < 86:
            facies.append('shaly sand')
        else:
            facies.append('shale')

    return facies


def vs_from_vp(df):
    """
    Calculates S-wave velocity (m/s) from compressional wave velocity using Gardner equation.

    Parameters
    ----------
    df:
        pandas DataFrame containing compressional wave velocity (m/s) in column 'vp'

    Returns
    ----------
    list of S-wave velocities (m/s)
    """
    vp = df['vp']
    vs = round(vp / (2 ** 0.5), 4)
    return vs.tolist()


# %matplotlib inline
class Petrophysics:
    """
        Need to test the outcomes
        """

    def __init__(self, df):
        self.df = df

    def shale_volume(self, x):
        """
        Calculates shale volume from gamma ray data.

        Parameters
        ----------
        x : int
            Column index of the gamma ray data in the dataframe.

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the calculated shale volume data.
        """

        # Extract gamma ray data from dataframe
        gamma_ray = self.df.iloc[:, x]

        # Calculate gamma ray percentiles
        gamma_ray_max = gamma_ray.quantile(q=0.99)
        gamma_ray_min = gamma_ray.quantile(q=0.01)

        # Calculate shale volume data
        vshale = (gamma_ray - gamma_ray_min) / (gamma_ray_max - gamma_ray_min)

        # Round shale volume data to four decimal places
        vshale = vshale.round(4)

        # Create a new column in the dataframe for the shale volume data
        self.df['vshale'] = vshale

        return self.df

    def density_porosity(self, x, matrix_density, fluid_density):
        """
        Calculates density porosity from density data.

        Parameters
        ----------
        x : int
            Column index of the density data in the dataframe.
        matrix_density : float
            Matrix density (g/cc).
        fluid_density : float
            Fluid density (g/cc).

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the calculated density porosity data.
        """

        # Extract density data from dataframe
        density = self.df.iloc[:, x]

        # Calculate density porosity data
        porosity = (matrix_density - density) / (matrix_density - fluid_density)

        # Round density porosity data to four decimal places
        porosity = porosity.round(4)

        # Create a new column in the dataframe for the density porosity data
        self.df['PHI'] = porosity

        return self.df

    def sw_archie(self, x, y, archieA, archieM, archieN):
        """
        Calculates water saturation using the Archie equation.

        Parameters
        ----------
        x : int
            Column index of the resistivity of the formation water (Rw) data in the dataframe.
        y : int
            Column index of the true resistivity (Rt) data in the dataframe.
        archieA : float
            Archie constant A.
        archieM : float
            Archie exponent m.
        archieN : float
            Archie exponent n.

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the calculated water saturation data.
        """

        # Extract necessary data from dataframe
        porosity = self.df['PHI']
        rw = self.df.iloc[:, x]
        rt = self.df.iloc[:, y]

        # Calculate water saturation using the Archie equation
        sw_archie = (archieA / (porosity ** archieM)) * (rw / rt) ** archieN

        # Create a new column in the dataframe for the water saturation data
        self.df['SW'] = sw_archie

        return self.df

    def sw_simandoux(self, rw_col, rt_col, archieA, archieM, archieN, rshale_col):
        """
        Calculates water saturation using the Simandoux equation.

        Parameters
        ----------
        rw_col (int):
            Index of the column containing the formation water resistivity values.
        rt_col (int):
            Index of the column containing the true resistivity values.
        archieA (float):
            Archie's A constant.
        archieM (float):
            Archie's M constant.
        archieN (float):
            Archie's N constant.
        rshale_col (float):
            Average resistivity in shale.

        Returns
        ----------
        sw_simandoux (list):
            List of water saturation values calculated using the Simandoux equation.
        """
        # Get required columns from DataFrame
        phie_col = self.df['effective porosity']
        rw = self.df.iloc[:, rw_col]
        rt = self.df.iloc[:, rt_col]
        vclay_col = self.df.iloc[:, rshale_col]

        # Calculate Simandoux equation components
        A = (1 - vclay_col) * archieA * rw / (phie_col ** archieM)
        B = A * vclay_col / (2 * rshale_col)
        C = A / rt

        # Calculate water saturation using Simandoux equation
        sw_simandoux = ((B ** 2 + C) ** 0.5 - B) ** (2 / archieN)

        return sw_simandoux

    def porosity_effective(self, phitclay):
        """
        Converts total porosity to effective porosity

        Parameters
        ----------
        phitclay : float
            Clay porosity - taken from a shale interval (decimal)

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the effective porosity (decimal)
        """

        # Extract input columns from dataframe
        phit = self.df['PHI']
        vclay = self.df['vshale']

        # Calculate effective porosity
        effective_porosity = phit - vclay * phitclay

        # Create a new column in the dataframe for the effective porosity
        self.df['effective porosity'] = effective_porosity

        return self.df

    def slowness_to_velocity(self, x):
        """
        Converts slowness to velocity.

        Parameters
        ----------
        x : int
            Column index of the slowness data in the dataframe.

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the converted velocity data.
        """

        # Extract slowness data from dataframe
        slowness = self.df.iloc[:, x]

        # Calculate velocity data
        velocity = 1000000 / slowness

        # Create a new column in the dataframe for the velocity data
        self.df['velocity'] = velocity

        return self.df

    def synthetic_seismic(self, x):
        """
        Calculates synthetic seismic data.

        Parameters
        ----------
        x : int
            Column index of the density data in the dataframe.

        Returns
        -------
        pandas.DataFrame
            A dataframe containing the calculated synthetic seismic data.
        """

        # Extract velocity and density data from dataframe
        velocity = self.df['velocity']
        density = self.df.iloc[:, x]

        # Calculate synthetic seismic data
        synthetic = velocity * density

        # Create a new column in the dataframe for the synthetic seismic data
        self.df['synthetic_seismic'] = synthetic

        return self.df

    def formation_factor(self, arch_a, arch_m):
        """
        Calculates formation factor using Archie's equation
        Parameters
        ----------
        arch_a : float
            Archie's constant 'a' (decimal)
        arch_m : float
            Archie's constant 'm' (decimal)
        Returns
        -------
        DataFrame
            Returns a dataframe containing the formation factor (decimal)
        """

        # Extract input columns from dataframe
        porosity = self.df['PHI']

        # Calculate synthetic formation factor
        formation_factor = arch_a / porosity ** arch_m

        # Create a new column in the dataframe for the formation factor data
        self.df['formation_factor'] = formation_factor
        return self.df

    def ro(self, rw_col_idx, formation_factor_col_idx):
        """
        Calculate formation resistivity factor.

        Parameters
        ----------
        formation_factor_col_idx : int
                Column index of the formation factor of the formation (Rw) data in the dataframe.
        rw_col_idx : int
                Column index of the true resistivity (Rw) data in the dataframe.
        df (pd.DataFrame):
                Dataframe containing resistivity and formation factor values.

        Returns
        ----------
        pd.DataFrame:
            Dataframe with formation resistivity values.
            """

        # Extract input columns from dataframe
        archie_rw = self.df.iloc[:, rw_col_idx]
        formation_factor = self.df.iloc[:, formation_factor_col_idx]

        # Calculate formation resistivity
        ro = archie_rw * formation_factor

        # Create a new column in the dataframe for the formation resistivity data
        self.df['ro'] = ro
        return self.df

    def swirr(self):
        """
        Calculate irreducible water saturation.

        Parameters
        ----------
        df (pd.DataFrame):
            Dataframe containing formation factor values.

        Returns
        ----------
        pd.DataFrame:
            Dataframe with irreducible water saturation values.
        """

        # Extract input columns from dataframe
        formation_factor = self.df[self.df['formation_factor']]

        # Calculate irreducible water saturation
        swirr = (formation_factor / 2000) ** (1 / 2)

        # Create a new column in the dataframe for the irreducible water saturation data
        self.df['swirr'] = swirr
        return self.df

    def permeability(self):
        """
        Calculate permeability using porosity and irreducible water saturation.

        Parameters
        ----------
        df (pd.DataFrame):
            Dataframe containing porosity and irreducible water saturation values.

        Returns
        ----------
        pd.DataFrame:
            Dataframe with permeability values.
        """

        # Extract input columns from dataframe
        porosity = self.df['PHI'].values
        swirr = self.df['swirr'].values

        # Calculate permeability
        permeability = 307 + (26552 * (porosity ** 2)) - (3450 * (porosity * swirr) ** 2)

        # Create a new column in the dataframe for the permeability data
        self.df['permeability'] = permeability
        return self.df

    def plot(self):
        fig, ax = plt.subplots(figsize=(15, 10))

        # Set up the plot axes
        ax1 = plt.subplot2grid((1, 7), (0, 0), rowspan=1, colspan=1)
        ax2 = plt.subplot2grid((1, 7), (0, 1), rowspan=1, colspan=1)
        ax3 = plt.subplot2grid((1, 7), (0, 2), rowspan=1, colspan=1)
        ax4 = plt.subplot2grid((1, 7), (0, 3), rowspan=1, colspan=1)
        ax5 = ax3.twiny()  # Twins the y-axis for the density track with the neutron track
        ax6 = plt.subplot2grid((1, 7), (0, 4), rowspan=1, colspan=1)
        ax7 = ax6.twiny()
        ax8 = plt.subplot2grid((1, 7), (0, 5), rowspan=1, colspan=1)
        ax9 = plt.subplot2grid((1, 7), (0, 6), rowspan=1, colspan=1)

        # As our curve scales will be detached from the top of the track,
        # this code adds the top border back in without dealing with splines
        ax10 = ax1.twiny()
        ax10.xaxis.set_visible(False)
        ax11 = ax2.twiny()
        ax11.xaxis.set_visible(False)
        ax12 = ax3.twiny()
        ax12.xaxis.set_visible(False)

        # Gamma Ray track
        ax1.plot("GR", "DEPTH", data=self.df, color="green")
        ax1.set_xlabel("Gamma")
        ax1.xaxis.label.set_color("green")
        ax1.set_xlim(0, 200)
        ax1.set_ylabel("Depth (m)")
        ax1.tick_params(axis='x', colors="green")
        ax1.spines["top"].set_edgecolor("green")
        ax1.title.set_color('green')
        ax1.set_xticks([0, 50, 100, 150, 200])

        # Resistivity track
        ax2.plot("RT", "DEPTH", data=self.df, color="red")
        ax2.set_xlabel("Resistivity")
        ax2.set_xlim(0.2, 2000)
        ax2.xaxis.label.set_color("red")
        ax2.tick_params(axis='x', colors="red")
        ax2.spines["top"].set_edgecolor("red")
        ax2.set_xticks([0.1, 1, 10, 100, 1000])
        ax2.semilogx()

        # Density track
        ax3.plot("RHOB", "DEPTH", data=self.df, color="red")
        ax3.set_xlabel("Density")
        ax3.set_xlim(1.95, 2.95)
        ax3.xaxis.label.set_color("red")
        ax3.tick_params(axis='x', colors="red")
        ax3.spines["top"].set_edgecolor("red")
        ax3.set_xticks([1.95, 2.45, 2.95])

        # Sonic track
        ax4.plot("DT", "DEPTH", data=self.df, color="purple")
        ax4.set_xlabel("Sonic")
        ax4.set_xlim(140, 40)
        ax4.xaxis.label.set_color("purple")
        ax4.tick_params(axis='x', colors="purple")
        ax4.spines["top"].set_edgecolor("purple")

        # Neutron track placed ontop of density track
        ax5.plot("NPHI", "DEPTH", data=self.df, color="blue")
        ax5.set_xlabel('Neutron')
        ax5.xaxis.label.set_color("blue")
        ax5.set_xlim(0.45, -0.15)
        ax5.set_ylim(4150, 3500)
        ax5.tick_params(axis='x', colors="blue")
        ax5.spines["top"].set_position(("axes", 1.08))
        ax5.spines["top"].set_visible(True)
        ax5.spines["top"].set_edgecolor("blue")
        ax5.set_xticks([0.45, 0.15, -0.15])

        # Porosity track
        ax6.plot("PHI", "DEPTH", data=self.df, color="black")
        ax6.set_xlabel("Total PHI")
        ax6.set_xlim(0.5, 0)
        ax6.xaxis.label.set_color("black")
        ax6.tick_params(axis='x', colors="black")
        ax6.spines["top"].set_edgecolor("black")
        ax6.set_xticks([0, 0.25, 0.5])

        # Porosity track
        ax7.plot("PHIECALC", "DEPTH", data=self.df, color="blue")
        ax7.set_xlabel("Effective PHI")
        ax7.set_xlim(0.5, 0)
        ax7.xaxis.label.set_color("blue")
        ax7.tick_params(axis='x', colors="blue")
        ax7.spines["top"].set_position(("axes", 1.08))
        ax7.spines["top"].set_visible(True)
        ax7.spines["top"].set_edgecolor("blue")
        ax7.set_xticks([0, 0.25, 0.5])

        # Sw track
        ax8.plot("SW_LIM", "DEPTH", data=self.df, color="black")
        ax8.set_xlabel("SW - Archie")
        ax8.set_xlim(0, 1)
        ax8.xaxis.label.set_color("black")
        ax8.tick_params(axis='x', colors="black")
        ax8.spines["top"].set_edgecolor("black")
        ax8.set_xticks([0, 0.5, 1])
        '''
        # Sw track
        ax9.plot("SW_SIM", "DEPTH", data=self.df, color="blue")
        ax9.set_xlabel("SW - Simandoux")
        ax9.set_xlim(0, 1)
        ax9.xaxis.label.set_color("blue")
        ax9.tick_params(axis='x', colors="blue")
        ax9.spines["top"].set_edgecolor("blue")
        ax9.set_xticks([0, 0.5, 1])
        '''
        # Common functions for setting up the plot can be extracted into
        # a for loop. This saves repeating code.
        for ax in [ax1, ax2, ax3, ax4, ax6, ax8, ax9]:
            ax.set_ylim(4150, 3500)
            ax.grid(which='major', color='lightgrey', linestyle='-')
            ax.xaxis.set_ticks_position("top")
            ax.xaxis.set_label_position("top")
            ax.spines["top"].set_position(("axes", 1.02))

        return plt.tight_layout()
