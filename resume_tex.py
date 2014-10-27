# Converts my Resume from YAML to TeX.
# Just don't forget to drop pdflatex on the output :)
#
# @contributor Aleksandr Mattal <https://github.com/qutebits>
# inspired by work of Brandon Amos <https://github.com/bamos/cv>

import re
import yaml
import sys

from datetime import date
from jinja2 import Environment, FileSystemLoader

yaml_contents = yaml.load(open("resume.yaml", 'r'))

env = Environment(loader=FileSystemLoader("template"),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')

this_loc = len(open("resume_tex.py", 'r').readlines()) #lets keep it at 42

def generate():
  body = ""
  for section in yaml_contents['order']:
    contents = yaml_contents[section[0]]
    name = section[1].title()
    body += env.get_template("resume-section.tmpl.tex").render(
      name = name.upper(),
      contents = contents
    )

  result = open("result/resume.tex", 'w')
  result.write(env.get_template("resume.tmpl.tex").render(
    name = yaml_contents['name'].upper(),
    email = yaml_contents['email'],
    loc = this_loc,
    body = body,
    today = date.today().strftime("%B %d, %Y")
  ))
  result.close()

generate()