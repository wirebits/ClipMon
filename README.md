# ClipMon
A tool which records the copied text of the clipboard.

# Key Features
- Record each copied text into the txt file.
- Show each copied text with proper date and time.
- If the clipboard is empty, then the program stopped.
- Update the txt file every second.
- After every 60 seconds, it email the txt file.

# OS Support
- Windows 10
- Kali Linux

# Setup
1. Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).<br>
2. Install the *pyperclip* module on your system (Windows/Linux/MacOS) by copy and run the following command :<br>

```
pip3 install -r requirements.txt
```

# Install and Run
1. Download or Clone the Repository.
2. Open the folder.
3. Put the *Sender EmailID*, *App Password* and *Reciever EmailID* at the indicated places.
4. After that run the *ClipMon.py* file.
- To run without console window in windows:<br>

```
pythonw.exe ClipMon.py
```
# Get App Password

1. Go to this link - [Google Account](https://myaccount.google.com/).
2. Search **App Passwords**.
3. Enter your gmail password to proceed.
4. It ask for *App Name*, give a name of the app.
5. After that, click on *Create*.
6. Wait for few seconds, it gives a 16-digit password.
7. Copy the password and paste in the code.
