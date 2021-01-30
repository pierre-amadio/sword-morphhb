#/bin/bash

installmgr -u OSHB
oldzip=/home/melmoth/dev/sword-morphhb/OSHB.zip

rm -rf ./tmp
mkdir ./tmp

if [ $1 = "devel" ]  
then
 echo "devel";
 cp oshb.conf $SWORD_PATH/mods.d
 cp -r mod/ $SWORD_PATH/modules/texts/ztext/oshb
else
 echo "standard";
 cp $oldzip ./tmp
 cd tmp
 unzip OSHB.zip
 cp mods.d/oshb.conf $SWORD_PATH/mods.d
 mv modules/texts/ztext/oshb/ $SWORD_PATH/modules/texts/ztext
fi 

