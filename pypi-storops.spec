#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v3
# autospec commit: 750e50d
#
Name     : pypi-storops
Version  : 1.2.11
Release  : 6
URL      : https://files.pythonhosted.org/packages/be/70/6b6fe61a2d5d53834c0bd979a8015d97799d09168d468f47cfad830fb837/storops-1.2.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/be/70/6b6fe61a2d5d53834c0bd979a8015d97799d09168d468f47cfad830fb837/storops-1.2.11.tar.gz
Summary  : Python API for VNX and Unity.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: pypi-storops-license = %{version}-%{release}
Requires: pypi-storops-python = %{version}-%{release}
Requires: pypi-storops-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bitmath)
BuildRequires : pypi(cachez)
BuildRequires : pypi(persist_queue)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(requests)
BuildRequires : pypi(retryz)
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
StorOps: The Python Library for VNX & Unity
===========================================

%package license
Summary: license components for the pypi-storops package.
Group: Default

%description license
license components for the pypi-storops package.


%package python
Summary: python components for the pypi-storops package.
Group: Default
Requires: pypi-storops-python3 = %{version}-%{release}

%description python
python components for the pypi-storops package.


%package python3
Summary: python3 components for the pypi-storops package.
Group: Default
Requires: python3-core
Provides: pypi(storops)
Requires: pypi(bitmath)
Requires: pypi(cachez)
Requires: pypi(persist_queue)
Requires: pypi(python_dateutil)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(retryz)
Requires: pypi(six)

%description python3
python3 components for the pypi-storops package.


%prep
%setup -q -n storops-1.2.11
cd %{_builddir}/storops-1.2.11
pushd ..
cp -a storops-1.2.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707143396
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-storops
cp %{_builddir}/storops-%{version}/.tox/pep8/Lib/site-packages/pip-22.0.3.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/d1816736d55c943e1ed44a003f72cb7d1afe0789 || :
cp %{_builddir}/storops-%{version}/.tox/pep8/Lib/site-packages/storops-1.2.10.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/storops-%{version}/.tox/pep8/Lib/site-packages/urllib3-1.26.8.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/fae7d86a68e1724238ed64674e4cd743a7dc6796 || :
cp %{_builddir}/storops-%{version}/.tox/pep8/Lib/site-packages/wheel-0.37.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/53aa128e9d6387e9bb9d945fdcbf1ab4d003baed || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/PyHamcrest-2.0.2.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/44345ae35cd4b8008ea5a55ebefd1b89a25a110c || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/colorama-0.4.4.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/151478b5f4a6291addb13da92ef3534597ed39a4 || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/coverage-5.5.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/bd0b945d001aebc12dd7cdbf100427f1bc8d6957 || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/mock-4.0.3.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/2eec66c59087d1cf096a35fc620161b222591e05 || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/pip-21.0.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/d02171b6f15af62da027708f275b5379b462bf25 || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/storops-1.2.9.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/urllib3-1.26.3.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/fae7d86a68e1724238ed64674e4cd743a7dc6796 || :
cp %{_builddir}/storops-%{version}/.tox/py37/Lib/site-packages/wheel-0.36.2.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/53aa128e9d6387e9bb9d945fdcbf1ab4d003baed || :
cp %{_builddir}/storops-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-storops/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-storops/151478b5f4a6291addb13da92ef3534597ed39a4
/usr/share/package-licenses/pypi-storops/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-storops/2eec66c59087d1cf096a35fc620161b222591e05
/usr/share/package-licenses/pypi-storops/44345ae35cd4b8008ea5a55ebefd1b89a25a110c
/usr/share/package-licenses/pypi-storops/53aa128e9d6387e9bb9d945fdcbf1ab4d003baed
/usr/share/package-licenses/pypi-storops/bd0b945d001aebc12dd7cdbf100427f1bc8d6957
/usr/share/package-licenses/pypi-storops/d02171b6f15af62da027708f275b5379b462bf25
/usr/share/package-licenses/pypi-storops/d1816736d55c943e1ed44a003f72cb7d1afe0789
/usr/share/package-licenses/pypi-storops/fae7d86a68e1724238ed64674e4cd743a7dc6796

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
