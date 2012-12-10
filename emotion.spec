#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/emotion emotion; \
#cd emotion; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf emotion-$PKG_VERSION.tar.xz emotion/ --exclude .svn --exclude .*ignore

%define	major 	1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:		emotion
Version:	1.7.3
Release:	1
Summary:	Enlightenment video and media library
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	evas >= 1.7.1
BuildRequires:	edje >= 1.7.1
BuildRequires:	pkgconfig(ecore) >= 1.7.1
BuildRequires:	pkgconfig(edje) >= 1.7.1
BuildRequires:	pkgconfig(eio)
BuildRequires:	pkgconfig(embryo) >= 1.7.1
BuildRequires:	pkgconfig(eet) >= 1.7.1
BuildRequires:	pkgconfig(evas) >= 1.7.1
BuildRequires:	pkgconfig(edje) >= 1.7.1
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gstreamer-video-0.10)
BuildRequires:	gstreamer0.10-tools
BuildRequires:	pkgconfig(eeze) >= 1.7.1
BuildRequires:	doxygen
BuildRequires:	pkgconfig(lua)

%description
Emotion is a video & media object library designed to interface with Evas and
Ecore to provide autonomous "video" and "audio" objects that can be moved,
resized and positioned like any normal object, but instead they can play video
and audio and can be controlled from a high-level control API allowing the
programmer to quickly piece together a multi-media system with minimal work.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
autoreconf -fi
%configure2_5x \
	--enable-gstreamer \
	--enable-xine \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/edje/modules/emotion/linux-*/*.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}*

%changelog
* Thu Jun 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.1-1
+ Revision: 807362
- version update 1.0.1

* Mon Jan 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.0.66791-0.20120103.1
+ Revision: 759241
- fixed build with missing BRs evas, eio, and libxine 1.1
- rediffed p0, but disabling
- adding BR for libgstbasevideo-devel
- fixed typo
- new snapshot 0.2.0.66791
- merged spec with UnityLinux
- cleaned up spec
- disabled static build

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 0.2.0-1.20101010.1mdv2011.0
+ Revision: 585564
- bump rel
- new snapshto

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 0.2.0-1.20100711.1mdv2011.0
+ Revision: 554407
- new snapshot

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 0.1.0.042-7.20090807.1mdv2010.0
+ Revision: 411179
- new snapshot to build with latest evas
- rebuild against new ecore

* Wed Jul 08 2009 Funda Wang <fwang@mandriva.org> 0.1.0.042-6mdv2010.0
+ Revision: 393497
- rebuild for new ecore

* Sun Mar 01 2009 Antoine Ginies <aginies@mandriva.com> 0.1.0.042-5mdv2009.1
+ Revision: 346358
- fix buildrequires
- SVN SNAPSHOT 20090227, release 0.1.0.042

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0.042-4mdv2009.0
+ Revision: 266622
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Mar 31 2008 Antoine Ginies <aginies@mandriva.com> 0.1.0.042-3mdv2009.0
+ Revision: 191232
- update buildrequires to support rebuild dor 2008.0 release

* Mon Feb 18 2008 Antoine Ginies <aginies@mandriva.com> 0.1.0.042-3mdv2008.1
+ Revision: 170106
- bump release
- remove old source

  + Thierry Vignaud <tv@mandriva.org>
    - fix gstreamer0.10-devel BR for x86_64

* Sat Feb 09 2008 Austin Acton <austin@mandriva.org> 0.1.0.042-2mdv2008.1
+ Revision: 164526
- buildrequires gstreamer plugins base devel

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 0.1.0.042-1mdv2008.1
+ Revision: 161555
- new version
- fix URL
- tidy spec
- build with cdda
- drop emotion-config

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1.008-1mdv2008.1
+ Revision: 104109
- add  gstreamer0.10-ffmpeg, ffmpeg buildrequires
- update buildrequires
- new tarball
- CVS SNAPSHOT 20071031, release 0.0.1.005

* Fri Aug 31 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1.005-4mdv2008.0
+ Revision: 76696
- fix missing emotion-config file
- fix path in tarball
- CVS SNAPSHOT 20070830, release 0.0.1.005
- CVS SNAPSHOT 20070529, release 0.0.1.005

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1.005-2mdv2008.0
+ Revision: 30682
- fix release tag
- disable cvs release
- increase mkrel
- CVS snapshot 20070524, release 0.0.1.005
- use version in source file

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1.005-0.20070516.1mdv2008.0
+ Revision: 29304
- replace corrupted source
- remove unwanted changelog
- cvs snapshot 20070516

  + Pascal Terjan <pterjan@mandriva.org>
    - Import emotion

