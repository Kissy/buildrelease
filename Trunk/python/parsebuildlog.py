import re

warninglist = []
warninglist.append("warning C\d{4}")

errorlist = []
errorlist.append("error LNK\d{4}")
errorlist.append("error C\d{4}")

def Parse(logfile, regexlist):
  resultlines = []
  with open(logfile, "r") as log:
    for line in log:
      for regex in regexlist:
        m = re.search(regex, line)
        if m:
          resultlines.append(line)
  return resultlines

def ParseWarning(logfile):
  warnings = []
  warnings = Parse(logfile, warninglist)
  return warnings
  
def ParseError(logfile):
  errors = []
  errors = Parse(logfile, errorlist)
  return errors

def TestParseBuildlog():
ws = ParseWarning("buildlog.txt")
    print( "warnings:" + str(len(ws)))
    for w in ws:
      print (w)
    es = ParseError("buildlog.txt")
    print( "errors:" + str(len(es)))
    for e in es:
      print(e)
