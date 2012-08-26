#!/bin/sh

echo "Setting up bash..."
cp .bashrc ~/.bashrc

echo "Setting up conky..."
cp .conkyrc ~/.conkyrc

echo "Setting up redshiftgui..."
cp .redshiftgrc ~/.redshiftgrc

echo "Setting up vim..."
cp .vimrc ~/.vimrc

echo "Setting up X init..."
cp .xinitrc ~/.xinitrc
chmod 755 ~/.xinitrc

echo "Setting up X display..."
cp .Xresources ~/.Xresources

#echo "Setting up Sublime Text 2..."
#cp -r sublime-text-2/ ~/.config/sublime-text-2/

echo "Setting up QTile..."
cp -r qtile/ ~/.config/qtile/

echo ""
echo "All done!"
