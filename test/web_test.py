import sys
from BotAPI import BotAPI


class generateWeb:
    def __init__(self):
        super().__init__()
        self.f = open("helloWorld.html", "w", encoding="utf-8")
        self.initDB = BotAPI()
        self.initDB.openCnx()

    def makeHTML(self):
        bstr = self.initDB.selectTweets()
        message = """
     <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <meta http-equiv="x-ua-compatible" content="ie=edge" />
  <title>Material Design for Bootstrap</title>
  <!-- MDB icon -->
  <link rel="icon" href="img/mdb-favicon.ico" type="image/x-icon" />
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
  <!-- Google Fonts Roboto -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
  <!-- Bootstrap core CSS -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <!-- Material Design Bootstrap -->
  <link rel="stylesheet" href="css/mdb.min.css">
  <!-- Your custom styles (optional) -->
  <link rel="stylesheet" href="css/style.css">
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
  </style>

  <body class="w3-light-grey">

    <!-- Top container -->
    <div class="w3-bar w3-top w3-black w3-large" style="z-index:4">
      <button class="w3-bar-item w3-button w3-hide-large w3-hover-none w3-hover-text-light-grey" onclick="w3_open();"><i
          class="fa fa-bars"></i> �Menu</button>
      <span class="w3-bar-item w3-right">Logo</span>
    </div>

    <!-- Sidebar/menu -->
    <nav class="w3-sidebar w3-collapse w3-white w3-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
      <div class="w3-container w3-row">
        <div class="w3-col s4">
          <img src="/w3images/avatar2.png" class="w3-circle w3-margin-right" style="width:46px">
        </div>
        <div class="w3-col s8 w3-bar">
          <span>Welcome, <strong>Mike</strong></span><br>
          <a href="#" class="w3-bar-item w3-button"><i class="fa fa-envelope"></i></a>
          <a href="#" class="w3-bar-item w3-button"><i class="fa fa-user"></i></a>
          <a href="#" class="w3-bar-item w3-button"><i class="fa fa-cog"></i></a>
        </div>
      </div>
      <hr>
      <div class="w3-container">
        <h5>Dashboard</h5>
      </div>
      <div class="w3-bar-block">
        <a href="#" class="w3-bar-item w3-button w3-padding-16 w3-hide-large w3-dark-grey w3-hover-black"
          onclick="w3_close()" title="close menu"><i class="fa fa-remove fa-fw"></i>� Close Menu</a>
        <a href="#overview" class="w3-bar-item w3-button w3-padding w3-blue"><i class="fa fa-users fa-fw"></i>�
          Overview</a>
        <a href="#foodpandapost" class="w3-bar-item w3-button w3-padding"><i class="fa fa-eye fa-fw"></i>� Food
          Panda</a>
        <a href="#deliveroopost" class="w3-bar-item w3-button w3-padding"><i class="fa fa-users fa-fw"></i>�
          Deliveroo</a>
        <a href="#grabfoodpost" class="w3-bar-item w3-button w3-padding"><i class="fa fa-bullseye fa-fw"></i>� Grab
          Food</a>
        <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-diamond fa-fw"></i>� Orders</a>
        <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-bell fa-fw"></i>� News</a>
        <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-bank fa-fw"></i>� General</a>
        <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-history fa-fw"></i>� History</a>
        <a href="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-cog fa-fw"></i>� Settings</a><br><br>
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
              <h3>insert total post crawled</h3>
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
              <h3>insert total post crawled</h3>
            </div>
            <div class="w3-clear"></div>
            <h4>Deliveroo</h4>
          </div>
        </div>
        <div class="w3-quarter">
          <div class="w3-container w3-flat-nephritis w3-padding-16">
            <div class="w3-left"><img class="grab" src=".\img\grabfood_icon.jpg" width="48" height="48"></i></div>
            <div class="w3-right">
              <h3>insert total post crawled</h3>
            </div>
            <div class="w3-clear"></div>
            <h4>Grab Food</h4>
          </div>
        </div>
        <div class="w3-panel">
          <div class="w3-row-padding" style="margin:0 -16px">
            <div class="w3-third">
              <h5>Post Count Spider Chart</h5>
              <img src="..\sent_anal_spider.png" style="width:100%" alt="spider chart">
            </div>
            <div class="w3-twothird">
              <h5>Feeds</h5>
              <table class="w3-table w3-striped w3-white">
                <tr>
                  <td><img class="reddit" src=".\img\eddit_icon.png" width="30" height="30"></i></td>
                  <td>Reddit</td>
                  <td><i>insert reddit post crawl count</i></td>
                </tr>
                <tr>
                  <td><img class="twitter" src=".\img\witter_icon.png" width="30" height="30"></i></td>
                  <td>Twitter.</td>
                  <td><i>insert reddit post crawl count</i></td>
                </tr>
                <tr>
                  <td><img class="instagram" src=".\img\insta_icon.png" width="30" height="30"></i></td>
                  <td>Instagram</td>
                  <td><i>insert yahoo post crawl count</i></td>
                </tr>
              </table>
            </div>
          </div>
        </div>
        <hr>
        <div class="w3-container">
          <h5>Positive Sentiment Percentage</h5>
          <p>Grab</p>
          <div class="w3-grey">
            <div class="w3-container w3-center w3-padding w3-flat-nephritis" style="width:25%">insert number</div>
          </div>

          <p>Deliveroo</p>
          <div class="w3-grey">
            <div class="w3-container w3-center w3-padding w3-flat-turquoise" style="width:50%">insert number</div>
          </div>

          <p>Food Panda</p>
          <div class="w3-grey">
            <div class="w3-container w3-center w3-padding w3-pink" style="width:75%">insert number</div>
          </div>
        </div>
        <hr>
        """
        self.f.write(message)

    def maketable(self):
        bstr = self.initDB.selectTweets()
        message = """<h1 id="foodpandapost" style="color:#D80765"><strong>Food Panda Posts</strong></h1>
        <table id="dtfoodpanda" class="table table-striped table-bordered table-sm" cellspacing="0" width="100%">
          <thead>
            <tr>
              <th class="th-sm">Content</th>
              <th class="th-sm">Author</th>
              <th class="th-sm">Date</th>
              <th class="th-sm">Retweets</th>
              <th class="th-sm">Likes</th>
              <th class="th-sm">Url</th>
            </tr>
          </thead>
          <tbody>
          """
        for item in bstr:
            message += "<tr>"
            message += "<td>"+str(item[2])+"</td>"
            message += "<td>"+str(item[1])+"</td>"
            message += "<td>"+str(item[3])+"</td>"
            message += "<td>"+str(item[4])+"</td>"
            message += "<td>"+str(item[5])+"</td>"
            message += "<td>"+str(item[6])+"</td>"
            message += "</tr>\n"
        message += """
          </tfoot>
        </table>
        <hr>
        <div class="w3-container">
          <h5>Recent Users</h5>
          <ul class="w3-ul w3-card-4 w3-white">
            <li class="w3-padding-16">
              <img src="/w3images/avatar2.png" class="w3-left w3-circle w3-margin-right" style="width:35px">
              <span class="w3-xlarge">Mike</span><br>
            </li>
            <li class="w3-padding-16">
              <img src="/w3images/avatar5.png" class="w3-left w3-circle w3-margin-right" style="width:35px">
              <span class="w3-xlarge">Jill</span><br>
            </li>
            <li class="w3-padding-16">
              <img src="/w3images/avatar6.png" class="w3-left w3-circle w3-margin-right" style="width:35px">
              <span class="w3-xlarge">Jane</span><br>
            </li>
          </ul>
        </div>
        <hr>

        <div class="w3-container">
          <h5>Recent Comments</h5>
          <div class="w3-row">
            <div class="w3-col m2 text-center">
              <img class="w3-circle" src="/w3images/avatar3.png" style="width:96px;height:96px">
            </div>
            <div class="w3-col m10 w3-container">
              <h4>John <span class="w3-opacity w3-medium">Sep 29, 2014, 9:12 PM</span></h4>
              <p>Keep up the GREAT work! I am cheering for you!! Lorem ipsum dolor sit amet, consectetur adipiscing
                elit,
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p><br>
            </div>
          </div>

          <div class="w3-row">
            <div class="w3-col m2 text-center">
              <img class="w3-circle" src="/w3images/avatar1.png" style="width:96px;height:96px">
            </div>
            <div class="w3-col m10 w3-container">
              <h4>Bo <span class="w3-opacity w3-medium">Sep 28, 2014, 10:15 PM</span></h4>
              <p>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p><br>
            </div>
          </div>
        </div>
        <br>
        <div class="w3-container w3-dark-grey w3-padding-32">
          <div class="w3-row">
            <div class="w3-container w3-third">
              <h5 class="w3-bottombar w3-border-green">Demographic</h5>
              <p>Language</p>
              <p>Country</p>
              <p>City</p>
            </div>
            <div class="w3-container w3-third">
              <h5 class="w3-bottombar w3-border-red">System</h5>
              <p>Browser</p>
              <p>OS</p>
              <p>More</p>
            </div>
            <div class="w3-container w3-third">
              <h5 class="w3-bottombar w3-border-orange">Target</h5>
              <p>Users</p>
              <p>Active</p>
              <p>Geo</p>
              <p>Interests</p>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <footer class="w3-container w3-padding-16 w3-light-grey">
          <h4>FOOTER</h4>
          <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
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
    <!-- Your custom scripts (optional) -->
    <script type="text/javascript">
      var a = document.getElementById('disc-50');
      a.onclick = function () {
        Clipboard_CopyTo("T9TTVSQB");
        var div = document.getElementById('code-success');
        div.style.display = 'block';
        setTimeout(function () {
          document.getElementById('code-success').style.display = 'none';
        }, 900);
      };
    </script>

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
a.maketable()
a.close()
