Name:           gnocky
Version:        0.0.5
Release:        %mkrel 1
Summary:        Mobile phone utility application

Group:          Communications
License:        GPL
URL:            http://sourceforge.net/projects/gnocky/
Source0:        http://gnokii.org/download/gnocky/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-datadir.patch

BuildRequires:  gettext, gnokii-devel >= 0.6.2, libglade2.0-devel
BuildRequires:  desktop-file-utils

%description
Gnocky is an application that will allow you to use many features of
your mobile phone (setting logos, sending SMS, addressbook
management).  It uses the user space mobile phone driver provided by
the Gnokii project.


%prep
%setup -q
#%patch0 -p1
sed 's|__ICON__|%{_datadir}/gnocky/glade/cellphone.png|' \
  < %{SOURCE1} > %{name}.desktop


%build
%configure --disable-rpath --disable-dependency-tracking
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
  --mode 644 \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --vendor "" \
  --add-category "X-MandrivaLinux-MoreApplications-Communications" \
  %{name}.desktop

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog COPYING README TODO
%{_bindir}/gnocky
%{_datadir}/gnocky
%{_datadir}/applications/*%{name}.desktop


