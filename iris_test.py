import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

# Load the Iris dataset
# Detail about the dataset

# Function to show progress


st.header("DATA VISUALIZATION")


def show_progress():
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0)
        progress.progress(i + 1)
    progress.empty()

# Function to load data


def load_data():
    data = pd.read_csv('Iris.csv')
    return data.drop('Id', axis=1)

# Function for univariate visualizations


def univariate_visualizations(data, rad1):
    show_progress()
    st.markdown(
        "<h2 style='color: rgb(255, 204, 255);'>UNIVARIATE VISUALIZATION</h2>", unsafe_allow_html=True)

    data = load_data()
    if rad1 == "Histogram":
        select = st.selectbox(
            "Select the Visualizations", ["Histogram of Sepal Length", "Histogram of Sepal Width", "Histogram of Petal Length", "Histogram of Petal Width"])

        def Sepal_Length():
            st.subheader("1. Histogram of Sepal Length")
            fig, ax = plt.subplots()
            sns.histplot(data['SepalLengthCm'], kde=True)
            st.pyplot(fig)

        def Sepal_width():
            st.subheader("2. Histogram of Sepal width")
            fig, ax = plt.subplots()
            sns.histplot(data['SepalWidthCm'], kde=True)
            st.pyplot(fig)

        def Petal_Length():
            st.subheader("3. Histogram of Petal Length")
            fig, ax = plt.subplots()
            sns.histplot(data['PetalLengthCm'], kde=True)
            st.pyplot(fig)

        def Petal_Width():
            st.subheader("4. Histogram of Petal Width")
            fig, ax = plt.subplots()
            sns.histplot(data['PetalWidthCm'], kde=True)
            st.pyplot(fig)

        if select == "Histogram of Sepal Length":
            Sepal_Length()
        elif select == "Histogram of Sepal Width":
            Sepal_width()
        elif select == "Histogram of Petal Length":
            Petal_Length()
        elif select == "Histogram of Petal Width":
            Petal_Width()
        else:
            st.warning("Please select a valid option from the sidebar.")

    elif rad1 == "Countplot":
        select = st.selectbox(
            "Select the Visualizations", ["Countplot of Sepal Length", "Countplot of Sepal Width", "Countplot of Petal Length", "Countplot of Petal Width"])

        def CSepal_Length():
            # Add a slider to select the range of SepalLengthCm
            sepal_length_range = st.slider("Select Sepal Length Range",
                                           min_value=data['SepalLengthCm'].min(
                                           ),
                                           max_value=data['SepalLengthCm'].max(
                                           ),
                                           value=(data['SepalLengthCm'].min(), data['SepalLengthCm'].max()))

            # Filter the data based on the selected Sepal Length range
            filtered_data = data[data['SepalLengthCm'].between(
                *sepal_length_range)]
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.countplot(x='SepalLengthCm', data=filtered_data, ax=ax)
            # Rotate x-axis labels for better visibility
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
            st.subheader("1. Countplot of Sepal Length")

        def CSepal_Width():
            sepal_width_range = st.slider("Select Sepal Width Range",
                                          min_value=data['SepalWidthCm'].min(
                                          ),
                                          max_value=data['SepalWidthCm'].max(
                                          ),
                                          value=(data['SepalWidthCm'].min(), data['SepalWidthCm'].max()))

            filtered_data = data[data['SepalWidthCm'].between(
                *sepal_width_range)]

            st.subheader("2. Countplot of Sepal Width")
            fig, ax = plt.subplots()
            sns.countplot(x='SepalWidthCm', data=filtered_data, ax=ax)
            st.pyplot(fig)

        def CPetal_Length():
            petal_length_range = st.slider("Select Petal Length Range",
                                           min_value=data['PetalLengthCm'].min(
                                           ),
                                           max_value=data['PetalLengthCm'].max(
                                           ),
                                           value=(data['PetalLengthCm'].min(), data['PetalLengthCm'].max()))

            filtered_data = data[data['PetalLengthCm'].between(
                *petal_length_range)]

            st.subheader("3. Countplot of Petal Length")
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.countplot(x='PetalLengthCm', data=filtered_data, ax=ax)
            st.pyplot(fig)

        def CPetal_Width():
            petal_width_range = st.slider("Select Petal Length Range",
                                          min_value=data['PetalWidthCm'].min(
                                          ),
                                          max_value=data['PetalWidthCm'].max(
                                          ),
                                          value=(data['PetalWidthCm'].min(), data['PetalWidthCm'].max()))

            filtered_data = data[data['PetalWidthCm'].between(
                *petal_width_range)]

            st.subheader("4. Countplot of Petal Width")
            fig, ax = plt.subplots()
            sns.countplot(x='PetalWidthCm', data=filtered_data, ax=ax)
            st.pyplot(fig)

        if select == "Countplot of Sepal Length":
            CSepal_Length()
        elif select == "Countplot of Sepal Width":
            CSepal_Width()
        elif select == "Countplot of Petal Length":
            CPetal_Length()
        elif select == "Countplot of Petal Width":
            CPetal_Width()
        else:
            st.warning("Please select a valid option from the sidebar.")

# Function for bivariate visualizations


def bivariate_visualizations(data, rad2):
    show_progress()
    st.markdown(
        "<h2 style='color: rgb(0, 204, 255);'>BIVARIATE VISUALIZATION</h2>", unsafe_allow_html=True)

    if rad2 == "Scatterplot":
        data = load_data()
        select = st.selectbox(
            "Select the Visualizations", ["Scatterplot of Sepal Length vs Sepal Width", "Scatterplot of Petal Length vs Petal Width"])

        def Slength_Swidth():
            st.subheader("1. Scatterplot of Sepal Length vs Sepal Width")
            fig, ax = plt.subplots()
            sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm',
                            hue='Species', data=data, ax=ax)
            st.pyplot(fig)

        def Plength_Pwidth():
            st.subheader("2. Scatterplot of Sepal Length vs Sepal Width")
            fig, ax = plt.subplots()
            sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm',
                            hue='Species', data=data, ax=ax)
            st.pyplot(fig)

        if select == "Scatterplot of Sepal Length vs Sepal Width":
            Slength_Swidth()
        elif select == "Scatterplot of Petal Length vs Petal Width":
            Plength_Pwidth()
        else:
            st.warning("Please select a valid option from the sidebar.")

    elif rad2 == "Boxplot":
        data = load_data()
        select = st.selectbox(
            "Select the Visualizations", ["Boxplot of Sepal Length by Species", "Boxplot of Sepal width by Species", "Boxplot of Petal Length by Species", "Boxplot of Petal width by Species"])

        def BSepal_Length():
            st.subheader("1. Boxplot of Sepal Length by Species")
            fig, ax = plt.subplots()
            sns.boxplot(x='Species', y='SepalLengthCm', data=data, ax=ax)
            st.pyplot(fig)

        def BSepal_width():
            st.subheader("2. Boxplot of Sepal width by Species")
            fig, ax = plt.subplots()
            sns.boxplot(x='Species', y='SepalWidthCm', data=data, ax=ax)
            st.pyplot(fig)

        def BPetal_Length():
            st.subheader("3. Boxplot of Petal Length by Species")
            fig, ax = plt.subplots()
            sns.boxplot(x='Species', y='PetalLengthCm', data=data, ax=ax)
            st.pyplot(fig)

        def BPetal_width():
            st.subheader("4. Boxplot of Petal width by Species")
            fig, ax = plt.subplots()
            sns.boxplot(x='Species', y='PetalWidthCm', data=data, ax=ax)
            st.pyplot(fig)

        if select == "Boxplot of Sepal Length by Species":
            BSepal_Length()
        elif select == "Boxplot of Sepal width by Species":
            BSepal_width()
        elif select == "Boxplot of Petal Length by Species":
            BPetal_Length()
        elif select == "Boxplot of Petal width by Species":
            BPetal_width()
        else:
            st.warning("Please select a valid option from the sidebar.")

# Function for multivariate visualizations


def multivariate_visualizations(data, rad3):
    show_progress()
    st.header("Multivariate Visualizations")

    if rad3 == "Pairplot of All Features by Species":
        st.subheader("1. Pairplot of All Features by Species")
        pair_plot = sns.pairplot(data=load_data(), hue='Species', height=3)
        st.pyplot(pair_plot)

    elif rad3 == "Heatmap of Feature Correlation":
        data = load_data()
        st.subheader("2. Heatmap of Feature Correlation")
        numeric_data = data.select_dtypes(include=['float64', 'int64'])
        fig, ax = plt.subplots(figsize=(8, 6))
        heat_map = sns.heatmap(numeric_data.corr(),
                               annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig, heat_map)

# Sidebar


def main():
    st.sidebar.subheader("Siva Subramaniam R")

    rad = st.sidebar.radio("Select the topic", [
                           "About this Dataset", "Data Visualizations", "Summary"])

    if rad == "Data Visualizations":
        data = load_data()
        st.markdown(
            "<h2 style='color: rgb(0, 204, 255);'>IRIS DATASET</h2>", unsafe_allow_html=True)
        data = pd.read_csv('Iris.csv')
        dt = data.drop('Id', axis=1)
        st.dataframe(data, width=900)

        st.markdown(
            "<h1 style='color: rgb(51, 204, 204);'>IRIS DATASET VISUALIZATION</h1>", unsafe_allow_html=True)

        st.sidebar.subheader("VISUALIZATION:")
        st.sidebar.subheader("Univariate Visualizations")
        rad1 = st.sidebar.radio("Select the Visualizations", [
                                "Histogram", "Countplot"])

        st.sidebar.subheader("Bivariate Visualizations")
        rad2 = st.sidebar.radio("Select the Visualizations", [
                                "Scatterplot", "Boxplot"])

        st.sidebar.subheader("Multivariate Visualizations")
        rad3 = st.sidebar.radio("Select the Visualizations", [
                                "Pairplot of All Features by Species", "Heatmap of Feature Correlation"])

        if rad1 or rad2 or rad3:
            univariate_visualizations(data, rad1)
            bivariate_visualizations(data, rad2)
            multivariate_visualizations(data, rad3)

    if rad == "About this Dataset":

        st.markdown(
            "<h1 style='color:rgb(102, 255, 153);'>ABOUT THIS DATASET</h1>", unsafe_allow_html=True)
        show_progress()
        st.info("This dataset is related to plant species")
        st.info("The Iris dataset was used in R.A. Fisher's classic 1936 paper, \nThe Use of Multiple Measurements in Taxonomic Problems")
        st.info("It includes three iris species with 50 samples each as well as some \nproperties about each flower. One flower species is linearly separable from \nthe other two, but the other two are not linearly separable from each other.")
        st.subheader("Description the Columns")
        st.text("SepalLengthCm\nSepalWidthCm\nPetalLengthCm\nPetalWidthCm\nSpecies")

    if rad == "Summary":
        st.markdown(
            "<h1 style='color:rgb(153, 204, 255);'>SUMMARY</h1>", unsafe_allow_html=True)
        show_progress()
        st.header("Univariate Visualizations")
        st.subheader("Histogram of Sepal Length:")
        st.info("Visualizes the distribution of a single feature using a histogram with an optional Kernel Density Estimate (KDE) overlay.")
        st.subheader("Countplot of Species:")
        st.info(
            "Displays the count of occurrences for different ranges of a feature using a countplot.")
        st.header("Bivariate Visualizations")
        st.subheader("Scatterplot of Sepal Length vs Sepal Width:")
        st.info("Visualizes the relationship between two features using a scatterplot, with points colored by species.")
        st.subheader("Boxplot of Petal Length by Species:")
        st.info(
            "Shows the distribution of a feature for different species using boxplots.")
        st.header("Multivariate Visualizations")
        st.subheader("Pairplot of All Features by Species:")
        st.info("Displays scatterplots for all pairs of features, colored by species, providing insights into feature relationships.")
        st.subheader("Heatmap of Feature Correlation:")
        st.info(
            "Illustrates the correlation between numeric features using a heatmap, with annotations.")


if __name__ == "__main__":
    main()
