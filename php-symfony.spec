%include	/usr/lib/rpm/macros.php
%define	sname	symfony
Summary:	open-source PHP web framework
Name:		php-%{sname}
Version:	1.0.3
Release:	1
License:	various free licenses
Group:		Libraries
Source0:	http://www.symfony-project.com/get/symfony-stable.tgz
# Source0-md5:	13f22e83634dc8fc8ba8b52a582a4d74
URL:		http://www.symfony-project.com/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
Based on the best practices of web development, thoroughly tried on several active websites, symfony aims to speed up the creation and maintenance of web applications, and to replace the repetitive coding tasks by power, control and pleasure.

Symfony provides a lot of features seamlessly integrated together, such as:
- simple templating and helpers
- cache management
- smart URLs
- scaffolding
- multilingualism and I18N support
- object model and MVC separation
- Ajax support 
- enterprise ready

%prep
%setup  -q -n %{sname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_phpsharedir}/%{sname}}

mv doc/LICENSE doc/LICENSE.doc

cp -a data lib $RPM_BUILD_ROOT%{_phpsharedir}/%{sname}
ln -s %{_phpsharedir}/%{sname}/data/bin/symfony $RPM_BUILD_ROOT%{_bindir}/%{sname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* licenses COPYRIGHT LICENSE README
%attr(755,root,root) %{_bindir}/*
%dir %{_phpsharedir}/%{sname}
%dir %{_phpsharedir}/%{sname}/data
%dir %{_phpsharedir}/%{sname}/data/bin
%attr(755,root,root) %{_phpsharedir}/%{sname}/data/bin/*
%{_phpsharedir}/%{sname}/data/[^b]*
%{_phpsharedir}/%{sname}/lib
