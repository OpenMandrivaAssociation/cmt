%global debug_package %{nil}

Summary: Computer Music Toolkit ladspa plugins
Name: cmt
Version: 1.17
Release: 1
Source0: http://www.ladspa.org/download/%{name}_%version.tgz
Patch:	 cmt-optflags.patch
Patch1:	cmt-1.17-fix-lto.patch
License: GPLv2+
Group: Sound
URL: http://www.ladspa.org
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ladspa-devel

%description 
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux.

This package contains several audio plugins, including freeverb.

%prep
%autosetup -p1 -n %{name}_%{version}

%build
cd src
%make targets OPTFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_libdir/ladspa
cp plugins/* $RPM_BUILD_ROOT%_libdir/ladspa

%files
%defattr(-,root,root)
%doc doc/*
%_libdir/ladspa/*.so
