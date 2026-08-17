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
    translation = "src/assets/translation/localisation.csv"
    with open("src/assets/README.md", "r") as readme:
        readme = readme.read()
    with open("src/assets/LICENSE", "r") as l:
        applicense = l.read()
    tr = TR(langcode=f"{lang}", csv_file=translation)
    license_dlg = ft.AlertDialog(
        title=ft.Text(tr.tr(target_key="LICENSE", langcode=f"{lang}")),
        content=ft.Text(applicense),
        scrollable=True,
    )
    readme_dlg = ft.AlertDialog(
        title=ft.Text(tr.tr(target_key="ABOUT", langcode=f"{lang}")),
        content=ft.Markdown(
            readme,
            on_tap_link=lambda e: page.launch_url(url=f"{e.data}"),
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        ),
        scrollable=True,
    )

    page.adaptive = True
    page.scroll = ft.ScrollMode.AUTO
    page.window.min_height = 500
    page.window.min_width = 500
    page.appbar = ft.AppBar(
        title=ft.Text("MySysInfo"),
        leading=ft.Image(
            src="src/assets/icon.png",
        ),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        content=tr.tr(target_key="ABOUT", langcode=f"{lang}"),
                        on_click=lambda e: page.show_dialog(readme_dlg),
                    ),
                    ft.PopupMenuItem(
                        content=tr.tr(target_key="LICENSE", langcode=f"{lang}"),
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
                        label=ft.Text(
                            tr.tr(
                                target_key="PARAMETER",
                                langcode=f"{lang}",
                            )
                        )
                    ),
                    ft.DataColumn(
                        label=ft.Text(tr.tr(target_key="VALUE", langcode=f"{lang}"))
                    ),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="SYSTEM",
                                        langcode=f"{lang}",
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(
                                ft.Text(str(page.platform.name))
                            ),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="USERNAME",
                                        langcode=f"{lang}",
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
                                        langcode=f"{lang}",
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
                                        langcode=f"{lang}",
                                    )
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(str(architecture))),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr.tr(
                                        target_key="PROCESSORTYPE",
                                        langcode=f"{lang}",
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
                                        langcode=f"{lang}",
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
