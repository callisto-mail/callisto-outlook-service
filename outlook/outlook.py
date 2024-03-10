import extract_msg

class OutlookMsg:
    def __init__(self, file_path):
        self.file = extract_msg.openMsg(file_path)

        self.header = self.file.header
        self.sender = self.file.sender
        self.date = self.file.date
        self.subject = self.file.subject
        self.body = self.file.body

    def get_header(self):
        return str(self.header)

    def get_sender(self):
        return str(self.sender)
    
    def get_date(self):
        return str(self.date)
    
    def get_subject(self):
        return str(self.subject)

    def get_body(self):
        return str(self.body)
