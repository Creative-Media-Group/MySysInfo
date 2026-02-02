import flet as ft
import locale
from mylocale.TR import tr
import platform as p
import os

# import screen

lang = locale.getlocale()
lang, _ = lang
translation = "assets/translation/localisation.csv"
with open("README.md", "r") as readme:
    readme = readme.read()
with open("LICENSE", "r") as l:
    applicense = l.read()
architecture = p.architecture()
architecture, _ = architecture
processor = p.processor()
version = p.version()
node = p.node()
machine = p.machine()
release = p.release()


def main(page: ft.Page):
    license_dlg = ft.AlertDialog(
        title=ft.Text(tr(csv_file=translation, target_key="LICENSE", langcode=lang)),
        content=ft.Text(applicense),
        scrollable=True,
    )
    readme_dlg = ft.AlertDialog(
        title=ft.Text(tr(csv_file=translation, target_key="ABOUT", langcode=lang)),
        content=ft.Markdown(
            readme,
            on_tap_link=lambda e: page.launch_url(e.data),
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        ),
        scrollable=True,
    )

    def open_license_dlg(e):
        page.open(license_dlg)
        page.update()

    def open_readme_dlg(e):
        page.open(readme_dlg)
        page.update()

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
                        text=tr(
                            csv_file=translation, target_key="ABOUT", langcode=lang
                        ),
                        on_click=open_readme_dlg,
                    ),
                    ft.PopupMenuItem(
                        text=tr(
                            csv_file=translation, target_key="LICENSE", langcode=lang
                        ),
                        on_click=open_license_dlg,
                    ),
                ]
            ),
        ],
    )
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.INFO, on_click=open_readme_dlg
    )
    page.add(
        ft.SafeArea(
            ft.DataTable(
                columns=[
                    ft.DataColumn(
                        ft.Text(
                            tr(
                                csv_file=translation,
                                target_key="PARAMETER",
                                langcode=lang,
                            )
                        )
                    ),
                    ft.DataColumn(
                        ft.Text(
                            tr(csv_file=translation, target_key="VALUE", langcode=lang)
                        )
                    ),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr(
                                        csv_file=translation,
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
                                    tr(
                                        csv_file=translation,
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
                                    tr(
                                        csv_file=translation,
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
                                    tr(
                                        csv_file=translation,
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
                                    tr(
                                        csv_file=translation,
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
                                    tr(
                                        csv_file=translation,
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


ft.app(main)
