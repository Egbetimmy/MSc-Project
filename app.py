import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")


# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

        st.write(
            '''
            File must be in CSV format,
            columns should be renamed as follows:
            [Thomsen_delta, Anisotropy_correction, Vint_cks(m/s), Vint_seismic(m/s)].
            They should also be arranged in that particular order.
            '''
        )

        st.write(
            '''
            This is basically a simple Streamlit app to aid visualization.
            All computations have been automated in my github page:
            https://github.com/Egbetimmy/MSc-Project
            '''
        )

        st.write(
            '''
            This is basically a simple Streamlit app to aid visualization.
            All computations have been automated in my github page:
            https://github.com/Egbetimmy/MSc-Project
            '''
        )

        st.write(
            '''
            This is basically a simple Streamlit app to aid visualization.
            All computations have been automated in my github page:
            https://github.com/Egbetimmy/MSc-Project
            '''
        )


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


# Add a title and intro text
st.title('Anisotropy Data Visualization')
st.text('This is a web app to allow Visualization of Anisotropy Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing Anisotropy data')
# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:',
                           ['Home', 'Data Summary', 'Data Header', 'Data Visualization'])

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
elif options == 'Data Visualization':
    displayplot()
