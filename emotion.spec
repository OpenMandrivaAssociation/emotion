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

%define	svndate	20120103
%define	svnrev	66791

%define	major 	0
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:		emotion
Version:	0.2.0.%{svnrev}
Release:	0.%{svndate}.1
Summary:	Enlightenment video and media library
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.tar.xz
Patch0:		emotion-0.2.0-drop-gstbase.patch

BuildRequires:	edje >= 1.0.0
BuildRequires:	pkgconfig(ecore) >= 1.0.0
BuildRequires:	pkgconfig(edje) >= 1.0.0
BuildRequires:	pkgconfig(embryo) >= 1.0.0
BuildRequires:	pkgconfig(eet) >= 1.4.0
BuildRequires:	pkgconfig(evas) >= 1.0.0
BuildRequires:	pkgconfig(gstreamer-0.10)
#BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	gstreamer0.10-ffmpeg, ffmpeg
BuildRequires:	gstreamer0.10-plugins-good gstreamer0.10-cdio

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
Libraries for %{name}

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries

%prep
%setup -qn %{name}
%patch0 -p0

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--enable-gstreamer \
	--enable-xine \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

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

