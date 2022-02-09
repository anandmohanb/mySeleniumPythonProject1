# import logging
#
# def test_logging():
#     logger = logging.getLogger(__name__)
#
#     fileHandler = logging.FileHandler('myLogFile.log')
#     myFormatter = fileHandler.formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#     fileHandler.setFormatter(myFormatter)
#     logger.addHandler(fileHandler)
#
#     logger.setLevel(logging.INFO)
#
#     logger.debug("This is my debug message")
#     logger.info("This is my info message")
#     logger.warning("This is my error message")
#     logger.error("This is my error message")
#     logger.critical("This is my critical message")


import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")