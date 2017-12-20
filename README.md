# FlaskRESTful

*This is a Simple Flask server that hands out JSON objects in RESTful scheme, **deployed as a WinService**.*

## Information

I created this script to give information about my PC, for instance: CPU percentage.<br/>
Then, a specific net_addr can access this through my domain: ```http://DOMAIN.me:PORT/computer_info```<br/>
Also, this doesn't use any kind of DB or library to support RESTful protocol due to simplicity.


## Installation:



### Windows:

   Highly recommend NSSM: `https://nssm.cc/credits`
   
   Steps:
   1. Download NSSM from here(it's under 'Latest release'): `https://nssm.cc/download  `
   2. Unzip it anywhere you'd like  
   3. Open CMD  
   4. Navigate to that directory, mine is at: `E:\nssm-2.24\ ` 
   5. Write: `nssm.exe install "YOUR_SERVICE_NAME" `
   6. GUI opened, from there it is self-explantory, honestly.



### Linux (Optional):
Linux's *systemd* is the simplest easiest solution.  
**Note: you have to change `disk_usuage_percent` in `restful_flask.py` to the directory you want.  
Also, I did not intend to run it linux, you might need to tweak `restful_flask.py` if anything happens.**

   Steps:
   1. Create a configuration file for systemd:  
   
		 	sudo nano /lib/systemd/system/restful_flask.service

   2. Type inside (and edit accordingly, please) and save:
   
		  [Unit]
		  Description=Simple Flask server designed in the most simple way of RESTful API, to hand out information.
		  After=multi-user.target

		  [Service]
		  Type=idle
		  User=YOUR_USER
		  ExecStart=/usr/bin/python /home/YOU_USER/restful_flask.py

		  [Install]
		  WantedBy=multi-user.target
			
   3. Run the following commands:
   
		 	sudo systemctl daemon-reload
			sudo systemctl enable restful_flask.service
			sudo reboot
			
   4. After the reboot you should be up and running, check service status:
   
   		 	sudo systemctl status restful_flask.service
   	

   

