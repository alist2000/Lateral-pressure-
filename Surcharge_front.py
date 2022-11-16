def generate_html_response_BFP(output):
    html = "<html>"
    html_end = "</html>"

    head = """<head>
	<title>Output Summary</title>
	<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
	<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
	<style type="text/css">
		* {font-size: 10px; }
		body {
			font: 10px Arial, Helvetica, sans-serif;
			line-height: 1.0;
		}
		@media print {
			.pagebreak { page-break-before: always; }
		}
		@page {
			size: letter;
			margin: 1.5cm;
			@bottom-right {
				content: "Page " counter(page) " of " counter(pages);
			}
		}
		.custom-page-start {
			margin-top: 0px;
			margin-bottom: 0px;
		}
		h1 {color: #2f4f6e; font-size: 15px;}
		h2 {
			background: #96B9D0; font-size: 13px;
			padding-top: 3px;
			padding-bottom: 3px;
			padding-left: 3px;
			margin-bottom: 5px; margin-top: 5px;
			margin-left: -1px; margin-right: -1px;
		}
		h3 {
			background: #84c1ff; font-size: 13px;
			font-size: 10px; 
			margin-bottom: -1px; margin-top: -1px;
			margin-left: -1px; margin-right: -1px;
			padding-top: 8px;
			padding-bottom: 8px;
			padding-left: 8px;
		}
		t1 {display: block; font-size: 15px; font-style: italic; padding-left: 3px;}
		t1b {font-size: 15px; font-style: italic; font-weight: bold;}
		t2 {font-size: 15px;}
		t2b {font-size: 15px;font-weight: bold;}
		p {font-size: 10px;}
		td {vertical-align: top;}
	</style>
  </head>"""

    body = "<body>"
    body_end = "</body>"
    div = """<div class="custom-page-start"> <hr>"""
    div_end = "</div>"
    h1 = "<h1>"
    h1_title = "<h1 style='font-size: 15px'>"
    h1_end = "</h1>"
    table = "<table border=1>"
    table_end = "</table>"
    tbody = "<tbody>"
    tbody_end = "</tbody>"
    hr = "<hr>"
    tr = "<tr>"
    tr_end = "</tr>"
    th = "<th>"
    th_end = "</th>"
    td = "<td>"
    td_end = "</td>"

    def title():

        t1 = """		<table border="0" style="border-collapse: collapse; width: 100%;">
			<tbody>
				<tr>
					<td style="width: 100%;font-size: 15px;">
						<h2>"""

        t2 = """</h2>
            </td>
          </tr>
        </tbody>
      </table>
    <hr>"""

        title = h1_title + output[0][0] + h1_end + t1 + output[0][1] + t2

        return title

    def solutions():

        t1 = """<table border="0" style="border-collapse: collapse; width: 100%;">
			<tbody>
				<tr>
					<td style="width: 60%; vertical-align: text-top;font-size: 15px"><h3>Solution No.:"""

        t2 = """</h3></td>
          </tr>
        </tbody>
      </table>"""

        t3 = """
          <table border="0" style="border-collapse: collapse; width: 100%;">
			<tbody>
				<tr>
					<td style="width: 7%;"><t1b>Download Reports:</t1b></td>
					<td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

        t4 = """
          " target="_blank" ><img height = "20px"src="http://civision.balafan.com:8010/icon/PDF_Summary"></a></td>
					<td style="width: 1%;"></td>
					<td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

        t5 = """
        " target="_blank" ><img height = "20px" src="http://civision.balafan.com:8010/icon/PDF_Detailed"></a></td>
              <td style="width: 78%;"></td>
            </tr>
          </tbody>
        </table>
        """
        m1 = """
      <table border="0" style="border-collapse: collapse; width: 100%;">
          <tbody>
            <tr>
              <td style="width: 100%;"><t1b></t1b></td>
            </tr>
          </tbody>
        </table>
          """

        h1 = """
          <table border="0" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
			<tbody>
				<tr>
					<td style="width: 100%;padding: 5px;border: 5px solid white;background-color: #bfd6f6  ;"><t2b>
          """

        h2 = """
          </t2b></td>
          </tr>
        </tbody>
      </table>
          """

        h3 = """
        <table border="1" bordercolor="#C0C0C0" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
			<tbody style="width: 100%;padding: 5px;border: 5px solid white;background-color: #e7eff6 ">
          """

        h4 = """
          </tbody>
      </table>
          """
        h5 = """
        <td style="width: 10%;"><t2>Section</t2></td>
        """
        h6 = """
        <td style="width: 10%;"><t2>Unit</t2></td>

          """
        h7 = """
        <td style="width: 10%;"><t2>Value</t2></td>

          """

        h8 = """
        <td style="width: 10%;text-align: center;" ><t2>
        """

        h9 = """
        </t2></td>
        """

        s = ""
        for k in range(len(output[4])):
            #  for l in range(len(output[4][0])):
            # if (k==0):
            # Table Header - Solution Number
            s = s + t1 + str(k + 1) + t2
            # Table Header - Solution Report Links
            # try:
            #     s = s + t3 + output[4][k][0] + t4 + output[4][k][1] + t5 + m1
            # except:
            #     s = s + t3 + str(output[4][k][0]) + \
            #         t4 + str(output[4][k][1]) + t5 + m1
            try:
                s = s + t3 + output[5][2 * k] + "_1" + t4 + output[5][2 * k + 1] + "_1" + t5 + m1
            except:
                s = s + t3 + str(output[5][0]) + \
                    t4 + str(output[5][1]) + t5 + m1

            c1 = 0
            c2 = 0
            c3 = 2

            # Table Solution Group Fields, Field labels, units and values
            for i in range(0, int(len(output[1]))):
                if i % 2 == 0:
                    s = s + h1 + str(output[1][i + 1]) + h2 + h3
                    for j in range(output[1][i]):
                        if (j == 0):
                            s = s + tr + h5
                        s = s + h8 + output[2][c1] + h9
                        c1 = c1 + 1
                    s = s + tr_end
                    for j in range(output[1][i]):
                        if (j == 0):
                            s = s + tr + h6
                        s = s + h8 + output[3][c2] + h9
                        c2 = c2 + 1
                    s = s + tr_end
                    for j in range(output[1][i]):
                        if (j == 0):
                            s = s + tr + h7
                        s = s + h8 + str(output[4][k][c3]) + h9
                        c3 = c3 + 1
                    s = s + tr_end
                    s = s + tbody_end + table_end
            s = s + m1 + hr

        return s

    export = html + head + body + div + title() + solutions() + \
             div_end + body_end + html_end

    return export


# no change till 10:49 - 11 september
def generate_html_response_BFP_multi(output):
    response = ""

    for project_num in range(int(len(output))):
        html = "<html>"
        html_end = "</html>"

        head = """<head>
        <title>Output Summary</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style type="text/css">
          * {font-size: 10px; }
          body {
            font: 10px Arial, Helvetica, sans-serif;
            line-height: 1.0;
          }
          @media print {
            .pagebreak { page-break-before: always; }
          }
          @page {
            size: letter;
            margin: 1.5cm;
            @bottom-right {
              content: "Page " counter(page) " of " counter(pages);
            }
          }
          .custom-page-start {
            margin-top: 0px;
            margin-bottom: 0px;
          }
          h1 {color: #2f4f6e; font-size: 15px;}
          h2 {
            background: #96B9D0; font-size: 13px;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 3px;
            margin-bottom: 5px; margin-top: 5px;
            margin-left: -1px; margin-right: -1px;
          }
          h3 {
            background: #84c1ff ; font-size: 13px;
            font-size: 10px; 
            margin-bottom: -1px; margin-top: -1px;
            margin-left: -1px; margin-right: -1px;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 3px;
          }
          t1 {display: block; font-size: 15px; font-style: italic; padding-left: 3px;}
          t1b {font-size: 15px; font-style: italic; font-weight: bold;}
          t2 {font-size: 15px;}
          t2b {font-size: 15px;font-weight: bold;}
          p {font-size: 10px;}
          td {vertical-align: top;}
        </style>
        </head>"""

        body = "<body>"
        body_end = "</body>"
        div = """<div class="custom-page-start"> <hr>"""
        div_end = "</div>"
        h1 = "<h1>"
        h1_title = "<h1 style='font-size: 15px'>"
        h1_end = "</h1>"
        table = """<table border=1 class="table table-responsive table-striped table-sm table-hover">"""
        table_end = "</table>"
        tbody = "<tbody>"
        tbody_end = "</tbody>"
        hr = "<hr>"
        tr = "<tr>"
        tr_end = "</tr>"
        th = "<th>"
        th_end = "</th>"
        td = "<td>"
        td_end = "</td>"

        def title(project_num):
            t1 = """	<table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
            <tbody>
              <tr>
                <td style="width: 100%;font-size: 15px;">
                  <h2>"""

            t2 = """</h2>
                  </td>
                </tr>
              </tbody>
            </table>
          <hr>"""

            pn = "Project " + str(project_num + 1) + " "

            title = h1_title + output[project_num][0][0] + h1_end + t1 + pn + output[project_num][0][1] + t2

            return title

        def solutions():

            t1 = """<table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
        <tbody>
          <tr>
            <td style="width: 60%; vertical-align: text-top;font-size: 15px"><h3>Solution No.:"""

            t2 = """</h3></td>
            </tr>
          </tbody>
        </table>"""

            t3 = """
            <table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
        <tbody>
          <tr>
            <td style="width: 7%;"><t1b>Download Reports:</t1b></td>
            <td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

            t4 = """
            " target="_blank" ><img height = "20px"src="http://civision.balafan.com:8010/icon/PDF_Summary"></a></td>
            <td style="width: 1%;"></td>
            <td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

            t5 = """
          " target="_blank" ><img height = "20px" src="http://civision.balafan.com:8010/icon/PDF_Detailed"></a></td>
                <td style="width: 78%;"></td>
              </tr>
            </tbody>
          </table>
          """
            m1 = """
        <table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
            <tbody>
              <tr>
                <td style="width: 100%;"><t1b></t1b></td>
              </tr>
            </tbody>
          </table>
            """

            h1 = """
            <table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
        <tbody>
          <tr>
           <td style="width: 100%;padding: 5px;border: 5px solid white;background-color: #bfd6f6  "><t2b>
            """

            h2 = """
            </t2b></td>
            </tr>
          </tbody>
        </table>
            """

            h3 = """
          <table border="1" class="table table-responsive table-striped table-sm table-hover" bordercolor="#C0C0C0" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
        <tbody style="width: 100%;padding: 5px;border: 5px solid white;background-color: #e7eff6">
            """
            h4 = """
            </tbody>
        </table>
            """
            h5 = """
          <td style="width: 10%;"><t2>Section</t2></td>
          """
            h6 = """
          <td style="width: 10%;"><t2>Unit</t2></td>

            """
            h7 = """
          <td style="width: 10%;"><t2>Value</t2></td>

            """

            h8 = """
          <td style="width: 10%;text-align: center"><t2>
          """

            h9 = """
          </t2></td>
          """

            s = ""
            for k in range(len(output[project_num][4])):
                #  for l in range(len(output[4][0])):
                # if (k==0):
                # Table Header - Solution Number
                s = s + t1 + str(k + 1) + t2
                # Table Header - Solution Report Links
                try:
                    s = s + t3 + output[project_num][5][2 * k] + "_" + str(project_num + 1) + t4 + \
                        output[project_num][5][
                            2 * k + 1] + "_" + str(project_num + 1) + t5 + m1
                except:
                    s = s + t3 + str(output[5][0]) + \
                        t4 + str(output[5][1]) + t5 + m1
                # s = s + t3 + output[project_num][4][k][0] + t4 + output[project_num][4][k][1] + t5 + m1

                c1 = 0
                c2 = 0
                c3 = 2

                # Table Solution Group Fields, Field labels, units and values
                for i in range(0, int(len(output[project_num][1]))):
                    if i % 2 == 0:
                        if i == 0:
                            c1 = 0
                            c2 = 0
                            c3 = 2
                        s = s + h1 + str(output[project_num][1][i + 1]) + h2 + h3
                        for j in range(output[project_num][1][i]):
                            if (j == 0):
                                s = s + tr + h5
                            s = s + h8 + output[project_num][2][c1] + h9
                            c1 = c1 + 1
                        s = s + tr_end
                        for j in range(output[project_num][1][i]):
                            if (j == 0):
                                s = s + tr + h6
                            s = s + h8 + output[project_num][3][c2] + h9
                            c2 = c2 + 1
                        s = s + tr_end
                        for j in range(output[project_num][1][i]):
                            if (j == 0):
                                s = s + tr + h7
                            s = s + h8 + str(output[project_num][4][k][c3]) + h9
                            c3 = c3 + 1
                        s = s + tr_end
                        s = s + tbody_end + table_end
                s = s + m1 + hr

            return s

        export = html + head + body + div + title(project_num) + solutions() + div_end + body_end + html_end

        response = response + export

    return response


def generate_html_response_BFP_no_solution(output):
    html = "<html>"
    html_end = "</html>"

    head = """<head>
	<title>Output Summary</title>
	<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
	<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
	<style type="text/css">
		* {font-size: 10px; }
		body {
			font: 10px Arial, Helvetica, sans-serif;
			line-height: 1.0;
		}
		@media print {
			.pagebreak { page-break-before: always; }
		}
		@page {
			size: letter;
			margin: 1.5cm;
			@bottom-right {
				content: "Page " counter(page) " of " counter(pages);
			}
		}
		.custom-page-start {
			margin-top: 0px;
			margin-bottom: 0px;
		}
		h1 {color: #2f4f6e; font-size: 15px;}
		h2 {
			background: #96B9D0; font-size: 13px;
			padding-top: 3px;
			padding-bottom: 3px;
			padding-left: 3px;
			margin-bottom: 5px; margin-top: 5px;
			margin-left: -1px; margin-right: -1px;
		}
		h3 {
			background: #84c1ff; font-size: 13px;
			font-size: 10px; 
			margin-bottom: -1px; margin-top: -1px;
			margin-left: -1px; margin-right: -1px;
			padding-top: 8px;
			padding-bottom: 8px;
			padding-left: 8px;
		}
		t1 {display: block; font-size: 15px; font-style: italic; padding-left: 3px;}
		t1b {font-size: 15px; font-style: italic; font-weight: bold;}
		t2 {font-size: 15px;}
		t2b {font-size: 15px;font-weight: bold;}
		p {font-size: 10px;}
		td {vertical-align: top;}
	</style>
  </head>"""

    body = "<body>"
    body_end = "</body>"
    div = """<div class="custom-page-start"> <hr>"""
    div_end = "</div>"
    h1 = "<h1>"
    h1_title = "<h1 style='font-size: 15px'>"
    h1_end = "</h1>"
    table = "<table border=1>"
    table_end = "</table>"
    tbody = "<tbody>"
    tbody_end = "</tbody>"
    hr = "<hr>"
    tr = "<tr>"
    tr_end = "</tr>"
    th = "<th>"
    th_end = "</th>"
    td = "<td>"
    td_end = "</td>"

    def title():

        t1 = """		<table border="0" style="border-collapse: collapse; width: 100%;">
			<tbody>
				<tr>
					<td style="width: 100%;font-size: 15px;">
						<h2>"""

        t2 = """</h2>
            </td>
          </tr>
        </tbody>
      </table>
    <hr>"""

        title = h1_title + output[0][0] + h1_end + t1 + output[0][1] + t2

        return title

    def solutions():

        t1 = """<table border="0" style="border-collapse: collapse; width: 100%;">
			<tbody>
				<tr>
					<td style="width: 60%; vertical-align: text-top;font-size: 15px"><h3>Solution No.:"""

        t2 = """</h3></td>
          </tr>
        </tbody>
      </table>"""

        t3 = """
          <table border="0" style="border-collapse: collapse; width: 100%;">
			<tbody>
				<tr>
					<td style="width: 7%;"><t1b>Download Reports:</t1b></td>
					<td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

        t4 = """
          " target="_blank" ><img height = "20px"src="http://civision.balafan.com:8010/icon/PDF_Summary"></a></td>
					<td style="width: 1%;"></td>
					<td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

        t5 = """
        " target="_blank" ><img height = "20px" src="http://civision.balafan.com:8010/icon/PDF_Detailed"></a></td>
              <td style="width: 78%;"></td>
            </tr>
          </tbody>
        </table>
        """
        m1 = """
      <table border="0" style="border-collapse: collapse; width: 100%;">
          <tbody>
            <tr>
              <td style="width: 100%;"><t1b></t1b></td>
            </tr>
          </tbody>
        </table>
          """

        h1 = """
          <table border="0" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
			<tbody>
				<tr>
					<td style="width: 100%;padding: 5px;border: 5px solid white;background-color: #bfd6f6  ;"><t2b>
          """

        h2 = """
          </t2b></td>
          </tr>
        </tbody>
      </table>
          """

        h3 = """
        <table border="1" bordercolor="#C0C0C0" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
			<tbody style="width: 100%;padding: 5px;border: 5px solid white;background-color: #e7eff6 ">
          """

        h4 = """
          </tbody>
      </table>
          """
        h5 = """
        <td style="width: 10%;"><t2>Section</t2></td>
        """
        h6 = """
        <td style="width: 10%;"><t2>Unit</t2></td>

          """
        h7 = """
        <td style="width: 10%;"><t2>Value</t2></td>

          """

        h8 = """
        <td style="width: 10%;text-align: center;" ><t2>
        """

        h9 = """
        </t2></td>
        """

        s = ""
        for k in range(len(output[4])):
            #  for l in range(len(output[4][0])):
            # if (k==0):
            # Table Header - Solution Number
            s = s + t1 + str(k + 1) + t2
            # Table Header - Solution Report Links
            # try:
            #     s = s + t3 + output[4][k][0] + t4 + output[4][k][1] + t5 + m1
            # except:
            #     s = s + t3 + str(output[4][k][0]) + \
            #         t4 + str(output[4][k][1]) + t5 + m1
            # try:
            #     s = s + t3 + output[5][2 * k] + "_1" + t4 + output[5][2 * k + 1] + "_1" + t5 + m1
            # except:
            #     s = s + t3 + str(output[5][0]) + \
            #         t4 + str(output[5][1]) + t5 + m1

            c1 = 0
            c2 = 0
            c3 = 2

            # Table Solution Group Fields, Field labels, units and values
            for i in range(0, int(len(output[1]))):
                if i % 2 == 0:
                    s = s + h1 + str(output[1][i + 1]) + h2 + h3
                    for j in range(output[1][i]):
                        if (j == 0):
                            s = s + tr + h5
                        s = s + h8 + output[2][c1] + h9
                        c1 = c1 + 1
                    s = s + tr_end
                    for j in range(output[1][i]):
                        if (j == 0):
                            s = s + tr + h6
                        s = s + h8 + output[3][c2] + h9
                        c2 = c2 + 1
                    s = s + tr_end
                    for j in range(output[1][i]):
                        if (j == 0):
                            s = s + tr + h7
                        s = s + h8 + str(output[4][k][c3]) + h9
                        c3 = c3 + 1
                    s = s + tr_end
                    s = s + tbody_end + table_end
            s = s + m1 + hr

        return s

    export = html + head + body + div + title() + solutions() + \
             div_end + body_end + html_end

    return export


def generate_html_response_BFP_multi_no_solution(output):
    response = ""

    for project_num in range(int(len(output))):
        html = "<html>"
        html_end = "</html>"

        head = """<head>
        <title>Output Summary</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style type="text/css">
          * {font-size: 10px; }
          body {
            font: 10px Arial, Helvetica, sans-serif;
            line-height: 1.0;
          }
          @media print {
            .pagebreak { page-break-before: always; }
          }
          @page {
            size: letter;
            margin: 1.5cm;
            @bottom-right {
              content: "Page " counter(page) " of " counter(pages);
            }
          }
          .custom-page-start {
            margin-top: 0px;
            margin-bottom: 0px;
          }
          h1 {color: #2f4f6e; font-size: 15px;}
          h2 {
            background: #96B9D0; font-size: 13px;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 3px;
            margin-bottom: 5px; margin-top: 5px;
            margin-left: -1px; margin-right: -1px;
          }
          h3 {
            background: #84c1ff ; font-size: 13px;
            font-size: 10px; 
            margin-bottom: -1px; margin-top: -1px;
            margin-left: -1px; margin-right: -1px;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 3px;
          }
          t1 {display: block; font-size: 15px; font-style: italic; padding-left: 3px;}
          t1b {font-size: 15px; font-style: italic; font-weight: bold;}
          t2 {font-size: 15px;}
          t2b {font-size: 15px;font-weight: bold;}
          p {font-size: 10px;}
          td {vertical-align: top;}
        </style>
        </head>"""

        body = "<body>"
        body_end = "</body>"
        div = """<div class="custom-page-start"> <hr>"""
        div_end = "</div>"
        h1 = "<h1>"
        h1_title = "<h1 style='font-size: 15px'>"
        h1_end = "</h1>"
        table = """<table border=1 class="table table-responsive table-striped table-sm table-hover">"""
        table_end = "</table>"
        tbody = "<tbody>"
        tbody_end = "</tbody>"
        hr = "<hr>"
        tr = "<tr>"
        tr_end = "</tr>"
        th = "<th>"
        th_end = "</th>"
        td = "<td>"
        td_end = "</td>"

        def title(project_num):
            t1 = """	<table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
            <tbody>
              <tr>
                <td style="width: 100%;font-size: 15px;">
                  <h2>"""

            t2 = """</h2>
                  </td>
                </tr>
              </tbody>
            </table>
          <hr>"""

            pn = "Project " + str(project_num + 1) + " "

            title = h1_title + output[project_num][0][0] + h1_end + t1 + pn + output[project_num][0][1] + t2

            return title

        def solutions():

            t1 = """<table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
        <tbody>
          <tr>
            <td style="width: 60%; vertical-align: text-top;font-size: 15px"><h3>Solution No.:"""

            t2 = """</h3></td>
            </tr>
          </tbody>
        </table>"""

            t3 = """
            <table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
        <tbody>
          <tr>
            <td style="width: 7%;"><t1b>Download Reports:</t1b></td>
            <td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

            t4 = """
            " target="_blank" ><img height = "20px"src="http://civision.balafan.com:8010/icon/PDF_Summary"></a></td>
            <td style="width: 1%;"></td>
            <td style="width: 7%;"><a href="http://civision.balafan.com:8010/report/BFP/"""

            t5 = """
          " target="_blank" ><img height = "20px" src="http://civision.balafan.com:8010/icon/PDF_Detailed"></a></td>
                <td style="width: 78%;"></td>
              </tr>
            </tbody>
          </table>
          """
            m1 = """
        <table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%;">
            <tbody>
              <tr>
                <td style="width: 100%;"><t1b></t1b></td>
              </tr>
            </tbody>
          </table>
            """

            h1 = """
            <table border="0" class="table table-responsive table-striped table-sm table-hover" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
        <tbody>
          <tr>
           <td style="width: 100%;padding: 5px;border: 5px solid white;background-color: #bfd6f6  "><t2b>
            """

            h2 = """
            </t2b></td>
            </tr>
          </tbody>
        </table>
            """

            h3 = """
          <table border="1" class="table table-responsive table-striped table-sm table-hover" bordercolor="#C0C0C0" style="border-collapse: collapse; width: 100%; background: #dfe3e6">
        <tbody style="width: 100%;padding: 5px;border: 5px solid white;background-color: #e7eff6">
            """
            h4 = """
            </tbody>
        </table>
            """
            h5 = """
          <td style="width: 10%;"><t2>Section</t2></td>
          """
            h6 = """
          <td style="width: 10%;"><t2>Unit</t2></td>

            """
            h7 = """
          <td style="width: 10%;"><t2>Value</t2></td>

            """

            h8 = """
          <td style="width: 10%;text-align: center"><t2>
          """

            h9 = """
          </t2></td>
          """

            s = ""
            for k in range(len(output[project_num][4])):
                #  for l in range(len(output[4][0])):
                # if (k==0):
                # Table Header - Solution Number
                s = s + t1 + str(k + 1) + t2
                # Table Header - Solution Report Links
                # try:
                #     s = s + t3 + output[project_num][5][2 * k] + "_" + str(project_num + 1) + t4 + \
                #         output[project_num][5][
                #             2 * k + 1] + "_" + str(project_num + 1) + t5 + m1
                # except:
                #     s = s + t3 + str(output[5][0]) + \
                #         t4 + str(output[5][1]) + t5 + m1
                # s = s + t3 + output[project_num][4][k][0] + t4 + output[project_num][4][k][1] + t5 + m1

                c1 = 0
                c2 = 0
                c3 = 2

                # Table Solution Group Fields, Field labels, units and values
                for i in range(0, int(len(output[project_num][1]))):
                    if i % 2 == 0:
                        if i == 0:
                            c1 = 0
                            c2 = 0
                            c3 = 2
                        s = s + h1 + str(output[project_num][1][i + 1]) + h2 + h3
                        for j in range(output[project_num][1][i]):
                            if (j == 0):
                                s = s + tr + h5
                            s = s + h8 + output[project_num][2][c1] + h9
                            c1 = c1 + 1
                        s = s + tr_end
                        for j in range(output[project_num][1][i]):
                            if (j == 0):
                                s = s + tr + h6
                            s = s + h8 + output[project_num][3][c2] + h9
                            c2 = c2 + 1
                        s = s + tr_end
                        for j in range(output[project_num][1][i]):
                            if (j == 0):
                                s = s + tr + h7
                            s = s + h8 + str(output[project_num][4][k][c3]) + h9
                            c3 = c3 + 1
                        s = s + tr_end
                        s = s + tbody_end + table_end
                s = s + m1 + hr

            return s

        export = html + head + body + div + title(project_num) + solutions() + div_end + body_end + html_end

        response = response + export

    return response