#
# Conditional build:
%bcond_without	allegro     # allegro support
#
Summary:	Guichan - small, efficient C++ GUI library designed for games
Summary(pl.UTF-8):	Guichan - mała, wydajna biblioteka GUI w C++ przeznaczona do gier
Name:		guichan
Version:	0.8.2
Release:	4
License:	BSD
Group:		Libraries
# NOTE: now sources available at https://github.com/wheybags/guichan
Source0:	http://guichan.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	af535d7f387e774e3197cef8023ea105
Patch0:		link.patch
URL:		http://guichan.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
%{?with_allegro:BuildRequires:      allegro-devel}
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guichan is a small, efficient C++ GUI library designed for games. It
comes with a standard set of widgets and can use several different
objects for displaying graphics and grabbing user input.

%description -l pl.UTF-8
Guichan to mała, wydajna biblioteka GUI w C++ przeznaczona do gier.
Zawiera standardowy zestaw widgetów, może używać kilku różnych
obiektów do wyświetlania grafiki i pobierania wejścia od użytkownika.

%package devel
Summary:	Header files for Guichan library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Guichan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for Guichan library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Guichan.

%package static
Summary:	Static version of Guichan library
Summary(pl.UTF-8):	Statyczna wersja biblioteki Guichan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Guichan library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki Guichan.

%package allegro
Summary:	Guichan Allegro interface library
Summary(pl.UTF-8):	Biblioteka interfejsu Guichan do Allegro
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description allegro
Guichan Allegro interface library.

%description allegro -l pl.UTF-8
Biblioteka interfejsu Guichan do Allegro.

%package allegro-devel
Summary:	Header files for Guichan Allegro library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Guichan Allegro
Group:		Development/Libraries
Requires:	%{name}-allegro = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	allegro-devel

%description allegro-devel
Header files for Guichan Allegro library.

%description allegro-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Guichan Allegro.

%package allegro-static
Summary:	Static Guichan Allegro library
Summary(pl.UTF-8):	Statyczna biblioteka Guichan Allegro
Group:		Development/Libraries
Requires:	%{name}-allegro-devel = %{version}-%{release}

%description allegro-static
Static Guichan Allegro library.

%description allegro-static -l pl.UTF-8
Statyczna biblioteka Guichan Allegro.

%package opengl
Summary:	Guichan OpenGL interface library
Summary(pl.UTF-8):	Biblioteka interfejsu Guichan do OpenGL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description opengl
Guichan OpenGL interface library.

%description opengl -l pl.UTF-8
Biblioteka interfejsu Guichan do OpenGL.

%package opengl-devel
Summary:	Header files for Guichan OpenGL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Guichan OpenGL
Group:		Development/Libraries
Requires:	%{name}-opengl = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-devel
# can also use allegro-devel+allegro-addons-devel or -sdl for image loading

%description opengl-devel
Header files for Guichan OpenGL library.

%description opengl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Guichan OpenGL.

%package opengl-static
Summary:	Static Guichan OpenGL library
Summary(pl.UTF-8):	Statyczna biblioteka Guichan OpenGL
Group:		Development/Libraries
Requires:	%{name}-opengl-devel = %{version}-%{release}

%description opengl-static
Static Guichan OpenGL library.

%description opengl-static -l pl.UTF-8
Statyczna biblioteka Guichan OpenGL.

%package sdl
Summary:	Guichan SDL interface library
Summary(pl.UTF-8):	Biblioteka interfejsu Guichan do SDL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sdl
Guichan SDL interface library.

%description sdl -l pl.UTF-8
Biblioteka interfejsu Guichan do SDL.

%package sdl-devel
Summary:	Header files for Guichan SDL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Guichan SDL
Group:		Development/Libraries
Requires:	%{name}-sdl = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	SDL-devel

%description sdl-devel
Header files for Guichan SDL library.

%description sdl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Guichan SDL.

%package sdl-static
Summary:	Static Guichan SDL library
Summary(pl.UTF-8):	Statyczna biblioteka Guichan SDL
Group:		Development/Libraries
Requires:	%{name}-sdl-devel = %{version}-%{release}

%description sdl-static
Static Guichan SDL library.

%description sdl-static -l pl.UTF-8
Statyczna biblioteka Guichan SDL.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_allegro:--disable-allegro}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	allegro -p /sbin/ldconfig
%postun	allegro -p /sbin/ldconfig

%post	opengl -p /sbin/ldconfig
%postun	opengl -p /sbin/ldconfig

%post	sdl -p /sbin/ldconfig
%postun	sdl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libguichan-0.8.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguichan-0.8.1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan.so
%{_libdir}/libguichan.la
%{_includedir}/guichan.hpp
%dir %{_includedir}/guichan
%{_includedir}/guichan/*.hpp
%exclude %{_includedir}/guichan/allegro.hpp
%exclude %{_includedir}/guichan/opengl.hpp
%exclude %{_includedir}/guichan/sdl.hpp
%{_includedir}/guichan/widgets
%{_pkgconfigdir}/guichan-0.8.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libguichan.a

%if %{with allegro}
%files allegro
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan_allegro-0.8.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguichan_allegro-0.8.1.so.1

%files allegro-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan_allegro.so
%{_libdir}/libguichan_allegro.la
%{_includedir}/guichan/allegro.hpp
%{_includedir}/guichan/allegro

%files allegro-static
%defattr(644,root,root,755)
%{_libdir}/libguichan_allegro.a
%endif

%files opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan_opengl-0.8.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguichan_opengl-0.8.1.so.1

%files opengl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan_opengl.so
%{_libdir}/libguichan_opengl.la
%{_includedir}/guichan/opengl.hpp
%{_includedir}/guichan/opengl
%{_pkgconfigdir}/guichan_opengl-0.8.pc

%files opengl-static
%defattr(644,root,root,755)
%{_libdir}/libguichan_opengl.a

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan_sdl-0.8.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguichan_sdl-0.8.1.so.1

%files sdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan_sdl.so
%{_libdir}/libguichan_sdl.la
%{_includedir}/guichan/sdl.hpp
%{_includedir}/guichan/sdl
%{_pkgconfigdir}/guichan_sdl-0.8.pc

%files sdl-static
%defattr(644,root,root,755)
%{_libdir}/libguichan_sdl.a
