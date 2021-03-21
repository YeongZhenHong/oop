import sys
from BotAPI import BotAPI
from Sentimental_Analysis import Sentimental_Analysis


class generateWeb:
    def __init__(self):
        super().__init__()
        self.f = open("./docs/index.html", "w", encoding="utf8")
        self.initDB = BotAPI()
        self.initDB.openCnx()

    def makeHTML(self):
        positive_score = Sentimental_Analysis.get_positive(self)
        grabFood = self.initDB.selectDB("GrabFood")
        foodPanda = self.initDB.selectDB("FoodPanda")
        deliveroo = self.initDB.selectDB("Deliveroo")
        message = """
       <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <meta http-equiv="x-ua-compatible" content="ie=edge" />
  <title>Tofu Crawler</title>
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
  <!-- Google Fonts Roboto -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
  <!-- Bootstrap core CSS -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <!-- Material Design Bootstrap -->
  <link rel="stylesheet" href="css/mdb.min.css">
  <!-- MDBootstrap Datatables  -->
  <link href="css/addons/datatables.min.css" rel="stylesheet">
</head>

<body>
  <!DOCTYPE html>
  <html>
  <title>W3.CSS Template</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-flat.css">
  <style>
    html,
    body,
    h1,
    h2,
    h3,
    h4,
    h5 {
      font-family: "Raleway", sans-serif
    }
    .fa {
      font-size: 30px;
    }
  </style>

  <body class="w3-light-grey">

    <!-- Top container -->
    <div class="w3-bar w3-top w3-black w3-large" style="z-index:4">
      <button class="w3-bar-item w3-button w3-hide-large w3-hover-none w3-hover-text-light-grey" onclick="w3_open();"><i
          class="fa fa-bars"></i>Menu</button>
      <span class="w3-bar-item w3-left">Hong's Holiday</span>
    </div>

    <!-- Sidebar/menu -->
    <nav class="w3-sidebar w3-collapse w3-white w3-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>

      <div class="w3-container">
        <h5>Dashboard</h5>
      </div>
      <div class="w3-bar-block">
        <a href="#" class="w3-bar-item w3-button w3-padding-16 w3-hide-large w3-dark-grey w3-hover-black"
          onclick="w3_close()" title="close menu"><i class="fa fa-remove fa-fw"></i>Close Menu</a>
        <a href="#overview" class="w3-bar-item w3-button w3-padding w3-blue"><i class="fa fa-users fa-fw"></i>
          Overview</a>
        <a href="#foodpandapost" class="w3-bar-item w3-button w3-padding"><img class="panda"
            src=".\img\koodpanda_menu_icon.png" width="40px" height="40px"></i>Food
          Panda</a>
        <a href="#deliveroopost" class="w3-bar-item w3-button w3-padding"><img class="roo"
            src=".\img\deliveroo_menu_icon.png" width="40px" height="40px"></i>
          Deliveroo</a>
        <a href="#grabfoodpost" class="w3-bar-item w3-button w3-padding"><img class="G" src=".\img\grab_menu_icon.png"
            width="40px" height="40px"></i>Grab
          Food</a>
        <a href="./doxygen//index.html" class="w3-bar-item w3-button w3-padding"><img class="G" src=".\img\doxygen.png"width="40px" height="40px"></i>Documentation</a>

      </div>
    </nav>


    <!-- Overlay effect when opening sidebar on small screens -->
    <div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer"
      title="close side menu" id="myOverlay"></div>

    <!-- !PAGE CONTENT! -->
    <div class="w3-main" style="margin-left:300px;margin-top:43px;">

      <!-- Header -->
      <header id='overview' class="w3-container" style="padding-top:22px">
        <h5><b><i class="fa fa-dashboard"></i> Food Delivery</b></h5>

      </header>

      <div class="w3-row-padding w3-margin-bottom">
        <div class="w3-quarter">
          <div class="w3-container w3-pink w3-padding-16">
            <div class="w3-left"><img class="panda" src=".\img\koodpanda_icon.png" width="48" height="48"></i></div>
            <div class="w3-right">
              <h3>
                       """
        message += str(grabFood[1])
        message += """ Tweets Crawled</h3>
            </div>
            <div class="w3-clear"></div>
            <h4>Food Panda</h4>
          </div>
        </div>
        <div class="w3-quarter">
          <div class="w3-container w3-flat-turquoise w3-padding-16">
            <div class="w3-left"><img class="deliveroo" src=".\img\deliveroo_icon.jpg" width="48" height="48"></i>
            </div>
            <div class="w3-right">
              <h3>
                       """
        message += str(foodPanda[1])
        message += """ Reddit Crawled</h3>
            </div>
            <div class="w3-clear"></div>
            <h4>Deliveroo</h4>
          </div>
        </div>
        <div class="w3-quarter">
          <div class="w3-container w3-flat-nephritis w3-padding-16">
            <div class="w3-left"><img class="grab" src=".\img\grabfood_icon.jpg" width="48" height="48"></i></div>
            <div class="w3-right">
              <h3>
                       """
        message += str(deliveroo[1])
        message += """ Instagram Crawled</h3>
            </div>
            <div class="w3-clear"></div>
            <h4>Grab Food</h4>
          </div>
        </div>
        <div class="w3-panel">
          <div class="w3-row-padding" style="margin:0 -16px">
          <div class="w3-third">
            <center>
              <h5>Post Count Spider Chart</h5>
            </center>
            <img src=".\sent_anal_spider.png" style="width:400px" alt="spider chart">
          </div>
          <div class="w3-third" style="padding-left:15px">
            <center>
              <h5>Frequency Over Datetime Chart</h5>
            </center>
            <img src=".\sent_anal_line.png" style="width:400px" alt="line chart">
            </div>
          </div>
        </div>
        <hr>
        <div class="w3-container">
          <h5>Positive Sentiment Percentage</h5>
          <p>Grab</p>
          <div class="w3-grey">
            <div class="w3-container w3-center w3-padding w3-flat-nephritis" style='width:
                    """
        message += str(positive_score[1]*100)+"%'>"
        message += str(positive_score[1]*100) + "% </div>"
        message += """
          </div>

          <p>Deliveroo</p>
          <div class="w3-grey">
            <div class="w3-container w3-center w3-padding w3-flat-turquoise" style='width:
            """
        message += str(positive_score[2]*100)+"%'>"
        message += str(positive_score[2]*100) + "% </div>"
        message += """
          </div>

          <p>Food Panda</p>
          <div class="w3-grey">
            <div class="w3-container w3-center w3-padding w3-pink" style='width:
            """
        message += str(positive_score[0]*100)+"%'>"
        message += str(positive_score[0]*100) + "% </div>"
        message += """
        </div>
              <hr>
        <h1 id="foodpandapost" style="color:#D80765"><strong>Food Panda Posts</strong></h1>
        <table id="dtfoodpanda" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
          <thead>
            <tr>
              <th class="th-sm"></th>
              <th class="th-sm">Content

              </th>
              <th class="th-sm">Author

              </th>
              <th class="th-sm">Date posted

              </th>
              <th class="th-sm">Likes/Shares

              </th>
              <th class="th-sm">Link

              </th>
            </tr>
          </thead>
          <tbody>
                  """
        for item in foodPanda[0]:
            message += "<tr>"
            message += "<td></td>"
            message += "<td>"+str(item[1])+"</td>"
            message += "<td>"+str(item[2])+"</td>"
            message += "<td>"+str(item[3])+"</td>"
            message += "<td>"+str(item[4])+"</td>"
            message += "<td>"+str(item[5])+"</td>"
            message += "</tr>"
        message += """
          </tbody>
        </table>
        <h1 id="deliveroopost" style="color:#02CCC0"><strong>Deliveroo Posts</strong></h1>
        <table id="dtdeliveroo" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
          <thead>
            <tr>
              <th class="th-sm"></th>
              <th class="th-sm">Content

              </th>
              <th class="th-sm">Author

              </th>
              <th class="th-sm">Date posted

              </th>
              <th class="th-sm">Likes/Shares

              </th>
              <th class="th-sm">Link

              </th>
            </tr>
          </thead>
          <tbody>
"""
        for item in deliveroo[0]:
            message += "<tr>"
            message += "<td></td>"
            message += "<td>"+str(item[1])+"</td>"
            message += "<td>"+str(item[2])+"</td>"
            message += "<td>"+str(item[3])+"</td>"
            message += "<td>"+str(item[4])+"</td>"
            message += "<td>"+str(item[5])+"</td>"
            message += "</tr>"
        message += """
          </tbody>
        </table>
        <h1 id="grabfoodpost" style="color:#029837"><strong>Grab Food Posts</strong></h1>
        <table id="dtgrabfood" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
          <thead>

            <tr>
              <th class="th-sm"></th>
              <th class="th-sm">Content

              </th>
              <th class="th-sm">Author

              </th>
              <th class="th-sm">Date posted

              </th>
              <th class="th-sm">Likes/Shares

              </th>
              <th class="th-sm">Link

              </th>
            </tr>

          </thead>
          <tbody>
"""
        for item in grabFood[0]:
            message += "<tr>"
            message += "<td></td>"
            message += "<td>"+str(item[1])+"</td>"
            message += "<td>"+str(item[2])+"</td>"
            message += "<td>"+str(item[3])+"</td>"
            message += "<td>"+str(item[4])+"</td>"
            message += "<td>"+str(item[5])+"</td>"
            message += "</tr>"
        message += """
          </tbody>

        </table>


        <!-- Footer -->
        <footer class="w3-container w3-padding-16 w3-light-grey">

        </footer>


        <!-- End page content -->
      </div>

      <script>
        // Get the Sidebar
        var mySidebar = document.getElementById("mySidebar");

        // Get the DIV with overlay effect
        var overlayBg = document.getElementById("myOverlay");

        // Toggle between showing and hiding the sidebar, and add overlay effect
        function w3_open() {
          if (mySidebar.style.display === 'block') {
            mySidebar.style.display = 'none';
            overlayBg.style.display = "none";
          } else {
            mySidebar.style.display = 'block';
            overlayBg.style.display = "block";
          }
        }

        // Close the sidebar with the close button
        function w3_close() {
          mySidebar.style.display = "none";
          overlayBg.style.display = "none";
        }

      </script>


  </body>

  </html>
  <!-- jQuery -->
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <!-- Bootstrap tooltips -->
  <script type="text/javascript" src="js/popper.min.js"></script>
  <!-- Bootstrap core JavaScript -->
  <script type="text/javascript" src="js/bootstrap.min.js"></script>
  <!-- MDB core JavaScript -->
  <script type="text/javascript" src="js/mdb.min.js"></script>
  <!-- MDBootstrap Datatables  -->
  <script type="text/javascript" src="js/addons/datatables.min.js"></script>


  <script>
    $(document).ready(function () {
      $('#dtfoodpanda').DataTable();
      $('#dtdeliveroo').DataTable();
      $('#dtgrabfood').DataTable();
      $('.dataTables_length').addClass('bs-select');
    });
  </script>
</body>

</html>


        """

        self.f.write(message)

    def close(self):
        self.f.close()
        self.initDB.closeCnx()


a = generateWeb()
a.makeHTML()
a.close()
