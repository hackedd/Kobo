OBJS="main.o rawtopng.o pngtoraw.o"
redo-ifchange link.sh $OBJS
./link.sh $3 $OBJS
