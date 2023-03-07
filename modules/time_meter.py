from datetime import datetime

from loguru import logger


def time_meter(func):
    def nested(*args, **kwargs):
        ini_time = datetime.now()
        result = func(*args, **kwargs)

        fin_time = datetime.now()
        tot_time = fin_time - ini_time

        logger.debug(
            f"A função {func.__name__} levou \
{tot_time.total_seconds():.0f}s para acabar"
        )
        return result

    return nested
