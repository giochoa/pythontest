import os, sys

from PIL import Image

# grab first and second argument

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if the folder exist and if not make one

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through pics
for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    #taking out the jpg in the name
    clean_name = os.path.splitext(file)[0]
    # convert the images then save 
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')



