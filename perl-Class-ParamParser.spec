%define	upstream_name    Class-ParamParser
%define upstream_version 1.041
Name:		perl-%{upstream_name}
Version:	1.041
Release:	1

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Class-ParamParser
Source0:	https://cpan.metacpan.org/authors/id/D/DU/DUNCAND/Class-ParamParser-1.041.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This Perl 5 object class implements two methods which inherited classes can use
to tidy up parameter lists for their own methods and functions.  The two
methods differ in that one returns a HASH ref containing named parameters and
the other returns an ARRAY ref containing positional parameters.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog ReadMe
%{perl_vendorlib}/Class/ParamParser.pm
%{_mandir}/*/*


