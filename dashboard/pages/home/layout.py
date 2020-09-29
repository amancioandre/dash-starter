## Layouts are responsible for structuring the HTML DOM.
from dashboard import html

def layout():
    return html.Div(
        html.H1("This is a dashboard")
    )