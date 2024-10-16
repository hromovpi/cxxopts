%define _unpackaged_files_terminate_build 1

Name: cxxopts
Version: 3.2.2
Release: alt1

Summary: Command line arguments parser
License: MIT
URL: https://github.com/jarro2783/cxxopts
Group: Development/C++
BuildArch: noarch

BuildRequires: cmake gcc-c++

Source0: %name-%version.tar

%description
Minimalistic header-only parser of command line arguments for C++ programs

%prep
%setup

%build
%cmake -DCXXOPTS_BUILD_EXAMPLES=OFF -DCXXOPTS_BUILD_TESTS=ON
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_libdir/cmake/%name
install -D -m644 %buildroot%_datadir/cmake/%name/* %buildroot%_libdir/cmake/%name/
install -D -m644 include/%name.hpp %buildroot%_includedir/%name.hpp
install -D -m644 LICENSE %buildroot%_datadir/doc/%name/LICENSE
install -D -m644 README.md %buildroot%_datadir/doc/%name/README.md
rm -rf %buildroot%_datadir/cmake

%files
%_includedir/%name.hpp
%_datadir/doc/%name/LICENSE
%_datadir/doc/%name/README.md
%_libdir/cmake/%name/%name-config.cmake
%_libdir/cmake/%name/%name-config-version.cmake
%_libdir/cmake/%name/%name-targets.cmake
%_datadir/pkgconfig/%{name}.pc

%changelog
* Tue Oct 15 2024 Pavel Khromov <hromovpi@altlinux.org> 3.2.2-alt1
- Installing CMake targets and pkgconfig

* Tue Sep 10 2024 Pavel Khromov <hromovpi@altlinux.org> 3.2.1-alt1
- Initial build
