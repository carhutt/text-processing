# !/usr/bin/python

"""
This is an example of a way to bulk rename a bunch of files in a directory.
This one renames a bunch of gdoc files.
In this example newnames holds all the new names.
The directory is hardcoded in in the for loop because os.listdir lets you filter
by file type.
Question: how to add an extension to the new files?
"""

import os, sys

newnames = [
"approach",
"cities",
"company",
"home",
"industrial",
"offices",
"p-buildingautomation",
"p-citizensafety",
"p-environment",
"p-guidance",
"p-instore",
"p-inventory",
"p-network",
"p-spaceplanning",
"p-storeops",
"p-systems",
"p-tech",
"p-telco",
"p-transportation",
"p-urbaneconomic",
"partnerships",
"stores"
];

index=0
# listing files
print "The current directory contains: %s"%os.listdir(os.getcwd())

#renaming -- number of items in newnames should match number in directory
for f in os.listdir("/Users/Andrew/Documents/KHi/Smart Cities/GE/bash_scraper/texts/html/GDrive/"):
	if f.endswith(".gdoc"):
		os.rename(f, newnames[index])
		index += 1

print "\n".
print "Successfully renamed."
print "\n".
# listing files after renaming
print "The current directory now contains: %s" %os.listdir(os.getcwd())
