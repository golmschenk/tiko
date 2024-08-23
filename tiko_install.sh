#!/bin/bash

set -x

mkdir -p "${HOME}/.local/bin"

# shellcheck disable=SC2016
echo 'if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi' >> "$HOME/.profile"
source "$HOME/.profile"

PORTABLE_NIX_URL="https://github.com/DavHau/nix-portable/releases/latest/download/nix-portable-$(uname -m)"
if command -v curl &> /dev/null; then
  curl -L "${PORTABLE_NIX_URL}" > "$HOME/.local/bin/nix-portable"
else
  wget -O "$HOME/.local/bin/nix-portable" "${PORTABLE_NIX_URL}"
fi
chmod +x "$HOME/.local/bin/nix-portable"

ln -s "$HOME/.local/bin/nix-portable" "$HOME/.local/bin/nix-env"
ln -s "$HOME/.local/bin/nix-portable" "$HOME/.local/bin/nix-shell"
ln -s "$HOME/.local/bin/nix-portable" "$HOME/.local/bin/nix-build"
ln -s "$HOME/.local/bin/nix-portable" "$HOME/.local/bin/nix-store"
ln -s "$HOME/.local/bin/nix-portable" "$HOME/.local/bin/nix-channel"
ln -s "$HOME/.local/bin/nix-portable" "$HOME/.local/bin/nix"

echo "Installing nu."
nix profile install nixpkgs#nushell

echo "Starting nu script."
nu tiko.nu
