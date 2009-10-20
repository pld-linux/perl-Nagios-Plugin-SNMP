#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Nagios
%define	pnam	Plugin-SNMP
Summary:	Nagios::Plugin::SNMP - Helper module to make writing SNMP-based plugins for Nagios easier.
Name:		perl-Nagios-Plugin-SNMP
Version:	1.2
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Nagios/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	478395097864e5130c2d44149a331882
URL:		http://search.cpan.org/dist/Nagios-Plugin-SNMP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Helper module to make writing SNMP-based plugins for Nagios easier.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Nagios/Plugin/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
