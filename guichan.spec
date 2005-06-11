#
# Conditional build:
%bcond_with  	allegro     # with allegro
#
Summary:	Guichan - small, efficient C++ GUI library designed for games
Summary(pl):	Guichan - ma³a, wydajna biblioteka GUI w C++ przeznaczona do gier
Name:		guichan
Version:	0.4.0
Release:	0.1
License:	see COPYING
Group:		Libraries
Source0:	http://dl.sourceforge.net/guichan/%{name}-%{version}-src.tar.gz
# Source0-md5:	f68b6c603c4fb3d70a8737f916214a35
URL:		http://guichan.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL-devel
%{?with_allegro:BuildRequires:      allegro}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guichan is a small, efficient C++ GUI library designed for games. It
comes with a standard set of widgets and can use several different
objects for displaying graphics and grabbing user input.

%description -l pl
Guichan to ma³a, wydajna biblioteka GUI w C++ przeznaczona do gier.
Zawiera standardowy zestaw widgetów i mo¿e u¿ywaæ kilku ró¿nych
obiektów do wy¶wietlania grafiki i pobierania wej¶cia od u¿ytkownika.

%prep
%setup -q

%build
%configure
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
%doc COPYING AUTHORS ChangeLog README TODO NEWS
%attr(755,root,root) %{_libdir}/*
%{_includedir}/*
