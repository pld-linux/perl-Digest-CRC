#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	CRC
Summary:	Digest::CRC - Generic CRC functions
Summary(pl.UTF-8):	Digest::CRC - podstawowe funkcje CRC
Name:		perl-Digest-CRC
Version:	0.18
Release:	6
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	baf8cb6c50782416b10f470b2e29bf7a
URL:		http://search.cpan.org/dist/Digest-CRC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains
wrapper functions with the correct parameters for CRC-CCITT, CRC-16
and CRC-32.

%description -l pl.UTF-8
Moduł Digest::CRC oblicza różnego rodzaju sumy kontrolne CRC. Posiada
funkcje - wrappery z odpowiednimi parametrami dla CRC-CCITT, CRC-16
oraz CRC-32.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%dir %{perl_vendorarch}/auto/Digest/CRC
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/CRC/CRC.so
%{_mandir}/man3/*
