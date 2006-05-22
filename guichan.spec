#
# Conditional build:
%bcond_with	allegro     # with allegro support (doesn't build)
#
Summary:	Guichan - small, efficient C++ GUI library designed for games
Summary(pl):	Guichan - ma³a, wydajna biblioteka GUI w C++ przeznaczona do gier
Name:		guichan
Version:	0.4.0
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/guichan/%{name}-%{version}-src.tar.gz
# Source0-md5:	f68b6c603c4fb3d70a8737f916214a35
Patch0:		%{name}-configure.patch
URL:		http://guichan.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
%{?with_allegro:BuildRequires:      allegro-devel}
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guichan is a small, efficient C++ GUI library designed for games. It
comes with a standard set of widgets and can use several different
objects for displaying graphics and grabbing user input.

%description -l pl
Guichan to ma³a, wydajna biblioteka GUI w C++ przeznaczona do gier.
Zawiera standardowy zestaw widgetów, mo¿e u¿ywaæ kilku ró¿nych
obiektów do wy¶wietlania grafiki i pobierania wej¶cia od u¿ytkownika.

%package devel
Summary:	Header files for Guichan library
Summary(pl):	Pliki nag³ówkowe biblioteki Guichan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for Guichan library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Guichan.

%package static
Summary:	Static version of Guichan libraries
Summary(pl):	Statyczne wersje bibliotek Guichan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Guichan libraries.

%description static -l pl
Statyczne wersje bibliotek Guichan.

%prep
%setup -q

%patch0 -p1

%build
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguichan*.so
%{_libdir}/libguichan*.la
%{_includedir}/guichan*

%files static
%defattr(644,root,root,755)
%{_libdir}/libguichan*.a
