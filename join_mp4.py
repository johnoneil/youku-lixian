#!/usr/bin/env python

import sys
#import struct
#from cStringIO import StringIO

##################################################
# main
##################################################

def concat_mp4s(mp4s_orig, outputFile):
  assert mp4s_orig, 'no mp4 input file found'
  assert outputFile, 'no output file specified'
  #simply emulate pass by value behavior
  #(i.e. don't ruin the mp4 list)
  mp4s = list(mp4s_orig)
  import os.path
  #for i,flv in enumerate(flvs):
  #  mp4 = mp4s[i]
  #print 'concatenating %s' % (','.join(mp4s))
  firstMp4 = mp4s.pop(0)
  systemCall="MP4Box -add \'" + firstMp4 + "\'"
  for mp4 in mp4s:
    systemCall = systemCall + " -cat \'" + mp4 +"\'"
  systemCall = systemCall + " -new \'" + outputFile + "\'"
  print "will execute system call :" + systemCall
  if( os.system( systemCall ) ):
    print "mp4 concatenaton failed"
    sys.exit()
  
    #Until we have a reliable ffmpeg wrapper, just make system call to ffmpeg
    #note the -y option automatically overwrites existing output files
    #and the 
    #if( os.system("ffmpeg -i \'%s\' -y -acodec copy -vcodec copy \'%s\'"%(flv,mp4)) ):
    #  print "could not successfully convert % into %. Exiting"%(flv,mp4)
    #  sys.exit()
  #return mp4s

def usage():
  print "this is not how the tool is used"

def main():
  if( len(sys.argv) < 3 ):
    print "usage: <first mp4 to concat> <2nd mp4 to concat>....<output filename>"
    sys.exit()
  mp4s = sys.argv[1:]
  output = mp4s.pop(-1)

  print "provided arguments are :" + " ".join(mp4s)
  print "output is " + output

  concat_mp4s(mp4s, output)

if __name__ == '__main__':
  main()
