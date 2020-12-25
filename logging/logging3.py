import logging2, logging

logging.basicConfig()

log = logging.getLogger("Logging3")
log.setLevel(1)
log.info("Starting my app")
try:
        logging2.doIt()
except Exception as e:
        log.exception("There was a problem.")
log.info("Ending my app")

print("Done.")