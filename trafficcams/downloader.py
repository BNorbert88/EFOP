#!/usr/bin/env python3
#
# Copyright (C) 2019-2020, University of Szeged, Bogya Norbert
#

from datetime import datetime
import json
import os
from io import BytesIO
import time
import numpy as np
import requests
from PIL import Image

FOLDER = 'images/'
APIKEY = 'SgdO57pmM7byDpbENqVkscYwdiF0G0GSsFwA'  # change it for yours


def save_all_traffic_cam():
    if not os.path.isdir(FOLDER):
        os.mkdir(FOLDER)

    features = []
    while True:
        try:
            response = requests.get('https://api.transport.nsw.gov.au/v1/live/cameras',
                                    headers={'Authorization': 'apikey ' + APIKEY})
            features = json.loads(response.content)['features']
            print("number of active cameras:", len(features))
        except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
            print("failed to update list of cameras")
            if len(features) < 10:
                time.sleep(60)

        for feature in features:
            cam_id = feature['id']
            print("downloading image from:", cam_id)
            url = feature['properties']['href']
            try:
                response = requests.get(url, stream=False)
                if response.status_code != 200:
                    print("unexpected response:", response.status_code)
                    continue

                img = Image.open(BytesIO(response.content))
                if np.array(img).shape == ():
                    print("broken image from:", cam_id)
                    continue

                folder_name = os.path.join(FOLDER, cam_id)
                if not os.path.isdir(folder_name):
                    os.mkdir(folder_name)
                file_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
                file_name = os.path.join(folder_name, cam_id + '-' + file_time + '.jpg')
                with open(file_name, 'wb') as f:
                    f.write(response.content)

                feature['file_name'] = file_name
                feature['file_time'] = file_time
                with open(os.path.join(FOLDER, 'adatok.txt'), 'at') as f:
                    f.write(json.dumps(feature) + '\n')

            except requests.exceptions.ConnectionError:
                print("download failed from:", cam_id)


def delete_broken_images():
    for dir_name, _, file_names in os.walk(FOLDER):
        for file_name in file_names:
            if not file_name.endswith('.jpg'):
                continue

            file_name = os.path.join(dir_name, file_name)
            img = np.array(Image.open(file_name))
            if img.shape == ():
                print("deleting:", file_name)
                os.unlink(file_name)


if __name__ == '__main__':
    save_all_traffic_cam()
    # delete_broken_images()
