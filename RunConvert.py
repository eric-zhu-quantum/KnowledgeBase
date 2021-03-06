from os.path import isfile, join
import os


mypath = os.getcwd()

#get all filenames in directory 
AllFiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]

# get all files with MKV suffix
Files_MKV = [f for f in AllFiles if '.mkv' in f]

#look at already converted files (which we assume will have mp4 extension)
Files_MP4 = [f for f in AllFiles if '.mp4' in f]

print(Files_MKV)



for filename in Files_MKV:

  filename_new = '"'+filename[:(-4)]+'.mp4'+'"'
  
  if (filename_new in Files_MP4):
    print(filename[1:(-1)] + ' is already converted')
    continue


  print(filename_new)
  ExecutedCode  = 'ffmpeg -i ' +'"'+ filename +'"'+ ' -acodec mp3 -vcodec h264 ' +\
  ' -q 25 -threads 4 ' + filename_new  #up the thread count if system has more cores to spare

  os.system(ExecutedCode)
