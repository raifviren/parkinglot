from __future__ import absolute_import

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

logger.info('I told you so')
__all__ = (logger)
