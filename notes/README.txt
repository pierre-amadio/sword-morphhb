
#where is the morphhb repository located ?
MORPHHBREPO=/home/melmoth/dev/morphhb/

rm -rf book
mkdir book
for i in `ls $MORPHHBREPO/wlc` ; do 
  ./bin/extractBook.py $MORPHHBREPO/wlc/$i book/
done
