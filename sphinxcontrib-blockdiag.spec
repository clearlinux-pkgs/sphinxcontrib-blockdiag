#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-blockdiag
Version  : 2.0.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/ad/7a/d9e57607522d414e1a089f8da982750ded0e100b1bfc210b17f0fe98db47/sphinxcontrib-blockdiag-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/7a/d9e57607522d414e1a089f8da982750ded0e100b1bfc210b17f0fe98db47/sphinxcontrib-blockdiag-2.0.0.tar.gz
Summary  : Sphinx "blockdiag" extension
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-blockdiag-license = %{version}-%{release}
Requires: sphinxcontrib-blockdiag-python = %{version}-%{release}
Requires: sphinxcontrib-blockdiag-python3 = %{version}-%{release}
Requires: Sphinx
Requires: blockdiag
BuildRequires : Sphinx
BuildRequires : blockdiag
BuildRequires : buildreq-distutils3

%description
sphinxcontrib-blockdiag
        =======================

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
Provides: pypi(sphinxcontrib_blockdiag)
Requires: pypi(blockdiag)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib-blockdiag package.


%prep
%setup -q -n sphinxcontrib-blockdiag-2.0.0
cd %{_builddir}/sphinxcontrib-blockdiag-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697182
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-blockdiag
cp %{_builddir}/sphinxcontrib-blockdiag-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-blockdiag/1df558a5711c101907d8f15c608a58793588fa6e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-blockdiag/1df558a5711c101907d8f15c608a58793588fa6e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
