Summary:	Create static HTML pages of a yum repository
Summary(pl):	Tworzenie statycznych stron HTML repozytorium yuma
Name:		repoview
Version:	0.5.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/mini/repoview/download/%{name}-%{version}.tar.gz
# Source0-md5:	b9568d9b71df1ee9628592b557d2b981
URL:		http://linux.duke.edu/projects/mini/repoview/
Requires:	python >= 2.2
Requires:	python-cElementTree
Requires:	python-kid
Requires:	yum >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
repoview allows to easily create a set of static HTML pages in a YUM
repository, allowing simple browsing of available packages. It uses
kid templating engine to create the pages and is therefore easily
customizeable.

%description -l pl
repoview pozwala ³atwo tworzyæ zbiór statycznych stron HTML w
repozytorium yuma, umo¿liwiaj±c proste przegl±danie dostêpnych
pakietów. Wykorzystuje do tworzenia stron silnik szablonów kid, wiêc
jest ³atwo konfigurowalny.

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
