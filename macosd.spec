# TODO: optflags
Summary:	MacOSD - a visualization frontend for PBButtonsD
Summary(pl):	MacOSD - wizualny frontend dla PBButtonsD
Name:		macosd
Version:	0.3.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.exactcode.de/oss/macosd/%{name}-%{version}.tar.bz2
# Source0-md5:	6ae216880c061587e63dd40661d9c78a
URL:		http://www.exactcode.de/oss/macosd/
BuildRequires:	evas-devel >= 0.9.9
BuildRequires:	pbbuttonsd-lib
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	xosd-devel >= 2.2.0
Requires:	pbbuttonsd
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MacOSD is a visualization frontend for PBButtonsD, the button and
power event daemon used for Apple computers. It utilizes Evas with its
anti-aliasing and alpha-blending canvas capabilities for rendering.
The less-eye-candy-rich Xosd can also be used to render shaped windows
that work over video overlays. The theme format is
GtkPBButtons-compatible.

%description -l pl
MacOSD to frontend wizualizuj±cy dla PBButtonsD - demona obs³uguj±cego
przyciski i zdarzenia zwi±zane z zasilaniem u¿ywanego na komputerach
Apple. U¿ywa biblioteki Evas wraz z jej mo¿liwo¶ciami antyaliasingu i
alpha-blendingu przy rysowaniu. Ubo¿sze w bajery Xosd tak¿e mo¿e byæ
u¿ywane do rysowania okienek ponad obrazem. Format motywów jest
kompatybilny z GtkPBButtons.

%prep
%setup -q

%build
#configure
./configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
