%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-memcached
%global commit 4c70dbd69fd00fe5ee10128e42abce96920faa91
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-memcached
Version:        6.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Manage memcached via Puppet
License:        ASL 2.0

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
* Thu Mar 25 2021 RDO <dev@lists.rdoproject.org> 6.0.0-1.4c70dbdgit
- Update to post 6.0.0 (4c70dbd69fd00fe5ee10128e42abce96920faa91)



