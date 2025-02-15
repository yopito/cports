pkgname = "libva"
pkgver = "2.18.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwith_glx=yes", "-Dwith_wayland=yes"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libxfixes-devel", "libxext-devel", "libdrm-devel", "libffi-devel",
    "wayland-devel", "mesa-devel"
]
pkgdesc = "Video Acceleration API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "9d666c70c12dfefcdd27ae7dea771557f75e24961d0ed4cb050d96fb6136f438"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()
