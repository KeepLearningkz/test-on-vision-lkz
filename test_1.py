#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# [START vision_quickstart]
import io
import os
import pandas as pd
import numpy as np
# Imports the Google Cloud client library
# [START vision_python_migration_import]
from google.cloud import vision
from google.cloud.vision import types
# [END vision_python_migration_import]


# In[ ]:


def run_quickstart(uri):

    #Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    name_list=list()
    percentage_list=list()
    for label in labels:
        name_list.append(label.description)
        percentage_list.append(label.score)
    return name_list, percentage_list


# In[ ]:


sample1=pd.read_excel("VISION_API_G1.xlsx")
for url in sample1['URL']:
    run_quickstart(url)

