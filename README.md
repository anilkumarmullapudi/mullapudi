This repository contains automation scripts and a Flask-based web application that help validate large server inventories efficiently. 
By leveraging Paramiko for SSH connections, the app executes Unix health check commands such as uptime and uname -a across multiple servers, then displays the results in a web interface with color-coded feedback. 
It also saves outputs into an Excel file (data.xlsx) using Pandas and XlsxWriter,
which can be downloaded for offline analysis, making it a practical tool for DevOps and SRE teams managing large infrastructures.

The documentation explains how to set up the environment, install dependencies, and run the application, while also highlighting security considerations like avoiding hardcoded credentials and using secure authentication in production. Example workflows demonstrate how to input server lists, run commands, and retrieve results, and future enhancements include support for more commands, parallel execution, and improved UI. Overall, the repo combines automation and monitoring into a single platform that simplifies health validation across large inventories
