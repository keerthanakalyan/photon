%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name aws-sdk-s3

Name: rubygem-aws-sdk-s3
Version:        1.79.1
Release:        1%{?dist}
Summary:        Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3).
Group:          Development/Languages
License:        Apache 2.0
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://github.com/aws/aws-sdk-ruby/tree/master/gems/aws-sdk-s3-%{version}.gem
%define sha1    aws-sdk-s3=7a8df7be2059e72b1d5deaa1d57da81979d9bfab
BuildRequires:  ruby

Requires: rubygem-aws-sdk-core >= 3.21.2
Requires: rubygem-aws-sdk-kms >= 1
Requires: rubygem-aws-sigv4 >= 1.0

%description
Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3).
This gem is part of the AWS SDK for Ruby.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Thu Jul 16 2020 Gerrit Photon <photon-checkins@vmware.com> 1.79.1-1
-   Automatic Version Bump
*   Tue Sep 11 2018 srinidhira0 <srinidhir@vmware.com> 1.19.0-1
-   Update to version 1.19.0
*   Mon Jul 30 2018 Srinidhi Rao <srinidhir@vmware.com> 1.17.0-1
-   Initial build
