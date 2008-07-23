%define name cmt
%define oname cmt_src
%define version 1.15
%define release %mkrel 7

Summary: Computer Music Toolkit ladspa plugins
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ladspa.org/download/%{oname}_%version.tar.bz2
Patch:	 cmt-gcc3.1.patch.bz2
License: GPL
Group: Sound
URL: http://www.ladspa.org
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ladspa-devel

%description 
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux.

This package contains several audio plugins, including freeverb.

%prep
%setup -q -n %name
%patch

%build
cd src
%make targets OPTFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_libdir/ladspa
cp plugins/* $RPM_BUILD_ROOT%_libdir/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/*
%_libdir/ladspa/*.so
