#!/bin/sh

echo "Re-adding bash..."
cp ~/.bashrc .bashrc

echo "Re-adding conky..."
cp ~/.conkyrc .conkyrc

echo "Re-adding redshiftgui..."
cp ~/.redshiftgrc .redshiftgrc

echo "Re-adding vim..."
cp ~/.vimrc .vimrc

echo "Re-adding X init..."
cp ~/.xinitrc .xinitrc

echo "Re-adding X display..."
cp ~/.Xresources .Xresources

#echo "Re-adding Sublime Text 2..."
#cp -r ~/.config/sublime-text-2/ sublime-text-2/

echo "Re-adding QTile..."
cp -r ~/.config/qtile/ qtile/

echo ""
echo "All done!"

