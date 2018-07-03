#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rsdmx
Version  : 0.5.12
Release  : 4
URL      : https://cran.r-project.org/src/contrib/rsdmx_0.5-12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsdmx_0.5-12.tar.gz
Summary  : Tools for Reading SDMX Data and Metadata
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RCurl
Requires: R-XML
Requires: R-markdown
Requires: R-plyr
Requires: R-stringi
BuildRequires : R-RCurl
BuildRequires : R-XML
BuildRequires : R-markdown
BuildRequires : R-plyr
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
exchanged through the Statistical Data and Metadata Exchange (SDMX) framework,
  currently focusing on the SDMX XML standard format (SDMX-ML).

%prep
%setup -q -c -n rsdmx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530659878

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530659878
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsdmx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsdmx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsdmx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rsdmx|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rsdmx/DESCRIPTION
/usr/lib64/R/library/rsdmx/INDEX
/usr/lib64/R/library/rsdmx/Meta/Rd.rds
/usr/lib64/R/library/rsdmx/Meta/features.rds
/usr/lib64/R/library/rsdmx/Meta/hsearch.rds
/usr/lib64/R/library/rsdmx/Meta/links.rds
/usr/lib64/R/library/rsdmx/Meta/nsInfo.rds
/usr/lib64/R/library/rsdmx/Meta/package.rds
/usr/lib64/R/library/rsdmx/Meta/vignette.rds
/usr/lib64/R/library/rsdmx/NAMESPACE
/usr/lib64/R/library/rsdmx/R/rsdmx
/usr/lib64/R/library/rsdmx/R/rsdmx.rdb
/usr/lib64/R/library/rsdmx/R/rsdmx.rdx
/usr/lib64/R/library/rsdmx/doc/index.html
/usr/lib64/R/library/rsdmx/doc/quickstart.R
/usr/lib64/R/library/rsdmx/doc/quickstart.Rmd
/usr/lib64/R/library/rsdmx/doc/quickstart.html
/usr/lib64/R/library/rsdmx/extdata/Example_Eurostat_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/Example_Eurostat_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXCodelists_Example_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXCodelists_Example_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXCompactDataExample_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXConceptSchemes_Example_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXConceptSchemes_Example_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXConcepts_Example_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXCrossSectionalDataExample_1.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXDataFlows_Example_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXDataStructureDefinition_Example_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXDataStructureDefinition_Example_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXDataStructures_Example_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXDataStructures_Example_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXGenericDataExample_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXGenericDataExample_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXMessageExample_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXMessageExample_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXMessageGroupExample_CompactData_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXMessageGroupExample_GenericData_2.0.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXOrganisationSchemes_Example_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMXStructureSpecificDataExample_2.1.xml
/usr/lib64/R/library/rsdmx/extdata/SDMX_SOAP_Example.xml
/usr/lib64/R/library/rsdmx/help/AnIndex
/usr/lib64/R/library/rsdmx/help/aliases.rds
/usr/lib64/R/library/rsdmx/help/paths.rds
/usr/lib64/R/library/rsdmx/help/rsdmx.rdb
/usr/lib64/R/library/rsdmx/help/rsdmx.rdx
/usr/lib64/R/library/rsdmx/html/00Index.html
/usr/lib64/R/library/rsdmx/html/R.css
