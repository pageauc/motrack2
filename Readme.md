# motrack2
#### Uses python3 and opencv to Track Largest moving object in camera view using picamera2 libcam, legacy picamera, RTSP IP cam stream or USB Webcam

## Introduction
This is just some demo code to test motion tracking using python picamera2 libcam, picamera legacy Camera,  rtsp IP camera or USB Webcam.
On completion of a successful track an image is saved in ./media/images
Optional tracking history can be displayed on images as contour center point circles or contour rectangles.
Images can be viewed on web browser via provided webserver.py run in foreground or background. 
Program user settings are saved in the config.py file.

## Install or Upgrade
***IMPORTANT*** - Update Raspberry Pi Operating System To ensure your system is up-to-date.
In SSH or Terminal Session run commands below.

    sudo apt update
    sudo apt upgrade -y

#### Step 1
Select copy icon on right of Github command box below  
or Alternatively with mouse left button highlight curl command in code box below. Right click mouse in **highlighted** area and Copy.     

    curl -L https://raw.github.com/pageauc/motrack2/master/install.sh | bash

#### Step 2
On RPI putty SSH or Terminal session, right click, select paste then Enter to download and run install.sh script.

***NOTE*** If config.py exists it will Not be overwritten. A config.py.new will be created/updated instead.
To update existing config.py perform commands below

    cd ~/motrack2
    cp config.py config.py.bak
    cp config.py.new config.py

## Edit Settings
To review and/or change settings execute command below in SSH or terminal session.
See comments for each variable setting. Ensure camera is installed and working.

    cd ~/motrack2
    nano config.py

To exit nano and save changes press

    ctrl-x y

## Run motrack2
  Open putty SSH or Terminal session then execute command below.

    cd ~/motrack2
    ./motrack2.py

If camera is working motion tracking logging information will be displayed.

## WebServer
Webserver.py will display saved motrack images from any network device using a web browser.

#### Foreground
To Run in Foreground open a new SSH or Terminal Session then execute command below.

    ./webserver.py

NOTE browser URL:PORT for accessing MoTrack web page will be displayed.  ctrl-c exits.

#### Background
To Run in Background execute command below in current SSH or Terminal Session. 
Then execute motrack.py in same terminal session per above.

    ./webserver.sh start

Access webserver with a web browser at provided URL and port  eg http://192.168.1.128:8090 or http://rpiname.local:8090

## More Info See

    https://github.com/pageauc/motrack2


Regards Claude....
