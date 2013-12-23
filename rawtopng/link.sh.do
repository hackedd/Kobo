redo-ifchange config.sh
. ./config.sh
echo "gcc -o \$@ $LDFLAGS" >$3
chmod +x $3
