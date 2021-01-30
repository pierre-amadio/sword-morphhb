
#where is the morphhb repository located ?
MORPHHBREPO=/home/melmoth/dev/morphhb/

rm -rf book
mkdir book
for i in `ls $MORPHHBREPO/wlc` ; do 
  ./bin/extractBook.py $MORPHHBREPO/wlc/$i book/
done

rm -rf clean
mkdir clean
for i in `ls book` ; do
  echo $i
  ./bin/cleanWNodes.py book/$i clean/
done
