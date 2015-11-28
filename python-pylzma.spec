%define 	module	pylzma
Summary:	Platform independent python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.3.0
Release:	3
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{module}-%{version}.tar.gz/download
# Source0-md5:	7ab1a1706cf3e19f2d10579d795babf7
URL:		http://www.joachim-bauch.de/projects/python/pylzma/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform independent python bindings for the LZMA compression library.

Features:
- Compression / decompression of a single block of data
- Compression from a file-like object (must provide a read method)
- Streaming decompression through multiple calls to decompress
- An initial library that supports reading of 7-zip archives (both
  solid and non-solid)
- Working on 32-bit Windows and Linux as well as AMD64 on Linux
- Multithreaded compression on Windows
- Built with 7-zip 4.42

%prep
%setup -q -n %{module}-%{version}

%build
%py_build \
	--debug

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%py_install

%py_comp $RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/usage.txt
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%{py_sitedir}/pylzma-*.egg-info
