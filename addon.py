import xbmcgui
import xbmc
from subprocess import check_output

ret = xbmcgui.Dialog().yesno("speedtest", "Run a speedtest?")

if ret == True:
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	try:
		out = check_output(["speedtest-cli", "--simple", "--share"])
		ping,up,down,share = out.splitlines()
		xbmcgui.Dialog().ok("speedtest", ping, up, down)
	except:
		xbmcgui.Dialog().ok("speedtest", "Error occured running speedtest, please try again")
	else:
		xbmc.executebuiltin("Dialog.Close(busydialog)")
