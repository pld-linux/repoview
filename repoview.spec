Summary:	Create static HTML pages of a yum repository
Summary(pl.UTF-8):	Tworzenie statycznych stron HTML repozytorium yuma
Name:		repoview
Version:	0.6.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://icon.fedorapeople.org/repoview/%{name}-%{version}.tar.gz
# Source0-md5:	53422482361a9d45242caff7a8bce9a2
URL:		http://icon.fedorapeople.org/repoview/
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	python >= 2.4
Requires:	python-cElementTree
Requires:	python-kid >= 0.6.3
Requires:	yum >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
repoview allows to easily create a set of static HTML pages in a YUM
repository, allowing simple browsing of available packages. It uses
kid templating engine to create the pages and is therefore easily
customizeable.

%description -l pl.UTF-8
repoview pozwala łatwo tworzyć zbiór statycznych stron HTML w
repozytorium yuma, umożliwiając proste przeglądanie dostępnych
pakietów. Wykorzystuje do tworzenia stron silnik szablonów kid, więc
jest łatwo konfigurowalny.

%prep
%setup -q

%{__sed} -i -e '
	s|^\(VERSION\) = .*$|\1 = "%{version}"|g;
	s|^\(DEFAULT_TEMPLATEDIR\) =.*$|\1 = "%{_datadir}/repoview/templates"|g;
	' repoview.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/repoview,%{_mandir}/man8}
install repoview.py $RPM_BUILD_ROOT%{_bindir}/repoview
install repoview.8 $RPM_BUILD_ROOT%{_mandir}/man8/repoview.8
cp -a templates $RPM_BUILD_ROOT%{_datadir}/repoview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/repoview
%{_mandir}/man8/repoview.8*
%{_datadir}/repoview
