Name: pgilinux-license-zdv
Version: 1.0
Release: 0
Vendor: Zentrum fuer Datenverarbeitung
Summary: License for PGI Workstation
License: Proprietary
Group: System
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
# prevent automatic dependency processing
# http://rpm5.org/docs/max-rpm.html#s2-rpm-depend-autoreqprov
AutoReqProv: no
BuildArch: noarch

%description
License for PGI Workstation for the university network

%prep

%setup -c -n %{name}-%{version}

%build

%install
[ -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}
/bin/mkdir -p ${RPM_BUILD_ROOT}
/bin/cp -axv ${RPM_BUILD_DIR}/%{name}-%{version}/* ${RPM_BUILD_ROOT}/


%post

%postun

%clean

%files
%defattr(-,root,root)
/opt/pgi/license.dat

%changelog

* Sat Feb 02 2013 Hinrich Winther <hwinther@uni-mainz.de>
- initial Version

