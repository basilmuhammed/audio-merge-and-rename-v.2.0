import os

audiofiles = "./audio-files/"
i = 1

for filename in os.listdir(audiofiles):
    os.rename(os.path.join(audiofiles, filename),
    os.path.join(audiofiles, 'tomergenumber-'+str(i)+'.ogg'))
    i += 1


# path = '/home/pi/images/'
# i = 0
# for filename in os.listdir(path):
#     os.rename(os.path.join(path,filename), os.path.join(path,'captured'+str(i)+'.jpg'))
#     i = i +1
