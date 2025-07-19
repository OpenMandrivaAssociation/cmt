%global debug_package %{nil}

Summary:	Computer Music Toolkit ladspa plugins
Name: cmt
Version: 1.18
Release: 1
License:	GPLv2+
Group:	Sound
Url:	https://www.ladspa.org
Source0:	https://www.ladspa.org/download/%{name}_%version.tgz
Patch0:	cmt-1.18-optflags.patch
Patch1:	cmt-1.17-fix-lto.patch
BuildRequires:	ladspa-devel

%description 
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for use
with software synthesis and recording packages on Linux.
This package contains several audio plugins, including freeverb.

%files
%doc doc/*.html
%{_libdir}/ladspa/%{name}.so

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}_%{version}


%build
cd src
%make targets OPTFLAGS="%{optflags}"


%install
cd src
mkdir -p %{buildroot}%{_libdir}/ladspa
%make_install INSTALL_PLUGINS_DIR="%{buildroot}%{_libdir}/ladspa"
