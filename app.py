# Standard Data Science helpers
import numpy as np
import pandas as pd
import scipy

# Instansiate the Plotly charting library.
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
# We use plotly.offline as this allows us to create interactive
# visualisations without the use of an internet connection,
# making our notebook more distributable to others.
from plotly.offline import iplot, init_notebook_mode
from ipywidgets import interact, interact_manual, widgets

init_notebook_mode(connected=True)

# The Cufflinks library allows us to directly bind
# Pandas dataframes to Plotly charts.
import cufflinks as cf

# Once again we use the Cufflinks library in offline mode.
cf.go_offline(connected=True)
cf.set_config_file(colorscale='plotly', world_readable=True)

# Extra options. We use these to make our interactive
# visualisations more aesthetically appealing.
from IPython.core.display import HTML

pd.options.display.max_rows = 30
pd.options.display.max_columns = 25

# Show all code cells outputs
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = 'all'
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from class3 import Anisotropy

st.set_page_config(layout="wide")


# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')


# TODO
def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())


# TODO
def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())


# TODO
def displayplot():
    st.header('Plot of Data')
    """
    test = Anisotropy(df)

    z = test.plot_data()
    """
    fig, axes = plt.subplots(figsize=(10, 10))
    curve_names = ['Thomsen_delta', 'Anisotropy_correction', "Vint_cks(m/s)", "Vint_seismic(m/s)"]

    # TODO: try to make it just two plots. Try it out and see how it works.

    ax1 = plt.subplot2grid((1, 3), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((1, 3), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((1, 3), (0, 2), rowspan=1, colspan=1)
    ax4 = ax3.twiny()

    ax1.plot('Thomsen_delta', 'Depth', data=df, color="green", lw=0.5)
    ax1.set_xlim(df.Thomsen_delta.min(), df.Thomsen_delta.max())

    ax2.plot('Anisotropy_correction', 'Depth', data=df, color="red", lw=0.5)
    ax2.set_xlim(df.Anisotropy_correction.min(), df.Anisotropy_correction.max())

    ax3.plot('Vint_cks(m/s)', 'Depth', data=df, color="blue", lw=0.5)
    ax3.set_xlim(df['Vint_cks(m/s)'].min(), df['Vint_cks(m/s)'].max())

    ax4.plot('Vint_seismic(m/s)', 'Depth', data=df, color="red", lw=0.5)
    ax4.set_xlim(df['Vint_cks(m/s)'].min(), df['Vint_cks(m/s)'].max())

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

    st.pyplot(fig)


# TODO
def interactive_plot():
    @interact
    def scatter_plot(x=list(df.select_dtypes('number').columns),
                     y=list(df.select_dtypes('number').columns)[1:]):
        if x == y:
            print(f"Please select seperate variables for X and Y")
        else:
            plot = df.iplot(kind='scatter', x=x, y=y, mode='markers',
                            xTitle=x.title(), yTitle=y.title(), title=f'{y.title()} vs {x.title()}')
            # if you are using Google Colab, comment out the above line of code and uncomment the lines below
            # fig = px.scatter(df, x=x, y=y, title=f'{y.title()} vs {x.title()}')
            # fig.show(renderer="colab")

        st.plotly_chart(plot, use_container_width=True)


# Add a title and intro text
st.title('Anisotropy Data Visualization')
st.text('This is a web app to allow Visualization of Anisotropy Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing Anisotropy data')
# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:',
                           ['Home', 'Data Summary', 'Data Header', 'Data Plot', 'Interactive Plots'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Data Plot':
    displayplot()
elif options == 'Interactive Plots':
    interactive_plot()
