%undefine _missing_build_ids_terminate_build
# tar -czf /tmp/pgilinux.tgz /opt/pgi/linux86/{2012,12.4} /opt/pgi/linux86/2012 /etc/profile.d/pgilinux-2012.*
Name: pgilinux-2012
Version: 124
Release: 1
Vendor: The Portland Group
Summary: PGI Workstation
License: Proprietary
Group: System
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
# prevent automatic dependency processing
# http://rpm5.org/docs/max-rpm.html#s2-rpm-depend-autoreqprov
AutoReqProv: no
requires: /bin/sh

%description
PGI Workstation™ is PGI's single-user scientific and engineering compilers and tools product.

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
/opt/pgi/linux86/2012/*
/opt/pgi/linux86-64/12.4/*
/opt/pgi/linux86-64/2012/*
/etc/profile.d/pgilinux-2012.sh
/etc/profile.d/pgilinux-2012.csh

%changelog

* Sat Feb 02 2013 Hinrich Winther <hwinther@uni-mainz.de>
- initial Version

