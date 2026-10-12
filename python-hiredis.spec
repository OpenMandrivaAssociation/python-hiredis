Name:		python-hiredis
Version:	3.3.1
Release:	2
Summary:	Python wrapper for hiredis
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/hiredis/
Source0:	hiredis-3.3.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	gcc
BuildRequires:	lib64python-devel
%description
Python wrapper for hiredis.

%files
%{python_sitearch}/*
