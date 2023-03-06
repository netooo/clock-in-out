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
