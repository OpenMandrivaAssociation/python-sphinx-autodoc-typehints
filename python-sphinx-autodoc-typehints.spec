# Created by pyp2rpm-3.3.5
%global pypi_name sphinx-autodoc-typehints

Name:           python-%{pypi_name}
Version:        1.11.1
Release:        1
Summary:        Type hints (PEP 484) support for the Sphinx autodoc extension
Group:          Development/Python
License:        MIT
URL:            None
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(dataclasses)
BuildRequires:  python3dist(pytest) 
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 36.2.7
BuildRequires:  python3dist(setuptools-scm) >= 1.7
BuildRequires:  python3dist(sphinx) >= 3
BuildRequires:  python3dist(sphinx) >= 3.2
BuildRequires:  python3dist(sphobjinv) >= 2
BuildRequires:  python3dist(typed-ast) >= 1.4
BuildRequires:  python3dist(typing-extensions) >= 3.5

%description
sphinx-autodoc-typehints This extension allows you to use Python 3 annotations
for documenting acceptable argument types and return value types of functions.
This allows you to use type hints in a very natural fashion, allowing you to
migrate from this:.. code-block:: python def format_unit(value, unit): """
Formats the given value as a human readable string using the given units.
:param...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/sphinx_autodoc_typehints.py
%{python3_sitelib}/sphinx_autodoc_typehints-%{version}-py%{python3_version}.egg-info
