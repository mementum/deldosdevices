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
import datetime
from utils.mvc import PubRecv
from utils.wxfb import WGroup, WButton, WMenuItem, WTool
import itertools
import wx

if True:

    def __init__(self, *args, **kwargs):
        # Operating System Details for column sizes
        winDC = wx.ClientDC(self)
        self.font = wx.Font(8, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        # Change the font
        self.m_textCtrlLog.SetFont(self.font)
        self.m_listCtrlDosDevices.SetFont(self.font)

        colwins = [('Drive', 8), ('Kernel Name', 80),]
        for icol, colitem in enumerate(colwins):
            colname, colwidth = colitem
            self.m_listCtrlDosDevices.InsertColumn(icol, colname)
            if not colwidth:
                colwidth = len(colname) + 1
            colwidth, colheight = winDC.GetTextExtent( 'a' * colwidth)
            self.m_listCtrlDosDevices.SetColumnWidth(icol, colwidth)


        WGroup('deletegroup', False) << WButton('DeleteSelected') << WTool('Delete') << WMenuItem('Delete')

if True:
    def ClearLog(self):
        self.m_textCtrlLog.Clear()

    def LogMsg(self, msg):
        dt = datetime.datetime.now()
        msg = dt.strftime('%Y-%m-%d %H:%M:%S') + ' - ' + msg + '\n'
        self.m_textCtrlLog.AppendText(msg)

if True:
    def GetSelectedDrives(self, data=False, dosdevice=False, colon=False):
        selected = list()
        item = self.m_listCtrlDosDevices.GetFirstSelected()
        while item != wx.NOT_FOUND:
            if data or dosdevice:
                itemdata = self.m_listCtrlDosDevices.GetItemData(item)
                if dosdevice:
                    itemdata = chr(itemdata)
                    if colon:
                        itemdata += ':'
                selected.append(itemdata)
            else:
                selected.append(item)
            item = self.m_listCtrlDosDevices.GetNextSelected(item)

        return selected

if True:
    @PubRecv('model.dosdevices.refresh')
    def OnModelDosDevicesRefresh(self, dosdevices):
        selected = self.GetSelectedDrives(data=True)
        self.m_listCtrlDosDevices.DeleteAllItems()

        toselect = list()
        for idx, dosdevice in enumerate(sorted(dosdevices.keys())):
            error, path = dosdevices[dosdevice]
            if error:
                self.LogMsg(dosdevice + ' ' + str(error))
            if not path and not self.emptydriveletters.value:
                continue

            if self.skipfloppys.value:
                if dosdevice.lower() in ['a:', 'b:',]:
                    continue

            col = itertools.count(1)
            displaydrive = dosdevice
            if self.capitaldriveletters.value:
                displaydrive = displaydrive.upper()
            newidx = self.m_listCtrlDosDevices.InsertStringItem(idx, displaydrive)

            self.m_listCtrlDosDevices.SetStringItem(newidx, col.next(), path)
            itemdata = ord(dosdevice[0])
            self.m_listCtrlDosDevices.SetItemData(newidx, itemdata)

            if itemdata in selected:
                toselect.append(newidx)

        if not toselect:
            self.deletegroup.disable()
        else:
            for item in toselect:
                self.m_listCtrlDosDevices.Select(item)

        self.m_listCtrlDosDevices.SortListItemsLastState()

if True:
    @PubRecv('model.dosdevices.delete')
    def OnModelDosDevicesDelete(self, dosdevices):
        for dosdevice, retval in dosdevices:
            if not retval:
                self.LogMsg(dosdevice + ' - DefineDosDevice reports success for deletion')
                continue

            self.LogMsg(dosdevice + ' - DefineDosDevice reports error: ' + str(retval))

        self.model.RefreshDosDevices()
