import json
import os
import os.path
import random
import threading
from datetime import datetime

import requests
from PIL import Image
from numpy import asarray


class CPicture:
    imageData = 'images/'

    def random_traffic(self, n):
        response = requests.get('https://api.transport.nsw.gov.au/v1/live/cameras',
                                headers={'Authorization': 'apikey SgdO57pmM7byDpbENqVkscYwdiF0G0GSsFwA'})
        tomb = json.loads(response.content)['features']
        for t in tomb[:n]:
            cam_id = t['id']
            print(cam_id)
            url = t['properties']['href']
            response2 = requests.get(url)
            if response2.status_code == 200:
                folder_name = self.imageData + "opentraffic/" + cam_id
                if not os.path.isdir(folder_name):
                    os.mkdir(folder_name)

                with open(folder_name + '/' + cam_id + '-'
                          + datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".jpg", 'wb') as f:
                    f.write(response2.content)

            with open(self.imageData + "opentraffic/adatok.txt", 'at') as f:
                f.write(json.dumps(t) + "\n")
        print("-------")

    def save_traffic_cam(self, lista):
        # DIR = self.imageData + 'opentraffic'
        threading.Timer(60.0, self.save_traffic_cam, [lista]).start()
        for a in lista:
            self.random_traffic(a)
            # print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

    def save_all_traffic_cam(self):
        response = requests.get('https://api.transport.nsw.gov.au/v1/live/cameras',
                                headers={'Authorization': 'apikey SgdO57pmM7byDpbENqVkscYwdiF0G0GSsFwA'})
        tomb = json.loads(response.content)['features']
        for t in tomb:
            cam_id = t['id']
            print(cam_id)
            url = t['properties']['href']
            response2 = requests.get(url)
            if response2.status_code == 200:
                folder_name = self.imageData + "opentraffic/" + cam_id
                if not os.path.isdir(folder_name):
                    os.mkdir(folder_name)

                with open(folder_name + '/' + cam_id + '-'
                          + datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".jpg", 'wb') as f:
                    f.write(response2.content)

            with open(self.imageData + "opentraffic/adatok.txt", 'at') as f:
                f.write(json.dumps(t) + "\n")
        print("-------")

    def random_picture(self):
        response = requests.get("https://picsum.photos/200/300.jpg")
        name = response.url[25:-12]

        f = open(self.imageData + 'picsum/' + name + '.jpg', 'wb')
        f.write(response.content)
        f.close()

        # response = requests.get("https://source.unsplash.com/random")

    def lists_to_string(self, lista):
        strr = ''
        for ll in lista:
            for i in ll:
                strr = strr + str(i) + ','
        return strr[0:-1]

    def print33ToFile(self, image, target):
        i = Image.open(image)
        data = asarray(i)
        size = i.size
        pos = [random.randint(0, size[1] - 3), random.randint(0, size[0] - 3)]
        with open(self.imageData + target, 'a') as out3:
            L = []
            for i in range(3):
                for j in range(3):
                    pixel = data[pos[0] + i, pos[1] + j].tolist()
                    L.append(pixel)
            out3.write(image + ',' + self.lists_to_string(L) + '\n')
