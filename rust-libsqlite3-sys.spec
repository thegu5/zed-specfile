# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate libsqlite3-sys

Name:           rust-libsqlite3-sys
Version:        0.26.0
Release:        %autorelease
Summary:        Native bindings to the libsqlite3 library

License:        MIT
URL:            https://crates.io/crates/libsqlite3-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Native bindings to the libsqlite3 library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/sqlcipher/LICENSE
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/Upgrade.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+buildtime_bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+buildtime_bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+buildtime_bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bundled-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bundled-devel %{_description}

This package contains library source intended for building other packages which
use the "bundled" feature of the "%{crate}" crate.

%files       -n %{name}+bundled-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bundled-sqlcipher-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bundled-sqlcipher-devel %{_description}

This package contains library source intended for building other packages which
use the "bundled-sqlcipher" feature of the "%{crate}" crate.

%files       -n %{name}+bundled-sqlcipher-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bundled-sqlcipher-vendored-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bundled-sqlcipher-vendored-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "bundled-sqlcipher-vendored-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+bundled-sqlcipher-vendored-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bundled-windows-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bundled-windows-devel %{_description}

This package contains library source intended for building other packages which
use the "bundled-windows" feature of the "%{crate}" crate.

%files       -n %{name}+bundled-windows-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bundled_bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bundled_bindings-devel %{_description}

This package contains library source intended for building other packages which
use the "bundled_bindings" feature of the "%{crate}" crate.

%files       -n %{name}+bundled_bindings-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cc-devel %{_description}

This package contains library source intended for building other packages which
use the "cc" feature of the "%{crate}" crate.

%files       -n %{name}+cc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+in_gecko-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+in_gecko-devel %{_description}

This package contains library source intended for building other packages which
use the "in_gecko" feature of the "%{crate}" crate.

%files       -n %{name}+in_gecko-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+min_sqlite_version_3_14_0-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+min_sqlite_version_3_14_0-devel %{_description}

This package contains library source intended for building other packages which
use the "min_sqlite_version_3_14_0" feature of the "%{crate}" crate.

%files       -n %{name}+min_sqlite_version_3_14_0-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-sys-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

%files       -n %{name}+openssl-sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pkg-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkg-config-devel %{_description}

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%files       -n %{name}+pkg-config-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+preupdate_hook-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+preupdate_hook-devel %{_description}

This package contains library source intended for building other packages which
use the "preupdate_hook" feature of the "%{crate}" crate.

%files       -n %{name}+preupdate_hook-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+session-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+session-devel %{_description}

This package contains library source intended for building other packages which
use the "session" feature of the "%{crate}" crate.

%files       -n %{name}+session-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sqlcipher-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sqlcipher-devel %{_description}

This package contains library source intended for building other packages which
use the "sqlcipher" feature of the "%{crate}" crate.

%files       -n %{name}+sqlcipher-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unlock_notify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unlock_notify-devel %{_description}

This package contains library source intended for building other packages which
use the "unlock_notify" feature of the "%{crate}" crate.

%files       -n %{name}+unlock_notify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vcpkg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vcpkg-devel %{_description}

This package contains library source intended for building other packages which
use the "vcpkg" feature of the "%{crate}" crate.

%files       -n %{name}+vcpkg-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wasm32-wasi-vfs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm32-wasi-vfs-devel %{_description}

This package contains library source intended for building other packages which
use the "wasm32-wasi-vfs" feature of the "%{crate}" crate.

%files       -n %{name}+wasm32-wasi-vfs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+winsqlite3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+winsqlite3-devel %{_description}

This package contains library source intended for building other packages which
use the "winsqlite3" feature of the "%{crate}" crate.

%files       -n %{name}+winsqlite3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-asan-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-asan-devel %{_description}

This package contains library source intended for building other packages which
use the "with-asan" feature of the "%{crate}" crate.

%files       -n %{name}+with-asan-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
