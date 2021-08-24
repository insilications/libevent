#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libevent
Version  : 2.1.12
Release  : 302
URL      : file:///aot/build/clearlinux/packages/libevent/libevent-v2.1.12.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libevent/libevent-v2.1.12.tar.gz
Summary  : libevent is an asynchronous notification event loop library
Group    : Development/Tools
License  : GPL-2.0
Requires: libevent-bin = %{version}-%{release}
Requires: libevent-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : openssl-lib32
BuildRequires : openssl-staticdev
BuildRequires : pkg-config
BuildRequires : sed
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: pcfiles.patch

%description
<p align="center">
<img src="https://libevent.org/libevent3.png" alt="libevent logo"/>
</p>

%package bin
Summary: bin components for the libevent package.
Group: Binaries

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

%description lib
lib components for the libevent package.


%package lib32
Summary: lib32 components for the libevent package.
Group: Default

%description lib32
lib32 components for the libevent package.


%package staticdev
Summary: staticdev components for the libevent package.
Group: Default
Requires: libevent-dev = %{version}-%{release}

%description staticdev
staticdev components for the libevent package.


%prep
%setup -q -n libevent
cd %{_builddir}/libevent
%patch1 -p1
pushd %{_builddir}
cp -a %{_builddir}/libevent build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629802922
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen  --enable-shared \
--enable-static \
--disable-gcc-hardening \
--disable-gcc-warnings \
--disable-doxygen-doc \
--enable-thread-support \
--enable-openssl \
--enable-samples
## make_prepend64 content
# find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libssl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libcrypto.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lnghttp2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libnghttp2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lsqlite3\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libsqlite3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lidn2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libidn2.a,/usr/lib64/libunistring.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lunistring\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libunistring.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lbrotlidec\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libbrotlidec-static.a,/usr/lib64/libbrotlicommon-static.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:/usr/lib64/libssl.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:/usr/lib64/libcrypto.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lnghttp2\b:/usr/lib64/libnghttp2.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lsqlite3\b:/usr/lib64/libsqlite3.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lidn2\b:/usr/lib64/libidn2.a /usr/lib64/libunistring.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lunistring\b:/usr/lib64/libunistring.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lbrotlidec\b:/usr/lib64/libbrotlidec-static.a /usr/lib64/libbrotlicommon-static.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:/usr/lib64/libzstd.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:/usr/lib64/libz.a:g' {} \;
# sd "\-lz" -- "/usr/lib64/libz.a" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*pro$) $(fd -uu --follow .*mk$)
sd "\-lssl" -- "-Wl,--whole-archive,--start-group,/usr/lib64/libssl.a,/usr/lib64/libcrypto.a,/usr/lib64/libz.a,--end-group,--no-whole-archive" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*pro$) $(fd -uu --follow .*mk$)
# sd "\-lcrypto" -- "/usr/lib64/libcrypto.a" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*pro$) $(fd -uu --follow .*mk$)
## make_prepend64 end
make  %{?_smp_mflags}    V=1 VERBOSE=1

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
pushd test/
./test-ratelim.sh || :
./bench || :
./bench_cascade || :
./bench_http & pid1=$! || :; \
sleep 3s; \
./bench_httpclient || :; \
sleep 1s; \
kill -s TERM $pid1 || :;
popd
make -j16 verify V=1 VERBOSE=1 || :
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end
make clean || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen --enable-shared \
--enable-static \
--disable-gcc-hardening \
--disable-gcc-warnings \
--disable-doxygen-doc \
--enable-thread-support \
--enable-openssl \
--enable-samples
## make_prepend64 content
# find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libssl.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libcrypto.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lnghttp2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libnghttp2.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lsqlite3\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libsqlite3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lidn2\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libidn2.a,/usr/lib64/libunistring.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lunistring\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libunistring.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lbrotlidec\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libbrotlidec-static.a,/usr/lib64/libbrotlicommon-static.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libzstd.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:-Wl,--whole-archive,--as-needed,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lssl\b:/usr/lib64/libssl.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lcrypto\b:/usr/lib64/libcrypto.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lnghttp2\b:/usr/lib64/libnghttp2.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lsqlite3\b:/usr/lib64/libsqlite3.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lidn2\b:/usr/lib64/libidn2.a /usr/lib64/libunistring.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lunistring\b:/usr/lib64/libunistring.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lbrotlidec\b:/usr/lib64/libbrotlidec-static.a /usr/lib64/libbrotlicommon-static.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lzstd\b:/usr/lib64/libzstd.a:g' {} \;
# find . -type f -name 'Makefile' -exec sed -i 's:-lz\b:/usr/lib64/libz.a:g' {} \;
# sd "\-lz" -- "/usr/lib64/libz.a" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*pro$) $(fd -uu --follow .*mk$)
sd "\-lssl" -- "-Wl,--whole-archive,--start-group,/usr/lib64/libssl.a,/usr/lib64/libcrypto.a,/usr/lib64/libz.a,--end-group,--no-whole-archive" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*pro$) $(fd -uu --follow .*mk$)
# sd "\-lcrypto" -- "/usr/lib64/libcrypto.a" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*pro$) $(fd -uu --follow .*mk$)
## make_prepend64 end
make  %{?_smp_mflags}    V=1 VERBOSE=1
fi

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CPATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
unset ASFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FCFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CFFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
%autogen  --enable-shared \
--disable-static \
--disable-gcc-warnings \
--disable-doxygen-doc \
--disable-samples \
--enable-thread-support --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1629802922
rm -rf %{buildroot}
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
/usr/include/event2/watch.h
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
/usr/lib64/libevent-2.2.so.1
/usr/lib64/libevent-2.2.so.1.0.0
/usr/lib64/libevent_core-2.2.so.1
/usr/lib64/libevent_core-2.2.so.1.0.0
/usr/lib64/libevent_extra-2.2.so.1
/usr/lib64/libevent_extra-2.2.so.1.0.0
/usr/lib64/libevent_openssl-2.2.so.1
/usr/lib64/libevent_openssl-2.2.so.1.0.0
/usr/lib64/libevent_pthreads-2.2.so.1
/usr/lib64/libevent_pthreads-2.2.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevent-2.2.so.1
/usr/lib32/libevent-2.2.so.1.0.0
/usr/lib32/libevent_core-2.2.so.1
/usr/lib32/libevent_core-2.2.so.1.0.0
/usr/lib32/libevent_extra-2.2.so.1
/usr/lib32/libevent_extra-2.2.so.1.0.0
/usr/lib32/libevent_openssl-2.2.so.1
/usr/lib32/libevent_openssl-2.2.so.1.0.0
/usr/lib32/libevent_pthreads-2.2.so.1
/usr/lib32/libevent_pthreads-2.2.so.1.0.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libevent.a
/usr/lib64/libevent_core.a
/usr/lib64/libevent_extra.a
/usr/lib64/libevent_openssl.a
/usr/lib64/libevent_pthreads.a
