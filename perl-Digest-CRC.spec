#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	CRC
Summary:	Digest::CRC - Generic CRC functions
Summary(pl):	Digest::CRC - podstawowe funkcje CRC
Name:		perl-%{pdir}-%{pnam}
Version:	0.09
Release:	1
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1456ba664d59a7ccc7d30e980f1695d0
URL:		http://search.cpan.org/dist/Digest-CRC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains
wrapper functions with the correct parameters for CRC-CCITT, CRC-16
and CRC-32.

%description -l pl
Modu³ Digest::CRC oblicza ró¿nego rodzaju sumy kontrolne CRC. Posiada
funkcje - wrappery z odpowiednimi parametrami dla CRC-CCITT, CRC-16
oraz CRC-32.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Digest/*.pm
%{_mandir}/man3/*
