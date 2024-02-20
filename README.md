 # IP Logger

This is a Python script that uses the IP Logger API to shorten a URL and track its visitors. The script is designed to be easy to use, even for junior developers.

### Step 1: Import the Necessary Libraries

The first step is to import the necessary libraries. We will need the following libraries:

```python
import secrets
import random
from time import sleep
```

### Step 2: Define the Colors

Next, we will define the colors that we will use in the script. We will use the following colors:

```python
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
```

### Step 3: Print the Welcome Message

Now, we will print the welcome message. The welcome message will include the script's name and a brief description of what it does.

```python
print(f'''{GREEN}

 ██▓ ██▓███      ██▓     ▒█████    ▄████   ▄████ ▓█████  ██▀███  
▓██▒▓██░  ██▒   ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒   ▒██░    ▒██   ██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░   ░██████▒░ ████▓▒░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░   

