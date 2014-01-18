%define _unpackaged_files_terminate_build 0
%define _target_os linux
%define project_version 1.0.13.4
%define _binaries_in_noarch_packages_terminate_build   0
Name:		CloudWatch
Version:	1.0.13.4
Release:	1
Vendor:		Amazon
Summary:	Packaged version of the Amazon CloudWatch Command Lines Tools
Source0:	CloudWatch-2010-08-01.zip 
License:	http://aws.amazon.com/terms/
Group:		Virtualization
Requires:	java
autoprov:	yes
autoreq:	yes
Prefix:		/opt/cloudwatch
BuildArch:	noarch
Packager:	Krasnobay Alexander <l3dz@ya.ru>

%description
The Command Line Tool serves as the client interface to the Amazon CloudWatch web service. 
Use this tool to monitor, manage, and publish Amazon CloudWatch metrics,
 as well as configure alarm actions based on data from metrics.

%setup -q 

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/%{prefix}/

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
echo 'export AWS_CLOUDWATCH_HOME=/opt/cloudwatch' >> $RPM_BUILD_ROOT/etc/profile.d/cloudwatch.sh
echo 'export AWS_CLOUDWATCH_URL=http://monitoring.us-west-1.amazonaws.com' >> $RPM_BUILD_ROOT/etc/profile.d/cloudwatch.sh
echo 'export PATH=$PATH:$AWS_CLOUDWATCH_HOME/bin' >> $RPM_BUILD_ROOT/etc/profile.d/cloudwatch.sh 
chmod +x $RPM_BUILD_ROOT/etc/profile.d/cloudwatch.sh

unzip -d  $RPM_BUILD_ROOT %{SOURCE0}
cp -Rp $RPM_BUILD_ROOT/%{name}-%{version}/* $RPM_BUILD_ROOT%{prefix}

# remove windows batch files.
rm -f $RPM_BUILD_ROOT%{prefix}/bin/*.cmd


%files
%defattr(-,root,root,-)
%dir %{prefix}/*
%dir %{prefix}/bin/*
%dir %{prefix}/lib/*

%pre

%post

%preun
if [ "$1" -eq "0" ]
then
rm -rf /etc/profile.d/cloudwatch.sh
fi

%postun

%posttrans

%changelog
* Sat Jan 18 2014 Krasnobai Alexander <l3dz@ya.ru> - 1.0.13.4
- Initial packaging attempt