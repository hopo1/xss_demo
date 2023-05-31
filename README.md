# XSS demonstration project
This app is XSS susceptible from all 3 types of attacks.
You can save a name to the database, write it into url and display and just display.
## Setup 
Install python 3 and pip. 
Run `pip install -r requirements.txt`
Run `python3 app.py`
Find the url open the app and you can try for your self.
## How to attack
### Reflected XSS
Add `/?name=<script>???</script>` to the url.
You can change `???` for a malicious script.
### Stored XSS
Input the malicious code into the input field like `<script>???</script>`. 
You can change `???` for a malicious script.
### DOM-based XSS
Input the malicious code into the input field like `<img src=1 onerror=???>`. 
You can change `???` for a malicious script.