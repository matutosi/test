import streamlit as st

import os
import sys

cmd = st.text_input("command")
os.system(cmd)
