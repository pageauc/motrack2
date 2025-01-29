#!/bin/bash
echo "motrack2 Install  written by Claude Pageau"
echo "INFO  : Create motrack Folders ..."
cd ~
mkdir -p motrack2
cd motrack2

echo "INFO  : Download Project Files ..."
wget -O motrack2.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/motrack2.py
wget -O webserver.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/webserver.py
wget -O webserver.sh -q --show-progress https://raw.github.com/pageauc/motrack2/master/webserver.sh

if [ -f config.py ]; then     # check if local file exists.
    wget -O config.py.new -q --show-progress https://raw.github.com/pageauc/motrack2/master/config.py
else
    wget -O config.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/config.py
fi


wget -O strmcam.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/strmcam.py
wget -O strmpilegcam.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/strmpilegcam.py
wget -O strmusbipcam.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/strmusbipcam.py
wget -O strmpilibcam.py -q --show-progress https://raw.github.com/pageauc/motrack2/master/strmpilibcam.py
wget -O Readme.md -q --show-progress https://raw.github.com/pageauc/motrack2/master/Readme.md

chmod +x motrack2.py webserver.py webserver.sh

echo "INFO  : Install Dependencies ...."
sudo apt install -yq python3-opencv
mkdir -p media
wget -O media/webserver.txt -q --show-progress https://raw.github.com/pageauc/motrack2/master/webserver.txt
echo "
                    INSTRUCTIONS
                    ============
How to Run
==========
In SSH or Terminal session
Edit config.py CAMERA and related settings
for RPI Legacy, Libcam or RTSP IP Camera per comments

    cd ~/motrack
    ./motrack2.py

EDIT SETTINGS
=============

    nano config.py

To exit and save settings. In nano press

    ctrl-x then y

RUN WEBSERVER
=============

Run Web in Foreground open a new terminal (Displays browser URL)

    ./webserver.py

Run in Background in existing terminal

    ./webserver.sh start

Access webserver with a web browser at URL per Foreground command.

Form More Info See https://github.com/pageauc/motrack2


