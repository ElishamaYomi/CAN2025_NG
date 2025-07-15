# -*- coding: utf-8 -*-

import streamlit as st
import streamlit.components.v1 as components

iframe_code = """
<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
  <iframe src="https://www.who.int/data/gho/data/indicators/indicator-details/GHO/number-of-deaths"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
          allowfullscreen>
  </iframe>
</div>
"""

components.html(iframe_code, height=600)
