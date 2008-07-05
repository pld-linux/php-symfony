%include	/usr/lib/rpm/macros.php
%define	sname	symfony
Summary:	Open-source PHP web framework
Summary(pl.UTF-8):	Szkielet aplikacji WWW w PHP o otwartych źródłach
Name:		php-%{sname}
Version:	1.1.0
Release:	2
License:	various free licenses
Group:		Libraries
Source0:	http://www.symfony-project.org/get/symfony-%{version}.tgz
# Source0-md5:	cc148058e555303ed155f3141687da49
URL:		http://www.symfony-project.com/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common
Requires:	Smarty
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# deps already provided by this package or broken deps (dir mismatches)
%define		_noautoreq	'pear(propel/.*)' 'pear(phing/.*)' 'pear(creole/.*)' 'pear(.*SYMFONY_LIB_DIR.*)' 'pear(Smarty.class.php)' 'pear('simpletest/.*)'

%define		_phpsharedir	%{_datadir}/php

%description
Based on the best practices of web development, thoroughly tried on
several active websites, symfony aims to speed up the creation and
maintenance of web applications, and to replace the repetitive coding
tasks by power, control and pleasure.

Symfony provides a lot of features seamlessly integrated together,
such as:
- simple templating and helpers
- cache management
- smart URLs
- scaffolding
- multilingualism and I18N support
- object model and MVC separation
- Ajax support
- enterprise ready

%description -l pl.UTF-8
Oparty na najlepszych praktykach tworzenia aplikacji WWW, gruntownie
wypróbowany na kilku aktywnych serwisach moduł symfony próbuje
przyspieszyć tworzenie i utrzymywanie aplikacji WWW oraz zastąpić
powtarzające się zadania kodowania potęgą, kontrolą i przyjemnością.

Symfony udostępnia wiele zintegrowanych w sposób przezroczysty cech,
takich jak:
- proste szablony i odwołania
- zarządzanie pamięcią podręczną
- inteligentne URL-e
- scaffolding
- obsługa wielojęzyczności i międzynarodowości
- rozdzielenie modelu obiektowego i MVC
- obsługa AJAX
- gotowość na zastosowania enterprise

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
%{_phpsharedir}/%{sname}/data/[!b]*
%{_phpsharedir}/%{sname}/lib
