import sys
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QDialog, QVBoxLayout, QCheckBox
import os
import json
import main

class Form(QDialog):
    settings_fp = "./salty_papers.config"
    def __init__(self, parent=None, settings_fp="./salty_papers.config"):
        self.settings_fp
        super(Form, self).__init__(parent)
        # Create widgets
        print(os.getcwd())
        with open(self.settings_fp, "r") as jsonFile:
            settings = json.load(jsonFile)
        print(settings["sub_reddits"])
        #self.sub_reddit_label = QLabel("Subreddits")
        self.sub_reddit_label = QLabel(os.getcwd())
        self.sub_reddit_input = QLineEdit(", ".join(settings["sub_reddits"]))
        self.interval_label = QLabel("Interval (seconds)")
        self.interval_input = QLineEdit(str(settings["interval"]))
        self.post_max_label = QLabel("Lowest Post Rank:")
        self.post_max_input = QLineEdit(str(settings["post_max"]))
        self.randomize_label = QLabel("Randomize")
        self.randomize_checkbox = QCheckBox()
        self.randomize_checkbox.setChecked(bool(settings["randomize"]))
        self.save_button = QPushButton("Save Settings")
        self.setWindowTitle("Salty Papers Settings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.sub_reddit_label)
        layout.addWidget(self.sub_reddit_input)
        layout.addWidget(self.interval_label)
        layout.addWidget(self.interval_input)
        layout.addWidget(self.randomize_label)
        layout.addWidget(self.randomize_checkbox)
        layout.addWidget(self.post_max_label)
        layout.addWidget(self.post_max_input)
        layout.addWidget(self.save_button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.save_button.clicked.connect(self.save_config)
        print("window built")
    def save_config(self):
        sub_reddits = list(self.sub_reddit_input.text().replace(" ", "").split(","))
        interval = int(self.interval_input.text())
        randomize = bool(self.randomize_checkbox.isChecked())
        post_max = int(self.post_max_input.text())
        with open(self.settings_fp, "r") as jsonFile:
            settings = json.load(jsonFile)

        settings["sub_reddits"] = sub_reddits
        settings["interval"] = interval
        settings["randomize"] = randomize
        settings["post_max"] = post_max
        with open(self.settings_fp, "w") as jsonFile:
            json.dump(settings, jsonFile)
        
        self.close()

def settings_gui(settings_fp):

    app = QApplication(sys.argv)
    form = Form(settings_fp=settings_fp)
    form.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    settings_gui()