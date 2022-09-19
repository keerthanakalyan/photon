Name:           python3-jsonpointer
Version:        2.3
Release:        1%{?dist}
Summary:        Applying JSON Patches in Python
License:        Modified BSD License
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
Source0: https://github.com/stefankoegl/python-json-pointer/archive/refs/tags/jsonpointer-%{version}.tar.gz
%define sha512 jsonpointer=e04da474a5ec376d1cd2c764c2d7a11ac296450df199449994cb1dedf02a49df3ae3a4e75b2963370dba1da166464602b849a79609f7a98d8246dab0b342c819

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-xml

Requires: python3

BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902.

%prep
%autosetup -p1 -n jsonpointer-%{version}

%build
%py3_build

%install
%py3_install

%check
python3 tests.py

%files
%defattr(-,root,root,-)
%{_bindir}/jsonpointer
%{python3_sitelib}/*

%changelog
* Sun Aug 21 2022 Gerrit Photon <photon-checkins@vmware.com> 2.3-1
- Automatic Version Bump
* Sat Jun 20 2020 Tapas Kundu <tkundu@vmware.com> 2.0-2
- Mass removal python2
* Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 2.0-1
- Update to version 2.0
* Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 1.10-6
- Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
* Wed Apr 26 2017 Sarah Choi <sarahc@vmware.com> 1.10-5
- Rename jsonpointer for python3
* Thu Apr 06 2017 Sarah Choi <sarahc@vmware.com> 1.10-4
- support python3
* Tue Oct 04 2016 ChangLee <changlee@vmware.com> 1.10-3
- Modified %check
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.10-2
- GA - Bump release of all rpms
* Tue Feb 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.10-1
- Updated to version 1.10
* Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
- Initial packaging for Photon
