%define major 13
%define libname %mklibname etpan %{major}
%define develname %mklibname etpan -d

Summary:	Mail purpose library
Name:		libetpan
Version:	0.58
Release:	%mkrel 3
Group:		System/Libraries
License:	BSD
URL:		http://libetpan.sourceforge.net/ 
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		libetpan-0.58-drop-ldflags.patch
BuildRequires:	gnutls-devel
BuildRequires:	db4.8-devel
BuildRequires:	libcurl-devel
BuildRequires:	libexpat-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The purpose of this mail library is to provide a portable, efficient 
framework for different kinds of mail access. When using the drivers 
interface, the interface is the same for all kinds of mail access, 
remote and local mailboxes.

Network protocols supported:
o IMAP/NNTP/POP3/SMTP over TCP/IP and SSL/TCP/IP, already implemented.
o Local storage (mbox/MH/maildir), message / MIME parser

%package -n %{libname}
Summary:	Mail purpose library
Group:		System/Libraries 
Obsoletes:	%mklibname etpan 11 < 0.54

%description -n %{libname}
The purpose of this mail library is to provide a portable, efficient 
framework for different kinds of mail access. When using the drivers 
interface, the interface is the same for all kinds of mail access, 
remote and local mailboxes.

Network protocols supported:
o IMAP/NNTP/POP3/SMTP over TCP/IP and SSL/TCP/IP, already implemented.
o Local storage (mbox/MH/maildir), message / MIME parser

%package -n %{develname}
Summary:	Libraries and include files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel  = %{version}-%{release}
Obsoletes:	%mklibname etpan 11 -d < 0.54
Provides:	%mklibname etpan 11 -d

%description -n %{develname}
This package contains the header files and static libraries for
developing with %{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--without-openssl \
	--with-gnutls \
	--enable-ipv6 \
	--enable-optim

%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

#workaround for *.h detections 
rm -f include/libetpan/libetpan-conf
install -m 644 include/libetpan/*.h %{buildroot}%{_includedir}/libetpan 

%multiarch_binaries %{buildroot}%{_bindir}/libetpan-config 

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig 
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig 
%endif

%clean
rm -rf %{buidroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*
 
%files -n %{develname}
%defattr(-,root,root) 
%doc ChangeLog NEWS 
%doc doc/*
%{_bindir}/libetpan-config
%multiarch %{multiarch_bindir}/*
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_libdir}/*.la 
