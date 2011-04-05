%define name	mk-livestatus
%define version 1.1.10
%define release	%mkrel 1
%define _disable_ld_no_undefined 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nagios Event Broker Module
Group:		System/Servers
License:	BSD
URL:		http://mathias-kettner.de/checkmk_livestatus.html
Source0:    http://www.mathias-kettner.de/download/mk-livestatus-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
MKLivestatus is a brand new Nagios Event Broker (NEB) Module which can be used
to extend the core of Nagios. The MKLivestatus module provides access to the
live status information kept in the running Nagios process. It serves a unix
socket for data exchange with external scripts/addons.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/unixcat
%{_libdir}/mk-livestatus/livestatus.o

