%{?scl:%scl_package nodejs-are-we-there-yet}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-are-we-there-yet

%global npm_name are-we-there-yet
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-are-we-there-yet
Version:	1.0.4
Release:	1%{?dist}
Summary:	Keep track of the overall completion of many dispirate processes
Url:		https://github.com/iarna/are-we-there-yet
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

BuildRequires:	%{?scl_prefix}npm(delegates)
BuildRequires:	%{?scl_prefix}npm(readable-stream)

Requires:	%{?scl_prefix}npm(delegates)
Requires:	%{?scl_prefix}npm(readable-stream)

%description
Keep track of the overall completion of many dispirate processes

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/are-we-there-yet

%doc README.md

%changelog
* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build
