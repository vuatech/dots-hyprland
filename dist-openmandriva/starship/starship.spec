%global debug_package %{nil}

Name:		starship
Version:	1.23.0
Release:	1
Source0:	https://github.com/starship/starship/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	The minimal, blazing-fast, and infinitely customizable prompt for any shell!
URL:		https://github.com/starship/starship
License:	ISC
Group:		?
BuildRequires:	cargo

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!

Fast: it's fast – really really fast! 🚀
Customizable: configure every aspect of your prompt.
Universal: works on any shell, on any operating system.
Intelligent: shows relevant information at a glance.
Feature rich: support for all your favorite tools.
Easy: quick to install – start using it in minutes.

%prep
%autosetup -p1

%build
cargo build --release

%install
install -Dpm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
