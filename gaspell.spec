Summary:	Gnome frontend to the Aspell library
Summary(pl):	Frontend Gnome do biblioteki aspell
Name:		gaspell
Version:	.28.5
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source0:	http://aspell.sourceforge.net/%{name}-%{version}.tar.gz
URL:		http://aspell.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	aspell

%description
Gnome frontend to the Aspell library. Or put another way a simple
spell checker that does a way better job than ispell does with coming
up with suggestions.

%description -l pl
Gaspell to interfejs (frontend) do biblioteki Aspell. Innymi s³owy
jest to narzedzie do sprawdzania pisownie które o wiele lepiej ni¿
ispell radzi sobie z propozycjami wymienników.

%prep
%setup -q

%build
%{__make} CXXFLAGS="%{rpmcflags}" ASPELL_PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gaspell $RPM_BUILD_ROOT%{_bindir}

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.gz README.gz TODO.gz
%attr(755,root,root) %{_bindir}/gaspell
