import subprocess
import pkg_resources
import sys

required_pkgs = {'pygame'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required_pkgs - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# 以降は元のコードに続く...
