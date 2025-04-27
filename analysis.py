import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

# Define the path to the CSV file
csv_file = 'student_data.csv'

# Check if the file exists
if not os.path.isfile(csv_file):
    # Create a new dataframe with the required columns
    df = pd.DataFrame(columns=[
        "Grade/Class", "Subject", "Attendance", "Test Scores", "Homework Scores", 
        "Project Scores", "Participation", "Final Grade", "Parental Education", 
        "Socioeconomic Status", "Extracurricular Activities", "Special Needs", "Behavior/Conduct"
    ])

    # Write the dataframe to a new CSV file
    df.to_csv(csv_file, index=False)
# Function to write data to CSV
def write_data(data):
    df = pd.DataFrame([data], columns=list(data.keys()))
    df.to_csv(csv_file, mode='a', index=False, header=not pd.io.parsers.read_csv(csv_file).shape[1])
    st.success("Data saved successfully!")

# Function to plot the data
def plot_data():
    df = pd.read_csv(csv_file)
    if df.shape[0] > 1:
        st.write("## Comparing Current Student Data with Previous Student")
        
        # Line plot for test, homework and project scores
        st.write("### Line Plot for Test, Homework, and Project Scores")
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df[['Test Scores', 'Homework Scores', 'Project Scores']][-2:])
        plt.xticks(ticks=range(2), labels=['Previous Student', 'Current Student'])
        st.pyplot(plt.gcf())

        # Pie chart for attendance and participation
        st.write("### Pie Chart for Attendance and Participation")
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        ax[0].pie(df['Attendance'][-2:], labels=['Previous Student', 'Current Student'], autopct='%1.1f%%')
        ax[0].set_title('Attendance')
        ax[1].pie(df['Participation'][-2:], labels=['Previous Student', 'Current Student'], autopct='%1.1f%%')
        ax[1].set_title('Participation')
        st.pyplot(fig)

        # Bar plot for final grade
        st.write("### Bar Plot for Final Grade")
        plt.figure(figsize=(10, 5))
        sns.barplot(x=['Previous Student', 'Current Student'], y=df['Final Grade'][-2:])
        st.pyplot(plt.gcf())

        # Histogram for socioeconomic status
        st.write("### Histogram for Socioeconomic Status")
        plt.figure(figsize=(10, 5))
        sns.histplot(df['Socioeconomic Status'], kde=True)
        st.pyplot(plt.gcf())

        # Scatterplot for test scores versus final grade
        st.write("### Scatterplot for Test Scores versus Final Grade")
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x=df['Test Scores'], y=df['Final Grade'])
        st.pyplot(plt.gcf())

        # Boxplot for attendance
        st.write("### Boxplot for Attendance")
        plt.figure(figsize=(10, 5))
        sns.boxplot(y=df['Attendance'])
        st.pyplot(plt.gcf())

        # Bar plot for extracurricular activities
        st.write("### Bar Plot for Extracurricular Activities")
        plt.figure(figsize=(10, 5))
        sns.barplot(x=['Previous Student', 'Current Student'], y=df['Extracurricular Activities'][-2:])
        st.pyplot(plt.gcf())
    else:
        st.warning("Not enough data for comparison. Please enter more students' data.")

# Collect student data
st.write("# Enter Student Data")

data = {
    "Grade/Class": st.number_input('Grade/Class', value=0),
    "Subject": st.number_input('Subject', value=0),
    "Attendance": st.number_input('Attendance', value=0),
    "Test Scores": st.number_input('Test Scores', value=0),
    "Homework Scores": st.number_input('Homework Scores', value=0),
    "Project Scores": st.number_input('Project Scores', value=0),
    "Participation": st.number_input('Participation', value=0),
    "Final Grade": st.number_input('Final Grade', value=0),
    "Parental Education": st.number_input('Parental Education', value=0),
    "Socioeconomic Status": st.number_input('Socioeconomic Status', value=0),
    "Extracurricular Activities": st.number_input('Extracurricular Activities', value=0),
    "Special Needs": st.number_input('Special Needs', value=0),
    "Behavior/Conduct": st.number_input('Behavior/Conduct', value=0)
}

if st.button('Submit'):
    write_data(data)

plot_data()
