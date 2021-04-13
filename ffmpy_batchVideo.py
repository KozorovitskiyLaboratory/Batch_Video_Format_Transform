#this program transforms all video file in a folder to a specified format
from ffmpy import FFmpeg
from os import listdir
from os.path import isfile, join

#set file folder path here
#file path sample:  r'C:\Users\K lab Yuejun\Box'
mypath=r' '

#the format you want
new_format='.avi'

#get all file names
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print('videos in the folder: ')
print (onlyfiles)

#split file name from format
for file in onlyfiles:
    fullname=file.split(".")
    trueName=fullname[0]

    print ('format changing: ')
    fullPath_in=mypath+'\\'+ file
    print(fullPath_in)
    fullPath_out=mypath+'\\'+trueName+new_format
    print(fullPath_out)
    ff = FFmpeg(inputs={fullPath_in: None},outputs={fullPath_out: ['-q:v', '0']})
    ff.cmd
    ff.run()
    print('Done')
