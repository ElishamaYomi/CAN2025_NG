# -*- coding: utf-8 -*-
import streamlit as st

import streamlit.components.v1 as components

iframe_code = """
<iframe title="Sickle Cell Climate Risk"
        width="1024"
        height="612"
        src="https://app.powerbi.com/view?r=eyJrIjoiNTQyMjcyZjMtYTAyNy00YzhhLWE5YzYtNDE2NDBhZDlkZDI1IiwidCI6ImYxYWU4ZTFmLWIxOTgtNDNlOC1iZjk0LTFmYmZlNTdkMDI2YyJ9"
        frameborder="0"
        allowfullscreen>
</iframe>
"""
components.html(iframe_code, height=620, width=1030)
