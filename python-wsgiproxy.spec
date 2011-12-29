%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-wsgiproxy
Version:        0.2
Release:        1%{?dist}
Summary:        HTTP proxying tools for WSGI apps

Group:          Development/Languages
License:        MIT
URL:            http://pythonpaste.org/wsgiproxy/
Source0:        http://pypi.python.org/packages/source/W/WSGIProxy/WSGIProxy-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  python-setuptools-devel
Requires:       python-paste
Requires:       python-paste-deploy

%description
WSGIProxy gives tools to proxy arbitrary(ish) WSGI requests to other
processes over HTTP.


%prep
%setup -q -n WSGIProxy-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

 
%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/wsgiproxy
%{python_sitelib}/*.egg-info


%changelog
* Thu Nov 19 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.2-1
- Upstream released a new version.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.1-4
- Change define to global.
- Remove old >= 8 conditional.
- Remove unnecessary BuildRequires on python-devel.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-2
- Rebuild for Python 2.6

* Sat Jun 14 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.1-1
- Initial RPM Package.
