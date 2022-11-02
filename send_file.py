# importing the requests library
import requests
import json
import os
import encoding
from producer import publish


# defining the api-endpoint
socket_address = "http://localhost:7777"

image_list = ['.tif', '.tiff', '.bmp', '.jpg', '.jpeg', '.gif', '.png',
              #   created by camera, etc
              '.raw', '.cr2', '.nef', '.orf', '.sr2']


def post_imageOLD(img_file):
    """ prepare headers for http request """
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    # filetype = 'image'
    URL = socket_address + f'/api/images/add'

    """ post image and return the response """
    img = open(img_file, 'rb').read()
    response = requests.post(URL, data=img, headers=headers)
    return response


def post_file(file_path):
    # get file name & extension from path
    file_name, file_extension = os.path.splitext(file_path)
    file = file_name + file_extension

    # convert file bytes to string
    file_string = encoding.bytes_to_string(file_path)

    # check content type
    if file_extension in image_list:
        content_type = 'image/jpeg'
    else:
        content_type = 'unknown'

    # send to queue
    publish(content_type, {'title': file, 'image': file_string})


if __name__ == '__main__':
    image_title = 'egg.bmp'
    # image_taken = encoding.get_meta_data(image_title)
    # print(image_taken)
    post_file(image_title)
