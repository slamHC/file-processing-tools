import pydbgen
import pylatex as pl
import shortuuid as sd
from pydbgen import pydbgen as dbgen
import os


myDB= dbgen.pydb()

geomtry_options = { 'margin': '0.7in'}

class GeneratedTable:
    def __init__(self,rows=10,columns=5,row_lines = None, vertical_lines = None): 
        self.rows = rows
        self.columns = columns 
        self.row_lines = row_lines
        self.vertical_lines = vertical_lines

        if self.vertical_lines ==  True:
            self.table_spec = 'c|c|c|c|c'
        else:
            self.table_spec = 'ccccc'
           
        self.generate_df(rows)


    def generate_df(self,rows):
        self.df = myDB.gen_dataframe(
        rows,fields=['name','city','phone',
        'license_plate','email'],
        real_email=False,phone_simple=True
        )
          

    def to_pdf(self):
        doc = pl.Document(geometry_options=geomtry_options)


        if self.row_lines == True:
            with doc.create(pl.Section('Table')):
                with doc.create(pl.Tabular(self.table_spec)) as table:
                    table.add_hline()
                    table.add_row(list(self.df.columns))
                    table.add_hline()
                    for row in self.df.index:
                        print(row)
                        table.add_row(list(self.df.loc[row,:]))
                        table.add_hline()
                    #table.add_hline()

                self.filename = sd.uuid()

                self.path = './generated_tables/' + self.filename 

                if not os.path.exists(self.path):
                    os.makedirs(self.path)

                doc.generate_pdf(self.path, compiler='pdflatex')
                self.path += '.pdf'
        else:
            with doc.create(pl.Section('Table')):
                with doc.create(pl.Tabular(self.table_spec)) as table:
                    table.add_hline()
                    table.add_row(list(self.df.columns))
                    table.add_hline()
                    for row in self.df.index:
                        print(row)
                        table.add_row(list(self.df.loc[row,:]))
                    table.add_hline()

            self.filename = sd.uuid()

            self.path = './generated_tables/' + self.filename 

            doc.generate_pdf(self.path, compiler='pdflatex')
            self.path += '.pdf'

    def get_path(self):
        return self.path
    
    def get_filename(self):
        return self.filename
        
