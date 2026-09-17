from kivy.app import App
from kivy.uix.label import Label


class RastaProofApp(App):
    def build(self):
        return Label(
            text="RASTA STUDIO\n\nBUILD PROOF OK",
            font_size="28sp",
            halign="center"
        )


if __name__ == "__main__":
    RastaProofApp().run()
