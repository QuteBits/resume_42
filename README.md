YAML to PDF Resume Generator
============================

That's some cute python shit here. It generates a beautiful resume from yaml data. Here's how the output looks:

PDF example: <a href="https://github.com/QuteBits/resume_42/blob/master/resume_example.pdf?raw=true">https://github.com/QuteBits/resume_42/blob/master/resume_example.pdf?raw=true</a> or the screenshot:

![Alt text](https://raw.github.com/QuteBits/onScriptogram/master/img/06-03.jpg "Resume Look")

and something for nerds (the story behind this project): <a href="http://scriptogr.am/qutebits/post/q06-resume-42">http://scriptogr.am/qutebits/post/q06-resume-42</a>

### Acknowledgements:

This project is inspired by the work of Brandon Amos: <a href="https://github.com/bamos/cv">https://github.com/bamos/cv</a>

### Pre-Install:
* Install Python (I tested it on <a href="https://www.python.org/download/releases/2.7.3/">Python 2.7.3</a>)
* Install <a href="http://miktex.org/">MikTeX</a> or any other LaTeX processor
* Install <a href="https://github.com/mitsuhiko/jinja2">Jinja2</a> package and install it (other packages are assumed to be there or to be installed on-the-fly by MikTeX during compiling for the first time)

### Install:
* Download this whole project from GitHub, unzip to some folder "x"

### Use:

* python resume_tex.py | cd result | pdflatex resume.tex | pdflatex resume.tex | cd ..

Human explanation: basically you put your data into *resume.yaml* (don't forget to read guidelines in the header), then convert it to TeX and compile TeX twice (you need it so that the page numbering would be correct. TeX doesn't know how many pages you compile during the first run). The conversion to TeX comes in 2 stages:

1. First, each section from *resume.yaml* is generated according to the */template/resume-section.tmpl.tex*
2. then the TeX wrapper is generated according to */template/resume.tmpl.tex* - which is then filled with generated sections from 1.

### Contact:
<a href="https://twitter.com/qutebits">@qutebits</a> or qute.bits (gmail)
