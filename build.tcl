#!/usr/bin/tclsh

set arch "x86_64"
set base "tcl3d-0.9.3"
set fileurl "http://www.bawt.tcl3d.org/download/InputLibs/tcl3d-0.9.3.7z"

set var [list wget $fileurl -O $base.7z]
exec >@stdout 2>@stderr {*}$var

set useArchive 1
if {[catch {package require archive} errMsg] == 1} {
    puts $errMsg
    set useArchive 0
}

if {$useArchive==1} {
    archive::extract $base.7z all all 1
    archive::create $base.tar.gz gzip ustar [list $base]
} else {
    set var2 [list 7z x $base.7z]
    exec >@stdout 2>@stderr {*}$var2

    set var2 [list tar czvf $base.tar.gz $base]
    exec >@stdout 2>@stderr {*}$var2
}

file delete -force $base.7z
file delete -force $base

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force CMakeLists.patch build/SOURCES
file copy -force CMakeModules.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl3d.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove source package
file delete -force $base.tar.gz
