%define module sphinx-autodoc-typehints
%define oname sphinx_autodoc_typehints
# tests disabled for abf
%bcond tests 1

Name:			python-sphinx-autodoc-typehints
Version:		3.13.0
Release:		1
Summary:		Type hints support for the Sphinx autodoc extension
Group:			Development/Python
License:		MIT
URL:			https://github.com/tox-dev/sphinx-autodoc-typehints
Source0:		https://github.com/tox-dev/sphinx-autodoc-typehints/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(setuptools-scm)
%if %{with tests}
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(defusedxml)
BuildRequires:	python%{pyver}dist(numpydoc)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-cov)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphobjinv)
BuildRequires:	python%{pyver}dist(typing-extensions)
%endif

%description
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

See an example of the Sphinx render at the pyproject-api docs.

This allows you to use type hints in a very natural fashion

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}"
# These either dont like running in mock or require internet access,
# skip all the failed tests.
skiptests+="not test_sphinx_output and not test_format_annotation"
skiptests+=" and not test_build_localns_adds_ancestor_classes"
skiptests+=" and not test_build_localns_preserves_existing_localns"
skiptests+=" and not test_namedtuple_no_forward_ref_warning"
skiptests+=" and not test_sphinx_build_stub_types_produce_crossrefs"
# Run pytest with --no-cov to disable upstream coverage checks.
# We have to BR pytest-cov in order to use the --no-cov flag to disable
# coverage checks which is a complete nonsense. It is what it is.
pytest --no-cov -k "$skiptests"
%endif

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
