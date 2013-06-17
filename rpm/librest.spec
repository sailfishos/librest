Name:          librest
Version:       0.7.12
Release:       1
Summary:       A library for access to RESTful web services
Group:         Development/Libraries
License:       LGPLv2
URL:           http://www.gnome.org
Source0:       %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: ca-certificates
Obsoletes:     rest <= 0.7.12

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: rest-devel <= 0.7.12

%description devel
Files for development with %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make
export LDFLAGS="${LDFLAGS} -lgthread-2.0"
autoreconf -v -i
%configure --disable-static --disable-gtk-doc --enable-introspection=no --without-gnome

make %{?jobs:-j%jobs} V=1

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/librest-0.7.so.0
%{_libdir}/librest-0.7.so.0.0.0
%{_libdir}/librest-extras-0.7.so.0
%{_libdir}/librest-extras-0.7.so.0.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/rest-0.7
%{_libdir}/pkgconfig/rest*
%{_libdir}/librest-0.7.so
%{_libdir}/librest-extras-0.7.so
