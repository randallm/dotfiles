#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

xset -b &
redshiftgui &
conky -p 20 &
volumeicon &
dropboxd &
deluged &
deluge-web &

# exec startxfce4 --with-ck-launch
exec ck-launch-session dbus-launch startxfce4
