
def TestLogBasic():
    import logging
    logging.basicConfig(filename = 'log.txt', filemode = 'a', level = logging.DEBUG,format = '%(asctime)s - %(levelname)s: %(message)s')
    logging.debug('this is a message')
    logging.error("this is a error")
    logging.info("this is a info")
    logging.warn("this is a warnning")
    logging.critical("this is a critical issue")
    try:
      raise Exception('this is a exception')
    except:
      logging.exception('exception')


TestLogBasic()
