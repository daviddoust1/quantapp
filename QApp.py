from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import urllib.request
import sys
from path import Path

dir = path.Path(__file__).abspath()
sys.append.path(dir.parent.parent)



# urllib.request.urlretrieve('https://raw.githubusercontent.com/daviddoust1/quantapp/refs/heads/main/TriangleText.png', 'TriangleText.png')

# Streamlit app: To run, open a terminal and run:
# streamlit run QApp.py
# May need to press enter to get past the welcome message

st.write('# QuantApp')
st.write(' ')

canvas_result = st_canvas(
    stroke_color='#ed13e2',
    # rgb 237, 19, 226
    stroke_width=4,
    height=500,
    width=600,
    background_image=Image.open('./static/TriangleText.png'), 
    drawing_mode='point',
    point_display_radius=4)

complete = st.checkbox(label='Complete', value=False)

if complete:
    if canvas_result.json_data is not None:
        objects = pd.json_normalize(canvas_result.json_data["objects"])
        for col in objects.select_dtypes(include=["object"]).columns:
            objects[col] = objects[col].astype("str")
        # st.dataframe(objects)
        # Configure the below coords by placing a point on each corner
        # and looking at the coords in objects dataframe
        top = [291,52]
        left = [81,440]
        right = [500,438]
        selection = [int(objects['left'][0]), int(objects['top'][0])]

        # Will need to fix these a bit - max_dist changes with the position of the point
        max_dist = ((top[0] - left[0])**2 + (top[1] - left[1])**2)**0.5
        top_score = 1-((((selection[0] - top[0])**2 + (selection[1] - top[1])**2)**0.5)/max_dist)
        left_score = 1-((((selection[0] - left[0])**2 + (selection[1] - left[1])**2)**0.5)/max_dist)
        right_score = 1-((((selection[0] - right[0])**2 + (selection[1] - right[1])**2)**0.5)/max_dist)

        st.write("things score: " + str(top_score))
        st.write("stuff and also things score: " + str(left_score))
        st.write("things and stuff score: " + str(right_score))
        
