from flask import Flask
from flask import Flask, redirect, url_for
from flask import Flask, request, send_file, render_template, flash
import paramiko
from paramiko.client import SSHClient
import os
import subprocess
import json, ast
from flask import Flask, session
from termcolor import colored
import pandas as pd
import xlsxwriter


app = Flask(__name__)
app.secret_key="filesystem"

@app.route('/unix_health_check', methods=['GET','POST'])
def unix_health_check():
                if request.method == 'POST':
                                cmd_option = request.form.get('Unix_commands')
                                on_this_servers = request.form.get('Servers_to_be_executed')
                                #li = on_this_servers.splitlines()
                                #print(li)
                                return redirect(url_for("unix_health", arg1 = cmd_option, arg2 = on_this_servers))
                else:
                                return render_template('unix_uptime.html')
@app.route("/unix_health")
def unix_health():
                cmd_option = request.args.get('arg1')
                on_this_servers = request.args.get('arg2')
                print(on_this_servers)
                li = on_this_servers.splitlines()
                print(li)
                username = "root"
                password = "root"
                list1 = []
                for host in li:
                        try:
                                client = paramiko.client.SSHClient()
                                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                client.connect(host, username=username, password=password)
                                stdin, stdout, stderr = client.exec_command("uptime")
                                uptime_output = stdout.readlines()
                                writer = pd.ExcelWriter('data.xlsx')
                                new_df = pd.DataFrame({'Server_Names': host, 'Result': uptime_output}, index=[0])
                                new_df.to_excel(writer)
                                writer.close()
                                flash(colored(uptime_output, 'green'))
                        except:
                                flash(colored(host+" --> "+"server not connecting", 'red'))
                return render_template('output.html')
@app.route("/download_file")
def download_file():
        p = 'data.xlsx'
        return send_file(p,as_attachment=True)

if __name__ == "__main__":
                app.run(host='0.0.0.0', debug = True)