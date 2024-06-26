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
        title=ft.Text(tr(csv_file=translation, target_key="LICENSE")),
        content=ft.Text(applicense),
        scrollable=True,
    )
    readme_dlg = ft.AlertDialog(
        title=ft.Text(tr(csv_file=translation, target_key="ABOUT")),
        content=ft.Markdown(
            readme,
            on_tap_link=lambda e: page.launch_url(e.data),
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        ),
        scrollable=True,
    )

    def open_license_dlg(e):
        page.dialog = license_dlg
        license_dlg.open = True
        page.update()

    def open_readme_dlg(e):
        page.dialog = readme_dlg
        readme_dlg.open = True
        page.update()

    page.adaptive = True
    page.scroll = True
    page.window_min_height = 500
    page.window_min_width = 500
    page.appbar = ft.AppBar(
        title=ft.Text("MySysInfo"),
        leading=ft.Image(
            src="assets/icon.png",
        ),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text=tr(csv_file=translation, target_key="ABOUT"),
                        on_click=open_readme_dlg,
                    ),
                    ft.PopupMenuItem(
                        text=tr(csv_file=translation, target_key="LICENSE"),
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
                        ft.Text(tr(csv_file=translation, target_key="PARAMETER"))
                    ),
                    ft.DataColumn(
                        ft.Text(tr(csv_file=translation, target_key="VALUE"))
                    ),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr(csv_file=translation, target_key="SYSTEM")
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(page.platform.value)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr(csv_file=translation, target_key="USERNAME")
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
                                    tr(csv_file=translation, target_key="VERSION")
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(version)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr(csv_file=translation, target_key="ARCHITECTURE")
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(architecture)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr(csv_file=translation, target_key="PROCESSORTYPE")
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(machine)),  # 2'nd collumn
                        ]
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    tr(csv_file=translation, target_key="HOSTNAME")
                                )  # 1'st collumn
                            ),
                            ft.DataCell(ft.Text(node)),  # 2'nd collumn
                        ]
                    ),
                ],
                width=page.window_width,
            )
        )
    )


ft.app(main)
