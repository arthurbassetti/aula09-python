from loguru import logger


logger.add("logerrors.log")

def soma (x,y):

    logger.info(x)
    logger.info(y)
    logger.info(x+y)

    return x+y

soma(2,3)