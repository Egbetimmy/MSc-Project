import matplotlib.pyplot as plt

# %matplotlib inline


class Anisotropy:
    def __init__(self, df):
        self.df = df
        self.seismic_data = self.df[self.df.columns[1]]
        self.well_data = self.df[self.df.columns[2]]

    def thomsen_delta(self):
        # TODO: add a proper documetation
        # TODO: review the code to optimize it
        thomsen_delta = []
        for well, seismic in zip(self.well_data, self.seismic_data):
            thomsen_anisotropy = ((well / seismic) - 1)

            thomsen_delta.append(thomsen_anisotropy)
        self.df['Thomsen_delta'] = thomsen_delta
        return self.df

    def correction(self):
        # TODO: add a proper documetation
        # TODO: review the code to optimize it
        self.seismic_data = self.df[self.df.columns[1]]
        self.well_data = self.df[self.df.columns[2]]
        thomsen_delta = self.df['Thomsen_delta']
        correction = []
        for delta, seismic in zip(thomsen_delta, self.seismic_data):
            anisotropy_correction = ((1 - delta) * seismic)

            correction.append(anisotropy_correction)
        self.df['Anistropy_correction'] = correction
        return self.df

    def plot_data(self, n_spaces=50):

        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        # mapping = {self.df.columns[0]: "Horizons",self.df.columns[1]: "Well_data",self.df.columns[2]: "Seismic_data",\
        # self.df.columns[3]: "Error", self.df.columns[4]: "Correction"}

        # self.df = self.df.rename(columns=mapping)

        # TODO: Nothing to do for this method. Try it out and see how it works.
        # TODO: Try to change the data columns in use to call the data from column name

        data_frame = self.df

        fig, axes = plt.subplots(figsize=(10, 10))
        curve_names = ['Thomsen_delta', 'Anistropy_correction', "Vint_cks(m/s)", "Vint_seismic(m/s)"]

        # TODO: try to make it just two plots. Try it out and see how it works.

        ax1 = plt.subplot2grid((1, 3), (0, 0), rowspan=1, colspan=1)
        ax2 = plt.subplot2grid((1, 3), (0, 1), rowspan=1, colspan=1)
        ax3 = plt.subplot2grid((1, 3), (0, 2), rowspan=1, colspan=1)
        ax4 = ax3.twiny()

        ax1.plot('Thomsen_delta', 'Depth', data=data_frame, color="green", lw=0.5)
        ax1.set_xlim(data_frame.Thomsen_delta.min(), data_frame.Thomsen_delta.max())

        ax2.plot('Anistropy_correction', 'Depth', data=data_frame, color="red", lw=0.5)
        ax2.set_xlim(data_frame.Anistropy_correction.min(), data_frame.Anistropy_correction.max())

        ax3.plot('Vint_cks(m/s)', 'Depth', data=data_frame, color="blue", lw=0.5)
        ax3.set_xlim(data_frame['Vint_cks(m/s)'].min(), data_frame['Vint_cks(m/s)'].max())

        ax4.plot('Vint_seismic(m/s)', 'Depth', data=data_frame, color="red", lw=0.5)
        ax4.set_xlim(data_frame['Vint_cks(m/s)'].min(), data_frame['Vint_cks(m/s)'].max())

        for i, ax in enumerate(fig.axes):
            ax.set_ylim(2154, 1350)

            ax.xaxis.set_ticks_position("top")
            ax.xaxis.set_label_position("top")
            ax.set_xlabel(curve_names[i])

            if i == 3:
                ax.spines["top"].set_position(("axes", 1.08))
            else:
                ax.grid()

        for ax in [ax2, ax3, ax4]:
            plt.setp(ax.get_yticklabels(), visible=False)

        return fig.subplots_adjust(wspace=0.05)
