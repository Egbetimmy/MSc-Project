import matplotlib.pyplot as plt


# %matplotlib inline
# TODO: add a proper documentation
# TODO: review the code to optimize it

class Anisotropy:
    def __init__(self, df):
        self.df = df

    def thomsen_delta(self, x, y):
        seismic_data = self.df[self.df.columns[x]]
        well_data = self.df[self.df.columns[y]]
        thomsen_delta = []
        for well, seismic in zip(well_data, seismic_data):
            thomsen_anisotropy = ((well / seismic) - 1)

            thomsen_delta.append(thomsen_anisotropy)
        self.df['Thomsen_delta'] = thomsen_delta
        return self.df

    def correction(self, x):
        seismic_data = self.df[self.df.columns[x]]
        thomsen_delta = self.df['Thomsen_delta']
        correction = []
        for delta, seismic in zip(thomsen_delta, seismic_data):
            anisotropy_correction = ((1 - delta) * seismic)

            correction.append(anisotropy_correction)
        self.df['Anisotropy_correction'] = correction
        return self.df

    def plot_data(self, n_spaces=50):
        data_frame = self.df

        fig, axes = plt.subplots(figsize=(10, 10))
        curve_names = ['Thomsen_delta', 'Anisotropy_correction', "Vint_cks(m/s)", "Vint_seismic(m/s)"]

        # TODO: try to make it just two plots. Try it out and see how it works.

        ax1 = plt.subplot2grid((1, 3), (0, 0), rowspan=1, colspan=1)
        ax2 = plt.subplot2grid((1, 3), (0, 1), rowspan=1, colspan=1)
        ax3 = plt.subplot2grid((1, 3), (0, 2), rowspan=1, colspan=1)
        ax4 = ax3.twiny()

        ax1.plot('Thomsen_delta', 'Depth', data=data_frame, color="green", lw=0.5)
        ax1.set_xlim(data_frame.Thomsen_delta.min(), data_frame.Thomsen_delta.max())

        ax2.plot('Anisotropy_correction', 'Depth', data=data_frame, color="red", lw=0.5)
        ax2.set_xlim(data_frame.Anisotropy_correction.min(), data_frame.Anisotropy_correction.max())

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
