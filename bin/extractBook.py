#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
get the content of the <book> node from an osi file and store the content in a file
first argument: osis file
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

print("Extracting book from %s"%shortName)

with open(inputFile) as fp:
  soup=BeautifulSoup(fp, features='xml')
  for book in soup.find_all('div',type="book"):
    outputFile="%s/%s"%(outputDir,shortName)
    with open(outputFile,"w",encoding='utf-8') as file:
      file.write(str(book))

