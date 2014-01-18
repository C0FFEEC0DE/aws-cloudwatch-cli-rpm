 
This repository contains CentOS/RPM packaging for the [Amazon CloudWatch Command Line Tools] 
(http://aws.amazon.com/developertools/2534), which are
command-line utilities that interface with Amazon's CloudWatch service.

If you wish to use `rpm`, or `yum` to install the Amazon
CloudWatch Tools on a Redhat/CentOS system, then you might
be interested in this packaging.

Current CloudWatch CLI Version in this repo is 1.0.13.4. 

## Requirements

Requires the following packages to be installed:
rpm-build

## Usage

### Building the Redhat/CentOS packages 

1. Clone this repository 
2. In the repository home directory, run

cp cloudwatch.spec ~/rpmbuild/SPECS/

wget http://ec2-downloads.s3.amazonaws.com/CloudWatch-2010-08-01.zip

cp CloudWatch-2010-08-01.zip ~/rpmbuild/SOURCES/

rpmbuild -bb ~/rpmbuild/SPEC/cloudwatch.spec  

RPM will be built and will be located ~/rpmbuild/RPMS/noarch/CloudWatch-1.0.13.4-1.noarch.rpm

## Information
If you are just looking for the rpm, check out the rpm folder in this project 
 
