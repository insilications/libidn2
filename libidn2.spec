#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x08302DB6A2670428 (tim.ruehsen@gmx.de)
#
%define keepstatic 1
Name     : libidn2
Version  : 2.3.0
Release  : 16
URL      : http://mirrors.kernel.org/gnu/libidn/libidn2-2.3.0.tar.gz
Source0  : http://mirrors.kernel.org/gnu/libidn/libidn2-2.3.0.tar.gz
Source1  : http://mirrors.kernel.org/gnu/libidn/libidn2-2.3.0.tar.gz.sig
Summary  : Library implementing IDNA2008 and TR46
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: libidn2-bin = %{version}-%{release}
Requires: libidn2-info = %{version}-%{release}
Requires: libidn2-lib = %{version}-%{release}
Requires: libidn2-locales = %{version}-%{release}
Requires: libidn2-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libunistring-dev
BuildRequires : libunistring-dev32
BuildRequires : libunistring-staticdev
BuildRequires : libunistring-staticdev32
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![build status](https://gitlab.com/libidn/libidn2/badges/master/build.svg)](https://gitlab.com/libidn/libidn2/pipelines)
[![coverage status](https://gitlab.com/libidn/libidn2/badges/master/coverage.svg)](https://libidn.gitlab.io/libidn2/coverage)
[![fuzz coverage status](https://libidn.gitlab.io/libidn2/fuzz-coverage/badge.svg)](https://libidn.gitlab.io/libidn2/fuzz-coverage)
[![Coverity Scan Build Status](https://scan.coverity.com/projects/12080/badge.svg)](https://scan.coverity.com/projects/libidn2)

%package bin
Summary: bin components for the libidn2 package.
Group: Binaries

%description bin
bin components for the libidn2 package.


%package dev
Summary: dev components for the libidn2 package.
Group: Development
Requires: libidn2-lib = %{version}-%{release}
Requires: libidn2-bin = %{version}-%{release}
Provides: libidn2-devel = %{version}-%{release}
Requires: libidn2 = %{version}-%{release}

%description dev
dev components for the libidn2 package.


%package dev32
Summary: dev32 components for the libidn2 package.
Group: Default
Requires: libidn2-lib32 = %{version}-%{release}
Requires: libidn2-bin = %{version}-%{release}
Requires: libidn2-dev = %{version}-%{release}

%description dev32
dev32 components for the libidn2 package.


%package doc
Summary: doc components for the libidn2 package.
Group: Documentation
Requires: libidn2-man = %{version}-%{release}
Requires: libidn2-info = %{version}-%{release}

%description doc
doc components for the libidn2 package.


%package info
Summary: info components for the libidn2 package.
Group: Default

%description info
info components for the libidn2 package.


%package lib
Summary: lib components for the libidn2 package.
Group: Libraries

%description lib
lib components for the libidn2 package.


%package lib32
Summary: lib32 components for the libidn2 package.
Group: Default

%description lib32
lib32 components for the libidn2 package.


%package locales
Summary: locales components for the libidn2 package.
Group: Default

%description locales
locales components for the libidn2 package.


%package man
Summary: man components for the libidn2 package.
Group: Default

%description man
man components for the libidn2 package.


%package staticdev
Summary: staticdev components for the libidn2 package.
Group: Default
Requires: libidn2-dev = %{version}-%{release}

%description staticdev
staticdev components for the libidn2 package.


%package staticdev32
Summary: staticdev32 components for the libidn2 package.
Group: Default
Requires: libidn2-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the libidn2 package.


%prep
%setup -q -n libidn2-2.3.0
cd %{_builddir}/libidn2-2.3.0
pushd ..
cp -a libidn2-2.3.0 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598139498
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto -Wl,--whole-archive /usr/lib64/libunistring.a -Wl,--no-whole-archive $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-lto -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto-partition=none -fPIC -ffat-lto-objects -fno-lto -Wl,--whole-archive /usr/lib64/libunistring.a -Wl,--no-whole-archive $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
 %configure --enable-shared --enable-static
make  %{?_smp_mflags}  VERBOSE=1 V=1

make VERBOSE=1 V=1 %{?_smp_mflags} check
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure --enable-shared --enable-static
make  %{?_smp_mflags}  VERBOSE=1 V=1

pushd ../build32/
export CFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O3 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --enable-shared --enable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  VERBOSE=1 V=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1598139498
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
%find_lang libidn2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/idn2

%files dev
%defattr(-,root,root,-)
/usr/include/idn2.h
/usr/lib64/libidn2.so
/usr/lib64/pkgconfig/libidn2.pc
/usr/share/man/man3/idn2_check_version.3
/usr/share/man/man3/idn2_free.3
/usr/share/man/man3/idn2_lookup_u8.3
/usr/share/man/man3/idn2_lookup_ul.3
/usr/share/man/man3/idn2_register_u8.3
/usr/share/man/man3/idn2_register_ul.3
/usr/share/man/man3/idn2_strerror.3
/usr/share/man/man3/idn2_strerror_name.3
/usr/share/man/man3/idn2_to_ascii_4i.3
/usr/share/man/man3/idn2_to_ascii_4i2.3
/usr/share/man/man3/idn2_to_ascii_4z.3
/usr/share/man/man3/idn2_to_ascii_8z.3
/usr/share/man/man3/idn2_to_ascii_lz.3
/usr/share/man/man3/idn2_to_unicode_44i.3
/usr/share/man/man3/idn2_to_unicode_4z4z.3
/usr/share/man/man3/idn2_to_unicode_8z4z.3
/usr/share/man/man3/idn2_to_unicode_8z8z.3
/usr/share/man/man3/idn2_to_unicode_8zlz.3
/usr/share/man/man3/idn2_to_unicode_lzlz.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libidn2.so
/usr/lib32/pkgconfig/32libidn2.pc
/usr/lib32/pkgconfig/libidn2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libidn2/api-index-full.html
/usr/share/gtk-doc/html/libidn2/home.png
/usr/share/gtk-doc/html/libidn2/index.html
/usr/share/gtk-doc/html/libidn2/left-insensitive.png
/usr/share/gtk-doc/html/libidn2/left.png
/usr/share/gtk-doc/html/libidn2/libidn2-idn2.html
/usr/share/gtk-doc/html/libidn2/libidn2.devhelp2
/usr/share/gtk-doc/html/libidn2/libidn2.html
/usr/share/gtk-doc/html/libidn2/right-insensitive.png
/usr/share/gtk-doc/html/libidn2/right.png
/usr/share/gtk-doc/html/libidn2/style.css
/usr/share/gtk-doc/html/libidn2/up-insensitive.png
/usr/share/gtk-doc/html/libidn2/up.png

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libidn2.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libidn2.so.0
/usr/lib64/libidn2.so.0.3.7

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libidn2.so.0
/usr/lib32/libidn2.so.0.3.7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/idn2.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libidn2.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libidn2.a

%files locales -f libidn2.lang
%defattr(-,root,root,-)

