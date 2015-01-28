# snickerdoodle
A Python Spotify Power Hour App

To install dependencies on Fedora 21, run the following commands as root:
yum install python
yum install python-pip
yum install pygame
yum localinstall --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
yum -y install libspotify-devel
yum -y install python-devel
pip install --pre pyspotify
yum install pyaudio

Make sure you add a Spotify API key named "spotify_appkey.key" to the top directory, then simply run snikcerdodole.py with Python.
