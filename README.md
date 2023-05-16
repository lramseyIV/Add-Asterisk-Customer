# Add-Asterisk-Customer
This script given a yaml file will create asterisk configurations. 

### Using the script
in sip_add.py there is a variable 'base_dir' which you should change to the absolute path where you want your customers directory.
This script is simply run the script in the same directory as your template configuration files and where you would like your actual customer configurations to go.
This was intended to be ran inside of an ansible directory so feel free to manipulate the script's paths as you see fit.

### Features
Following the format of the yaml file you will add new customers there. Last name, phone number, and secret.
Note this will only make changes for new customers. This script will not re-make any directories and configurations that already exist. 
