#!/usr/bin/env python3
# coding: utf8

import logging
import time
import random

def test_procedure():
    logging.debug("Enter test_procedure()")

    time.sleep(0.5)
    result = random.random() # result receives a value between 0 and 1
    if result > 0.7:
        logging.error("something really bad happened")
    elif result > 0.3:
        logging.warning("something happened")
    else:
         logging.info("done")
       
    logging.debug("Leave test_procedure()")



def main():
    # could also specify to log to file, the format of the messages and much more. See https://docs.python.org/3/library/logging.html#logging.basicConfig
    # level is quite important because default log level is WARNING
    logging.basicConfig(level=logging.INFO, filename='log.log') 

    logging.info("Start of main")
    test_procedure()
    logging.info("End of main")


if __name__ == '__main__':    
    main()
