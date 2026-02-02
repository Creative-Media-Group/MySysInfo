import flet as ft
import locale
from mylocale import TR
import platform as p
import os
from pathlib import Path

# import screen

lang = locale.getlocale()
lang, _ = lang

architecture = p.architecture()
architecture, _ = architecture
processor = p.processor()
version = p.version()
node = p.node()
machine = p.machine()
release = p.release()


def main(page: ft.Page):
    translation = "assets/translation/localisation.csv"
    with open("assets/README.md", "r") as readme:
        readme = readme.read()
    with open("assets/LICENSE", "r") as l:
        applicense = l.read()
    tr = TR(langcode=lang, csv_file=translation)
    license_dlg = ft.AlertDialog(
        title=ft.Text(tr.tr(target_key="LICENSE", langcode=lang)),
        content=ft.Text(applicense),
        scrollable=True,
    )
    readme_dlg = ft.AlertDialog(
        title=ft.Text(tr.tr(target_key="ABOUT", langcode=lang)),
        content=ft.Markdown(
            readme,
            on_tap_link=lambda e: page.launch_url(e.data),
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        ),
        scrollable=True,
    )

    page.adaptive = True
    page.scroll = True
    page.window.min_height = 500
    page.window.min_width = 500
    page.appbar = ft.AppBar(
        title=ft.Text("MySysInfo"),
        leading=ft.Image(
            src="assets/icon.png",
        ),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        content=tr.tr(target_key="ABOUT", langcode=lang),
                        on_click=lambda e: page.show_dialog(readme_dlg),
                    ),
                    ft.PopupMenuItem(
                        content=tr.tr(target_key="LICENSE", langcode=lang),
                        on_click=lambda e: page.show_dialog(license_dlg),
                    ),
                ]
            ),
        ],
    )
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.INFO, on_click=lambda e: page.show_dialog(readme_dlg)
    )
    page.add(
        ft.SafeArea(
            ft.DataTable(
                columns=[
                    ft.DataColumn(
                        ft.Text(
                            tr.tr(
                                target_key="PARAMETER",
                                langcode=lang,
                            )
                        )
                    ),
                    ft.DataColumn(ft.Text(tr.tr(target_key="VALUE", langcode=lang))),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="SYSTEM",
                                        langcode=lang,
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(page.platform.value)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="USERNAME",
                                        langcode=lang,
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(
                                ft.Text(str(os.getenv("USER")))
                            ),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="VERSION",
                                        langcode=lang,
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(version)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="ARCHITECTURE",
                                        langcode=lang,
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(architecture)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="PROCESSORTYPE",
                                        langcode=lang,
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(machine)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="HOSTNAME",
                                        langcode=lang,
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(node)),  # 2'nd collumn
                        ]
                    ),
                ],
                width=page.window.width,
            )
        )
    )


ft.run(main=main)
