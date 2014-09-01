deldosdevices
=============

Needs to run as Admin (UAC Prompt)

The application graphically presents the list of "DosDevices"
via QueryDosDevice (from a to z)

Additionally and in case a DosDevice definition has been left
behind, it can be deleted (this happens with applications like
Ext2Mgr)

Inspired by the command line application by Uwe Sieber deletedosdevice

  - http://www.uwe-sieber.de/drivetools_e.html

Just felt like making it visual and open source

Developed with the following things (list not comprehensive)

  - WinPython to get most of Python 2.7+ and modules (like PyWin32)
  - Python 2.7+
  - wxPython 3.0.0
  - Cygwin (shell)
  - Emacs (editor)
  - Pyinstaller (executable generation)
  - Innosetup (setup generation)

Developed using my pseudo-mvc framework and wxPython basis:
  - wxskeletonapp