#!/bin/bash

set -x

echo "Installing homebrew."
if [[ $(uname) == "Darwin" ]]; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
elif [[ $(uname) == "Linux" ]]; then
  mkdir $HOME/.homebrew
  curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip-components 1 -C $HOME/.homebrew
  eval "$($HOME/.homebrew/bin/brew shellenv)"
  brew update --force --quiet
  chmod -R go-w "$(brew --prefix)/share/zsh"
else
  echo "Unexpected operating system: $(uname)"
  exit 1
fi

brew install gcc
brew link gcc

echo "Installing nu."
brew install nu

echo "Starting nu script."
nu tiko.nu