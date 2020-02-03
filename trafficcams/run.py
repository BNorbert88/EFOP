from cpicture import CPicture
import os

c = CPicture()

############################################################################
# Calculate RGB values from the folder kitti
############################################################################

# testdir = '/mnt/data/PycharmProjects/imagepixel/images/kitti/'
#
# for file in os.listdir(os.fsencode(testdir)):
#     filename = os.fsdecode(file)
#     c.print33ToFile(testdir + filename, 'test_kitti.txt')


############################################################################
# Random picture download from API and creation of a txt from pixel RGB values
############################################################################

# for i in range(10):
#     print(i)
#     c.randomPicture()

# testdir = '/mnt/data/PycharmProjects/imagepixel/images/picsum/'
#
# for file in os.listdir(os.fsencode(testdir)):
#     filename = os.fsdecode(file)
#     c.print33ToFile(testdir + filename, 'test_picsum.txt')


############################################################################
# Acces to an open API
############################################################################

c.save_all_traffic_cam()
