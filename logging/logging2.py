import logging
log = logging.getLogger("Logging2")
log.setLevel(1)

def doIt():
        log.debug("Doing stuff...")
        #do stuff...
        raise TypeError("Bogus type error for testing")