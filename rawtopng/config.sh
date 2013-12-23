PACKAGES="zlib libpng"
CFLAGS="-Wall -Wpedantic -O2 $(pkg-config --cflags $PACKAGES)"
LDFLAGS="$(pkg-config --libs $PACKAGES)"
