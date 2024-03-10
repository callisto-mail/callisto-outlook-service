import extract_msg

class OutlookMsg:
    def __init__(self, file_path):
        self.file = extract_msg.openMsg(file_path)

o = OutlookMsg("./data/ap.msg")