PACKAGES="zlib libpng"
CFLAGS="-g -Wall -Wpedantic $(pkg-config --cflags $PACKAGES)"
LDFLAGS="$(pkg-config --libs $PACKAGES)"
