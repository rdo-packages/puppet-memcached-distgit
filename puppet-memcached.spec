%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppet-memcached
%global commit 66d3a667d4e7e0253949f9d83c230b5f8ccca596
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-memcached
Version:        6.0.0
Release:        1%{?dist}
Summary:        Manage memcached via Puppet
License:        ASL 2.0

URL:            https://github.com/saz/puppet-memcached

Source0:        https://github.com/saz/%{upstream_name}/archive/v%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-firewall
Requires:       puppet >= 2.7.0

%description
Manage memcached via Puppet

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached/



%files
%{_datadir}/openstack-puppet/modules/memcached/


%changelog
* Wed Mar 10 2021 RDO <dev@lists.rdoproject.org> 6.0.0-1
- Update to 6.0.0

* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 3.4.0-1.66d3a66git
- Update to post 3.4.0 (66d3a667d4e7e0253949f9d83c230b5f8ccca596)



