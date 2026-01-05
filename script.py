with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html_with_css = f"<style>{css}</style>{html}"
st.components.v1.html(html_with_css, height=600, scrolling=True)
