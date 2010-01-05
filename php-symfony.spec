# TODO
# - use system creole, propel, phing packages (or better do not do that to avoid incompatibilities)
# - php deps autofinder finds a lot of crap (that's why we use manual R now), maybe there is a way to improve
%define		sname	symfony
Summary:	Open-source PHP web framework
Summary(pl.UTF-8):	Szkielet aplikacji WWW w PHP o otwartych źródłach
Name:		php-%{sname}
Version:	1.4.1
Release:	1
License:	various free licenses
Group:		Libraries
Source0:	http://www.symfony-project.org/get/symfony-%{version}.tgz
# Source0-md5:	b80e8efe2415d388480e8aea738b12b3
URL:		http://www.symfony-project.org/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	Smarty
Requires:	php-common
Requires:	php-ctype
Requires:	php-pear-Archive_Tar
Requires:	php-pear-Log
Requires:	php-pear-PEAR
Requires:	php-pear-PEAR-core
Requires:	php-pear-PEAR_PackageFileManager
Requires:	php-pear-PHPUnit2
Requires:	php-pear-VersionControl_SVN
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_data_dir}/%{sname}}

cp -a data lib $RPM_BUILD_ROOT%{php_data_dir}/%{sname}
ln -s %{php_data_dir}/%{sname}/data/bin/symfony $RPM_BUILD_ROOT%{_bindir}/%{sname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc licenses CHANGELOG COPYRIGHT LICENSE README
%attr(755,root,root) %{_bindir}/*
%dir %{php_data_dir}/%{sname}
%dir %{php_data_dir}/%{sname}/data
%dir %{php_data_dir}/%{sname}/data/bin
%attr(755,root,root) %{php_data_dir}/%{sname}/data/bin/*
%{php_data_dir}/%{sname}/data/[!b]*
%{php_data_dir}/%{sname}/lib
