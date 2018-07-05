# Scan-O-Matik
##### by @wocsor
## Introducing the amazing ~SCAN-O-MATIK~!
This amazing program is able to pull images from "\\metcamfps01\public$\Paint Display\" according to the display number and scanned part number. It is written in Python 3 for easy portability and modifications.


## PREREQUISITES:

+ PiBakery
+ Set up internet connection sharing to Pi Ethernet Gadget in Control Panel
+ PuTTy (in case something goes wrong)
+ Angry IP Scanner (IP will be 192.168.137.x)
+ RealVNC Viewer


## HOW IT WORKS: 

The hostname of the Pi determines what folder the instruction is pulled from. Simply edit both files in etc and replace the entry with the folder name you wish to pull from. The folders should correspond with the number of the monitor the instructions will be displayed at.

After editing the host files, use PiBakery to import the XML file with the OS Setup instructions (recipe.xml) and write the OS to an SD card. After writing a drive named "boot" should appear. Copy the contents of the boot folder to the boot drive and plug the pi into your PC using the middle (USB) port. It will now install all the required software and setup the pi to autoboot scan-o-matik using the parameters we set earlier. When the LED on the pi goes out, you'll know it is ready and the script has finished. Once verified working, deploy on the shop floor and you'll be right as rain! 

## VERIFICATION:

Verification of scan-o-matik is simple. To begin, plug the USB gadget into the PC using the middle USB port of the Pi. Load up Angry IP Scanner and set the IP range to 192.168.137.1 - 254. The Pi will be the only other host alive. Enter this IP into RealVNC. The credentials to login are stored in KeePass. Once in, you can test by entering a part number that's been saved into the correct folder, and a picture should load. If not, move on to the debug phase.

## DEBUGGING:

When debugging, always be sure to plug the pi into a desktop through the USB gadget port (middle port.)

+ Pi does not show up in Network 
	- verify that the Pi is working correctly. Burn the image using PiBakery and ensure that you have copied the files in the boot folder to the root of the boot drive. Overwrite the two conflicting files and ensure that "config.txt" contains "dtoverlay=dwc2" and that "cmdline.txt" contains "modules-load=dwc2,g_ether" after "rootwait."
+ Desktop loads, but no Scn-O-MATIK
	- Open a terminal once you have logged in through VNC. Run "python3 scan-o-matik.py" and observe the output.
+ Scan-O-Matik is not loading any images
	- Open a Terminal and run "sudo mount -a" and observe the output. Ensure there is network connectivity (WiFi via "Warehouse" network) to mount the Windows share on metcamfps01. If these options change, PiBakery and scan-o-matik.py must be updated to reflect the changes.
