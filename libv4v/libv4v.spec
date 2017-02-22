Name: libv4v
Summary: libv4v
Source0: libv4v.tar.gz
BuildArch: i686 x86_64
Version: 1.0
Release: 1%{?dist}
License: LGPL2.1

%description
libv4v

%prep
%setup -q

%build
libtoolize --force
# aclocal complains about configure.in being named configure.ac,
#   redirect stderr to stdout
aclocal 2>&1
autoheader
# automake complains a lot about various stuff,
#   redirect stderr to stdout
automake --force-missing --add-missing 2>&1
autoconf
./configure
make

%install
rm -rf %{buildroot}
# make install triggers libtool warnings,
#   redirect stderr to stdout
make DESTDIR=%{buildroot} install 2>&1

%files
/usr/local/*
