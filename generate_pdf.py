import fpdf

class CustomPDF(fpdf.FPDF):
 
    def header(self):
        # Set up a logo
        self.image('jdb.jpg', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
 
        # Add an address
        self.cell(100)
        self.cell(0, 5, 'Mike Driscoll', ln=1)
        self.cell(100)
        self.cell(0, 5, '123 American Way', ln=1)
        self.cell(100)
        self.cell(0, 5, 'Any Town, USA', ln=1)
 
        # Line break
        self.ln(20)
 
    def footer(self):
        self.set_y(-10)
 
        self.set_font('Arial', 'I', 8)
 
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')
  
if __name__ == '__main__':

    fpdf.SYSTEM_TTFONTS = 'c:/windows/fonts/'
    pdf = CustomPDF()
    
    # 修改字体
    pdf.add_page()
    pdf.add_font('lishu', '', 'simhei.ttf', uni=True)

    pdf.set_font("lishu", size=12)
    pdf.cell(200, 10, txt="标题1", ln=1, align="C")

    # 画图
    pdf.add_page()
    pdf.set_fill_color(255, 0, 0)
    pdf.ellipse(10, 10, 10, 100, 'F')
 
    pdf.set_line_width(1)
    pdf.set_fill_color(0, 255, 0)
    pdf.rect(20, 20, 100, 50)

    # 添加图片
    pdf.add_page()
    pdf.image('jdb.jpg', x=10, y=8, w=100)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)  # move 85 down
    pdf.cell(200, 10, txt="{}".format('jdb.jpg'), ln=1)

    # 表格
    data = [['First Name', 'Last Name', 'email', 'zip'],
            ['Mike', 'Driscoll', 'mike@somewhere.com', '55555'],
            ['John', 'Doe', 'jdoe@doe.com', '12345'],
            ['Nina', 'Ma', 'inane@where.com', '54321']
            ]
    pdf.set_font("Arial", size=12)
    pdf.add_page()
 
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    spacing = 2.0
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)

    pdf.output("simple_demo.pdf")