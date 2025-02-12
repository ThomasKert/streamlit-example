from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

    # Table with random values
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))

    # Chat example
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.write("Streamlit is an open-source Python library that is used for creating web applications and interactive web-based dashboards with minimal effort. It is designed to make it easy for data scientists, engineers, and developers to quickly turn data scripts into shareable web applications. Streamlit is known for its simplicity and ease of use, allowing users to create web apps with just a few lines of Python code.")
        st.line_chart(np.random.randn(30, 3))
    
    prompt = st.chat_input("Say something")
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
