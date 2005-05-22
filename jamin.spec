Summary:	JAMin - JACK audio mastering interface
Summary(pl):	JAMin - nak³adka na JACK-a do masteringu d¼wiêku
Name:		jamin
Version:	0.95.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/sourceforge/jamin/%{name}-%{version}.tar.gz
# Source0-md5:	032f2a4a578a8938f76282112d56c8d6
Source1:	%{name}.png
URL:		http://jamin.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-single-devel >= 3.0.1
BuildRequires:	gtk+2-devel >= 1.3.13
BuildRequires:	intltool
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	liblo-devel >= 0.18
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
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

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	plugindir=%{_libdir}/ladspa

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_libdir}/ladspa

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/jamin.svg
rm -f $RPM_BUILD_ROOT%{_libdir}/ladspa/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
update-mime-database %{_datadir}/mime ||:
%update_desktop_database_post

%postun
umask 022
update-mime-database %{_datadir}/mime
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/jamin
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*.desktop
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
