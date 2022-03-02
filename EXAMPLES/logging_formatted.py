#!/usr/bin/env python

import logging

logging.basicConfig(
    format='%(name)s:%(asctime)s:%(levelname)s:%(message)s', # <1>
    filename='../TEMP/formatted.log',
    level=logging.ERROR,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.critical("this is critical")
