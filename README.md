# Scan-O-Matik
##### by @wocsor
## Introducing the amazing *SCAN-O-MATIK*!
This amazing program is able to display images from a folder named after the hostname (set in etc/hostname) according to a scanned filename. It is written in Python 3 for easy portability and modifications. It is particularly useful for displaying items such as work instructions on an assembly line where little to no user interaction and a cheap embedded deployment is rquired.


## PREREQUISITES:

+ PiBakery
+ Set up internet connection sharing to Pi Ethernet Gadget in Control Panel
+ PuTTy (in case something goes wrong)
+ Angry IP Scanner (IP will be 192.168.137.x)
+ RealVNC Viewer


## HOW IT WORKS: 

The hostname of the Pi determines what folder the image is pulled from. Simply edit both files in the "boot/etc/" folder and replace the entry with the folder name you wish to pull from. Edit the Python Script in the "boot/home/pi/" folder to reflect the path of the folder you want to pull images from.

After editing the host files, use PiBakery to import the XML file with the OS Setup instructions (recipe.xml) and edit the contents of the blocks to your specifications (automount SMB share, set password, etc) amking sure to leave in the "install package" blocks as these are required to run scan-o-matik correctly. Write the OS to an SD card. After writing a drive named "boot" should appear. Copy the contents of the "boot" folder to the drive named "boot" and plug the pi into your PC using the middle (USB) port. In Control Panel, ensure you have shared your Internet Connection to the USB RNDIS (Pi Ethernet Gadget) Connection. The Pi will now install all the required software and will be set to autoboot scan-o-matik using the parameters we set earlier. When the LED on the pi goes out or begins flashing at a steady pace (shutdown), you'll know it is ready and the script has finished. 

## VERIFICATION:

Verification of scan-o-matik is simple. To begin, plug the USB gadget into the PC using the middle USB port of the Pi. Load up Angry IP Scanner and set the IP range to 192.168.137.1 - 254. The Pi will be the only other host alive. Enter this IP into RealVNC. The credentials to login are set from PiBakery (default raspberry). Once in, you can test by entering a filename that's been saved into the correct folder, and a picture should load. If not, move on to the debug phase.

## DEBUGGING:

When debugging, always be sure to plug the pi into a desktop through the USB gadget port (middle port.)

+ Pi does not show up in Network 
	- verify that the Pi is working correctly. Burn the image using PiBakery and ensure that you have copied the files in the boot folder to the root of the boot drive. Overwrite the two conflicting files and ensure that "config.txt" contains "dtoverlay=dwc2" and that "cmdline.txt" contains "modules-load=dwc2,g_ether" after "rootwait."
+ Desktop loads, but no Scn-O-MATIK
	- Open a terminal once you have logged in through VNC. Run "python3 scan-o-matik.py" and observe the output.
+ Scan-O-Matik is not loading any images
	- Open a Terminal and run "sudo mount -a" and observe the output. Ensure there is network connectivity (WiFi via "Warehouse" network) to mount the Windows share on metcamfps01. If these options change, PiBakery and scan-o-matik.py must be updated to reflect the changes.
