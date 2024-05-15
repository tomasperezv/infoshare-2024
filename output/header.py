import pyfiglet
import json
from termcolor import colored
from pygments import highlight, lexers, formatters

def print_art(text):
  text = text
  font = "slant"

  ascii_art = pyfiglet.figlet_format(text, font=font)

  print(colored(ascii_art, 'yellow'))

def print_json(data):
  json_str = json.dumps(data, indent=4)

  colorful_json = highlight(json_str, lexers.JsonLexer(), formatters.TerminalFormatter())

  print(colorful_json)

def print_exception(e):
  print(colored(f"{e}", 'yellow'))
