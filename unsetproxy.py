

import subprocess
check= subprocess.call("env","|","grep","proxy",shell=True)
def unset(check):
    if check:
        proxy = subprocess.call("unset","http_proxy","HTTPS_PROXY","https_proxy","no_proxy","HTTP_PROXY", shell=True)
    else:
        print("Done")

unset(check)
