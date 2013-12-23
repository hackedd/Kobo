redo-ifchange config.sh
. ./config.sh
echo "gcc -c -MD -MF \$2.d -o \$3 \$2.c $CFLAGS" >$3
chmod +x $3
