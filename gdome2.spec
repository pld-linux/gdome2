Summary:	DOM level2 library for accessing XML files
Summary(pl):	Biblioteka dostêpu do plików XML, DOM poziom 2
Name:		gdome2
Version:	0.8.1
Release:	6
License:	LGPL
Group:		Libraries
Source0:	http://gdome2.cs.unibo.it/tarball/%{name}-%{version}.tar.gz
# Source0-md5:	bfc114e59eec50cbda8e4ece751ff022
Patch0:		%{name}-glib2.patch
URL:		http://gdome2.cs.unibo.it/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.26
BuildRequires:	pkgconfig
Requires:	libxml2 >= 2.4.26
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

%description -l pl
gdome2 jest szybk±, lekk± i kompletn± implementacj± poziomu 2 DOM
opart± o libxml2. Pomimo, ¿e gdome2 zosta³o napisane z my¶l± o
projekcie GNOME, mo¿e byæ u¿ywane samodzielnie.

Implementacja DOM (zwana równie¿ implementacj± hosta) udostêpnia
przeanalizowany sk³adniowo dokument XML lub HTML w celu dalszego
jego przetwarzania poprzez interfejs DOM.

gdome2 w chwili obecnej wspiera nastêpuj±ce modu³y rekomendacji DOM2:
"Core", "XML", "Events" oraz "MutationEvents" (wiêcej informacji mo¿na
uzyskaæ pod adresem http://www.w3.org/TR/DOM-Level-2-Core/ oraz
http://www.w3.org/TR/DOM-Level-2-Events/), a w przysz³o¶ci ma zostaæ
pe³n± implementacj± standardu poziomu 2 DOM.

gdome2 wspiera równie¿ czê¶ciowo poziom 3 DOM, konkretnie XPath.

%package devel
Summary:	Development files for gdome2
Summary(pl):	Pliki nag³ówkowe gdome2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	libxml2-devel >= 2.4.26

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

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe oraz skrypty konfiguracyjne
potrzebne do rozwijania oprogramowania opartego o gdome2.

gdome2 jest szybk±, lekk± i kompletn± implementacj± poziomu 2 DOM
opart± o libxml2. Pomimo, ¿e gdome2 zosta³o napisane z my¶l± o
projekcie GNOME, mo¿e byæ u¿ywane samodzielnie.

Implementacja DOM (zwana równie¿ implementacj± hosta) udostêpnia
przeanalizowany sk³adniowo dokument XML lub HTML w celu dalszego
jego przetwarzania poprzez interfejs DOM.

gdome2 w chwili obecnej wspiera nastêpuj±ce modu³y rekomendacji DOM2:
"Core", "XML", "Events" oraz "MutationEvents" (wiêcej informacji mo¿na
uzyskaæ pod adresem http://www.w3.org/TR/DOM-Level-2-Core/ oraz
http://www.w3.org/TR/DOM-Level-2-Events/), a w przysz³o¶ci ma zostaæ
pe³n± implementacj± standardu poziomu 2 DOM.

gdome2 wspiera równie¿ czê¶ciowo poziom 3 DOM, konkretnie XPath.

%package static
Summary:	Static libraries for gdome2
Summary(pl):	Biblioteki statyczne dla gdome2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries for developing with gdome2.

%description static -l pl
Pakiet ten zawiera statyczne biblioteki potrzebne do rozwijania
oprogramowania opartego o gdome2.

%prep
%setup -q
%patch0 -p1

echo 'AM_DEFUN([AM_PATH_GLIB], [$3])' >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

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
%doc AUTHORS MAINTAINERS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc gtk-doc/html/*.html
%attr(755,root,root) %{_bindir}/gdome-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/libgdome
%{_mandir}/man1/gdome-config.1*
%{_aclocaldir}/%{name}.m4
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
