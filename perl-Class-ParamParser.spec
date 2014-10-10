%define	upstream_name    Class-ParamParser
%define	upstream_version 1.041

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DU/DUNCAND/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This Perl 5 object class implements two methods which inherited classes can use
to tidy up parameter lists for their own methods and functions.  The two
methods differ in that one returns a HASH ref containing named parameters and
the other returns an ARRAY ref containing positional parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.41.0-5mdv2011.0
+ Revision: 680825
- mass rebuild

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.41.0-4mdv2011.0
+ Revision: 505695
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.041-3mdv2010.0
+ Revision: 430332
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.041-2mdv2008.1
+ Revision: 136684
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 1.041-2mdv2007.0
+ Revision: 107894
- rebuilt
- using mkrel

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Class-ParamParser

* Thu Jul 21 2005 Andreas Hasenack <andreas@mandriva.com> 1.041-1mdk
- packaged for Mandriva

