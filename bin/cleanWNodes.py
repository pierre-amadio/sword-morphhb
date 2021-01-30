#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make some modification in the <w> node of a book file:

<w lemma="c/1254 a" morph="HC/Vqw3ms" id="016kU">וַ/יִּבְרָ֣א</w>
->
<w lemma="1254 a" morph="HC/Vqw3ms" id="016kU">וַ/יִּבְרָ֣א</w>

<w lemma="5921 a" morph="HR" id="01CCj">עַל</w><seg type="x-maqqef">־</seg><w lemma="d/776" n="0.1" morph="HTd/Ncbsa" id="01gV8">הָ/אָ֔רֶץ</w>
->
<w lemma="5921" morph="HR" id="01CCj">עַל</w><seg type="x-maqqef">־</seg><w lemma="d/776" n="0.1" morph="HTd/Ncbsa" id="01gV8">הָ/אָ֔רֶץ</w>


let s extract only the integer from the lemma attribute (strong number)
let s get rid of the id  attribute.
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
  del(link["id"])
  m=re.search(".*?(\d+).*?",link["lemma"])
  if m:
    #print(m.group(1))
    #link["lemma"]="strong:H%s"%m.group(1)
    link["lemma"]="%s"%m.group(1)
    a=1
  #else:
  #  print("Cannot parse '%s'"%link)

outputFile="%s/%s"%(outputDir,shortName)
with open(outputFile,"w",encoding='utf-8') as file:
  file.write(str(soup))


