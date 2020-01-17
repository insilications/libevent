#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB86086848EF8686D (bin@azat.sh)
#
Name     : libevent
Version  : 2.1.11.stable
Release  : 31
URL      : https://github.com/libevent/libevent/releases/download/release-2.1.11-stable/libevent-2.1.11-stable.tar.gz
Source0  : https://github.com/libevent/libevent/releases/download/release-2.1.11-stable/libevent-2.1.11-stable.tar.gz
Source1  : https://github.com/libevent/libevent/releases/download/release-2.1.11-stable/libevent-2.1.11-stable.tar.gz.asc
Summary  : libevent is an asynchronous notification event loop library
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libevent-bin = %{version}-%{release}
Requires: libevent-lib = %{version}-%{release}
Requires: libevent-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : openssl-lib32
BuildRequires : pkg-config
BuildRequires : sed
BuildRequires : zlib-dev32
Patch1: pcfiles.patch

%description
<p align="center">
<img src="https://strcpy.net/libevent3.png" alt="libevent logo"/>
</p>

%package bin
Summary: bin components for the libevent package.
Group: Binaries
Requires: libevent-license = %{version}-%{release}

%description bin
bin components for the libevent package.


%package dev
Summary: dev components for the libevent package.
Group: Development
Requires: libevent-lib = %{version}-%{release}
Requires: libevent-bin = %{version}-%{release}
Provides: libevent-devel = %{version}-%{release}
Requires: libevent = %{version}-%{release}

%description dev
dev components for the libevent package.


%package dev32
Summary: dev32 components for the libevent package.
Group: Default
Requires: libevent-lib32 = %{version}-%{release}
Requires: libevent-bin = %{version}-%{release}
Requires: libevent-dev = %{version}-%{release}

%description dev32
dev32 components for the libevent package.


%package lib
Summary: lib components for the libevent package.
Group: Libraries
Requires: libevent-license = %{version}-%{release}

%description lib
lib components for the libevent package.


%package lib32
Summary: lib32 components for the libevent package.
Group: Default
Requires: libevent-license = %{version}-%{release}

%description lib32
lib32 components for the libevent package.


%package license
Summary: license components for the libevent package.
Group: Default

%description license
license components for the libevent package.


%prep
%setup -q -n libevent-2.1.11-stable
cd %{_builddir}/libevent-2.1.11-stable
%patch1 -p1
pushd ..
cp -a libevent-2.1.11-stable build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579287324
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-libevent-regress
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-libevent-regress   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1579287324
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libevent
cp %{_builddir}/libevent-2.1.11-stable/LICENSE %{buildroot}/usr/share/package-licenses/libevent/0f375374b877550ade2e001905a1f9c9b7128714
cp %{_builddir}/libevent-2.1.11-stable/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libevent/cc31ae51223e291f3f7389a4c96b2cf4c1e62757
cp %{_builddir}/libevent-2.1.11-stable/cmake/Copyright.txt %{buildroot}/usr/share/package-licenses/libevent/b7708e46727dc00ced77b6421d1f4b4e4045c12d
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/event_rpcgen.py

%files dev
%defattr(-,root,root,-)
/usr/include/evdns.h
/usr/include/event.h
/usr/include/event2/buffer.h
/usr/include/event2/buffer_compat.h
/usr/include/event2/bufferevent.h
/usr/include/event2/bufferevent_compat.h
/usr/include/event2/bufferevent_ssl.h
/usr/include/event2/bufferevent_struct.h
/usr/include/event2/dns.h
/usr/include/event2/dns_compat.h
/usr/include/event2/dns_struct.h
/usr/include/event2/event-config.h
/usr/include/event2/event.h
/usr/include/event2/event_compat.h
/usr/include/event2/event_struct.h
/usr/include/event2/http.h
/usr/include/event2/http_compat.h
/usr/include/event2/http_struct.h
/usr/include/event2/keyvalq_struct.h
/usr/include/event2/listener.h
/usr/include/event2/rpc.h
/usr/include/event2/rpc_compat.h
/usr/include/event2/rpc_struct.h
/usr/include/event2/tag.h
/usr/include/event2/tag_compat.h
/usr/include/event2/thread.h
/usr/include/event2/util.h
/usr/include/event2/visibility.h
/usr/include/evhttp.h
/usr/include/evrpc.h
/usr/include/evutil.h
/usr/lib64/libevent.so
/usr/lib64/libevent_core.so
/usr/lib64/libevent_extra.so
/usr/lib64/libevent_openssl.so
/usr/lib64/libevent_pthreads.so
/usr/lib64/pkgconfig/libevent.pc
/usr/lib64/pkgconfig/libevent_core.pc
/usr/lib64/pkgconfig/libevent_extra.pc
/usr/lib64/pkgconfig/libevent_openssl.pc
/usr/lib64/pkgconfig/libevent_pthreads.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libevent.so
/usr/lib32/libevent_core.so
/usr/lib32/libevent_extra.so
/usr/lib32/libevent_openssl.so
/usr/lib32/libevent_pthreads.so
/usr/lib32/pkgconfig/32libevent.pc
/usr/lib32/pkgconfig/32libevent_core.pc
/usr/lib32/pkgconfig/32libevent_extra.pc
/usr/lib32/pkgconfig/32libevent_openssl.pc
/usr/lib32/pkgconfig/32libevent_pthreads.pc
/usr/lib32/pkgconfig/libevent.pc
/usr/lib32/pkgconfig/libevent_core.pc
/usr/lib32/pkgconfig/libevent_extra.pc
/usr/lib32/pkgconfig/libevent_openssl.pc
/usr/lib32/pkgconfig/libevent_pthreads.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libevent-2.1.so.7
/usr/lib64/libevent-2.1.so.7.0.0
/usr/lib64/libevent_core-2.1.so.7
/usr/lib64/libevent_core-2.1.so.7.0.0
/usr/lib64/libevent_extra-2.1.so.7
/usr/lib64/libevent_extra-2.1.so.7.0.0
/usr/lib64/libevent_openssl-2.1.so.7
/usr/lib64/libevent_openssl-2.1.so.7.0.0
/usr/lib64/libevent_pthreads-2.1.so.7
/usr/lib64/libevent_pthreads-2.1.so.7.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevent-2.1.so.7
/usr/lib32/libevent-2.1.so.7.0.0
/usr/lib32/libevent_core-2.1.so.7
/usr/lib32/libevent_core-2.1.so.7.0.0
/usr/lib32/libevent_extra-2.1.so.7
/usr/lib32/libevent_extra-2.1.so.7.0.0
/usr/lib32/libevent_openssl-2.1.so.7
/usr/lib32/libevent_openssl-2.1.so.7.0.0
/usr/lib32/libevent_pthreads-2.1.so.7
/usr/lib32/libevent_pthreads-2.1.so.7.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libevent/0f375374b877550ade2e001905a1f9c9b7128714
/usr/share/package-licenses/libevent/b7708e46727dc00ced77b6421d1f4b4e4045c12d
/usr/share/package-licenses/libevent/cc31ae51223e291f3f7389a4c96b2cf4c1e62757
