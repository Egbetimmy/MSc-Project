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
            """
            Welcome to the Thomsen Delta and Anisotropy visualization app. 
            This app is designed to help you explore and visualize the relationships between Thomsen Delta 
            and Anisotropy data in your well logs. Thomsen Delta is a measure of the anisotropy of a rock formation 
            and is used to describe the relationship between the horizontal and vertical velocities of compressional 
            waves in the formation. Anisotropy, on the other hand, refers to the directional dependence of the 
            physical properties of a rock formation.
            """
        )

        st.write(
            """
            To use this app, you will need to upload a CSV file containing Thomsen Delta and Anisotropy data, 
            with columns named "Thomsen_delta" and "Anisotropy_correction" respectively. 
            The data should also be arranged in that particular order.
            """
        )

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
            Once you have uploaded your data, you can use the menu on the left to explore the data and generate 
            visualizations. You can view basic statistics of your dataset in the "Data Summary" tab, and view the first 
            few rows of your dataset in the "Data Header" tab. The "Data Visualization" tab allows you to create a plot 
            of Thomsen Delta and Anisotropy as a function of depth, allowing you to visualize the relationships between 
            these parameters in your well logs.
            '''
        )

        st.write(
            '''
            If you need more information about how to use this app, please refer to the documentation on our GitHub page 
            at https://github.com/Egbetimmy/MSc-Project. We hope that this app will be a useful tool in your exploration of 
            Thomsen Delta and Anisotropy data, and we welcome any feedback or suggestions you may have.
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

# Add a slider widget to filter depth
if options == 'Data Visualization':
    depth_min = st.sidebar.slider('Minimum depth', df['Depth'].min(), df['Depth'].max(), df['Depth'].min())
    depth_max = st.sidebar.slider('Maximum depth', df['Depth'].min(), df['Depth'].max(), df['Depth'].max())
    displayplot(depth_min, depth_max)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Data Visualization':
    displayplot()
