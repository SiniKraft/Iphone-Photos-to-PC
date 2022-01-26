# Iphone-Photos-to-PC
Extract photos from unencrypted iTunes backup of iPhone  
## But, How ???
Simply open terminal/cmd in the backup folder (the one you can find Manifest.db)  
On windows, the folder is like %AppData%\Apple Computer\MobileSync\Backup\<random-uuid>-<date>\  
Remember : the backup MUST NOT BE ENCRYPTED  
To make backup, open iTunes  
Connect your iphone via usb
Click on the small Phone icon on the top left corner  
In Saves, click save now.
Once finished, in the terminal run python iphone-to-pc-photo-extractor.py  
or python3 if on macOS.
Good luck !
