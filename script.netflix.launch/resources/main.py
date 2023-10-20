import os
import sys
import subprocess
import time
import shutil
import stat
import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
import xbmcvfs

osWin = xbmc.getCondVisibility('system.platform.windows')

installdir = xbmcaddon.Addon().getSetting("installdir")

url = 'netflix:/app'

if osWin:
    # ___ Open the url with the default web browser
    #xbmc.executebuiltin("System.Exec(cmd.exe /c start "+url+")")
    xbmc.executebuiltin('System.Exec(cmd.exe /c title Managing Netflix app and Kodi... && taskkill /im kodi.exe && start /w '+url+' && start "" "'+installdir+'")')