Summary:	Morphological analysis using a fast lookup transducer
Summary(pl.UTF-8):	Analiza morfologiczna przy użyciu szybko wyszukującego automatu z wyjściem
Name:		hfst-optimized-lookup
Version:	1.3
Release:	1
License:	Apache v2.0
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/hfst/%{name}-%{version}.tar.gz
# Source0-md5:	87e1084f716840e3a6ac050da15434a3
URL:		http://hfst.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a lookup implementation for a new transducer
format optimized for speed.

%description -l pl.UTF-8
Ten pakiet zawiera implementację wyszukiwania dla nowego formatu
automatów z wyjściem, zoptymalizowaną pod kątem szybkości.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/hfst-optimized-lookup
