#!/usr/bin/python3

# Visual Cron API
# 
# This script takes an executable, and interfaces it with the visual cron database.
# It takes data, and throws it into whatever database is connected to sqlalchemy
# 
# the easiest way to use this tool is to add it to your PATH, then as the cron job the command should be:
#
# vc-api.py (COMMANDS TO RUN)+
# ^ it will capture both stdout and stderr into separate log files. 
#
# OR pipe if you only want one big log file for both stdout and stderr:
#
# (COMMAND TO RUN) | vc-api.py
#
# the default config settings will be in config.toml here. To add your own config, use the following flag:
# vc-api.sh -c /path/to/config.toml

DEBUG = True

# print debug
def printd(str):
    if DEBUG:
        warning_color = "\033[93m"
        end_color = "\033[0m"
        print(f"{warning_color}{str}{end_color}")

"""
open_config:
    given a config file, opens it into a python object
    for now, only deals with TOML. Refactor if you need another config file structure. 
"""
def open_config(config_filepath):
    import toml
    return toml.load(config_filepath)

"""
run_with_api:
    given an executable filepath (as a path string to the file), the file is run in a subprocess
    and is connected with an API to log information related to the file. All of the settings related to the path
    will be in the config_filepath. 
"""
def run_with_api(executable_filepath, config_filepath):
    printd(f"executable filepath: {executable_filepath}")
    printd(f"config filepath: {config_filepath}")
    config = open_config(config_filepath)
    printd(f"python config: {config}")

if __name__ == "__main__":
    import sys
    config_path = "config.toml"
    if len(sys.argv) < 2:
        print("usage: python vc-api.py (/path/to/executable)+")
        print("for help run: python vc-api.py -h")
        print("-----------------------------------")
        sys.exit("no arguments given") 
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "-c":
            if len(sys.argv) <= i+1:
                sys.exit(f"not enough arguments given: len({sys.argv}) = {len(sys.argv)} <= i+1 = {i+1}")
            printd(f"config file path: {sys.argv[i+1]}")
            i += 1
        else:
            run_with_api(arg, config_path)
        i += 1
