#!/usr/bin/env python

#import struct
#from cStringIO import StringIO

##################################################
# main
##################################################

def convert(flvs, outputDir=None):
  assert flvs, 'no flv input file found'
  import os.path
  #if not output:
  #  output = guess_output(flvs)
  #elif os.path.isdir(output):
  #  output = os.path.join(output, guess_output(flvs))
  mp4s = []
  for flv in flvs:
    output = flv + '.mp4'
    mp4s.append(output)
    #print 'Joining %s into %s' % (', '.join(flvs), output)
  for i,flv in enumerate(flvs):
    mp4 = mp4s[i]
    print 'converting %s into %s' % (flv,mp4)
    #Until we have a reliable ffmpeg wrapper, just make system call to ffmpeg
    #note the -y option automatically overwrites existing output files
    #and the 
    if( os.system("ffmpeg -i \'%s\' -y -acodec copy -vcodec copy \'%s\'"%(flv,mp4)) ):
      print "could not successfully convert % into %. Exiting"%(flv,mp4)
      sys.exit()
  return mp4s 

def main():
  import sys, getopt
  try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
  except getopt.GetoptError, err:
    usage()
    sys.exit(1)
  output = None
  for o, a in opts:
    if o in ("-h", "--help"):
      usage()
      sys.exit()
    elif o in ("-o", "--output"):
      output = a
    else:
      usage()
      sys.exit(1)
  if not args:
    usage()
    sys.exit(1)

  convert(args, output)

if __name__ == '__main__':
  main()
