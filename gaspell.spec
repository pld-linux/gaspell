%define	name	gaspell
%define	version	.28.5
%define	release	1
%define	serial	1

Summary:	Gnome frontend to the Aspell library.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Applications/Text
URL:		http://metalab.unc.edu/kevina/aspell
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}
Requires:	aspell

Distribution:	Freshmeat RPMs
Packager:	Ryan Weaver <ryanw@infohwy.com>

%description
Gnome frontend to the Aspell library. Or put another way a simple
spell checker that does a way better job than ispell does with coming
up with suggestions.

%prep
%setup -q

%build
make CXXFLAGS=$RPM_OPT_FLAGS ASPELL_PREFIX=/usr

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -s -m 755 gaspell $RPM_BUILD_ROOT/usr/bin

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
%doc ChangeLog README TODO
/usr/bin/gaspell

%changelog
* Mon Sep 27 1999 Ryan Weaver <ryanw@infohwy.com>
  [gaspell-.28.5-1]
- Added the ability to lookup the definition of a suggestion using
  the WordNet definitions form a DICT server.

* Thu Jul 29 1999 Ryan Weaver <ryanw@infohwy.com>
  [gaspell-.28.2-1]
- Reverted to Gaspell .28 code as my bug fixed now causes Gaspell to
  randomly crash when the text is unhighlighted. I then fixed the bug
  in .28 by a cheap hack. I hope eventually find out what is really going on.
- Changed the text window to use word wrap.

* Wed Jul 28 1999 Ryan Weaver <ryanw@infohwy.com>
  [gaspell-.28.1-1]
- Fixed a bug that caused gaspell to dump core when clearing a
  file that has a word highlighted in red.

* Mon Jul 26 1999 Ryan Weaver <ryanw@infohwy.com>
  [gaspell-.28-1]
- Fixed the code so that it would word with aspell .28
- Fixed the code so that it will provide an nice error message
  if there is a problem duren startup rather than just
  dumping core.
- Re did the command line options a bit

  [gaspell-.27-1]
- Fixed code so that it would work with aspell .27
- Added support for Aspell URL skip mode.
- Added an option to not save personal dictionaries on exit.

  [gaspell-.26-1]
- First real release
