from genericpath import isfile
import os
import json
directory = 'students'

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        with open(filepath) as obj:
            student = json.load(obj)
            print(f"{student.get('name')} is majoring in {student.get('major')} and will graduate in {student.get('class_year')} ")