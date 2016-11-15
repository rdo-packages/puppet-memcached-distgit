%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-memcached
%global commit 7671b5f9dd9999948ee3916fc93a860891929275
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-memcached
Version:        2.8.1
Release:        2%{?alphatag}%{?dist}
Summary:        Manage memcached via Puppet
License:        Apache License, Version 2.0

URL:            https://github.com/saz/puppet-memcached

Source0:        https://github.com/saz/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 2.8.1-2.7671b5f.git
- Newton update 2.8.1 (7671b5f9dd9999948ee3916fc93a860891929275)

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 2.8.1-1.bfa64e0.git
- Newton update 2.8.1 (bfa64e066a709cae8bed12ff95e9d630ad50af14)


