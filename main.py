import flet as ft
import locale
from mylocale.TR import tr

lang = locale.getlocale()
lang, _ = lang
translation = "assets/translation/localisation.csv"
with open("README.md", "r") as readme:
    readme = readme.read()
with open("LICENSE", "r") as l:
    applicense = l.read()


def main(page: ft.Page):
    license_dlg = ft.AlertDialog(
        title=ft.Text("applicense"), content=ft.Text(""), scrollable=True
    )
    readme_dlg = ft.AlertDialog(
        title=ft.Text(tr(csv_file=translation, target_key="ABOUT")),
        content=ft.Markdown(readme, on_tap_link=lambda e: page.launch_url(e.data)),
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
    page.appbar = ft.AppBar(title=ft.Text("MySysInfo"))
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.INFO, on_click=open_readme_dlg
    )
    page.add(ft.SafeArea(ft.Text(tr(csv_file=translation, target_key="HELLOWORLD"))))


ft.app(main)
