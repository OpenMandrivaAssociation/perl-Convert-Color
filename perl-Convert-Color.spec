%define upstream_name    Convert-Color
%define upstream_version 0.08

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Convert::Color::HueBased\\)'
%else
%define %define _requires_exceptions perl(Convert::Color::HueBased)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A color value represented as red/green/blue in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(List::UtilsBy)
BuildArch:	noarch

%description
This module provides conversions between commonly used ways to express
colors. It provides conversions between color spaces such as RGB and HSV,
and it provides ways to look up colors by a name.

This class provides a base for subclasses which represent particular color
values in particular spaces. The base class provides methods to represent
the color in a few convenient forms, though subclasses may provide more
specific details for the space in question.

For more detail, read the documentation on these classes; namely:

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 659890
- update to new version 0.08

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2
+ Revision: 656894
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 602097
- new version

* Sun Aug 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 419898
- adding requires exception

* Sun Aug 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 419897
- import perl-Convert-Color


* Sun Aug 23 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
