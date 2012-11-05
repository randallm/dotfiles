#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

alias calc='ipython -ic "from __future__ import division; from math import *; from random import *"'

export BROWSER=chromium
export WINEDEBUG=-all
export EDITOR="vim"
export HISTSIZE=1000
export G_FILENAME_ENCODING=utf-8
export LC_ALL="en_US.UTF-8"

alias taskmgr='ps at'
alias getprocess='ps -ef | grep'
alias v='amixer sset "Master" 15%'
