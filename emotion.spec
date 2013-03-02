%define	gstapi 	0.10
%define	major 	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Enlightenment video and media library
Name:		emotion
Version:	1.7.5
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	evas >= 1.7.1
BuildRequires:	edje >= 1.7.1
BuildRequires:	gstreamer%{gstapi}-tools
BuildRequires:	pkgconfig(ecore) >= 1.7.1
BuildRequires:	pkgconfig(edje) >= 1.7.1
BuildRequires:	pkgconfig(eio)
BuildRequires:	pkgconfig(embryo) >= 1.7.1
BuildRequires:	pkgconfig(eet) >= 1.7.1
BuildRequires:	pkgconfig(eeze) >= 1.7.1
BuildRequires:	pkgconfig(evas) >= 1.7.1
BuildRequires:	pkgconfig(edje) >= 1.7.1
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-video-%{gstapi})
BuildRequires:	pkgconfig(libxine)
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

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries.

%prep
%setup -q

%build
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
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}*

