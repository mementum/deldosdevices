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
from uimods.aboutdialog import AboutDialog
from utils.mvc import DynBind
import wx

if True:
    @DynBind.EVT_CHECKBOX.CheckBox.SkipFloppys
    @DynBind.EVT_CHECKBOX.CheckBox.CapitalDriveLetters
    @DynBind.EVT_CHECKBOX.CheckBox.EmptyDriveLetters
    @DynBind.EVT_TOOL.Tool.Refresh
    @DynBind.EVT_BUTTON.Button.Refresh
    def OnEventRefreshDosDevices(self, event):
        event.Skip()
        self.model.RefreshDosDevices()

if True:
    @DynBind.EVT_MENU.MenuItem.Delete
    @DynBind.EVT_BUTTON.Button.DeleteSelected
    @DynBind.EVT_TOOL.Tool.Delete
    def OnEventDelete(self, event):
        event.Skip()

        # Get Selection - We are active ... thus ... something is selected
        drives = self.view.GetSelectedDrives(dosdevice=True, colon=True)
        if not drives:
            return

        warnmsg = '\
        You are about to delete the following drive(s):\n\n\
        %s\n\n\
        Are you sure?' % ', '.join(drives)

        retval = wx.MessageBox(warnmsg, 'Warning!', wx.YES_NO | wx.ICON_EXCLAMATION)
        if retval != wx.YES:
            return

        self.model.DeleteDosDevices(drives)
            
if True:
    @DynBind.EVT_TOOL.Tool.Exit
    @DynBind.EVT_BUTTON.Button.Exit
    @DynBind.EVT_MENU.MenuItem.Exit
    def OnEventExit(self, event):
        event.Skip()
        self.Close()

if True:
    @DynBind.EVT_BUTTON.Button.About
    @DynBind.EVT_MENU.MenuItem.About
    @DynBind.EVT_TOOL.Tool.About
    def OnEventAbout(self, event):
        event.Skip()
        dialog = AboutDialog(self)
        dialog.ShowModal()

if True:
    @DynBind.EVT_LIST_ITEM_SELECTED.ListCtrl.DosDevices
    def OnListCtrlItemSelected(self, event):
        event.Skip()
        self.deletegroup.enable()

if True:
    # @DynBind.EVT_TOOL.Tool.About
    # @DynBind.EVT_MENU.MenuItem.ClearLog
    @DynBind.EVT_BUTTON.Button.ClearLog
    def OnEventClerLog(self, event):
        event.Skip()
        self.view.ClearLog()
