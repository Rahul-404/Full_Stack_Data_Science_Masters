import logging


logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = logger.FileHandler("logs/my_log.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)