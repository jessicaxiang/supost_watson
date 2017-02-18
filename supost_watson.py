# Program: SUpost Watson
# Author: Greg Wientjes, Jessica Xiang
# Date: 2/18/17
# Purpose: Make a MVP for the Treehacks hackathon. We will classify incoming
# SUpost post photos. We focus first on bike photos.
# Notes:
# We first got this code from IBM Watson sample code at https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/visual_recognition_v3.py
# Then we modified the code to meet our purpose.

import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

test_url = 'http://supost-prod.s3.amazonaws.com/posts/129805618/post_129805618a'

visual_recognition = VisualRecognitionV3('2017-02-18', api_key='203d41f3ef200e7522fe945b876a50c58ec78da5')

with open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars, \
       open(join(dirname(__file__), '../resources/bikes.zip'), 'rb') as
trucks:
    print(json.dumps(visual_recognition.create_classifier('Cars vs Bikes',
 cars_positive_examples=bikes,

negative_examples=cars), indent=2))

# maybe we want this part later
# with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
#     print(json.dumps(
#         visual_recognition.classify(images_file=image_file, threshold=0.1,
#                                     classifier_ids=['CarsvsTrucks_1479118188',
#                                                     'default']), indent=2))

# print(json.dumps(visual_recognition.get_classifier('YOUR CLASSIFIER ID'),
# indent=2))

# with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as
# image_file:
#     print(json.dumps(visual_recognition.update_classifier(
# 'CarsvsTrucks_1479118188',
#
# cars_positive_examples=image_file), indent=2))

print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

# face recognition - we don't need it
# print(
#     json.dumps(visual_recognition.detect_faces(images_url=test_url), indent=2))

# print(json.dumps(visual_recognition.delete_classifier(classifier_id='YOUR
# CLASSIFIER ID'), indent=2))

# do we need this?
# print(json.dumps(visual_recognition.list_classifiers(), indent=2))

# text recognition - we don't need it
# with open(join(dirname(__file__), '../resources/text.png'), 'rb')\
#         as image_file:
#     print(json.dumps(visual_recognition.recognize_text(images_file=image_file),
#                      indent=2))

# face recognition - we don't need it
# with open(join(dirname(__file__), '../resources/face.jpg'), 'rb')\
#         as image_file:
#     print(json.dumps(visual_recognition.detect_faces(images_file=image_file),
#                      indent=2))

# with open(join(dirname(__file__), '../resources/face.jpg'), 'rb') as \
#     image_file:
# print(json.dumps(
#     visual_recognition.find_similar(collection_id="YOUR_COLLECTION_ID",
#                                     image_file=image_file),
#     indent=2))