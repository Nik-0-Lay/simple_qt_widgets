from conan import ConanFile
from conan.tools.cmake import cmake_layout

class SimpleQt(ConanFile):
    name        = "simple_qt"
    author      = "Author Name"
    license     = "Proprietary"
    description = "Simple Qt-Widgets application"
    settings    = "os", "compiler", "build_type", "arch"
    generators  = "CMakeDeps", "CMakeToolchain"
    exports     = "version.txt"

    def configure(self):
        #  Qt
        self.options["qt"].shared             = True
        self.options["qt"].qtdeclarative      = True
        self.options["qt"].qttools            = True 

    def requirements(self):
        self.requires("qt/6.7.3")

    def layout(self):
        cmake_layout(self)