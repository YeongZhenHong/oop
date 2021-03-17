
import sys
from BotAPI import BotAPI


class generateWeb:
    def __init__(self):
        super().__init__()
        self.f = open("helloWorld.html", "w")
        self.initDB = BotAPI()

    def makeHTML(self):
        bstr = self.initDB.selectAll()
        message = """<html>
        <head></head>
        <table class="table">
            <thead>
                <tr>
                    <th>Content</th>
                    <th>Author</th>
                    <th>Date</th>
                    <th>Retweets</th>
                    <th>Likes</th>
                    <th>Url</th>
                </tr>
            </thead>
        <tbody>
        """
        for item in bstr:
            message += "<tr>"
            message += "<td>"+str(item[2])+"</td>"
            message += "<td>"+str(item[1])+"</td>"
            message+="</tr>"
        message += """
         </tbody>
         </table>
        """
        message+="<img src=\'sent_anal.png\'> "
        message+="</html>"
        self.f.write(message)

    def close(self):
        self.f.close()


a = generateWeb()
a.makeHTML()
a.close()
