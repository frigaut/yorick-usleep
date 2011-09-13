%define name yorick-usleep
%define version 0.1.01
%define release gemini2008jan09

Summary: simple sleep/pause functionality for yorick
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: Development/Languages
Packager: Francois Rigaut <frigaut@gemini.edu>
Url: http://www.maumae.net/yorick/doc/plugins.php
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: yorick >= 2.1

%description
Provides true sleep()

%prep
%setup -q

%build
yorick -batch make.i
make
if [ -f check.i ] ; then
   mv check.i %{name}_check.i
fi;

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/yorick/lib
mkdir -p $RPM_BUILD_ROOT/usr/lib/yorick/i0
mkdir -p $RPM_BUILD_ROOT/usr/lib/yorick/i-start
mkdir -p $RPM_BUILD_ROOT/usr/lib/yorick/packages/installed

install -m 755 usleep.so $RPM_BUILD_ROOT/usr/lib/yorick/lib
install -m 644 *.i $RPM_BUILD_ROOT/usr/lib/yorick/i0
install -m 644 *_start.i $RPM_BUILD_ROOT/usr/lib/yorick/i-start
install -m 644 usleep.info $RPM_BUILD_ROOT/usr/lib/yorick/packages/installed

rm $RPM_BUILD_ROOT/usr/lib/yorick/i0/*_start.i


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/yorick/lib/usleep.so
/usr/lib/yorick/i0/*.i
/usr/lib/yorick/i-start/*_start.i
/usr/lib/yorick/packages/installed/*

%changelog
* Tue Jan 09 2008 <frigaut@users.sourceforge.net>
- included the info file for compat with pkg_mngr
