
%define		ver	.30

Summary:	GNOME frontend to the Aspell library
Summary(pl):	Frontend GNOME do biblioteki aspell
Name:		gaspell
Version:	0%{ver}
Release:	1
License:	GPL
Group:		Applications/Text
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source0:	http://aspell.sourceforge.net/%{name}-%{ver}.tar.gz
# Source0-md5:	c1fe839bda64b16a9a610f2f8564ef66
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	aspell


%description
GNOME frontend to the Aspell library. Or put another way a simple
spell checker that does a way better job than ispell does with coming
up with suggestions.

%description -l pl
Gaspell to interfejs (frontend) do biblioteki Aspell. Innymi s³owy
jest to narzedzie do sprawdzania pisownie które o wiele lepiej ni¿
ispell radzi sobie z propozycjami wymienników.

%prep
%setup -q -n %{name}-%{ver}

%build
%{__make} CXXFLAGS="%{rpmcflags}" ASPELL_PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

install gaspell $RPM_BUILD_ROOT%{_bindir}
install gaspell.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gaspell
%{_applnkdir}/Utilities/gaspell.desktop
