import streamlit as st

# CSS
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

#   HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# دمج CSS داخل HTML
html_with_css = f"<style>{css}</style>{html}"

# عرض الصفحة
st.components.v1.html(html_with_css, height=600, scrolling=True)
