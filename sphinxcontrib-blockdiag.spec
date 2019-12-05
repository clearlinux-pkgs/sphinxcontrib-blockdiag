#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-blockdiag
Version  : 1.5.5
Release  : 19
URL      : https://files.pythonhosted.org/packages/04/50/7a43117a5a8a16acaceabc5ad69092fa1dacb11ef83c84fdf234e5a3502f/sphinxcontrib-blockdiag-1.5.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/50/7a43117a5a8a16acaceabc5ad69092fa1dacb11ef83c84fdf234e5a3502f/sphinxcontrib-blockdiag-1.5.5.tar.gz
Summary  : Sphinx "blockdiag" extension
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-blockdiag-license = %{version}-%{release}
Requires: sphinxcontrib-blockdiag-python = %{version}-%{release}
Requires: sphinxcontrib-blockdiag-python3 = %{version}-%{release}
Requires: Sphinx
Requires: blockdiag
BuildRequires : buildreq-distutils3

%description
=======================
sphinxcontrib-blockdiag
=======================
.. image:: https://travis-ci.org/tk0miya/sphinxcontrib-blockdiag.svg?branch=master
:target: https://travis-ci.org/tk0miya/sphinxcontrib-blockdiag

%package license
Summary: license components for the sphinxcontrib-blockdiag package.
Group: Default

%description license
license components for the sphinxcontrib-blockdiag package.


%package python
Summary: python components for the sphinxcontrib-blockdiag package.
Group: Default
Requires: sphinxcontrib-blockdiag-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-blockdiag package.


%package python3
Summary: python3 components for the sphinxcontrib-blockdiag package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-blockdiag package.


%prep
%setup -q -n sphinxcontrib-blockdiag-1.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551037837
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-blockdiag
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-blockdiag/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-blockdiag/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
