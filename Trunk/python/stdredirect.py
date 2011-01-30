import sys

def stdoutToFile(filename, function, args ):
    oldStdout = sys.stdout
    f = open(filename, "w" )
    sys.stdout = f 
    function(args)
    #sys.stdout.flush()
    #f.close()
    sys.stdout = oldStdout


if __name__=='__main__':
  print("modules")
  stdoutToFile("modules.txt", help, "modules")
  print("builtins")
  stdoutToFile("builtins.txt", help, "builtins")
  print("keywords")
  stdoutToFile("keyword.txt", help, "keywords")

