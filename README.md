# ClearNet
ClearNet it's a program that allows you to change your IP address using the Tor network.
tested on Kali Linux and Termux 
don't forget to check your browser settings
your browser must have a manual connection configured with 127.0.0.1 IP and port 9050, socks5 must also be enabled
According to the standard, the program changes your IP every few seconds, but since this is just a test of the pen, more flexible settings will be added in future versions
For the program to work, the requests, colorama, stem libraries are required
how to install?
git clone https://github.com/Zen5ex/ClearNet/ 
cd ClearNet/
python3 ClearNet.py
