# -*- coding: utf-8 -*-
"""largest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11DkveGIWE8W0B2blSTzC-MpNVCg2MZbg
"""

!pip install -q streamlit

import streamlit as st
import pandas as pd

st.write("""
#Largest number prediction App""")

st.header('User inputs')

def user_input_features():
  num1 = st.number_input("num1", min_value = -2000000000, max_value = 2000000000, step = 1)
  num2 = st.number_input("num2", min_value = -2000000000, max_value = 2000000000, step = 1)
  num3 = st.number_input("num3", min_value = -2000000000, max_value = 2000000000, step = 1)

  numbers = [num1, num2, num3]
  return numbers

  numbers = user_input_features()
  res = max(numbers)

  st.subheader("Result : the largest of the 3 numbers is ")
  st.write(res)

