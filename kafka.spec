%define  __jar_repack 0
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
Source1: kafka.service
Source2: kafka.sysconfig

Requires(post): systemd

%description
Kafka is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

%clean
rm -rf %{buildroot}

%prep

%build
tar xvf %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/opt/kafka/{bin,libs}
install -d $RPM_BUILD_ROOT/etc/kafka
install -d $RPM_BUILD_ROOT/etc/sysconfig/kafka

install -m 755 %{kafka_filename}/bin/*.sh $RPM_BUILD_ROOT/opt/kafka/bin
install -m 644 %{kafka_filename}/libs/* $RPM_BUILD_ROOT/opt/kafka/libs
install -m 644 %{kafka_filename}/config/server.properties $RPM_BUILD_ROOT/etc/kafka
install -m 644 %{kafka_filename}/config/log4j.properties $RPM_BUILD_ROOT/etc/kafka
# install -m 755 %{S:1} $RPM_BUILD_ROOT/%{_unitdir}/
install -m 644 %{S:2} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/kafka

%files
%defattr(-,root,root,-)
/opt/kafka
/etc/kafka
# %{_unitdir}/kafka.service
%{_sysconfdir}/sysconfig/kafka
