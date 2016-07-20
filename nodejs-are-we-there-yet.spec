%{?scl:%scl_package nodejs-are-we-there-yet}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-are-we-there-yet

%global npm_name are-we-there-yet
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-are-we-there-yet
Version:	1.0.6
Release:	2%{?dist}
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
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

BuildRequires:	%{?scl_prefix}nodejs-delegates
BuildRequires:	%{?scl_prefix}nodejs-readable-stream

Requires:	%{?scl_prefix}nodejs-delegates
Requires:	%{?scl_prefix}nodejs-readable-stream

%description
Keep track of the overall completion of many dispirate processes

%prep
%setup -q -n package

rm -rf node_modules

%nodejs_fixdep delegates '<1.0.0'
%nodejs_fixdep readable-stream

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

%doc README.md LICENSE

%changelog
* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.6-2
- Resolves: rhbz#1334856 , fixes wrong license, update

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-4
- Add %%nodejs_fixdep macro

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-3
- rebuilt

* Sat Feb 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-2
- Remove unnecessary file

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build
