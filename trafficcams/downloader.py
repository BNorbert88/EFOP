#!/usr/bin/env python3
#
# Copyright (C) 2019-2020, University of Szeged, Bogya Norbert
#

import json
import os
from datetime import datetime
import requests

FOLDER = 'images/'
APIKEY = 'SgdO57pmM7byDpbENqVkscYwdiF0G0GSsFwA'  # change it for yours


def save_all_traffic_cam():
    if not os.path.isdir(FOLDER):
        os.mkdir(FOLDER)

    response = requests.get('https://api.transport.nsw.gov.au/v1/live/cameras',
                            headers={'Authorization': 'apikey ' + APIKEY})
    features = json.loads(response.content)['features']
    print("active cameras", len(features))

    for feature in features:
        cam_id = feature['id']
        print("downloading from", cam_id)
        url = feature['properties']['href']
        try:
            response2 = requests.get(url)
            if response2.status_code == 200:
                folder_name = os.path.join(FOLDER, cam_id)
                if not os.path.isdir(folder_name):
                    os.mkdir(folder_name)
                file_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
                file_name = os.path.join(folder_name, cam_id + '-' + file_time + '.jpg')
                with open(file_name, 'wb') as f:
                    f.write(response2.content)

            feature['file_name'] = file_name
            feature['file_time'] = file_time
            with open(os.path.join(FOLDER, 'adatok.txt'), 'at') as f:
                f.write(json.dumps(feature) + '\n')
        except requests.exceptions.ConnectionError:
            print("download failed from", cam_id)


if __name__ == '__main__':
    while True:
        save_all_traffic_cam()
