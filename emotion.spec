%define	name	emotion
%define	version 0.2.0
%define release %mkrel 1.201010.1

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightenment video and media library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.bz2
Patch0:		emotion-0.2.0-drop-gstbase.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	ecore-devel >= 1.0.0
BuildRequires:	edje-devel >= 1.0.0
BuildRequires:	edje >= 1.0.0
BuildRequires:	libxine-devel
BuildRequires:	gstreamer0.10-tools
BuildRequires:	gstreamer0.10-ffmpeg gstreamer0.10-cdio
BuildRequires:	libgstreamer-devel

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
Requires: %{name} >= %{version}-%{release}

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
%setup -q
%patch0 -p0

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --enable-gstreamer --enable-xine --disable-vlc
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%{_datadir}/%name
%{_libdir}/%name
%{_libdir}/edje/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/emotion-0
