# Generated by rust2rpm 25
%bcond_without check

Name:           zed
Version:        0.123.2
Release:        %autorelease
Summary:        Fast, collaborative code editor

SourceLicense:  AGPL-3.0-or-later AND Apache-2.0 AND GPL-3.0-or-later AND MIT
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown

URL:            https://zed.dev
Source:         https://github.com/zed-industries/zed/archive/refs/tags/v%{version}.tar.gz

# Patch0: bump-tree-sitter-lua.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
The fast, collaborative code editor.}

%description %{_description}

%prep
# -n v%{version} 
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE-AGPL
%license LICENSE-APACHE
%license LICENSE-GPL
%license assets/themes/LICENSES
%license assets/themes/andromeda/LICENSE
%license assets/themes/atelier/LICENSE
%license assets/themes/ayu/LICENSE
%license assets/themes/gruvbox/LICENSE
%license assets/themes/one/LICENSE
%license assets/themes/rose_pine/LICENSE
%license assets/themes/sandcastle/LICENSE
%license assets/themes/solarized/LICENSE
%license assets/themes/summercamp/LICENSE
%license crates/activity_indicator/LICENSE-GPL
%license crates/ai/LICENSE-GPL
%license crates/assets/LICENSE-GPL
%license crates/assistant/LICENSE-GPL
%license crates/audio/LICENSE-GPL
%license crates/auto_update/LICENSE-GPL
%license crates/breadcrumbs/LICENSE-GPL
%license crates/call/LICENSE-GPL
%license crates/channel/LICENSE-GPL
%license crates/cli/LICENSE-GPL
%license crates/client/LICENSE-GPL
%license crates/clock/LICENSE-GPL
%license crates/collab/LICENSE-AGPL
%license crates/collab_ui/LICENSE-GPL
%license crates/collections/LICENSE-APACHE
%license crates/color/LICENSE-GPL
%license crates/command_palette/LICENSE-GPL
%license crates/copilot/LICENSE-GPL
%license crates/copilot_ui/LICENSE-GPL
%license crates/db/LICENSE-GPL
%license crates/diagnostics/LICENSE-GPL
%license crates/editor/LICENSE-GPL
%license crates/extension/LICENSE-GPL
%license crates/extensions_ui/LICENSE-GPL
%license crates/feature_flags/LICENSE-GPL
%license crates/feedback/LICENSE-GPL
%license crates/file_finder/LICENSE-GPL
%license crates/fs/LICENSE-GPL
%license crates/fsevent/LICENSE-GPL
%license crates/fuzzy/LICENSE-GPL
%license crates/git/LICENSE-GPL
%license crates/go_to_line/LICENSE-GPL
%license crates/gpui/LICENSE-APACHE
%license crates/gpui_macros/LICENSE-APACHE
%license crates/install_cli/LICENSE-GPL
%license crates/journal/LICENSE-GPL
%license crates/language/LICENSE-GPL
%license crates/language_selector/LICENSE-GPL
%license crates/language_tools/LICENSE-GPL
%license crates/live_kit_client/LICENSE-GPL
%license crates/live_kit_server/LICENSE-AGPL
%license crates/lsp/LICENSE-GPL
%license crates/markdown_preview/LICENSE-GPL
%license crates/media/LICENSE-APACHE
%license crates/menu/LICENSE-GPL
%license crates/multi_buffer/LICENSE-GPL
%license crates/node_runtime/LICENSE-GPL
%license crates/notifications/LICENSE-GPL
%license crates/outline/LICENSE-GPL
%license crates/picker/LICENSE-GPL
%license crates/plugin/LICENSE-GPL
%license crates/plugin_macros/LICENSE-GPL
%license crates/plugin_runtime/LICENSE-GPL
%license crates/prettier/LICENSE-GPL
%license crates/project/LICENSE-GPL
%license crates/project_panel/LICENSE-GPL
%license crates/project_symbols/LICENSE-GPL
%license crates/quick_action_bar/LICENSE-GPL
%license crates/recent_projects/LICENSE-GPL
%license crates/refineable/LICENSE-APACHE
%license crates/refineable/derive_refineable/LICENSE-APACHE
%license crates/release_channel/LICENSE-GPL
%license crates/rich_text/LICENSE-GPL
%license crates/rope/LICENSE-GPL
%license crates/rpc/LICENSE-GPL
%license crates/search/LICENSE-GPL
%license crates/semantic_index/LICENSE-GPL
%license crates/settings/LICENSE-GPL
%license crates/snippet/LICENSE-GPL
%license crates/sqlez/LICENSE-GPL
%license crates/sqlez_macros/LICENSE-GPL
%license crates/story/LICENSE-GPL
%license crates/storybook/LICENSE-GPL
%license crates/sum_tree/LICENSE-APACHE
%license crates/task/LICENSE-GPL
%license crates/tasks_ui/LICENSE-GPL
%license crates/terminal/LICENSE-GPL
%license crates/terminal_view/LICENSE-GPL
%license crates/text/LICENSE-GPL
%license crates/theme/LICENSE-GPL
%license crates/theme_importer/LICENSE-GPL
%license crates/theme_selector/LICENSE-GPL
%license crates/ui/LICENSE-GPL
%license crates/util/LICENSE-APACHE
%license crates/vcs_menu/LICENSE-GPL
%license crates/vim/LICENSE-GPL
%license crates/welcome/LICENSE-GPL
%license crates/workspace/LICENSE-GPL
%license crates/zed/LICENSE-GPL
%license crates/zed_actions/LICENSE-GPL
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/Zed
%{_bindir}/cli
%{_bindir}/collab
%{_bindir}/dotenv
%{_bindir}/extension_json_schemas
%{_bindir}/seed
%{_bindir}/storybook
%{_bindir}/theme_importer

%changelog
%autochangelog
