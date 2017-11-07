#!/usr/bin/env python

from jinja2 import Template
import yaml
import sys
import telnetlib
"""
Add to variable to prompt user to add var file and template and save the file:

        you should add the full location to those files.
"""

var = raw_input("Var file name> ")
temp  = raw_input("Temp file name> ")
file_name = raw_input("Saving configuration file name> ")



datavars = yaml.load(open(var+".yml").read())
template = Template(open(temp+".j2").read())

"""
render the output and save it into new file 

"""" 
readoutput = template.render(datavars)
saveconfigs = open(file_name , "w")
saveconfigs.write(readoutput)
saveconfigs.write("\n")
saveconfigs.close()

print "Done !"
