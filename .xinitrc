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

test `hostname` == 'skynet' && xfce4-power-manager && xbacklight -set 100

xrdb ~/.Xresources &
redshiftgui &
volumeicon &
deluged &

#dropboxd &
#(sleep 10; conky -q) &

#tint2 &
xfce4-panel &
(sleep 3; gnome-do) & # built in autostart doesn't work

test `hostname` == 'skynet' && exec dbus-launch qtile # laptop
exec fusion-icon # everything else
