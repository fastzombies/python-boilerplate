import logging


def module1_function1():
    l = logging.getLogger()
    l.debug('module1')
    l.info('module1')
    #logger.warning('module1')
    #logger.error('module1')
    #logger.critical('module1')
    #logger.fatal('module1')
    print('module1_function1 plain print\n')
