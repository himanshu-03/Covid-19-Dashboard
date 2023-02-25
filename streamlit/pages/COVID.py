import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "NSE.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "NSE-TATAGLOBAL.csv")

st.title("Dashboard: NSE-TATAGLOBAL")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

