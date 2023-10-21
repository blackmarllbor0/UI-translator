import npyscreen


class Input(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

    def when_value_edited(self):
        self.parent.parentApp.queue_event(npyscreen.Event("event_value_edited"))
