import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>9x9</title>
 
<style type="text/css">
table{
	width:600px;
	border-collapse:collapse;
	}
table th{
	border:#CC0000 1px solid
	}
</style>
</head>
<body>
 
<script type="text/javascript">
 
document.write("<table>");
 
for (var x = 1; x <= 9; x++)
{
	document.write("<tr>");
	for (var y = 1; y <= x; y++)
	{
		document.write("<th>"+y+"*"+x+"="+y*x+"</th>");
	}
	document.write("</tr>");
}
document.write("</table>");
 
</script>
</body>
</html>
''')


class www(tornado.web.RequestHandler):
    def get(self,n):
        self.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>nxn</title>
 
<style type="text/css">
table{
	width:600px;
	border-collapse:collapse;
	}
table th{
	border:#CC0000 1px solid
	}
</style>
</head>
<body>
 
<script type="text/javascript">
 
document.write("<table>");
 
for (var x = 1; x <= 4; x++)
{
	document.write("<tr>");
	for (var y = 1; y <= x; y++)
	{
		document.write("<th>"+y+"*"+x+"="+y*x+"</th>");
	}
	document.write("</tr>");
}
document.write("</table>");
 
</script>
</body>
</html>
''')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/([0-9]+)", www),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
