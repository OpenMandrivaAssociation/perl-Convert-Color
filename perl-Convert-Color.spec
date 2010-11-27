%define upstream_name    Convert-Color
%define upstream_version 0.07

%define _requires_exceptions perl(Convert::Color::HueBased)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A color value represented as red/green/blue in
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(List::UtilsBy)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


