%define	name	emotion
%define	version 0.0.1.008
%define release %mkrel 1

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
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.041, ecore-devel >= 0.9.9.041, eet-devel >= 0.9.0.011, embryo-devel >= 0.9.1.041
BuildRequires:	edje-devel >= 0.5.0.041
BuildRequires:	edje >= 0.5.0.041
BuildRequires:	libxine-devel
Buildrequires:  gstreamer0.10-ffmpeg, ffmpeg
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
%setup -q

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
cp -v $RPM_BUILD_DIR/%name-%version/%name-config %buildroot/%_bindir/
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
%multiarch_bindir/%name-config
