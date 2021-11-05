#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rsdmx
Version  : 0.6
Release  : 33
URL      : https://cran.r-project.org/src/contrib/rsdmx_0.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsdmx_0.6.tar.gz
Summary  : Tools for Reading SDMX Data and Metadata
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-R6
Requires: R-XML
Requires: R-httr
Requires: R-plyr
BuildRequires : R-R6
BuildRequires : R-XML
BuildRequires : R-httr
BuildRequires : R-plyr
BuildRequires : buildreq-R

%description
exchanged through the Statistical Data and Metadata Exchange (SDMX) framework,
  currently focusing on the SDMX XML standard format (SDMX-ML).

%prep
%setup -q -c -n rsdmx
cd %{_builddir}/rsdmx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612808911

%install
export SOURCE_DATE_EPOCH=1612808911
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsdmx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsdmx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsdmx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rsdmx || :


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
/usr/lib64/R/library/rsdmx/tests/test-all.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Codelists.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_CompactData.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Concepts.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_CrossSectionalData.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Data.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_DataFlows.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_DataStructureDefinition.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_DataStructures.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Footer.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_GenericData.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Header.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Main.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Main_Helpers.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_MessageGroup.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Namespaces.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_OrganisationSchemes.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_RequestBuilder.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Schema.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_ServiceProvider.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Soap.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_StructureSpecificData.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_Type.R
/usr/lib64/R/library/rsdmx/tests/testthat/test_saveSDMX.R
