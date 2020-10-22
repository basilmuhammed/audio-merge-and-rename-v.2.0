import os

audiofiles = "./audio-files/"

for filename in os.listdir(audiofiles):
    print(os.path.join(audiofiles, filename))
    # print(str(filename))
    # print('hi')
    # p = os.chdir(filename)
    
