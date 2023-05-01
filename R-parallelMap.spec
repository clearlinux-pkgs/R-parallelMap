#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-parallelMap
Version  : 1.5.1
Release  : 8
URL      : https://cran.r-project.org/src/contrib/parallelMap_1.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/parallelMap_1.5.1.tar.gz
Summary  : Unified Interface to Parallelization Back-Ends
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-BBmisc
Requires: R-checkmate
BuildRequires : R-BBmisc
BuildRequires : R-BatchJobs
BuildRequires : R-batchtools
BuildRequires : R-checkmate
BuildRequires : buildreq-R

%description
back-end, designed for internal package and interactive usage.  The
    main operation is parallel mapping over lists.  Supports 'local',
    'multicore', 'mpi' and 'BatchJobs' mode.  Allows tagging of the
    parallel operation with a level name that can be later selected by the
    user to switch on parallel execution for exactly this operation.

%prep
%setup -q -c -n parallelMap
cd %{_builddir}/parallelMap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641069844

%install
export SOURCE_DATE_EPOCH=1641069844
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parallelMap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parallelMap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parallelMap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc parallelMap || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/parallelMap/DESCRIPTION
/usr/lib64/R/library/parallelMap/INDEX
/usr/lib64/R/library/parallelMap/LICENSE
/usr/lib64/R/library/parallelMap/Meta/Rd.rds
/usr/lib64/R/library/parallelMap/Meta/features.rds
/usr/lib64/R/library/parallelMap/Meta/hsearch.rds
/usr/lib64/R/library/parallelMap/Meta/links.rds
/usr/lib64/R/library/parallelMap/Meta/nsInfo.rds
/usr/lib64/R/library/parallelMap/Meta/package.rds
/usr/lib64/R/library/parallelMap/NAMESPACE
/usr/lib64/R/library/parallelMap/NEWS.md
/usr/lib64/R/library/parallelMap/R/parallelMap
/usr/lib64/R/library/parallelMap/R/parallelMap.rdb
/usr/lib64/R/library/parallelMap/R/parallelMap.rdx
/usr/lib64/R/library/parallelMap/help/AnIndex
/usr/lib64/R/library/parallelMap/help/aliases.rds
/usr/lib64/R/library/parallelMap/help/parallelMap.rdb
/usr/lib64/R/library/parallelMap/help/parallelMap.rdx
/usr/lib64/R/library/parallelMap/help/paths.rds
/usr/lib64/R/library/parallelMap/html/00Index.html
/usr/lib64/R/library/parallelMap/html/R.css
/usr/lib64/R/library/parallelMap/test_source_file.R
/usr/lib64/R/library/parallelMap/tests/run-all.R
/usr/lib64/R/library/parallelMap/tests/testthat/helper_sockettest.R
/usr/lib64/R/library/parallelMap/tests/testthat/helpers.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_01_registerLevels.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_autodetectCpus.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_batchjobs.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_batchtools.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_local.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_mpi.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_multicore.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_parallelApply.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_parallelGetOptions.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_parallelLibrary.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_parallelStart.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_reproducibility.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_socket.R
/usr/lib64/R/library/parallelMap/tests/testthat/test_stopWithJobErrorMessages.R
