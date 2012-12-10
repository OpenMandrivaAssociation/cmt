%define name cmt
%define oname cmt_src
%define version 1.16
%define release %mkrel 3

Summary: Computer Music Toolkit ladspa plugins
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ladspa.org/download/%{oname}_%version.tgz
Patch:	 cmt-optflags.patch
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
%setup -q -n %name
%patch -p1

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


%changelog
* Tue Dec 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.16-3mdv2012.0
+ Revision: 738097
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-2mdv2011.0
+ Revision: 610147
- rebuild

* Fri Apr 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.16-1mdv2010.1
+ Revision: 368967
- new version
- drop patch 0
- patch to use the right optflags

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.15-7mdv2009.0
+ Revision: 243572
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.15-5mdv2008.1
+ Revision: 165929
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.15-5mdv2008.0
+ Revision: 37220
- Import cmt



* Wed Jun 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.15-5mdk
- Rebuild
- use mkrel

* Mon Jun 06 2005 Götz Waschk <waschk@mandriva.org> 1.15-4mdk
- Rebuild

* Fri Jun  4 2004 Götz Waschk <waschk@linux-mandrake.com> 1.15-3mdk
- add source URL
- drop prefix
- new g++

* Fri Jan  2 2004 Götz Waschk <waschk@linux-mandrake.com> 1.15-2mdk
- routinely rebuild 

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 1.15-1mdk
- new version

* Fri Aug 16 2002 Götz Waschk <waschk@linux-mandrake.com> 1.14-3mdk
- gcc 3.2-0.3mdk rebuild

* Mon Aug 12 2002 Götz Waschk <waschk@linux-mandrake.com> 1.14-2mdk
- arrgh, use real sources
- fix patch (half-merged)

* Mon Aug 12 2002 Götz Waschk <waschk@linux-mandrake.com> 1.14-1mdk
- new version

* Mon Jul 29 2002 Götz Waschk <waschk@linux-mandrake.com> 1.12-3mdk
- gcc 3.2 build

* Tue May 28 2002 Götz Waschk <waschk@linux-mandrake.com> 1.12-2mdk
- use our optflags
- patch to allow build with g++3.1
- gcc 3.1

* Fri Mar 29 2002 Götz Waschk <waschk@linux-mandrake.com> 1.12-1mdk
- initial package
