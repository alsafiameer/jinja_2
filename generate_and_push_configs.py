# generat the configs from var file and open it and print every line with skip option. 

from jinja2 import Template
import yaml
import sys


def print_line(file_to_open):
	while True: 
		with open (file_to_open , 'r') as f: 
			for line in f: 
				print "Line > " + line , 
				print_line = raw_input ("Enter 'y' for print and 'n' to skip > ")
				if print_line == "y": 
					print line.strip() + "\n"
				elif print_line == "n":
					print " You dont need to print line " + line 
					pass
				else: 
					print " Worng input! " 
		f.close()
	return 


var = raw_input("Var file name> ")

datavars = yaml.load(open(var+".yml").read())
template = Template(open("config_temp.j2").read())

readoutput = template.render(datavars)
saveconfigs = open(var + "_conf" , "w")
saveconfigs.write(readoutput)
saveconfigs.write("\n")
saveconfigs.close()

print "configuration has been creat! "

while True: 
	ex_config = raw_input ("Enter y to excude the configs and n to abort > ") 
	if ex_config == "y": 
		config_file = var + "_conf" 
		print_line(config_file) 
	else: 
		exit()
