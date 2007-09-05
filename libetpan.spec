%define name        libetpan
%define version     0.52
%define release     %mkrel 1
%define lib_major        11
%define lib_name    %mklibname etpan %lib_major
%define Summary  LibEtPan is a mail purpose library
 
 
Summary:      %Summary
Name:            %name
Version:          %version
Release:         %release
Group:            System/Libraries
License:          BSD
URL:               http://libetpan.sourceforge.net/ 
Source:           http://unc.dl.sourceforge.net/sourceforge/%{name}-%{version}.tar.bz2
Source1:          libetpan-0.31-libetpan.la.tar.bz2
BuildRoot:       %{_tmppath}/%{name}-buildroot
BuildRequires:  openssl-devel  
BuildRequires:  db4.2-devel 
Obsoletes: %name 
Provides: %name 

%description
libEtPan is a mail purpose library.
It is used for low-level mail handling.

Network protocols supported:
o IMAP/NNTP/POP3/SMTP over TCP/IP and SSL/TCP/IP, already implemented.
o Local storage (mbox/MH/maildir), message / MIME parser

%package -n %lib_name
Summary:%Summary
Group: System/Libraries 

%description -n %lib_name
%Summary

%package -n %lib_name-devel
Summary: Libraries and include files for %name
Group:    Development/C
Requires: %lib_name = %{version}
Provides: %name-devel  = %version
Conflicts: %name-devel < %version

%description -n %lib_name-devel
This package contains the header files and static libraries for
developing with %name.

%prep
%setup -qn %{name}-%{version}

%build
%configure2_5x --enable-openssl

# 0.42: parallel build broken on x86_64
make

%install
 rm -rf $RPM_BUILD_ROOT  
%makeinstall

#workaround for *.h detections 
rm -f include/libetpan/libetpan-conf
install -m 644 include/libetpan/*.h %buildroot/%_includedir/libetpan 
 
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/libetpan-config 

%post -n %lib_name -p /sbin/ldconfig 

%postun -n %lib_name -p /sbin/ldconfig 

%clean
rm -rf $RPM_BUILD_ROOT  
 
%files -n %lib_name
%defattr(-, root, root) 
%_libdir/lib*.so.%{lib_major}*
 
%files -n %lib_name-devel
%defattr(-,root,root) 
%doc COPYRIGHT ChangeLog NEWS 
%doc doc/*
%{_bindir}/libetpan-config
%multiarch %{multiarch_bindir}/*
%_includedir/*
%_libdir/lib*.so
%_libdir/*.a
%_libdir/*.la 



