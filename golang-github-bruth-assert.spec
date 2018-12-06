# Run tests in check section
%bcond_without check

%global goipath         github.com/bruth/assert
%global commit          de420fa3b72e87255136e10ade1e267581cc3947
%global common_description %{expand:
Simple test assertions for Go. This is a fork of a fork of a
bmizerany/assert with improved support for things like nil pointers,
etc.}

Version:        0

%gometa

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Simple test assertions for Golang tests
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         add-license.patch

BuildRequires:  golang(github.com/kr/pretty)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
%patch0 -p1

%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Aug 13 2018 Gabe <redhatrises@gmail.com> - 0.1.20180813gitde420fa
- First package for Fedora
