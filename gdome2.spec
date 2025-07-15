#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	DOM level2 library for accessing XML files
Summary(pl.UTF-8):	Biblioteka dostępu do plików XML, DOM poziom 2
Name:		gdome2
Version:	0.8.1
Release:	17
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://gdome2.cs.unibo.it/tarball/%{name}-%{version}.tar.gz
# Source0-md5:	bfc114e59eec50cbda8e4ece751ff022
Patch0:		%{name}-glib2.patch
Patch1:		%{name}-build_fix.patch
Patch2:		format-security.patch
Patch3:		%{name}-destdir.patch
Patch4:		%{name}-no-common.patch
URL:		http://gdome2.cs.unibo.it/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.4.26
BuildRequires:	pkgconfig
Requires:	glib2 >= 2.2.0
Requires:	libxml2 >= 1:2.4.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdome2 is a fast, light and complete DOM level2 implementation based
on libxml2. Although it has been written for the GNOME project, it can
be used stand-alone.

A DOM implementation (also called a host implementation) is what makes
a parsed XML or HTML document available for processing via the DOM
interface.

gdome2 currently supports the "Core", "XML", "Events" and
"MutationEvents" modules from the DOM2 Recommendation (see
http://www.w3.org/TR/DOM-Level-2-Core/ and
http://www.w3.org/TR/DOM-Level-2-Events/), and is supposed to become a
full implementation of all the DOM Level2 standard.

Now gdome2 also partially supports the XPath module from the DOM level
3 drafts.

%description -l pl.UTF-8
gdome2 jest szybką, lekką i kompletną implementacją poziomu 2 DOM
opartą o libxml2. Pomimo, że gdome2 zostało napisane z myślą o
projekcie GNOME, może być używane samodzielnie.

Implementacja DOM (zwana również implementacją hosta) udostępnia
przeanalizowany składniowo dokument XML lub HTML w celu dalszego jego
przetwarzania poprzez interfejs DOM.

gdome2 w chwili obecnej wspiera następujące moduły rekomendacji DOM2:
"Core", "XML", "Events" oraz "MutationEvents" (więcej informacji można
uzyskać pod adresem http://www.w3.org/TR/DOM-Level-2-Core/ oraz
http://www.w3.org/TR/DOM-Level-2-Events/), a w przyszłości ma zostać
pełną implementacją standardu poziomu 2 DOM.

gdome2 wspiera również częściowo poziom 3 DOM, konkretnie XPath.

%package devel
Summary:	Development files for gdome2
Summary(pl.UTF-8):	Pliki nagłówkowe gdome2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	libxml2-devel >= 1:2.4.26

%description devel
This package contains the header files and configuration scripts for
developing with gdome2.

gdome2 is a fast, light and complete DOM level2 implementation based
on libxml2. Although it has been written for the GNOME project, it can
be used stand-alone.

A DOM implementation (also called a host implementation) is what makes
a parsed XML or HTML document available for processing via the DOM
interface.

gdome2 currently supports the "Core", "XML", "Events" and
"MutationEvents" modules from the DOM2 Recommendation (see
http://www.w3.org/TR/DOM-Level-2-Core/ and
http://www.w3.org/TR/DOM-Level-2-Events/), and is supposed to become a
full implementation of all the DOM Level2 standard.

Now gdome2 also partially supports the XPath module from the DOM level
3 drafts.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe oraz skrypty konfiguracyjne
potrzebne do rozwijania oprogramowania opartego o gdome2.

gdome2 jest szybką, lekką i kompletną implementacją poziomu 2 DOM
opartą o libxml2. Pomimo, że gdome2 zostało napisane z myślą o
projekcie GNOME, może być używane samodzielnie.

Implementacja DOM (zwana również implementacją hosta) udostępnia
przeanalizowany składniowo dokument XML lub HTML w celu dalszego jego
przetwarzania poprzez interfejs DOM.

gdome2 w chwili obecnej wspiera następujące moduły rekomendacji DOM2:
"Core", "XML", "Events" oraz "MutationEvents" (więcej informacji można
uzyskać pod adresem http://www.w3.org/TR/DOM-Level-2-Core/ oraz
http://www.w3.org/TR/DOM-Level-2-Events/), a w przyszłości ma zostać
pełną implementacją standardu poziomu 2 DOM.

gdome2 wspiera również częściowo poziom 3 DOM, konkretnie XPath.

%package static
Summary:	Static libraries for gdome2
Summary(pl.UTF-8):	Biblioteki statyczne dla gdome2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries for developing with gdome2.

%description static -l pl.UTF-8
Pakiet ten zawiera statyczne biblioteki potrzebne do rozwijania
oprogramowania opartego o gdome2.

%package apidocs
Summary:	API documentation for gdome2 library
Summary(pl.UTF-8):	Dokumentacja API biblioteki gdome2
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for gdome2 library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gdome2.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

# disable glib 1.x in order to force 2.x
echo 'AM_DEFUN([AM_PATH_GLIB], [$3])' >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdome.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS ChangeLog README
%attr(755,root,root) %{_libdir}/libgdome.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdome.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdome-config
%attr(755,root,root) %{_libdir}/libgdome.so
%attr(755,root,root) %{_libdir}/gdomeConf.sh
%{_includedir}/libgdome
%{_mandir}/man1/gdome-config.1*
%{_aclocaldir}/gdome2.m4
%{_pkgconfigdir}/gdome2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdome.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdome2-%{version}
