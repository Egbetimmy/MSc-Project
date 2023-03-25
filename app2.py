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
            Welcome to our well log visualization app! 
            This app is designed to help you visualize and analyze well log data for oil and gas exploration. 
            Here's a step-by-step guide to help you get started:
            """
        )

        st.write(
            """
            Uploading Data: To use this app, you'll need to upload your well log data. We accept CSV files with columns 
            for depth, gamma ray, resistivity, and porosity. The CSV file should have a header row specifying the names 
            of the columns. The depth column should be in meters or feet, and the data columns should be in API units. 
            You can upload your data by clicking the "Upload Data" button on the sidebar and selecting your CSV file. 
            Once you've uploaded your data, it will be displayed in a table below the plot.
            """
        )

        st.write(
            """
            Visualizing Data: Once you've uploaded your data, you can visualize it using the interactive plot on the 
            main page. The plot displays depth on the y-axis and the selected data column on the x-axis. You can select 
            which data columns to display by checking the appropriate boxes in the sidebar. You can also adjust the 
            scale of the plot using the slider at the bottom. To zoom in or out of the plot, click and drag on the 
            x-axis or use the scroll wheel on your mouse. To pan the plot, click and drag on the plot.
            """
        )

        st.write(
            """
            Analyzing Data: The app also provides a few tools to help you analyze your well log data. You can view 
            statistical summaries for each data column by clicking the "Show Stats" button in the sidebar. The app will 
            display the mean, median, standard deviation, minimum, and maximum values for the selected column. You can 
            also filter your data by depth range or by specific values using the filter options in the sidebar. 
            To filter by depth range, enter the minimum and maximum depth values in the "Depth Range" fields and click 
            the "Filter" button. To filter by specific values, enter the values in the appropriate fields and click the 
            "Filter" button. The app will display only the rows of the table that match the filter criteria.
            """
        )

        st.write(
            """
            Documentation: If you need more information about the app or the data format, you can refer to our 
            documentation. Click the "Documentation" button in the sidebar to access our user guide and data format 
            specifications. The user guide provides detailed instructions on how to use the app, including screenshots 
            and examples. The data format specifications provide information on the required format for the CSV file, 
            including the column names and units.
            """
        )

        st.write(
            """
            We hope you find our app useful for your well log analysis needs. If you have any questions or feedback, 
            please don't hesitate to contact us using the contact information provided in the "About" section of the 
            sidebar.
            """
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
