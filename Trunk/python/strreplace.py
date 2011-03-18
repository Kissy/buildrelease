

def constructSearchFilter(fullname):
    logging.error("This is one error!")
    logging.debug("This is one debug")
    logging.info("This is one info")
    fullname = fullname.replace('(','\(')
    fullname = fullname.replace(')', '\)')
    searchFilter = "displayName=%s" % fullname
    return searchFilter


import logging 
def setlogging(filename = '', level = logging.INFO):
  logging.basicConfig(filename = filename, filemode = 'a', level = level, format = '%(levelname)s: %(message)s')
  
setlogging()
print constructSearchFilter("Mike(jian)Zhang")