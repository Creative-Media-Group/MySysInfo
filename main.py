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
    license_dlg = ft.AlertDialog(title=ft.Text(applicense))
    readme_dlg = ft.AlertDialog(title=ft.Text(readme))

    def open_license_dlg(e):
        license_dlg.open = True

    def open_readme_dlg(e):
        readme_dlg.open = True

    page.adaptive = True
    page.appbar = ft.AppBar(title=ft.Text("MySysInfo"))
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.INFO, on_click=lambda e: self.open_readme_dlg(e)
    )
    page.add(ft.SafeArea(ft.Text(tr(csv_file=translation, target_key="HELLOWORLD"))))


ft.app(main)
