# -*- coding: utf-8 -*-

import streamlit as st  #import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv('food_coded.csv')

# Title of the app
# Main content
st.title("Food Choices and Preferences of College Students")



st.set_option('deprecation.showPyplotGlobalUse', False)
    
# Sidebar
st.sidebar.title("Food Choices Analysis")
analysis_option = st.sidebar.selectbox("Select an analysis:", ["Summary", "Gender Distribution", "Exercise Frequency", "Favorite Cuisine"])

# Debugging
st.write("Selected Option:", analysis_option)

# Analyses
if analysis_option == "Summary":
    st.write(df.describe())
elif analysis_option == "Gender Distribution":
    gender_count = df["Gender"].value_counts()
    st.bar_chart(gender_count)
elif analysis_option == "Calories Intake Distribution":
    sns.histplot(df["calories_day"], bins=20, kde=True)
    st.pyplot()
elif analysis_option == "Exercise Frequency":
    exercise_freq_count = df["exercise"].value_counts()
    st.bar_chart(exercise_freq_count)
elif analysis_option == "Favorite Cuisine":
    cuisine_count = df["fav_cuisine"].value_counts()
    st.bar_chart(cuisine_count)
elif analysis_option == "Weight Distribution":
    sns.histplot(df["weight"], bins=20, kde=True)
    st.pyplot()

# Visualization section
#Each visualization below offers unique insights into different aspects of the data
st.subheader("Data Visualization")

#Gender Distribution
#Shows the distribution of genders in the dataset
plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=df)
plt.xlabel('Gender\n1 – Female\n2 – Male')
plt.ylabel('Count')
st.pyplot()


# Employment Status vs. Eating Out Frequency
# Reorder the categories for better visualization
df['eating_out'] = df['eating_out'].map({1: "Never", 2: "1-2 times", 3: "2-3 times", 4: "3-5 times", 5: "Every day"})

# Reorder the categories for employment status
df['employment'] = df['employment'].map({1: "Yes, full time", 2: "Yes, part time", 3: "No", 4: "Other"})

# Plot the data
plt.figure(figsize=(10, 6))
sns.countplot(x="employment", hue="eating_out", data=df, order=["Yes, full time", "Yes, part time", "No", "Other"])
plt.xlabel("Employment Status")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.title("Employment Status vs. Eating Out Frequency")
plt.legend(title="Eating Out Frequency")

# Add descriptions with increased vertical spacing
plt.text(0, -0.4, "Eating Out Frequency:\n1 - Never\n2 - 1-2 times\n3 - 2-3 times\n4 - 3-5 times\n5 - Every day",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
plt.text(0, -0.5, "Employment Status:\n1 - Yes, full time\n2 - Yes, part time\n3 - No\n4 - Other",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
st.pyplot(plt.gcf())  # Display the plot in Streamlit

#Comfort Food vs. Weight
def display_comfort_food_vs_weight():
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.swarmplot(x="comfort_food_reasons_coded", y="weight", data=df, ax=ax)
    ax.set_xlabel("Comfort Food Reasons (Coded)\n0) stress\n1) boredom\n2) depression/sadness\n3) hunger\n4) laziness\n5) cold weather\n6) happiness\n7) watching tv\n8) none")
    ax.set_ylabel("Weight")
    st.pyplot(fig)

# Call the function to display the plot
display_comfort_food_vs_weight()

#Run the Streamlit app locally
#streamlit run app.py
