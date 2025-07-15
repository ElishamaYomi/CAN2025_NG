# -*- coding: utf-8 -*-

import streamlit as st
import streamlit.components.v1 as components

iframe_code = """
<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src=""https://app.powerbi.com/view?r=eyJrIjoiNTQyMjcyZjMtYTAyNy00YzhhLWE5YzYtNDE2NDBhZDlkZDI1IiwidCI6ImYxYWU4ZTFmLWIxOTgtNDNlOC1iZjk0LTFmYmZlNTdkMDI2YyJ9""
            title="Sickle Cell Climate Risk"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
            allowfullscreen>
    </iframe>
</div>
"""

components.html(iframe_code) 
