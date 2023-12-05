import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Load the Iris dataset
# Detail about the dataset


# sidebar
st.sidebar.subheader("Siva Subramaniam R PA2312044010107")

rad = st.sidebar.radio(
    "Select the topic", ["About this Dataset", "Data Visualizations", "Summary"])

if rad == "Data Visualizations":
    # Content
    st.sidebar.subheader("Content:")
    st.sidebar.subheader("Univariate Visualizations")
    select = st.sidebar.selectbox(
        "Select the Visualizations", ["Histogram of Sepal Length", "Countplot of Species"])

    st.sidebar.subheader("Bivariate Visualizations")
    select1 = st.sidebar.selectbox(
        "Select the Visualizations", ["Scatterplot of Sepal Length vs Sepal Width", "Boxplot of Petal Length by Species"])

    st.sidebar.subheader("Multivariate Visualizations")
    select2 = st.sidebar.selectbox(
        "Select the Visualizations", ["Pairplot of All Features by Species", "Heatmap of Feature Correlation"])

# title & infomation
st.header("20PAIC51J - PYTHON FOR DATA SCIENCE \nCT3 - MINOR PROJECT")
st.markdown("<h1 style='color: rgb(0, 230, 230);'>IRIS DATASET VISUALIZATION</h1>",
            unsafe_allow_html=True)

if rad == "About this Dataset":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0)
        progress.progress(i+1)
    progress.empty()
    st.info("This dataset is related to plant species")
    st.info("The Iris dataset was used in R.A. Fisher's classic 1936 paper, \nThe Use of Multiple Measurements in Taxonomic Problems")
    st.info("It includes three iris species with 50 samples each as well as some \nproperties about each flower. One flower species is linearly separable from \nthe other two, but the other two are not linearly separable from each other.")
    st.subheader("Description the Columns")
    st.text("SepalLengthCm\nSepalWidthCm\nPetalLengthCm\nPetalWidthCm\nSpecies")

if rad == "Data Visualizations":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0)
        progress.progress(i+1)
    progress.empty()
    # load dataset
    st.header("The Iris Dataset")
    data = pd.read_csv('Iris.csv')
    dt = data.drop('Id', axis=1)
    st.dataframe(data, width=900)

    # Univariate Visualizations
    st.header("Univariate Visualizations")

    def histogram():
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0)
            progress.progress(i+1)
        progress.empty()
        # Histogram of Sepal Length
        st.subheader("1. Histogram of Sepal Length")
        fig, ax = plt.subplots()
        sns.histplot(data['SepalLengthCm'], kde=True)
        st.pyplot(fig)

    def countplot():
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0)
            progress.progress(i+1)
        progress.empty()
        # Countplot of Species
        st.subheader("2. Countplot of Species")
        fig, ax = plt.subplots()
        sns.countplot(x='Species', data=data, ax=ax)
        st.pyplot(fig)

    if select == "Histogram of Sepal Length":
        histogram()
    elif select == "Countplot of Species":
        countplot()
    else:
        st.warning("Please select a valid option from the sidebar.")

    # Bivariate Visualizations
    st.header("Bivariate Visualizations")

    def scatterplot():
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0)
            progress.progress(i+1)
        progress.empty()
        # Scatterplot of Sepal Length vs Sepal Width
        st.subheader("1. Scatterplot of Sepal Length vs Sepal Width")
        fig, ax = plt.subplots()
        scatter_plot = sns.scatterplot(
            x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=data, ax=ax)
        st.pyplot(fig)

    def Boxplot():
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0)
            progress.progress(i+1)
        progress.empty()
        # Boxplot of Petal Length by Species
        st.subheader("2. Boxplot of Petal Length by Species")
        fig, ax = plt.subplots()
        boxp_lot = sns.boxplot(
            x='Species', y='PetalLengthCm', data=data, ax=ax)
        st.pyplot(fig)

    if select1 == "Scatterplot of Sepal Length vs Sepal Width":
        scatterplot()
    elif select1 == "Boxplot of Petal Length by Species":
        Boxplot()
    else:
        st.warning("Please select a valid option from the sidebar.")

    # Multivariate Visualizations
    st.header("Multivariate Visualizations")

    def Pairplot():
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0)
            progress.progress(i+1)
        progress.empty()
        # Pairplot of All Features by Species
        st.subheader("1. Pairplot of All Features by Species")
        pair_plot = sns.pairplot(dt, hue='Species', height=3)
        st.pyplot(pair_plot)

    def Heatmap():
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0)
            progress.progress(i+1)
        progress.empty()
        # Heatmap of Feature Correlation
        # Exclude non-numeric columns for the heatmap
        numeric_data = data.select_dtypes(include=['float64', 'int64'])
        st.subheader("2. Heatmap of Feature Correlation")
        fig, ax = plt.subplots(figsize=(8, 6))
        heat_map = sns.heatmap(numeric_data.corr(),
                               annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    if select2 == "Pairplot of All Features by Species":
        Pairplot()
    elif select2 == "Heatmap of Feature Correlation":
        Heatmap()
    else:
        st.warning("Please select a valid option from the sidebar.")


if rad == "Summary":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0)
        progress.progress(i+1)
    progress.empty()
    st.header("Univariate Visualizations")
    st.subheader("Histogram of Sepal Length:")
    st.info("Insight: The distribution of sepal lengths in the dataset.")
    st.info("Observation: Identify patterns, peaks, or clusters in sepal lengths.")
    st.subheader("Countplot of Species:")
    st.info("Insight: Distribution of Iris species in the dataset.")
    st.info("Observation: Understand the balance or imbalance between different species")
    st.header("Bivariate Visualizations")
    st.subheader("Scatterplot of Sepal Length vs Sepal Width:")
    st.info("Insight: Relationship between sepal length and sepal width.")
    st.info("Observation: Check for patterns or clusters and assess how well the two features\nseparate different species.")
    st.subheader("Boxplot of Petal Length by Species:")
    st.info(
        "Insight: Comparison of petal length distributions among different Iris species.")
    st.info(
        "Observation: Identify species-specific patterns and variations in petal length.")
    st.header("Multivariate Visualizations")
    st.subheader("Pairplot of All Features by Species:")
    st.info("Insight: Comprehensive view of pairwise feature relationships.")
    st.info("Observation: Assess how different features correlate and distinguish between species.")
    st.subheader("Heatmap of Feature Correlation:")
    st.info("Insight: Visual representation of feature correlations.")
    st.info("Observation: Identify strong positive or negative correlations between features,\nhelping to understand which features are related.")
