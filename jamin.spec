# TODO:
# - with liblo http://plugin.org.uk/liblo
# - correct install or send back to Moscow russian translation
#   (ALT got a patch for this)
#
Summary:	JAMin - JACK audio mastering interface
Summary(pl):	JAMin - nak³adka na JACK-a do masteringu d¼wiêku
Name:		jamin
Version:	0.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/jamin/%{name}-%{version}.tar.gz
# Source0-md5:	2c98cd525304c35f6b9f881209b5e6e4
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gcc34.patch
URL:		http://jamin.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-single-devel >= 3.0.1
BuildRequires:	gtk+2-devel >= 1.3.13
BuildRequires:	intltool
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5
Requires:	ladspa-swh-plugins >= 0.4.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JAMin is the JACK Audio Connection Kit Audio Mastering interface,
designed to perform professional audio mastering of any number of
input streams.

%description -l pl
JAMin jest nak³adk± na JACK Audio Connection Kit umo¿liwiaj±c±
profesjonalny mastering z dowolnej ilo¶ci ¼róde³ d¼wiêku.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --force --copy
intltoolize --copy --force --automake
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -c %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/jamin
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
