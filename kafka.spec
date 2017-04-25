%define  scala_version 2.11

Name:    kafka
Version: 0.10.2.0
Release: 1%{?dist}
Summary: Apache Kafka - A distributed streaming platform

License: Apache License Version 2.0
URL:     https://kafka.apache.org/
Source0: http://apache.cs.utah.edu/kafka/%{version}/%{name}_%{scala_version}-%{version}.tgz

BuildArch: noarch

%description
Kafka is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

%clean
rm -rf %{buildroot}

%prep

%build
tar xvf %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/opt/kafka/{libs,bin,config}

install -m 755 bin/*.sh $RPM_BUILD_ROOT%/opt/kafka/bin
install -m 644 config/* $RPM_BUILD_ROOT%/opt/kafka/config
install -m 644 libs/* $RPM_BUILD_ROOT%/opt/kafka/libs

%postun

%files
