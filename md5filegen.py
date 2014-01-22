#! /usr/bin/python
#MD5 FILE HASH GENERATOR
#Version: 1.0
#Codedy by @boshox
#########################
#########################
#########################
#########################

#imports
import argparse
import hashlib

#argument parser
parser = argparse.ArgumentParser(description='Massive MD5 Hashes Generator from list')
parser.add_argument('-i','--input', help='Input filename, txt file with strings per line', required=True)
parser.add_argument('-o','--output', help='Output file, file generated with MD5 hashes', required=True)
args = parser.parse_args() 

#files operations
filer = open (args.input, 'r')
filew = open (args.output, 'w')
#md5 generator
for line in filer:
	if line.strip():
		string = line.strip()
		filew.write(hashlib.md5(string).hexdigest()+"\n")

filer.close()
filew.close()

#values
print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )
