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

parent_dir = "/home/palash/" # for my system
photo_dir = '/home/palash/Pictures/' # OR os.getcwd()
# parent_dir = photo_dir[photo_dir.rfind('/')] ## FOR WINDOWS
photos = []

# parent_dir += "\\" ## For Windows
# photo_dir += "\\" ## For Windows

for photo in os.walk(photo_dir):
    photos += [photo]
    
for i in photos:
    for j in i:
        if type(j) == list and not j == []:
            a += j
    
### Assuming all photos are in the same directory ###

for images in a:
    print(images)
    match1 = re.search( r'\d{4}-\d{2}-\d{2}', images) # OR r'\d{8} ## For images saved like: IMG_20200720
    print(match1)
    match2 = re.search( r'\d{8}', images) # OR r'\d{8} ## For images saved like: IMG_20200720
    if match1:
        date = str(datetime.strptime(match1.group(), '%Y-%m-%d').date()) # OR %Y%m%d For images saved like: IMG_20200720
    if match2:
        date = str(datetime.strptime(match2.group(), '%Y%m%d').date()) # OR %Y%m%d For images saved like: IMG_20200720
    if os.path.isdir(parent_dir + date):
        shutil.move(photo_dir + images, parent_dir + date)
    else:
        os.mkdir(parent_dir + date)
        shutil.move(photo_dir + images, parent_dir + date)
