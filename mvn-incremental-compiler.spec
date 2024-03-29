#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-incremental-compiler
Version  : 0.13.15
Release  : 2
URL      : https://repo1.maven.org/maven2/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.jar
Source0  : https://repo1.maven.org/maven2/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.jar
Source1  : https://repo1.maven.org/maven2/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.pom
Source2  : https://repo1.maven.org/maven2/com/typesafe/sbt/incremental-compiler/0.13.5/incremental-compiler-0.13.5.jar
Source3  : https://repo1.maven.org/maven2/com/typesafe/sbt/incremental-compiler/0.13.5/incremental-compiler-0.13.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: mvn-incremental-compiler-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-incremental-compiler package.
Group: Data

%description data
data components for the mvn-incremental-compiler package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.15
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.15
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.5
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.5/incremental-compiler-0.13.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.5/incremental-compiler-0.13.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.jar
/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.15/incremental-compiler-0.13.15.pom
/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.5/incremental-compiler-0.13.5.jar
/usr/share/java/.m2/repository/com/typesafe/sbt/incremental-compiler/0.13.5/incremental-compiler-0.13.5.pom
