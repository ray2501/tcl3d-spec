#
# spec file for package tcl3d
#

Name:           tcl3d
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  tcl-devel >= 8.5
BuildRequires:  tk-devel >= 8.5
BuildRequires:  swig
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  glu-devel
BuildRequires:  libXrandr-devel
Requires:       tcl >= 8.5
Requires:       tk >= 8.5
License:        BSD 3-Clause
Group:          Development/Libraries/Tcl
Version:        0.9.2
Release:        0
Summary:        3D functionality of OpenGL and other 3D libraries for Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://www.tcl3d.org/
Source0:        %{name}-%{version}.tar.gz
Patch0:         CMakeLists.patch
Patch1:         CMakeModules.patch

%description
Tcl3D offers the 3D functionality of OpenGL and other 3D libraries at
the Tcl scripting level.

This package includes tcl3dOgl, tcl3dGl2ps and tcl3dGauges.

%prep
%setup -q -n %{name}-%{version}
%patch0
%patch1

%build
cmake CMakeLists.txt
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}/%{name}%{version}

