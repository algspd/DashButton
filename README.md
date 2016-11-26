# DashButton
Some simple scripts to trigger events with your Dash button

This code is intended to trigger an action when a Dash button is pushed, without having to break the Dash button (it cannot be opened and closed again without breaking the plastic seal). You will need a Dash button and a computer running linux (a raspberry pi or some similar board is ok)

## How it works?
When you push a Dash button, it connects to your WiFi network and generates some traffic. What this script does is to read that traffic, identifies the pushed button by its MAC address, and triggers the proper action.

## Installation
If you are running a debian based linux distribution, you can install dependencies simply by running:
```shell
apt-get update
apt-get install python python-scapy tcpdump
```
On other distributions, install equivalent packages.

## How to setup the Dash button
### Setup the physical button
First of all, setup your button by following Amazon instructions, but in the "Choose an Item" screen, just push back and exit the app. This will avoid buying an item each time you push the button. You may also want to disable Dash button notifications, or use an alternative account, to avoid getting a notification each time you push a button not associated with a product.

### Get the button MAC addres
Run "dash_detect.py", and just after running it, push the Dash button you want to detect. dash_detect will show you the Dash button MAC address.
```shell
# python dash_detect.py 
01:23:45:67:89:AB
```


### Setup the action
Edit the "dash_actions.py" file, and add a block similar to this, changing the MAC address with the one you got in the previous step.
```python
if pkt[Ether].src=="01:23:45:67:89:AB":
  print "Dash button pressed!"
```
You can duplicate the example blocks already written in the file
After that, you will have to add the mac address to the list in the "sniff" line. Just edit the example or add another "or ether src 01:23:45:67:89:AB" block

## Run it!
Run the "dash_actions.py" script, and check that the proper action runs after 2-3 seconds (depending on such a lot of things, maybe more seconds) for each button.
```shell
# python dash_actions.py 
Dash button pressed!
```

## The "fixme"
If you understand the code, you will see that it "sleeps" 3 seconds after a matching packet is found. It avoids launching each action several times when a button is pressed.
When you press the button, it wakes up, connects to the WiFi, sends several packets (some of them exactly the same) and goes again to sleep. Between the first and the last packet, tipically less then 3 seconds pass, but it can obviously fail.
I'm sure a safer way to do this can be found.
