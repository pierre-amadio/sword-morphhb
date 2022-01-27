#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make some modification in the <w> node of a book file:

By expl, in Psalm 80:14
<w lemma="m/3293 a" n="1" morph="HR/Ncmsa" id="193SD">מִ/יָּ<seg type="x-suspended">עַ</seg>ר</w>
end up as:
<w lemma="strong:H3293" morph="oshm:HR/Ncmsa">מִיָּעַר</w>

- remove the id attribute
- remove the n attribute
- remove <seg> node within <w>
- remove  / in strings
- remove non numerical character in strong numbers.
- pad strong numbers so they always have the same lenght (H+5 digits)
- add morph: in the morph attribute

first argument: book file
second argument: result directory
"""

import sys
import re
from bs4 import BeautifulSoup

inputFile=sys.argv[1]
outputDir=sys.argv[2]
m=re.search(".*\/(\S+)$",inputFile)
if m:
  shortName=m.group(1)
else:
  shortName=inputFile

print("Cleaning %s"%shortName)

soup=False
with open(inputFile) as fp:
  soup=BeautifulSoup(fp, features='xml')

for link in soup.find_all("w"):
  #Let's remove the id node.
  del(link["id"])

  #Let's remove n nodes.
  del(link["n"])

  #let's deal with all the <seg> content (such as Deut 6.4 or Psalm 80:14
  if len(link.find_all("seg"))>=1:
    newString=""
    for elem in link:
      if(elem.name=="seg"):
        newString+=elem.string
      else:
        newString+=elem

    link.contents=[]
    link.string=newString

  #Let's get rid of "/"
  if(link.string.find("/")>-1):
    link.string=link.string.replace("/","")


  #Let's be sure strong number are only number.
  m=re.search(".*?(\d+).*?",link["lemma"])
  if m:
    link["lemma"]="strong:H%s"%m.group(1).rjust(5,"0")

  #Let's put the oshm prefix in the morph tag.
  if(len(link["morph"])!=0):
    link["morph"]="oshm:%s"%link["morph"]

outputFile="%s/%s"%(outputDir,shortName)
with open(outputFile,"w",encoding='utf-8') as file:
  file.write(str(soup))


