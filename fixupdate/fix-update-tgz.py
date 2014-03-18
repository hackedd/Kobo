#!/usr/bin/env python
import os
import sys
import tempfile
import subprocess
import shutil


if "--help" in sys.argv or len(sys.argv) > 3:
    print >>sys.stderr, "Usage: %s [ORIG [NEW]]" % sys.argv[0]
    sys.exit(1)

thisdir = os.path.dirname(__file__)

archive = sys.argv[1] if len(sys.argv) >= 2 else "KoboRoot.tgz"
new_archive = sys.argv[2] if len(sys.argv) >= 3 else "KoboRoot-fixed.tgz"

# Extract update archive to tempdir
root = tempfile.mkdtemp("KoboRoot")
try:
    try:
        subprocess.check_call(["tar", "xf", archive, "-C", root])
    except subprocess.CalledProcessError:
        print >>sys.stderr, "Unable to extract '%s' to '%s'" % (archive, root)
        sys.exit(1)

    # Overwrite some files in /etc
    for filename in ["inetd.conf", "services", "inittab"]:
        src_name = os.path.join(thisdir, filename)
        dest_name = os.path.join(root, "etc", filename)
        shutil.copyfile(src_name, dest_name)

    # Append code to /etc/init.d/rcS if it is overwritten by update
    rcs = os.path.join(root, "etc", "init.d", "rcS")
    if os.path.exists(rcs):
        with open(os.path.join(thisdir, "append-rcS")) as src:
            with open(rcs, "a") as dest:
                shutil.copyfileobj(src, dest)

    # Create new update archive
    subprocess.check_call(["tar", "czf", new_archive, "-C", root, "."])
    print >>sys.stderr, "Created '%s' from '%s'" % (new_archive, archive)
finally:
    shutil.rmtree(root, ignore_errors=True)
