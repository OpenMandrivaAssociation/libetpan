%define major 17
%define libname %mklibname etpan %{major}
%define develname %mklibname etpan -d

Summary:	Mail purpose library
Name:		libetpan
Version:	1.6
Release:	1
Group:		System/Libraries
License:	BSD
URL:		http://libetpan.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	libetpan.rpmlintrc
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	db-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	libgcrypt-devel

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
Obsoletes:	%{_lib}etpan13 < 1.0

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

%description -n %{develname}
This package contains the header files and static libraries for
developing with %{name}.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x \
	--without-openssl \
	--with-gnutls \
	--enable-ipv6 \
	--enable-optim

%make

%check
make check

%install
%makeinstall_std

#workaround for *.h detections
#rm -f include/libetpan/libetpan-conf
#install -m 644 include/libetpan/*.h %{buildroot}%{_includedir}/libetpan


%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc ChangeLog NEWS
%doc doc/*
%{_bindir}/libetpan-config
%{_includedir}/*
%{_libdir}/lib*.so


