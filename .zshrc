ZSH=$HOME/.oh-my-zsh
ZSH_THEME="sorin"
COMPLETION_WAITING_DOTS="true"

plugins=(git)
source $ZSH/oh-my-zsh.sh

# history settings
HISTFILE=~/.histfile
HISTSIZE=100000
SAVEHIST=100000

# default apps
export EDITOR="vim"

# binds
alias calc='python2 -ic "from __future__ import division; from math import *; from random import *"'

export PATH=/usr/local/bin:/usr/local/sbin:$PATH  # for brew'd python
export WORKON_HOME=~/Workspace
source /usr/local/bin/virtualenvwrapper.sh
workoncd() {
    workon $1
    cd $WORKON_HOME/$1
}
alias workon=workoncd
alias workoff=deactivate
