#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
#  Copyright (C) 2014 Daniel Rodriguez
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from utils.mvc import DynamicClass, PubSend

import pywintypes
import win32api
import win32con
import win32file

@DynamicClass(moddirs=['modules',])
class MainModel(object):

    FIRSTDRIVE = 'a'
    LASTDRIVE = 'z'

    def __init__(self):
        pass

    @PubSend('model.dosdevices.refresh')
    def RefreshDosDevices(self):
        dosdevices = dict()
        atoz = xrange(ord(self.FIRSTDRIVE), ord(self.LASTDRIVE) + 1)
        for device in atoz:
            dosdevice = chr(device) + ':'
            try:
                path = win32file.QueryDosDevice(dosdevice)
                e = None
            except pywintypes.error, error:
                path = ''
                e = error[2] # Return only error description
            
            dosdevices[dosdevice] = (e, path)

        return dosdevices

    @PubSend('model.dosdevices.delete')
    def DeleteDosDevices(self, dosdevices):
        retvals = list()
        for dosdevice in dosdevices:
            try:
                retval = None
                ret = win32file.DefineDosDevice(win32con.DDD_RAW_TARGET_PATH, dosdevice, '')
                # DDD_REMOVE_DEFINITION has proven to not work
                # This alternative doesn't seem to do the full job
                # ret = win32file.DeleteVolumeMountPoint(dosdevice + '\\')
            except pywintypes.error, error:
                retval = error[2] # Return only error description
            else:
                if not ret:
                    retval = win32api.FormatMessage(0) # GetLastError will be called internally
            retvals.append((dosdevice, retval))

        return retvals
