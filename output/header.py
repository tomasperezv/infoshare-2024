import pyfiglet
import json
import textwrap
from termcolor import colored
from pygments import highlight, lexers, formatters

def print_art(text):
  text = text
  font = "slant"

  ascii_art = pyfiglet.figlet_format(text, font=font)

  print(colored(ascii_art, 'yellow'))

def print_json(data, fg_color='black', bg_color='blue', width=150):
    def format_json(obj, indent=0):
        if isinstance(obj, dict):
            items = []
            for k, v in obj.items():
                formatted_key = ' ' * indent + json.dumps(k)
                formatted_value = format_json(v, indent + 4)
                items.append(f'{formatted_key}: {formatted_value}')
            return '{\n' + ',\n'.join(items) + '\n' + ' ' * indent + '}'
        elif isinstance(obj, list):
            items = [format_json(item, indent + 4) for item in obj]
            return '[\n' + ',\n'.join(items) + '\n' + ' ' * indent + ']'
        elif isinstance(obj, str):
            wrapped_lines = []
            for line in obj.split('\n'):
                wrapped_lines.extend(textwrap.wrap(line, width=150))
            return '\n'.join([' ' * indent + json.dumps(line) for line in wrapped_lines])
        else:
            return ' ' * indent + json.dumps(obj)

    formatted_json = format_json(data, indent=4)
    for line in formatted_json.splitlines():
        print_colored_text(line, fg_color, bg_color)

def print_colored_text(text, fg_color, bg_color):
    print(colored(text, fg_color, f'on_{bg_color}'))

def print_exception(e):
    print_colored_text(f"{e}", 'white', 'red')
