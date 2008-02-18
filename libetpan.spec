%define major 11
%define libname %mklibname etpan %major
%define develname %mklibname etpan -d

Summary:	Mail purpose library
Name:		libetpan
Version:	0.52
Release:	%mkrel 2
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD
URL:		http://libetpan.sourceforge.net/ 
Source:		http://unc.dl.sourceforge.net/sourceforge/%{name}-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	db4.6-devel
BuildRequires:	libcurl-devel
BuildRequires:	libexpat-devel
Obsoletes:	%{name}
Provides:	%{name}

%description
libEtPan is a mail purpose library.
It is used for low-level mail handling.

Network protocols supported:
o IMAP/NNTP/POP3/SMTP over TCP/IP and SSL/TCP/IP, already implemented.
o Local storage (mbox/MH/maildir), message / MIME parser

%package -n %{libname}
Summary:	Mail purpose library
Group:		System/Libraries 

%description -n %{libname}
%Summary

%package -n %{develname}
Summary:	Libraries and include files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel  = %{version}-%{release}
Obsoletes:	%mklibname etpan 11 -d
Provides:	%mklibname etpan 11 -d

%description -n %{develname}
This package contains the header files and static libraries for
developing with %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-openssl

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#workaround for *.h detections 
rm -f include/libetpan/libetpan-conf
install -m 644 include/libetpan/*.h %{buildroot}%{_includedir}/libetpan 

%multiarch_binaries %{buildroot}%{_bindir}/libetpan-config 

%post -n %{libname} -p /sbin/ldconfig 

%postun -n %{libname} -p /sbin/ldconfig 

%clean
rm -rf %{buidroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*
 
%files -n %{develname}
%defattr(-,root,root) 
%doc COPYRIGHT ChangeLog NEWS 
%doc doc/*
%{_bindir}/libetpan-config
%multiarch %{multiarch_bindir}/*
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_libdir}/*.la 
