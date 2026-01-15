#
# Copyright (c) 2025 ACOAUTO Team.
# All rights reserved.
#
# Detailed license information can be found in the LICENSE file.
#
# File: __init__.py Vehicle SOA module.
#
# Author: Han.hui <hanhui@acoinfo.com>
#

# Parser
from . import parser

# All sub-modules
from .timer import *
from .events import *
from .server import *
from .client import *
from .position import *
from .interface import *
from .workqueue import *

# Method
METHOD_GET = 0
METHOD_SET = 1

# Version
__version__ = '0.9.0'

# end
