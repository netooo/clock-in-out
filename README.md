# Description
Automated clock in/out to KOT with location-based and slack notifications.

# Tools
- raspberry pi
- AB Shutter3
- GPS/GLONASS

# Configs
Need to prepare your setting file.

`settings.py`
```
KOT_TOP_URL="https://s2.kingtime.jp/independent/recorder/personal/"
KOT_ID=""
KOT_PASS=""
ATTENDANCE_DEV_URL="https://hooks.slack.com/services/<snip>"
```

# CLI
Setting .zshrc
```zsh
alias clock-in="python3 ~/clock-in-out/in.py"
alias clock-out="python3 ~/clock-in-out/out.py"
```

Type its.
```zsh
clock-in
```
