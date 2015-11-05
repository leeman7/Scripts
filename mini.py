#!/usr/bin/python 
import urllib

print "enter a file name:"
infile = raw_input()

lines = []

with open(infile, "r") as file:
    for line in file.readlines():
        if line[-1] == "\n":
           line = line[:-1]
        lines.append(line)

#Faculty member name
temp = lines[294]
firstName = temp.replace(" ", "").replace("("," (")

temp = lines[297]
lastName = temp.replace(" ","")
name = firstName + " " + lastName 

#Faculty member Education
temp = lines[365]
tempEducation = temp.replace("\"","").replace("</p></div>","").replace("<div class=","").replace("panel-body","").replace("><p>","")
education2 = tempEducation.split()
education = ""
for word in education2:
    education += word
    education += " "

#Faculty member Research Interests
temp = lines[353]
tempResearch = temp.replace("\"","").replace("</p></div>","").replace("<div class=","").replace("panel-body","").replace("><p>","")
research2 = tempResearch.split()
research = ""
for word in research2:
    research += word
    research += " "

#Faculty member Webpage
temp = lines[339]
tempWeb = temp.replace("\"","").replace("<h4><small><a target=","").replace("_blank","").replace(" href=","").replace("%7E","~").replace(">Homepage</a></small></h4>","")
web = tempWeb.replace(" ","")

#Get Faculty member email address
email = web.replace("http://www.cs.txstate.edu/~","").replace("http://cs.txstate.edu/~","")

#Generate output file and write output to file
outfile = name + ".txt"
file = open(outfile, "w")

file.write("Name: %s\n" %name)
file.write("Education: %s\n" %education)
file.write("Research Interests: %s\n" %research)
file.write("Email: %s@txstate.edu\n" %email)
file.write("Webpage: %s\n" %web)
