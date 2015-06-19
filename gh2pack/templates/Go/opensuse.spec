#
# spec file for package opensuse
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           go-{{name}}
Version:        0
Release:        0
License:        {{license.key|upper}}
Summary:        {{description}}
Url:            {{homepage}}
Group:          Development/Languages/Other
Source:         {{name}}-%{version}.tar.bz2
BuildRequires:  go-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_requires}
%{go_provides}
# The following line is only needed for (static) libraries:
%{go_recommends}
 
%description

%godoc_package 

%prep
%setup -q -n {{name}}-%{version}

%build
%goprep github.com/{{full_name}}
%gobuild ...

%install
%goinstall
%godoc

%check
%gotest github.com/{{full_name}}

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{go_contribdir}/*

%files doc
%defattr(-,root,root,-)
%{go_contribsrcdir}/*

%changelog
