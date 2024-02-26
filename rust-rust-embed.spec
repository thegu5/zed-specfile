# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate rust-embed

Name:           rust-rust-embed
Version:        8.0.0
Release:        %autorelease
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev

License:        MIT
URL:            https://crates.io/crates/rust-embed
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust Custom Derive Macro which loads files into the rust binary at
compile time during release and loads the file from the fs during dev.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/license
%doc %{crate_instdir}/changelog.md
%doc %{crate_instdir}/readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+actix-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+actix-devel %{_description}

This package contains library source intended for building other packages which
use the "actix" feature of the "%{crate}" crate.

%files       -n %{name}+actix-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+actix-web-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+actix-web-devel %{_description}

This package contains library source intended for building other packages which
use the "actix-web" feature of the "%{crate}" crate.

%files       -n %{name}+actix-web-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+axum-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+axum-devel %{_description}

This package contains library source intended for building other packages which
use the "axum" feature of the "%{crate}" crate.

%files       -n %{name}+axum-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+axum-ex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+axum-ex-devel %{_description}

This package contains library source intended for building other packages which
use the "axum-ex" feature of the "%{crate}" crate.

%files       -n %{name}+axum-ex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compression-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compression-devel %{_description}

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%files       -n %{name}+compression-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug-embed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-embed-devel %{_description}

This package contains library source intended for building other packages which
use the "debug-embed" feature of the "%{crate}" crate.

%files       -n %{name}+debug-embed-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hex-devel %{_description}

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%files       -n %{name}+hex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+include-exclude-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+include-exclude-devel %{_description}

This package contains library source intended for building other packages which
use the "include-exclude" feature of the "%{crate}" crate.

%files       -n %{name}+include-exclude-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+include-flate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+include-flate-devel %{_description}

This package contains library source intended for building other packages which
use the "include-flate" feature of the "%{crate}" crate.

%files       -n %{name}+include-flate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+interpolate-folder-path-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+interpolate-folder-path-devel %{_description}

This package contains library source intended for building other packages which
use the "interpolate-folder-path" feature of the "%{crate}" crate.

%files       -n %{name}+interpolate-folder-path-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mime-guess-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mime-guess-devel %{_description}

This package contains library source intended for building other packages which
use the "mime-guess" feature of the "%{crate}" crate.

%files       -n %{name}+mime-guess-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mime_guess-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mime_guess-devel %{_description}

This package contains library source intended for building other packages which
use the "mime_guess" feature of the "%{crate}" crate.

%files       -n %{name}+mime_guess-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+poem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+poem-devel %{_description}

This package contains library source intended for building other packages which
use the "poem" feature of the "%{crate}" crate.

%files       -n %{name}+poem-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+poem-ex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+poem-ex-devel %{_description}

This package contains library source intended for building other packages which
use the "poem-ex" feature of the "%{crate}" crate.

%files       -n %{name}+poem-ex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rocket-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rocket-devel %{_description}

This package contains library source intended for building other packages which
use the "rocket" feature of the "%{crate}" crate.

%files       -n %{name}+rocket-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+salvo-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+salvo-devel %{_description}

This package contains library source intended for building other packages which
use the "salvo" feature of the "%{crate}" crate.

%files       -n %{name}+salvo-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+salvo-ex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+salvo-ex-devel %{_description}

This package contains library source intended for building other packages which
use the "salvo-ex" feature of the "%{crate}" crate.

%files       -n %{name}+salvo-ex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+warp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+warp-devel %{_description}

This package contains library source intended for building other packages which
use the "warp" feature of the "%{crate}" crate.

%files       -n %{name}+warp-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+warp-ex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+warp-ex-devel %{_description}

This package contains library source intended for building other packages which
use the "warp-ex" feature of the "%{crate}" crate.

%files       -n %{name}+warp-ex-devel
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
