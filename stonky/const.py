from datetime import date
from platform import platform, python_version
from sys import argv, gettrace

from teletype.__version__ import VERSION as teletype_version

from stonky.__version__ import VERSION

IS_DEBUG = gettrace() is not None
SYSTEM = {
    "date": date.today(),
    "platform": platform(),
    "arguments": argv[1:],
    "python version": python_version(),
    "stonky version": VERSION,
    "teletype version": teletype_version,
}
