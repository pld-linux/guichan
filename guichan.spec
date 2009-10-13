# Conditional build:
%bcond_without	allegro     # without allegro support
#
Summary:	Guichan - small, efficient C++ GUI library designed for games
Summary(pl.UTF-8):	Guichan - mała, wydajna biblioteka GUI w C++ przeznaczona do gier
Name:		guichan
Version:	0.8.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://guichan.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	af535d7f387e774e3197cef8023ea105
URL:		http://guichan.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
%{?with_allegro:BuildRequires:      allegro-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Summary:	Static version of Guichan libraries
Summary(pl.UTF-8):	Statyczne wersje bibliotek Guichan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Guichan libraries.

%description static -l pl.UTF-8
Statyczne wersje bibliotek Guichan.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_allegro:--disable-allegro}
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libguichan*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguichan*.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan*.so
%{_libdir}/libguichan*.la
%{_includedir}/guichan*
%{_pkgconfigdir}/guichan*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libguichan*.a
