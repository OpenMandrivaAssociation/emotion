%define	name	emotion
%define	version 0.0.1.005
%define mrelease %mkrel 1

%define cvsrel 20070516
%define release 0.%{cvsrel}.%{mrelease}

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment video and media library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{cvsrel}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel ecore-devel eet-devel embryo-devel
BuildRequires:	edje-devel
BuildRequires:	edje
BuildRequires:	libxine-devel
BuildRequires:	libgstreamer0.10-devel
BuildRequires:	multiarch-utils

%description
Emotion is a video & media object library designed to interface with Evas and
Ecore to provide autonomous "video" and "audio" objects that can be moved,
resized and positioned like any normal object, but instead they can play video
and audio and can be controlled from a high-level control API allowing the
programmer to quickly piece together a multi-media system with minimal work.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Requires: %{name}

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x --enable-gstreamer --enable-xine
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
# remove unneeded files?
#rm -f %buildroot/%_libdir/xine/plugins/*/*.{a,la}
#rm -f %buildroot/%_libdir/%name/*.{a,la}
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
#%{_bindir}/%name
%{_bindir}/%{name}_*
%{_datadir}/%name
%{_libdir}/%name
#%{_libdir}/xine/plugins/*/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h
%{_bindir}/%name-config
%multiarch %multiarch_bindir/%name-config

%changelog
* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1.005-0.20070516.1mdv2008.0
- CVS snapshot

* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20060323.1mdk
- new cvs checkout
- enable xine backend too

* Fri Feb 17 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.1.004-0.20060216.2mdk
- Fix BuildRequires

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20060216.1mdk
- new cvs checkout

* Wed Jan 18 2006 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20060117.1mdk
- new cvs checkout

* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20051124.1mdk
- new cvs checkout
- use gstreamer backend

* Fri Nov 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.0.1.004-0.20051109.2mdk
- rebuild against openssl-0.9.8

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20051109.1mdk
- new cvs checkout

* Sat Nov 05 2005 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20051104.1mdk
- new cvs checkout

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20050904.1mdk
- new cvs checkout

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.0.1.004-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050627.1mdk
- new cvs checkout

* Wed Jun 08 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050608.1mdk
- new cvs checkout

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050524.2mdk
- multiarch binaries

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050524.1mdk
- new cvs checkout

* Sun May 15 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050511.3mdk
- until plugins are split, lib requires name

* Sun May 15 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050511.2mdk
- clean spec

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 0.0.1.003-0.20050511.1mdk
- initial package

