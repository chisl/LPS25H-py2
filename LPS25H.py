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

from LPS25H_constants import *

# name:        LPS25H
# description: 260-1260 hPa absolute digital output barometer
# manuf:       STMicroelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/lps25h.pdf
# date:        2018-01-04


# Derive from this class and implement read and write
class LPS25H_Base:
	"""260-1260 hPa absolute digital output barometer"""
	# Register REF_P
	# 7.1-3
	#       Reference pressure
	#       The full reference pressure value is composed
	#       by REF_P_XL, REF_P_H & REF_P_L and is represented as 2’s complement. The
	#       reference pressure value can also be used to detect a measured pressure beyond
	#       programmed limits (see INT_CFD at 23h), and for Autozero function (see RESET_AZ
	#       bit, at 20h). 
	
	
	def setREF_P(self, val):
		"""Set register REF_P"""
		self.write(REG.REF_P, val, 24)
	
	def getREF_P(self):
		"""Get register REF_P"""
		return self.read(REG.REF_P, 24)
	
	# Bits REF_P
	# Register WHO_AM_I
	# 7.4
	#       Contains the device ID, BDh 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register RES_CONF
	# 7.5
	#       Pressure and temperature internal average configuration. 
	
	
	def setRES_CONF(self, val):
		"""Set register RES_CONF"""
		self.write(REG.RES_CONF, val, 8)
	
	def getRES_CONF(self):
		"""Get register RES_CONF"""
		return self.read(REG.RES_CONF, 8)
	
	# Bits reserved_0
	# Bits AVGT
	# select the pressure internal average. 
	# Bits AVGP
	# select the temperature internal average. 
	# Register CTRL_REG1
	# 7.6
	#       Control register 1. 
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits PD
	# Power-down control. 
	#           PD bit allows to turn on the device. The device is in power-down mode when PD = ‘0’ 
	#           (default value after boot). The device is active when PD is set to ‘1’. 
	
	# Bits ODR
	# ODR2- ODR1 - ODR0 bits allow to change the output data rates of pressure and temperature samples. 
	#           The default value is “000” which corresponds to “one shot configuration” for both pressure and 
	#           temperature output.  
	
	# Bits DIFF_EN
	# Interrupt circuit enable.
	#           The DIFF_EN bit is used to enable the computing of differential pressure output. 
	#           It is recommended to enable DIFF_EN after the configuration of REF_P_H (0Ah), 
	#           REF_P_L (09h), REF_P_XL (08h), THS_P_H (31h) and THS_P_L (30h). 
	
	# Bits BDU
	# Block data update. 
	#           BDU bit is used to inhibit the output registers update between the reading of upper and 
	#           lower register parts. In default mode (BDU = ‘0’), the lower and upper register parts are 
	#           updated continuously. If it is not sure to read faster than output data rate, it is 
	#           recommended to set BDU bit to ‘1’. In this way, after the reading of the lower (upper)
	#           register part, the content of that output registers is not updated until the upper (lower)
	#           part is read too.
	#           This feature avoids reading LSB and MSB related to different samples. 
	
	# Bits RESET_AZ
	# Reset AutoZero function. Reset REF_Preg, set pressure to default value in RPDS register (@0x39/A).
	#           RESET_AZ bit is used to Reset AutoZero function. Reset REF_P reg (@0x08..0A) set pressure 
	#           reference to default value RPDS reg (0x39/3A). RESET_AZ is self cleared. See AutoZero function. 
	
	# Bits SIM
	# SPI Serial Interface Mode selection. 
	# Register CTRL_REG2
	# 7.7
	#       Control register 2 
	
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	#           BOOT bit is used to refresh the content of the internal registers stored in the 
	#           Flash memory block. At the device power-up the content of the Flash memory block 
	#           is transferred to the internal registers related to trimming functions to permit 
	#           a good behavior of the device itself. If for any reason, the content of the trimming 
	#           registers is modified, it is sufficient to use this bit to restore the correct values. 
	#           When BOOT bit is set to ‘1’ the content of the internal Flash is copied inside the 
	#           corresponding internal registers and is used to calibrate the device. These values 
	#           are factory trimmed and they are different for every device. They permit good behavior 
	#           of the device and normally they should not be changed. At the end of the boot process 
	#           the BOOT bit is set again to ‘0’ by hardware. BOOT bit takes effect after one ODR 
	#           clock cycle. 
	
	# Bits FIFO_EN
	# FIFO enable. 
	# Bits WTM_EN
	# Enable FIFO Watermark level use. 
	# Bits FIFO_MEAN_DEC
	# Enable 1Hz ODR decimation
	#            
	
	# Bits reserved_0
	# Bits SWRESET
	# Software reset. 
	#           SWRESET is the software reset bit. The device is reset to the power on configuration 
	#           if the SWRESET bit is set to ‘1’ and BOOT is set to ‘1’. 
	
	# Bits AUTOZERO
	# Autozero enable. 
	#           AUTO_ZERO, when set to ‘1’, the actual pressure output is copied in the 
	#           REF_P_H & REF_P_L & REF_P_XL and kept as reference and the 
	#           PRESS_OUT_H & PRESS_OUT_L & PRESS _OUT_XL is the difference between this reference and 
	#           the pressure sensor value. 
	
	# Bits ONE_SHOT
	# One-shot enable. 
	#           ONE_SHOT bit is used to start a new conversion when ODR2..0 bits in CTRL_REG1 are set 
	#           to “000”. Write ‘1’ in ONE_SHOT to trigger a single measurement of pressure and temperature. 
	#           Once the measurement is done, ONE_SHOT bit will self-clear and the new data are available 
	#           in the output registers, and the STATUS_REG bits are updated. 
	
	# Register CTRL_REG3
	# 7.8
	#       Control register 3 - INT_DRDY pin control register 
	#       The device features one fully-programmable interrupt sources (INT1) that can be configured to 
	#       trigger different pressure events. Figure 12 shows the block diagram of the interrupt generation 
	#       block and output pressure data. 
	#       The device may also be configured to generate, through interrupt pins, a Data Ready signal (Drdy) 
	#       which indicates when a new measured pressure data is available, thus simplifying data synchronization 
	#       in digital systems or to optimize the system power consumption.
	#       See Fig. 12. 
	
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits INT_H_L
	# Interrupt active-high/low. 
	# Bits PP_OD
	# Push-pull/open drain selection on interrupt pads. 
	# Bits reserved_0
	# Bits INT_S
	# Data signal on INT1 pad control bits. 
	# Register CTRL_REG4
	# Interrupt configuration 
	
	def setCTRL_REG4(self, val):
		"""Set register CTRL_REG4"""
		self.write(REG.CTRL_REG4, val, 8)
	
	def getCTRL_REG4(self):
		"""Get register CTRL_REG4"""
		return self.read(REG.CTRL_REG4, 8)
	
	# Bits reserved_0
	# keep these bits at 0 
	# Bits P1_EMPTY
	# Empty signal on INT1 pin. 
	# Bits P1_WTM
	# Watermark signal on INT1 pin. 
	# Bits P1_OVERRUN
	# Overrun signal on INT1 pin. 
	# Bits P1_DRDY
	# Dataready signal on INT1 pin. 
	# Register INTERRUPT_CFG
	# 7.1
	#       Interrupt configuration 
	
	
	def setINTERRUPT_CFG(self, val):
		"""Set register INTERRUPT_CFG"""
		self.write(REG.INTERRUPT_CFG, val, 8)
	
	def getINTERRUPT_CFG(self):
		"""Get register INTERRUPT_CFG"""
		return self.read(REG.INTERRUPT_CFG, 8)
	
	# Bits reserved_0
	# Bits LIR
	# Latch interrupt request into INT_SOURCE register. 
	# Bits PLE
	# Enable interrupt generation on differential pressure low event. 
	# Bits PHE
	# Enable interrupt generation on differential pressure high event. 
	# Register INT_SOURCE
	# 7.15
	#       Interrupt source 
	#       INT_SOURCE register is cleared by reading it. 
	
	
	def setINT_SOURCE(self, val):
		"""Set register INT_SOURCE"""
		self.write(REG.INT_SOURCE, val, 8)
	
	def getINT_SOURCE(self):
		"""Get register INT_SOURCE"""
		return self.read(REG.INT_SOURCE, 8)
	
	# Bits reserved_0
	# keep these bits at 0. 
	# Bits IA
	# Interrupt active. 
	# Bits PL
	# Differential pressure Low. 
	# Bits PH
	# Differential pressure High. 
	# Register STATUS_REG
	# 7.12
	#       Status register. 
	#       This register is updated every ODR cycle, regardless of the BDU value in CTRL_REG1. 
	
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits reserved_0
	# Bits P_OR
	# Pressure data overrun. 
	#           P_OR bit is set to '1' whenever new pressure data is available and P_DA was set in 
	#           the previous ODR cycle and not cleared. P_OR is cleared when PRESS_OUT_H (2Ah) 
	#           register is read.
	
	# Bits T_OR
	# Temperature data overrun. 
	#           T_OR is set to ‘1’ whenever new temperature data is available and T_DA was set in the previous 
	#           ODR cycle and not cleared. T_OR is cleared when TEMP_OUT_H (2Ch) register is read.
	
	# Bits unused_1
	# Bits P_DA
	# Pressure data available. 
	#           P_DA is set to 1 whenever a new pressure sample is available. P_DA is cleared when 
	#           PRESS_OUT_H (2Ah) register is read.
	
	# Bits T_DA
	# Temperature data available. 
	#           T_DA is set to 1 whenever a new temperature sample is available. T_DA is cleared 
	#           when TEMP_OUT_H (2Ch) register is read.
	
	# Register PRESS_OUT
	# 7.13-15
	#       The PRESS_OUT_XL register contains the lowest part of the pressure output value, 
	#       that is the difference between the measured pressure and the reference pressure 
	#       (REF_P registers). See AUTOZERO bit in CTRL_REG2.
	#       The full reference pressure value is composed by PRESS_OUT_H/_L/_XL and is represented 
	#       as 2’s complement. Pressure Values exceeding the operating pressure Range (see Table 3) 
	#       are clipped.
	#       Pressure output data: Pout(hPa) = PRESS_OUT / 4096
	#       Example: P_OUT = 0x3ED000 LSB = 4116480 LSB = 4116480/4096 hPa= 1005 hPa Default value 
	#       is 0x2F800 = 760 hPa 
	
	
	def setPRESS_OUT(self, val):
		"""Set register PRESS_OUT"""
		self.write(REG.PRESS_OUT, val, 24)
	
	def getPRESS_OUT(self):
		"""Get register PRESS_OUT"""
		return self.read(REG.PRESS_OUT, 24)
	
	# Bits PRESS_OUT
	# Register TEMP_OUT
	# 7.16-17
	#       Temperature output value
	#       The TEMP_OUT_L register contains the low part of the temperature output value.
	#       Temperature data are expressed as TEMP_OUT_H & TEMP_OUT_L as 2’s complement numbers. 
	#       Temperature output data:
	#         T(°C) = 42.5 + (TEMP_OUT / 480)
	#         If TEMP_OUT = 0 LSB then Temperature is 42.5 °C 
	
	
	def setTEMP_OUT(self, val):
		"""Set register TEMP_OUT"""
		self.write(REG.TEMP_OUT, val, 8)
	
	def getTEMP_OUT(self):
		"""Get register TEMP_OUT"""
		return self.read(REG.TEMP_OUT, 8)
	
	# Bits TEMP_OUT
	# Register FIFO_CTRL
	# 7.18
	#       FIFO control register. The FIFO_CTRL registers allows to control the FIFO functionality.
	#      
	
	
	def setFIFO_CTRL(self, val):
		"""Set register FIFO_CTRL"""
		self.write(REG.FIFO_CTRL, val, 8)
	
	def getFIFO_CTRL(self):
		"""Get register FIFO_CTRL"""
		return self.read(REG.FIFO_CTRL, 8)
	
	# Bits F_MODE
	# FIFO mode selection. 
	#           FIFO_MEAN_MODE: The FIFO can be used for implementing a HW moving average on the pressure 
	#           measurements. The number of samples of the moving average can be 2, 4, 8, 16 or 32 samples, 
	#           by selecting the watermark levels as per Table 21. Different configuration are not 
	#           guaranteed. 
	#           When using the FIFO_MEAN_MODE it is not possible to access the FIFO. 
	
	# Bits WTM_POINT
	# FIFO threshold (watermark) level selection. 
	#           Please note that when using the FIFO Mean mode it is not possible to access the FIFO content. 
	
	# Register FIFO_STATUS
	# 7.19
	#       FIFO status 
	
	
	def setFIFO_STATUS(self, val):
		"""Set register FIFO_STATUS"""
		self.write(REG.FIFO_STATUS, val, 8)
	
	def getFIFO_STATUS(self):
		"""Get register FIFO_STATUS"""
		return self.read(REG.FIFO_STATUS, 8)
	
	# Bits WTM_FIFO
	# Watermark status. 
	# Bits FULL_FIFO
	# Overrun bit status. 
	# Bits EMPTY_FIFO
	# Empty FIFO bit. 
	# Bits DIFF_POINT
	# FIFO stored data level. 
	# Register THS_P
	# 7.20-21 
	#         Threshold value for pressure interrupt generation.
	#         The complete threshold value is given by THS_P and is expressed as unsigned number.
	#           P_ths (hPa) = (THS_P)/16. 
	
	
	def setTHS_P(self, val):
		"""Set register THS_P"""
		self.write(REG.THS_P, val, 16)
	
	def getTHS_P(self):
		"""Get register THS_P"""
		return self.read(REG.THS_P, 16)
	
	# Bits THS
	# Refer to Section 10.2: "THS_P_L (0Ch)" 
	# Register RPDS
	# 7.22-23
	#       Pressure offset.
	#       This register contains the pressure offset value after soldering,for differential pressure computing. 
	#       The value is expressed as signed 2 complement value. 
	
	
	def setRPDS(self, val):
		"""Set register RPDS"""
		self.write(REG.RPDS, val, 16)
	
	def getRPDS(self):
		"""Get register RPDS"""
		return self.read(REG.RPDS, 16)
	
	# Bits RPDS
