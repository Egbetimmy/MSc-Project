import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from class1 import Volumetrics
from class2 import Petrophysics
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
    area = input()
    fvf = input()
    test = Volumetrics(df, area, fvf)
    x = test.bulk_volume()
    st.header('Statistics of Dataframe')
    st.write(df.describe())
    st.write(x)


# TODO
def data_header():
    test = Anisotropy(df)
    x = test.thomsen_delta()
    y = test.correction()
    st.header('Header of Dataframe')
    st.write(df.head())
    st.write(x)
    st.write(y)
    z = test.plot_data()


# TODO
def displayplot():
    st.header('Plot of Data')

    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)


# TODO
def interactive_plot():
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)


# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:',
                           ['Home', 'Data Summary', 'Data Header', 'Data Plot', 'Fancy Plots'])

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
