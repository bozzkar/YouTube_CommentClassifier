<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page
	import="java.util.List,java.io.BufferedReader,java.io.IOException,java.io.PrintWriter,java.io.FileReader"%>	
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta charset="utf-8">
<title>Classified Comments!</title>
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
<link rel="stylesheet" href="/resources/demos/style.css">
<script>
	$(function() {
		$("#tabs").tabs();
	});
</script>
</head>
<body>

	<%
	//String videoID = "CY82JG7sdeg";
	String videoID = request.getParameter("videoID");
	String cmd = "python getComments.py "+videoID;
	System.out.println(cmd);
	Process proc;	
		String val;
		try { 
			try{
				proc = Runtime.getRuntime().exec(cmd);
				proc.waitFor();
				java.io.InputStream is = proc.getInputStream();
				java.util.Scanner s = new java.util.Scanner(is)
						.useDelimiter("\\A");
				
				if (s.hasNext()) {
					val = s.next();
				} else {
					val = "";
				}
				%><%=val %><%
			}catch(Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println("Finished execution");
			
        
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		//request.getParameter("videoID");
		String categories[] = { "offensive", "spam", "others" };

		String pluginContent = "";

		// Generation of the following html snippet
		// <div id="tabs">

		pluginContent = pluginContent + "<div id=\"tabs\"><ul>";
		// <ul>
		// <li><a href="#tabs-0">Nunc tincidunt</a></li>
		// <li><a href="#tabs-1">Proin dolor</a></li>
		// <li><a href="#tabs-2">Aenean lacinia</a></li>
		// </ul>
		for (int i = 0; i < categories.length; i++) {
			pluginContent = pluginContent + "<li><a href=\"#tabs-" + i
					+ "\">" + categories[i] + "</a></li>";
		}
		pluginContent = pluginContent + "</ul>";
		// Generation of Comments inside the tab
		// <div id="tabs-0">
		// <br>Proin elit arcu, rutrum commodo, vehicula tempus, commodo a,
		// risus. Curabitur nec arcu. Donec sollicitudin mi sit amet mauris. Nam
		// elementum quam ullamcorper ante. Etiam aliquet massa et lorem. Mauris
		// dapibus lacus auctor risus. Aenean tempor ullamcorper leo. Vivamus
		// sed magna quis ligula eleifend adipiscing. Duis orci. Aliquam sodales
		// tortor vitae ipsum. Aliquam nulla. Duis aliquam molestie erat. Ut et
		// mauris vel pede varius sollicitudin. Sed ut dolor nec orci tincidunt
		// interdum. Phasellus ipsum. Nunc tristique tempus lectus.</p>
		// </div>
		for (int i = 0; i < categories.length; i++) {
			pluginContent = pluginContent + "<div id=\"tabs-" + i + "\">";
			String fileName = videoID + "_" + categories[i] + ".txt";
			System.out.println(fileName);
			String fileLine;
			BufferedReader br = new BufferedReader(new FileReader(fileName));

			while ((fileLine = br.readLine()) != null) {
				pluginContent = pluginContent + "<br>-> " + fileLine;
			}

			pluginContent = pluginContent + "</div>";
			br.close();
		}

		pluginContent = pluginContent + "</div>";
	%>
	<div id="pluginContent"><%=pluginContent%></div>
</body>
</html>