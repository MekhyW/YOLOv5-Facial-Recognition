import os

annotations = os.listdir('Annotations')

for image in os.listdir('Fursuit_unused'):
    if image.replace('jpg', 'xml').replace('png', 'xml') in annotations:
        os.replace('Fursuit_unused/' + image, 'Fursuit/' + image)

for image in os.listdir('Human_unused'):
    if image.replace('jpg', 'xml').replace('png', 'xml') in annotations:
        os.replace('Human_unused/' + image, 'Human/' + image)