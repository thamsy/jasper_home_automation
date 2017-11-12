# jasper_home_automation

## Installation

Add youtube-api secrets (`client_secret.json` and `main.py-ouath2.json`), and telegram bot secrets (`secret.py`)

```bash
pip install -r requirements.txt
```
## Dependencies

### Mopidy
[to be described further later]

### Nginx
[to be described further later]


## Run

### Mopidy

You need mopidy running in the background first
```bash
# tmux new -s mopidy
tmux a -t mopidy
mopidy
# ctrl-b then d
```

### Nginx
You will need to configure nginx as a proxy for mopidy
```bash
sudo service nginx reload
```

### Main python file

```bash
# tmux new -s jasper-ha
tmux a -t jasper-ha
python main.py
# ctrl-b then d
```

## Troubleshoot
**Q: There is no music coming out from the speakers.**

A: You may need to change the raspi-config to detect your speakers. To do so you need `ssh` into your raspi-pi, go to `sudo raspi-config`, then `Advanced`, then `Audio` and choose the right audio feed.

**Q: I can't quit the application**

A: Try `Ctrl-backslash`
