%define 	module	requests

Summary:	HTTP library for Python
Name:		python-%{module}
Version:	1.2.3
Release:	0.3
License:	Apache2
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/r/requests/%{module}-%{version}.tar.gz
# Source0-md5:	adbd3f18445f7fe5e77f65c502e264fb
URL:		http://python-requests.org
Patch0:		%{name}-system-cert.patch
Patch1:		%{name}-system-charade-and-urllib3.patch
BuildRequires:	python-charade
BuildRequires:	python-modules
BuildRequires:	python-urllib3
BuildRequires:	python3-charade
BuildRequires:	python3-modules
BuildRequires:	python3-urllib3
BuildRequires:	rpm-pythonprov
Requires:	ca-certificates
Requires:	python-charade
Requires:	python-modules
Requires:	python-urllib3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Requests is a HTTP library, written in Python, for human beings.

Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python's builtin urllib2 module provides most
of the HTTP capabilities you should need, but the API is thoroughly
broken. It requires an enormous amount of work (even method overrides)
to perform the simplest of tasks. Things shouldn't be this way. Not in
Python.

%package -n python3-requests
Summary:	HTTP library, written in Python, for human beings
Group:		Development/Languages/Python
Requires:	ca-certificates
Requires:	python3-charade
Requires:	python3-modules
Requires:	python3-urllib3

%description -n python3-requests
Requests is a HTTP library, written in Python, for human beings.

%prep
%setup -qn %{module}-%{version}
%patch0 -p1
%patch1 -p0

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%{__rm} -rf $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py3_sitescriptdir}}/%{module}/{cacert.pem,packages}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py_sitescriptdir}/%{module}

%files -n python3-requests
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py3_sitescriptdir}/%{module}

