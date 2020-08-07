#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:09:41 2020

@author: palash
"""


import shutil, os, re
from PIL import Image
import datetime
from datetime import datetime

parent_dir = "/home/palash/"
photo_dir = '/home/palash/Pictures/'
photos = []

for photo in os.walk(photo_dir):
    photos += [photo]
    
for i in photos:
    for j in i:
        if type(j) == list and not j == []:
            a = j
    
### Assuming all photos are in the same directory ###

for images in a:
    print(images)
    match = re.search( r'\d{4}-\d{2}-\d{2}', images)
    print(match)
    date = str(datetime.strptime(match.group(), '%Y-%m-%d').date())
    if os.path.isdir(parent_dir + date):
        shutil.move(photo_dir + images, parent_dir + date)
    else:
        os.mkdir(parent_dir + date)
        shutil.move(photo_dir + images, parent_dir + date)
