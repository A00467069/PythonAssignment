import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt


def main():

    file_to_plot = st.file_uploader("Upload your CSV file", type="csv")

    if file_to_plot is not None:
        df = pd.read_csv(file_to_plot)
        if set(df.columns) == {"Name", "Age"}:
            st.success("CSV file is valid")
            fig, ax = plt.subplots()
            ax.hist(df['Age'].astype(float), bins=10)
            ax.set_xlabel("Age")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        else :
            st.error("Invalid CSV")


if __name__ == "__main__":
    main()