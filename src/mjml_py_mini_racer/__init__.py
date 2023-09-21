from py_mini_racer import py_mini_racer
from pathlib import Path

__version__ = "0.0.1"

# Init mini racer context & load the JS file
def init():
    c = py_mini_racer.MiniRacer()
    js_file_path = Path(__file__).parent.joinpath('../../mjml-lib/dist/index.js')
    with js_file_path.open('r') as js_file:
        c.eval(js_file.read())
    return c


ctx = init()

# Call JS function with MJML JSON string and returns HTML
def mjml2html(mjmlJSONString):
    return ctx.call("mjml.mjml2html", mjmlJSONString)
