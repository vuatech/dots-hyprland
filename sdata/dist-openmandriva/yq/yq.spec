%global debug_package %{nil}

Name:		yq
Version:	4.48.1
Release:	1
Source0:	https://github.com/mikefarah/yq/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor
URL:		https://github.com/mikefarah/yq
License:	MIT
Group:		?
BuildRequires:	go

%description
%summary

%prep
%autosetup -p1


%build
go build -buildmode=pie

%install
install -Dt %{buildroot}%{_bindir}/ yq

%files
%license LICENSE
%doc README.md
%{_bindir}/yq
