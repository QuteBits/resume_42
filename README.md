YAML to PDF Resume Generator
============================

That's some cute python shit here. It generates a beautiful resume from yaml data. Quasi-Screenshot:

![Alt text](https://raw.github.com/QuteBits/onScriptogram/master/img/06-03.jpg "Resume Look")

and something for nerds (the story behind this project): 

<a href="http://scriptogr.am/qutebits/post/q06-resume-42">http://scriptogr.am/qutebits/post/q06-resume-42</a>

# Acknowledgements:

This project is inspired by the work of Brandon Amos: <a href="https://github.com/bamos/cv">https://github.com/bamos/cv</a>

# Install:
* Install Python (I tested it on 2.7.3)
* Install MikTeX or any other LaTeX processor
* Install Jinja2 package (other packages will be installed on-the-fly during compiling for the first time)

# Use:

Basically you put your data into *resume.yaml*, then convert it to TeX and compile TeX twice (you need it so that the page numbering would be correct. TeX doesn't know how many pages you compile in the first run)

* python resume_tex.py | cd result | pdflatex resume.tex | pdflatex resume.tex | cd ..

## Contact:
<a href="https://twitter.com/qutebits">@qutebits</a> or qute.bits (gmail)
