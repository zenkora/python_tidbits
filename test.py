import os
from sys import argv

import _mod_config as config

###############################################################################
# Begin per-program config
###############################################################################
py2_gtfo = True
unix_check = False
###############################################################################
# End per-program config
###############################################################################

if __name__ == '__main__':
    config.sanity_check()
