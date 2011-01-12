

def TestSys():
  import sys
  for arg in sys.argv[1:]:
    print (arg)


def TestGetOpt():
  import sys
  import getopt
  try:
    opts, args = getopt.getopt(sys.argv[1:],'d:f:h',['days=','files=','help'])
  except getopt.GetoptError:
     usage()
     sys.exit()

  print (opts)
  print (args)
  for o, a in opts:
     if o in ("-h", "--help"):
         usage()
         sys.exit()
     elif o in ("-d", "--days"):
         day = a
     elif o in ("-f", "--files"):
         files = a
  print (day)
  print (files)


def TestOprse():
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
  parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
  (options, args) = parser.parse_args()
  print (options.filename)
  print (options.verbose)
  print (args)

  
if __name__=="__main__":
  #print("the arguments will like: -d 7 -f files.txt c:\backup")
  #TestSys()
  #TestGetOpt()
  TestOprse()
   