pkgname = "rust-bindgen"
pkgver = "0.65.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins", "--path", "bindgen-cli"]
hostmakedepends = ["cargo"]
makedepends = ["rust"]
depends = ["libclang"]
checkdepends = ["libclang"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = f"https://github.com/rust-lang/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e4f3491ad342a662fda838c34de03c47ef2fa3019952adbfb94fe4109c06ccf2"
# needs rustfmt nightly to run suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
