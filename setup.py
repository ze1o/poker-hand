from UI import *
from feature import *
from preprocess import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)    

    Form.show()
    sys.exit(app.exec_())

