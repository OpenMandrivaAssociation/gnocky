Name:           gnocky
Version:        0.0.7
Release:        %mkrel 4
Summary:        Mobile phone utility application

Group:          Communications
License:        GPL
URL:            http://sourceforge.net/projects/gnocky/
Source0:        http://gnokii.org/download/gnocky/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  gettext, gnokii-devel >= 0.6.2, libglade2.0-devel
BuildRequires:  desktop-file-utils

%description
Gnocky is an application that will allow you to use many features of
your mobile phone (setting logos, sending SMS, addressbook
management).  It uses the user space mobile phone driver provided by
the Gnokii project.


%prep
%setup -q

%build
%configure2_5x --disable-rpath --disable-dependency-tracking
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog COPYING README TODO
%{_bindir}/gnocky
%{_datadir}/gnocky
%{_datadir}/applications/*%{name}.desktop


%changelog
* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 0.0.7-4mdv2011.0
+ Revision: 565957
- rebuild for new gnokii

* Thu Mar 11 2010 Frederic Crozat <fcrozat@mandriva.com> 0.0.7-3mdv2010.1
+ Revision: 518090
- Rebuild with latest gnokii

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 0.0.7-1mdv2009.1
+ Revision: 317784
- new version 0.0.7

* Sun Oct 26 2008 Funda Wang <fwang@mandriva.org> 0.0.6-3mdv2009.1
+ Revision: 297403
- rebuild for new gnokii

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6-2mdv2009.0
+ Revision: 266909
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.0.6-1mdv2009.0
+ Revision: 213895
- update to new version 0.0.6

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.0.5-1mdv2008.1
+ Revision: 115736
- New release 0.0.5

* Mon Aug 13 2007 Jérôme Soyer <saispo@mandriva.org> 0.0.4-1mdv2008.0
+ Revision: 62448
- New release 0.0.4


* Sat Jan 13 2007 Jérôme Soyer <saispo@mandriva.org> 0.0.3-1mdv2007.0
+ Revision: 108285
- Import gnocky

