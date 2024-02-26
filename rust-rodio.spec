# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate rodio

Name:           rust-rodio
Version:        0.17.1
Release:        %autorelease
Summary:        Audio playback library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rodio
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Audio playback library.}

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
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+claxon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+claxon-devel %{_description}

This package contains library source intended for building other packages which
use the "claxon" feature of the "%{crate}" crate.

%files       -n %{name}+claxon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+flac-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+flac-devel %{_description}

This package contains library source intended for building other packages which
use the "flac" feature of the "%{crate}" crate.

%files       -n %{name}+flac-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hound-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hound-devel %{_description}

This package contains library source intended for building other packages which
use the "hound" feature of the "%{crate}" crate.

%files       -n %{name}+hound-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lewton-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lewton-devel %{_description}

This package contains library source intended for building other packages which
use the "lewton" feature of the "%{crate}" crate.

%files       -n %{name}+lewton-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+minimp3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+minimp3-devel %{_description}

This package contains library source intended for building other packages which
use the "minimp3" feature of the "%{crate}" crate.

%files       -n %{name}+minimp3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mp3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mp3-devel %{_description}

This package contains library source intended for building other packages which
use the "mp3" feature of the "%{crate}" crate.

%files       -n %{name}+mp3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-aac-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-aac-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-aac" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-aac-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-all-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-all" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-all-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-flac-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-flac-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-flac" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-flac-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-isomp4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-isomp4-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-isomp4" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-isomp4-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-mp3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-mp3-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-mp3" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-mp3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-vorbis-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-vorbis-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-vorbis" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-vorbis-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+symphonia-wav-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+symphonia-wav-devel %{_description}

This package contains library source intended for building other packages which
use the "symphonia-wav" feature of the "%{crate}" crate.

%files       -n %{name}+symphonia-wav-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vorbis-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vorbis-devel %{_description}

This package contains library source intended for building other packages which
use the "vorbis" feature of the "%{crate}" crate.

%files       -n %{name}+vorbis-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wasm-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+wasm-bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wav-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wav-devel %{_description}

This package contains library source intended for building other packages which
use the "wav" feature of the "%{crate}" crate.

%files       -n %{name}+wav-devel
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
