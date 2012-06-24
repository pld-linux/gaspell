Summary:	Gnome frontend to the Aspell library
Name:		gaspell
Version:	.28.5
Release:	1
License:	GPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narz�dzia/Tekst
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source0:	%{name}-%{version}.tar.gz
URL:		http://metalab.unc.edu/kevina/aspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	aspell

%description
Gnome frontend to the Aspell library. Or put another way a simple
spell checker that does a way better job than ispell does with coming
up with suggestions.

%description -l pl
Gaspell to interfejs (frontend) do biblioteki Aspell. Innymi s�owy
jest to narzedzie do sprawdzania pisownie kt�re o wiele lepiej ni�
ispell radzi sobie z propozycjami wymiennik�w.

%prep
%setup -q

%build
make CXXFLAGS=$RPM_OPT_FLAGS ASPELL_PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s gaspell $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gaspell
