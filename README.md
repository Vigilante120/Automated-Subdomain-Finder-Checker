Automated Subdomain Finder and Checker

This script automates the process of discovering subdomains using Subfinder and checking their availability with Httpx. It streamlines the workflow by allowing users to input a target domain and quickly retrieve live subdomains.

Requirements
Python 3.x installed on your system.
Subfinder: A tool for finding subdomains.
Httpx: A fast HTTP toolkit for checking the status of URLs.

Setup Instructions
Install Subfinder and Httpx:
Follow the installation instructions from their respective GitHub repositories:
Subfinder
Httpx

Download the Script:
Place the provided Python script in the directory where you want the results to be saved.

How to Run the Script
Open your terminal.
Navigate to the folder containing the script.
Execute the following command:
bash
python3 main.py
When prompted, enter the target URL in this format: google.com

Script Functionality

Subfinder: The script first runs Subfinder to identify potential subdomains of the entered URL, saving them to subdomains.txt.

Httpx: It then utilizes Httpx to check which of those subdomains are alive, outputting the results to alive_subdomains.txt. The script uses 10 threads for faster processing.
Output Files

OUTPUT
subdomains.txt: Contains all discovered subdomains.
alive_subdomains.txt: Lists only those subdomains that are currently reachable.
Notes

Disclaimer 
Ensure you have proper permissions and ethical considerations in mind when scanning domains.
Adjust thread count in Httpx as needed for performance optimization.
Feel free to adjust any part of this documentation to better fit your style or specific requirements!
