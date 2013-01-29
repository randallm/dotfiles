ZSH=$HOME/.oh-my-zsh
ZSH_THEME="sorin"
COMPLETION_WAITING_DOTS="true"

plugins=(git)
source $ZSH/oh-my-zsh.sh
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/android-sdk/tools:/usr/bin/vendor_perl:/usr/bin/core_perl:/opt/android-sdk/platform-tools:/opt/android-sdk/platform-tools

# history settings
HISTFILE=~/.histfile
HISTSIZE=100000
SAVEHIST=100000

# default apps
export BROWSER="chromium"
export EDITOR="vim"

# uniform look between QT and GTK
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

# binds
alias ls='ls --color=auto'  # colored ls output
alias v="amixer sset \"Master\" 15%"
alias git="hub"
alias calc='python2 -ic "from __future__ import division; from math import *; from random import *"'
alias pycd='find . -name "*.pyc" -exec rm -rf {} \;'
alias wth_f='cd workspace/whatsthehomework_flask/ && source bin/activate && cd src'
