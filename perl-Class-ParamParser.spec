%define	real_name Class-ParamParser
%define	name	perl-%{real_name}
%define	version	1.041
%define	release	2

Summary:	CPAN %{real_name} perl module
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/D/DU/DUNCAND/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This Perl 5 object class implements two methods which inherited classes can use
to tidy up parameter lists for their own methods and functions.  The two
methods differ in that one returns a HASH ref containing named parameters and
the other returns an ARRAY ref containing positional parameters.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog ReadMe
%{perl_vendorlib}/Class/ParamParser.pm
%{_mandir}/*/*


