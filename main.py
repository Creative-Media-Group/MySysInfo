import flet as ft
import locale
from mylocale.TR import tr

lang = locale.getlocale()
lang, _ = lang
translation = "assets/translation/localisation.csv"

def main(page: ft.Page):
    page.adaptive = True
    page.appbar = ft.AppBar(title=ft.Text("MySysInfo"))
    page.add(ft.SafeArea(ft.Text(tr(csv_file=translation,target_key="HELLOWORLD"))))


ft.app(main)
