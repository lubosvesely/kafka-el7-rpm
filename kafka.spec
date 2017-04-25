%define  scala_version 2.11
%define  kafka_version 0.10.2.0

Name:    kafka
Version: %{kafka_version}
Release: 1%{?dist}
Summary: Apache Kafka - A distributed streaming platform

%define  kafka_filename %{name}_%{scala_version}-%{version}

License: Apache License Version 2.0
URL:     https://kafka.apache.org/
Source0: http://apache.cs.utah.edu/kafka/%{version}/%{kafka_filename}.tgz

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

install -m 755 %{kafka_filename}/bin/*.sh $RPM_BUILD_ROOT/opt/kafka/bin
install -m 644 %{kafka_filename}/config/* $RPM_BUILD_ROOT/opt/kafka/config
install -m 644 %{kafka_filename}/libs/* $RPM_BUILD_ROOT/opt/kafka/libs

%postun

%files
