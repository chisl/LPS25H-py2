#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LPS25H: 260-1260 hPa absolute digital output barometer"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	REF_P = 8
	WHO_AM_I = 15
	RES_CONF = 16
	CTRL_REG1 = 32
	CTRL_REG2 = 33
	CTRL_REG3 = 34
	CTRL_REG4 = 35
	INTERRUPT_CFG = 36
	INT_SOURCE = 37
	STATUS_REG = 39
	PRESS_OUT = 40
	TEMP_OUT = 43
	FIFO_CTRL = 46
	FIFO_STATUS = 47
	THS_P = 48
	RPDS = 57
