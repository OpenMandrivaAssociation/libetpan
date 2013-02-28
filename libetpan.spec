%define major 16
%define libname %mklibname etpan %{major}
%define develname %mklibname etpan -d

Summary:	Mail purpose library
Name:		libetpan
Version:	1.1
Release:	6
Group:		System/Libraries
License:	BSD
URL:		http://libetpan.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	db-devel
BuildRequires:	libexpat-devel
BuildRequires:	libgpg-error-devel
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
%{_libdir}/*.a



%changelog
* Thu Jul 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1-3
+ Revision: 810151
- Drop some ancient junk

* Tue May 08 2012 Crispin Boylan <crisb@mandriva.org> 1.1-2
+ Revision: 797462
- Rebuild

* Sat Sep 03 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1-1
+ Revision: 698131
- drop patch0, not needed at all
- disable muliarch stuff
- update to new version 1.1
- bump major

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - build with db 5.1 (from fwang | 2011-04-12 11:28:56 +0200)

* Sat Jul 10 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-1mdv2011.0
+ Revision: 550142
- update to new version 1.0
- drop patch 1, fixed by upstream

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 0.58-4mdv2010.1
+ Revision: 498456
- really build against db 4.8

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 0.58-3mdv2010.1
+ Revision: 498446
- drop ldflags from libetpan-config

* Fri Jan 15 2010 Colin Leroy <colinl@mandriva.org> 0.58-2mdv2010.1
+ Revision: 491616
- Build against new libdb

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.58-1mdv2010.0
+ Revision: 387832
- Update to new version 0.58
- Build against libdb4.7

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-2mdv2009.1
+ Revision: 358022
- rebuild for syncing i586 and x86_64

* Fri Oct 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.57-1mdv2009.1
+ Revision: 291532
- update to new version 0.57

* Sun Sep 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.56-2mdv2009.0
+ Revision: 284742
- enable checks

* Sun Sep 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.56-1mdv2009.0
+ Revision: 284736
- update to new version 0.56
- fix url for source
- build with gnutls instead of openssl
- enable optimizations

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.54-3mdv2009.0
+ Revision: 267815
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.54-2mdv2009.0
+ Revision: 195479
- obsolete old library

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.54-1mdv2009.0
+ Revision: 195300
- new version
- drop patch 0, merged upstream
- better description
- enable support for IPv6

* Mon Feb 18 2008 Colin Leroy <colinl@mandriva.org> 0.53-1mdv2008.1
+ Revision: 170630
- Upgrade libetpan to 0.53:
        Fix ipv6 issues
        Fix some GMail issues
        Mingw32-buildable
  Add patch to fix a bug with APPEND on some servers (already in upstream CVS)

  + Thierry Vignaud <tv@mandriva.org>
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix no-buildroot-tag

* Sun Dec 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.52-2mdv2008.1
+ Revision: 139408
- spec file rewrite
- new devel library policy
- drop source 1, not needed though
- enable parallel build
- add missing build requires on libcurl-devel and libexpat-devel
- rebuild against db4.6

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.52-1mdv2008.0
+ Revision: 79861
- New release 0.52


* Sun Mar 04 2007 Emmanuel Andry <eandry@mandriva.org> 0.49-3mdv2007.0
+ Revision: 131993
- build against db4.5

* Mon Jan 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.49-2mdv2007.1
+ Revision: 111868
- fix major; prevent this error to happen again

* Thu Jan 18 2007 Jérôme Soyer <saispo@mandriva.org> 0.49-1mdv2007.1
+ Revision: 110088
- New release 0.49

* Wed Jan 03 2007 Jérôme Soyer <saispo@mandriva.org> 0.48-1mdv2007.1
+ Revision: 103587
- New release 0.48

* Fri Nov 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.46-2mdv2007.0
+ Revision: 80623
- Rebuild for missing package ( bugreport: #27088)
- import libetpan-0.46-1mdv2007.0

* Wed Jul 19 2006 Charles A Edwards <eslrahc@mandriva.org> 0.46-1mdv2007.0
- 0.46
- bump major (previously missed)

* Fri Jun 23 2006 Erwan Velu <erwan@seanodes.com> 0.39-2
- Rebuild

* Sat Apr 08 2006 Jerome Soyer <saispo@mandriva.org> 0.45-1mdk
- 0.45

* Wed Mar 22 2006 Lenny Cartier <lenny@mandriva.com> 0.44-1mdk
- 0.44

* Wed Jan 18 2006 Marcel Pol <mpol@mandriva.org> 0.42-2mdk
- parallel build broken on x86_64

* Sun Jan 15 2006 Marcel Pol <mpol@mandriva.org> 0.42-1mdk
- 0.42
- new soname

* Sat Dec 03 2005 Marcel Pol <mpol@mandriva.org> 0.40-0.cvs6.1mdk
- 0.40cvs6
- mkrel

* Wed Oct 12 2005 Erwan Velu <erwan@seanodes.com> 0.39-1mdk
- 0.39

* Sat Sep 03 2005 Marcel Pol <mpol@mandriva.org> 0.38-2mdk
- fix %%prep 
[           1      -eq 1 ] || exit 0 
[           1      -eq 1 ] || exit 0 
[           1      -eq 1 ] || exit 0 
 (-n libetpan)

* Fri Jul 22 2005 Lenny Cartier <lenny@mandriva.com> 0.38-1mdk
- 0.38

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 0.37-1mdk
- 0.37

* Wed Feb 23 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.36-1mdk
- 0.36

* Sat Nov 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.34-1mdk
- 0.34

* Thu Aug 26 2004 Charles A Edwards <eslrahc@mandrake.org> 0.33-1mdk
- 0.33

