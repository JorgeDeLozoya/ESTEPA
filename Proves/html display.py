import pandas as pd
from bokeh import plotting, embed, resources
from PyQt6 import QtCore, QtWidgets, QtWebEngineWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        button = QtWidgets.QPushButton("Submit")
        self.m_output = QtWebEngineWidgets.QWebEngineView()

        button.clicked.connect(self.on_button_clicked)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(button)
        lay.addWidget(self.m_output)
        self.resize(640, 480)

    @QtCore.pyqtSlot()
    def on_button_clicked(self):
        p = plotting.figure(plot_width=300, plot_height=300)
        data = {"Day": [0, 1, 2, 3, 0, 1], "Num": [0, 0, 1, 1, 2, 3]}
        df = pd.DataFrame(data)
        p.hexbin(df.Day, df.Num, size=0.5)
        html = embed.file_html(p, resources.CDN, "my plot")
        self.m_output.setHtml(html)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = Widget()
    w.show()

    sys.exit(app.exec_())