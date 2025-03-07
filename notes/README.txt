
#where is the morphhb repository located ?
# You ll find the original sources in the openscriptures's morphhb repository:
# git clone git@github.com:openscriptures/morphhb.git
MORPHHBREPO=/home/pierre/dev/morphhb/

rm -rf book
mkdir book
for i in `ls $MORPHHBREPO/wlc` ; do 
  ./bin/extractBook.py $MORPHHBREPO/wlc/$i book/
done

rm -rf clean
mkdir clean
for i in `ls book` ; do
  ./bin/cleanWNodes.py book/$i clean/ ;
  sed -i '1d' ./clean/$i ;
done

rm morphhb.osis.xml
cp header.txt morphhb.osis.xml
for i in `ls clean/` ; do 
 cat clean/$i >>morphhb.osis.xml
done;

echo "</osisText></osis>">>morphhb.osis.xml

#wget http://www.crosswire.org/osis/osisCore.2.1.1.xsd
wget http://www.crosswire.org/~dmsmith/osis/osisCore.2.1.1-cw-latest.xsd
#Validate the files:
xmllint --noout --schema osisCore.2.1.1-cw-latest.xsd morphhb.osis.xml


#https://www.crosswire.org/sword/develop/swordmodule/
rm -rf mod
mkdir mod
# 1 text so far
# 8 book and chapter introduction are determined
# 32 milestone
# 64 extra canonical issues
# 513 : general
#
#Also do not use normalisation
#http://tracker.crosswire.org/browse/MOD-350

/usr/local/sword/bin/osis2mod mod morphhb.osis.xml -N -z z -v MT -d 618


