

def TestLogBasic():
    import logging 
    logging.basicConfig(filename = 'log.txt', filemode = 'a', level = logging.NOTSET, datefmt='%a, %d %b %Y %H:%M:%S', format = '%(asctime)s - %(levelname)-8s: %(message)s')
    logging.debug('this is a message')
    logging.info("this is a info")
    logging.disable(30)#logging.WARNING
    logging.warning("this is a warnning")
    logging.critical("this is a critical issue")
    logging.error("this is a error")
    logging.addLevelName(88,"MyCustomError")
    logging.log(88,"this is an my custom error")
    try:
      raise Exception('this is a exception')
    except:
      logging.exception( 'exception')
    logging.shutdown()

#TestLogBasic()
#logging level 
#logging.NOTSET 0
#logging.DEBUG 10
#logging.INFO 20
#logging.WARNING 30 
#logging.ERROR 40 
#logging.CRITICAL 50

def TestHanderAndFormat():
    import logging
    logger = logging.getLogger("simple")
    logger.setLevel(logging.DEBUG)
    
    # create file handler which logs even debug messages
    fh = logging.FileHandler("simple.log")
    fh.setLevel(logging.DEBUG)
    
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    # "application" code
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")

#TestHanderAndFormat()

def TestRotating():
    import glob
    import logging
    import logging.handlers
    
    LOG_FILENAME = 'logging_rotatingfile_example.out'

    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5)

    my_logger.addHandler(handler)

    # Log some messages
    for i in range(20):
        my_logger.debug('i = %d' % i)

    # See what files are created
    logfiles = glob.glob('%s*' % LOG_FILENAME)

    for filename in logfiles:
        print(filename)
        
TestRotating()
