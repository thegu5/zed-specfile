# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate ipc-channel

Name:           rust-ipc-channel
Version:        0.16.0
Release:        %autorelease
Summary:        Multiprocess drop-in replacement for Rust channels

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ipc-channel
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          ipc-channel-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A multiprocess drop-in replacement for Rust channels.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-devel %{_description}

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%files       -n %{name}+async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+force-inprocess-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+force-inprocess-devel %{_description}

This package contains library source intended for building other packages which
use the "force-inprocess" feature of the "%{crate}" crate.

%files       -n %{name}+force-inprocess-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-test-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-test" feature of the "%{crate}" crate.

%files       -n %{name}+futures-test-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+memfd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memfd-devel %{_description}

This package contains library source intended for building other packages which
use the "memfd" feature of the "%{crate}" crate.

%files       -n %{name}+memfd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sc-devel %{_description}

This package contains library source intended for building other packages which
use the "sc" feature of the "%{crate}" crate.

%files       -n %{name}+sc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+win32-trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+win32-trace-devel %{_description}

This package contains library source intended for building other packages which
use the "win32-trace" feature of the "%{crate}" crate.

%files       -n %{name}+win32-trace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+windows-shared-memory-equality-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+windows-shared-memory-equality-devel %{_description}

This package contains library source intended for building other packages which
use the "windows-shared-memory-equality" feature of the "%{crate}" crate.

%files       -n %{name}+windows-shared-memory-equality-devel
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