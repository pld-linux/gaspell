Summary:	Gnome frontend to the Aspell library.
Name:		gaspell
Version:	.28.5
Release:	1
License:	GPL
Group:		Applications/Text
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source:		%{name}-%{version}.tar.gz
URL:		http://metalab.unc.edu/kevina/aspell
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	aspell

%description
Gnome frontend to the Aspell library. Or put another way a simple spell
checker that does a way better job than ispell does with coming up with
suggestions.

%description -l pl
Gaspell to interfejs (frontend) do biblioteki Aspell. Innymi s³owy jest to
narzedzie do sprawdzania pisownie które o wiele lepiej ni¿ ispell radzi sobie
z propozycjami wymienników.

%prep
%setup -q

%build
make CXXFLAGS=$RPM_OPT_FLAGS ASPELL_PREFIX=/usr

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
install -d $RPM_BUILD_ROOT/usr/bin
install -s -m 755 gaspell $RPM_BUILD_ROOT/usr/bin

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
/usr/bin/gaspell
