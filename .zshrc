

#
# User configuration sourced by interactive shells
#

# Source zim
if [[ -s ${ZDOTDIR:-${HOME}}/.zim/init.zsh ]]; then
  source ${ZDOTDIR:-${HOME}}/.zim/init.zsh
fi

alias g='git'
alias ga='git add'
alias gd='git diff'
alias gpl='git pull'
alias gr='git reset'
alias gcp='git cherry-pick'
alias gc='git commit'
alias gs='git status'
alias gco='git checkout'
alias gst='git stash'
alias glog='git log'
alias gb='git branch'

export NVM_LAZY_LOAD=true
source ~/.zsh-nvm/zsh-nvm.plugin.zsh
