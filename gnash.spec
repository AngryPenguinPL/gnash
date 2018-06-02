%define with_tests 0

%{?_with_gstreamer: %{expand: %%global with_tests 1}}

%define libname %mklibname %{name} 0
%define devname %mklibname -d %{name}
%define libname_orig lib%{name}

%define bzr	0
%define rel	11
%define major	0

%if %bzr
%define release		-c %bzr %rel
%define distname	%{name}-%bzr.tar.xz
%define dir_name	%{name}
%define buildversion	trunk
%else
%define release		%rel
%define distname	%{name}-%{version}.tar.bz2
%define dir_name	%{name}-%{version}
%define buildversion	%{version}
%endif

Name: gnash
Version: 0.8.10
Release: %{release}
Summary: %{name} - a GNU Flash movie player
License: GPLv3
Group: Networking/WWW
Url: http://www.gnu.org/software/gnash
Source0: %{distname}
Patch1:	%{name}-0.8.3-manual.patch
Patch2: gnash-0.8.10-gcc47.patch
Patch4: gnash-0.8.10-CVE-2012-1175.diff
Patch5: gnash-0.8.10-link.patch
Patch6: gnash-0.8.10-giflib5.patch

BuildRequires:  kdelibs4-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  boost-devel
BuildRequires:  curl-devel
BuildRequires:  doxygen
BuildRequires:  rarian
BuildRequires:  slang-devel
BuildRequires:  xsltproc
BuildRequires:  agg-devel
BuildRequires:  mysql-devel
BuildRequires:  libtool-devel
BuildRequires:	tslib-devel
BuildRequires:	gtkglext-devel
BuildRequires:	gsm-devel
BuildRequires:	nspr-devel
BuildRequires:	expat-devel
BuildRequires:  gstreamer0.10-plugins-base-devel
BuildRequires:	ffmpeg-devel
BuildRequires:  csound-devel
Buildrequires:	dejagnu
BuildRequires:	speex-devel
BuildRequires:	pkgconfig(xi)
BuildRequires:  desktop-file-utils
BuildRequires:	pygtk2.0-devel
#BuildRequires:	python-gobject-devel
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:  xulrunner-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(xt)
%if %{with_tests}
BuildRequires:  ming-devel >= 0.4.3
BuildRequires:  ming-utils >= 0.4.3
Buildrequires:  netcat
Buildrequires:  wget
%endif
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-ugly
Requires:	gstreamer0.10-plugins-bad
Requires:	gstreamer0.10-ffmpeg
Suggests:	lightspark

%description
%{name} is capable of reading up to SWF v9 files and opcodes, but primarily
supports SWF v7, with better SWF v8 and v9 support under heavy development.
With the 0.8.2 release, %{name} includes initial parser support for SWF v8
and v9. Not all ActionScript 2 classes are implemented yet, but all of
the most heavily used ones are. Many ActionScript 2 classes are partially
implemented; there is support for all of the commonly used methods of each
class.

%files -f %{name}.lang
%doc README AUTHORS COPYING NEWS
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_bindir}/%{name}-gtk-launcher
%{_bindir}/fb-%{name}
%{_bindir}/gtk-%{name}
%{_bindir}/sdl-%{name}
%{_bindir}/findmicrophones
%{_bindir}/findwebcams
%{_mandir}/man1/findmicrophones.1.*
%{_mandir}/man1/findwebcams.1.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/fb-%{name}.1*
%{_mandir}/man1/%{name}-gtk-launcher.1*
%{_mandir}/man1/gtk-%{name}.1*
%{_mandir}/man1/sdl-%{name}.1*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

#--------------------------------------------------------------------

%package -n	%{libname}
Summary:	%{name} library
Group:	        Networking/WWW
Provides:	%{libname_orig} = %{version}

%description -n %{libname}
%{name} library.

%files -n %{libname}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}render-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}base-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}core-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}amf-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}media-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}net-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}sound-%{buildversion}.so
%{_libdir}/%{name}/lib%{name}device-%{buildversion}.so

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Obsoletes: %{libname}-devel

%description -n %{devname}
Headers of %{name} for development.

%files -n %{devname}
%{_includedir}/%{name}/*
%{_libdir}/%{name}/lib%{name}render.so
%{_libdir}/%{name}/lib%{name}amf.so
%{_libdir}/%{name}/lib%{name}base.so
%{_libdir}/%{name}/lib%{name}core.so
%{_libdir}/%{name}/lib%{name}media.so
%{_libdir}/%{name}/lib%{name}net.so
%{_libdir}/%{name}/lib%{name}sound.so
%{_libdir}/%{name}/lib%{name}device.so
%{_libdir}/pkgconfig/%{name}.pc

#--------------------------------------------------------------------

%package -n %{name}-firefox-plugin
Summary:	%{name} firefox plugin
Group:		Networking/WWW
Requires:	%{name} = %{version}-%{release}

%description -n %{name}-firefox-plugin
%{name} firefox plugin

%files -n %{name}-firefox-plugin
%config(noreplace) %{_sysconfdir}/%{name}pluginrc
%{_libdir}/mozilla/plugins/*.so

#--------------------------------------------------------------------

%package -n	klash
Summary:	%{name} konqueror plugin
Group:		Graphical desktop/KDE
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-konqueror-plugin
Provides:	%{name}-konqueror-plugin

%description -n klash
%{name} Konqueror plugin

%files -n klash
%{_bindir}/gnash-qt-launcher
%{_kde_bindir}/qt4-%{name}
%{_kde_libdir}/kde4/libklashpart.so
%{_kde_datadir}/kde4/services/klash_part.desktop
%{_datadir}/applications/klash.desktop
%{_datadir}/icons/hicolor/32x32/apps/klash.xpm
%{_kde_datadir}/apps/klash/
%{_mandir}/man1/qt4-%{name}.1*
%{_mandir}/man1/%{name}-qt-launcher.1*

#--------------------------------------------------------------------

%package cygnal
Summary:   Streaming media server
Requires:  %{name}-tools = %{version}-%{release}
Group:     System/Servers 

%description cygnal
Cygnal is a streaming media server that's Flash aware.

%files cygnal
%config(noreplace) %{_sysconfdir}/cygnalrc
%{_bindir}/cygnal
%{_mandir}/man1/cygnal.1*
%dir %{_libdir}/cygnal
%dir %{_libdir}/cygnal/plugins/
%{_libdir}/cygnal/plugins/*.so*

#--------------------------------------------------------------------

%package tools
Summary:   gnash tools
Requires:  %{name} = %{version}-%{release}
Group:     Video

%description tools
Gnash tools.

%files tools
%{_bindir}/gprocessor
%{_bindir}/soldumper
%{_bindir}/flvdumper
%{_bindir}/rtmpget
%{_mandir}/man1/gprocessor.1*
%{_mandir}/man1/soldumper.1*
%{_mandir}/man1/flvdumper.1*
%{_mandir}/man1/rtmpget.1*

#--------------------------------------------------------------------

%package -n python-gnash
Summary:   Gnash Python bindings
Requires:  %{name} = %{version}-%{release}
Group:     Development/Python

%description -n python-gnash
Python bindings for the Gnash widget. Can be used to embed Gnash 
into any PyGTK application.

%files -n python-gnash
%doc COPYING
%{python_sitearch}/gtk-2.0/gnash.so

#--------------------------------------------------------------------

%package extension-fileio
Summary:   Fileio extension for Gnash
Group:     Networking/WWW
Requires:  %{name} = %{version}-%{release}

%description extension-fileio
This extension allows SWF files being played within Gnash to have 
direct access to the file system. 
The API is similar to the C library one.

%files extension-fileio
%doc COPYING
%{_libdir}/gnash/plugins/fileio.so

#--------------------------------------------------------------------

%package extension-lirc
Summary:   LIRC extension for Gnash
Group:     Networking/WWW
Requires:  %{name} = %{version}-%{release}

%description extension-lirc
This extension allows SWF files being played within Gnash to have 
direct access to a LIRC based remote control device. 
The API is similar to the standard LIRC one.

%files extension-lirc
%doc COPYING
%{_libdir}/gnash/plugins/lirc.so

#--------------------------------------------------------------------

%package extension-dejagnu
Summary:   DejaGnu extension for Gnash
Group:     Development/Other
Requires:  %{name} = %{version}-%{release}

%description extension-dejagnu
This extension allows SWF files to have a simple unit testing API. 
The API is similar to the DejaGnu unit testing one.

%files extension-dejagnu
%doc COPYING
%{_libdir}/gnash/plugins/dejagnu.so

#--------------------------------------------------------------------

%package extension-mysql
Summary:   MySQL extension for Gnash
Group:     Development/Databases
Requires:  %{name} = %{version}-%{release}

%description extension-mysql
This extension allows SWF files being played within Gnash to have 
direct access to a MySQL database. 
The API is similar to the standard MySQL one.

%files extension-mysql
%doc COPYING
%{_libdir}/gnash/plugins/mysql.so

#--------------------------------------------------------------------


%prep
%setup -q -n %{dir_name}
%patch1 -p1 -b .manual~
%patch2 -p1 -b .gcc
%patch4 -p1 -b .CVE-2012-1175
%patch5 -p0 -b .link
%patch6 -p0 -b .giflib5
./autogen.sh

%build
%define _disable_ld_no_undefined 0

export CXXFLAGS="%{optflags} -Wc++0x-compat"
%configure2_5x --disable-static --with-npapi-plugindir=%{_libdir}/mozilla/plugins \
  --enable-extensions=fileio,lirc,dejagnu,mysql \
  --enable-renderer=all \
  --with-plugins-install=system \
  --disable-ghelp \
  --disable-rpath \
  --enable-gui=gtk,kde4,sdl,fb \
%if %{with_tests}
  --enable-testsuite \
%else
  --disable-testsuite \
  --without-swfdec-testsuite \
%endif
  --enable-media=gst \
  --enable-cygnal \
  --disable-dependency-tracking \
  --enable-python \
  --enable-doublebuf \
  --disable-jemalloc \
  --disable-docbook \
  --htmldir=%{_datadir}/gnash/html
   

%make

%if %{with_tests}
%make check
%endif

%install
make install install-plugins \
 DESTDIR=%{buildroot} INSTALL='install -p' \
 KDE4_PLUGINDIR=%{_kde_libdir}/kde4 \
 KDE4_SERVICESDIR=%{_kde_datadir}/kde4/services \
 KDE4_CONFIGDIR=%{_kde_configdir} \
 KDE4_APPSDATADIR=%{_kde_appsdir}/klash


#menu entry
desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	%{buildroot}%{_datadir}/applications/klash.desktop


rm -rf %{buildroot}/%{_localstatedir}/lib/scrollkeeper
rm -f %{buildroot}/%{_libdir}/mozilla/plugins/*.a
rm -f %{buildroot}/%{_libdir}/mozilla/plugins/*.la

%find_lang %{name}

