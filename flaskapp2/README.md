# Unix Health Check Web Application

A simple Flask-based web platform that allows users to execute Unix commands (like `uptime`, `uname -a`) on multiple servers via SSH and download the results in Excel format.

---
## Features
- Web interface to select Unix commands and target servers.
- Executes commands remotely using **Paramiko (SSH)**.
- Displays results on the web page with color-coded flash messages.
- Saves results into an **Excel file (`data.xlsx`)** using **Pandas + XlsxWriter**.
- Provides a **download option** for the generated Excel file.

