Summary:	DOM level2 library for accessing XML files
Summary(pl):	Biblioteka dostêpu do plików XML, DOM poziom 2
Name:		gdome2
Version:	0.7.1
Release:	1
License:	LGPL
Group:		Libraries
URL:		http://phd.cs.unibo.it/gdome2/
Source0:	http://phd.cs.unibo.it/gdome2/tarball/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
BuildRequires:	libxml2-devel >= 2.4.19
BuildRequires:	glib-devel >= 1.2.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	glib >= 1.2.10
Requires:	libxml2 >= 2.4.19
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
gdome2 jest szybk±, lekk± i kompletn± implementacj± DOM poziom 2
opart± o libxml2. Pomimo, ¿e gdome2 zosta³o napisane z my¶l± o
projekcie GNOME mo¿e byæ u¿ywane samodzielnie.

Implementacja DOM (zwana równie¿ implementacj± hosta) udostêpnia
przeparsowany dokument XML lub HTML dla dalszego przetwarzania poprzez
interfejs DOM.

gdome2 w chwili obecnej wspiera nastêpuj±ce modu³y rekomendacji DOM2:
"Core", "XML", "Events" oraz "MutationEvents" (wiêcej informacji mo¿na
uzyskaæ pod adresem http://www.w3.org/TR/DOM-Level-2-Core/ oraz
http://www.w3.org/TR/DOM-Level-2-Events/), a w przysz³o¶ci ma zostaæ
pe³n± implementacj± standardu DOM Poziom 2.

gdome2 wspiera równie¿ czê¶ciowo DOM Poziom 3, konkretnie XPath.

%package devel
Summary:	Development files for gdome2
Summary(pl):	Pliki nag³ówkowe gdome2
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib-devel >= 1.2.10
Requires:	libxml2-devel >= 2.4.19

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

%description -l pl
Pakiet ten zawiera pliki nag³ówkowe oraz skrypty konfiguracyjne
potrzebne do rozwiajania oprogramowania opartego o gdome2.

gdome2 jest szybk±, lekk± i kompletn± implementacj± DOM poziom 2
opart± o libxml2. Pomimo, ¿e gdome2 zosta³o napisane z my¶l± o
projekcie GNOME mo¿e byæ u¿ywane samodzielnie.

Implementacja DOM (zwana równie¿ implementacj± hosta) udostêpnia
przeparsowany dokument XML lub HTML dla dalszego przetwarzania poprzez
interfejs DOM.

gdome2 w chwili obecnej wspiera nastêpuj±ce modu³y rekomendacji DOM2:
"Core", "XML", "Events" oraz "MutationEvents" (wiêcej informacji mo¿na
uzyskaæ pod adresem http://www.w3.org/TR/DOM-Level-2-Core/ oraz
http://www.w3.org/TR/DOM-Level-2-Events/), a w przysz³o¶ci ma zostaæ
pe³n± implementacj± standardu DOM Poziom 2.

gdome2 wspiera równie¿ czê¶ciowo DOM Poziom 3, konkretnie XPath.

%package static
Summary:	Static libraries for gdome2
Summary(pl):	Biblioteki statyczne dla gdome2
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib-devel >= 1.2.10
Requires:	libxml2-devel >= 2.4.19

%description static
This package contains static libraries for developing with gdome2.

%description static -l pl
Pakiet ten zawiera statyczne biblioteki potrzebne do rozwiajania
oprogramowania opartego o gdome2.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
%{__autoconf}
automake -a -c

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS ChangeLog README gtk-doc/html/*.html
%attr(755,root,root) %{_bindir}/gdome-config
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/*.sh
%{_mandir}/man1/gdome-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
