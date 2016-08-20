# coding: utf-8
import Tkinter as tk
import sqlite3


FOOTER_FONT = ('Verdana', '8')
SMALL_FONT = ('Verdana', '10')
NORMAL_FONT = ('Verdana', '10', 'bold')
LARGE_FONT = ('Verdana', '12', 'italic', 'bold')
LARGE1_FONT = ('Verdana', '12', 'italic')
TITLE_FONT = ('Verdana', '14', 'italic', 'bold')
SUBTITLE_FONT = ('Verdana', '12', 'italic', 'bold')




def fechapopup(popup, parent, frame):

	parent.show_frame(frame)
	popup.destroy()





class SecretariaApp(tk.Tk):

	def __init__(self, *args, **kwargs):

	
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, "Colégio Escolha Certa")
		

		container = tk.Frame(self)
		container.grid()
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		
		for F in (PaginaInicial, Alunos, Turmas, Matricular, Buscar, TodosAlunos):
		
			frame = F(self, container)
	
			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")
			
	
		self.show_frame(PaginaInicial)


	def show_frame(self, cont):

	
		frame = self.frames[cont]
		frame.tkraise()




class PaginaInicial(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


		parent.geometry("680x500+200+200")
	


		self.label = tk.Label(self, text = 'Colégio Escolha Certa', fg = 'black', font = TITLE_FONT, height = 3, width = 50)
		self.label.pack(pady=10, padx=10)


		self.botao1 = tk.Button(self, text = 'Alunos', fg = 'black', font = LARGE_FONT, height = 3, width = 50,command=lambda: parent.show_frame(Alunos))
		self.botao1.pack()

		self.botao2 = tk.Button(self, text = 'Turmas', fg = 'black', font = LARGE_FONT, height = 3, width = 50,command=lambda: parent.show_frame(Turmas))
		self.botao2.pack()


		self.botao3 = tk.Button(self, text = 'Sair', fg = 'black', font = LARGE_FONT, height = 3, width = 50, command=quit)
		self.botao3.pack()



class Alunos(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)




		self.label = tk.Label(self, text = 'Colégio Escolha Certa', fg = 'black', font = TITLE_FONT, height = 3, width = 50)
		self.label.pack(pady=10, padx=10)


		self.label2 = tk.Label(self, text = 'Alunos', fg = 'black', font = SUBTITLE_FONT, height = 3, width = 50)
		self.label2.focus_force()		
		self.label2.pack(pady=10, padx=10)

		
		self.botao1 = tk.Button(self, text = 'Matricular', fg = 'black', font = LARGE_FONT, height = 3, width = 50,command=lambda: parent.show_frame(Matricular))
		self.botao1.pack()

		self.botao2 = tk.Button(self, text = 'Buscar Aluno', fg = 'black', font = LARGE_FONT, height = 3, width = 50,command=lambda: parent.show_frame(Buscar))
		self.botao2.pack()

		self.botao3 = tk.Button(self, text = 'Voltar', fg = 'black', font = LARGE_FONT, height = 3, width = 50,command=lambda: parent.show_frame(PaginaInicial))
		self.botao3.pack()







class Turmas(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


		self.label = tk.Label(self, text = 'Colégio Escolha Certa', fg = 'black', font = TITLE_FONT, height = 3, width = 50)
		self.label.place(x=20, y=0)

		self.label1 = tk.Label(self, text="Visualizar Turmas", font=TITLE_FONT, height = 3, width = 50)
		self.label1.place(x=20, y=50)
		
		self.todos = tk.Button(self, text = 'Todos os Alunos', fg = 'black', font = SMALL_FONT,command=lambda: parent.show_frame(TodosAlunos))
		self.todos.place(x=50, y=73)


		self.serie = tk.IntVar()
		self.serie.set(0)
		self.turno = tk.StringVar()
		self.turno.set("a")

		self.series = []
		self.turnos = []

		self.serielabel = tk.Label(self, text="Série:*", font=LARGE1_FONT)
		self.serielabel.place(x=10, y=150)

		self.turnolabel = tk.Label(self, text="Turno:*", font=LARGE1_FONT)
		self.turnolabel.place(x=290, y=150)


		for i in range(3):

			pos_x = (80+80*i)

			self.series.append(tk.Radiobutton(self, text=i+1, value=i+1,state="active", variable=self.serie, font=LARGE1_FONT))
			self.series[i].place(x=pos_x, y= 150)

		TURNO = [("Manhã",0), ("Tarde",1)]

		for turno, indices in TURNO:
		
			pos_x = (360+120*indices)

			self.turnos.append(tk.Radiobutton(self, text=turno, value=turno,state="active", variable=self.turno, font=LARGE1_FONT))
			self.turnos[indices].place(x=pos_x, y= 150)

		self.botaobuscar = tk.Button(self, text = 'Buscar', fg = 'black', font = SMALL_FONT,command=lambda: buscar(self))
		self.botaobuscar.place(x=250, y=250)


		self.botaovoltar = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: voltarinicial(self, parent))
		self.botaovoltar.place(x=350, y=250)

		self.legendalabel = tk.Label(self, text="(*) Campos obrigatórios", font=FOOTER_FONT)
		self.legendalabel.place(x=50, y=300)

		def voltarinicial(self, parent):

			self.serie.set(0)	
			self.turno.set("a")
		
			parent.show_frame(PaginaInicial)

		def buscar(self):
	
			for i in range(3):

				self.series[i].destroy()


			for i in range(2):
		
				self.turnos[i].destroy()

			self.botaobuscar.destroy()
			self.botaovoltar.destroy()
			self.legendalabel.destroy()
			self.serielabel.destroy()
			self.turnolabel.destroy()
			self.todos.destroy()

			self.serielabel = tk.Label(self, text="Série:", font=LARGE_FONT)
			self.serielabel.place(x=90, y=130)

			self.series = tk.Label(self, text=self.serie.get(), font=LARGE_FONT)
			self.series.place(x=190, y=130)


			self.turnolabel = tk.Label(self, text="Turno:", font=LARGE_FONT)
			self.turnolabel.place(x=290, y=130)

			self.turnos = tk.Label(self, text=self.turno.get(), font=LARGE_FONT)
			self.turnos.place(x=400, y=130)

			self.matriculalabel = tk.Label(self, text = "Matrícula", font=LARGE_FONT)
			self.matriculalabel.place(x=120, y=170)		
		
			self.matricula = tk.Label(self, font=SMALL_FONT)
			self.matricula.place(x=160,y=200)
		

			self.alunoslabel = tk.Label(self, text = "Aluno", font=LARGE_FONT)
			self.alunoslabel.place(x=400, y=170)
		
			self.alunos = tk.Label(self, font=SMALL_FONT)
			self.alunos.place(x=300,y=200)

			connection = sqlite3.connect('alunos.db')
			c = connection.cursor()

			
			c.execute('SELECT id,nome,turno FROM alunos WHERE serie = ?', [(self.serie.get())])

			self.lista = c.fetchall()			

			matricula=""
			alunos=""

			
			for i in range(len(self.lista)):
		

				if self.lista[i][2] == self.turno.get():	
					matricula = matricula+str(self.lista[i][0])+'\n'
					alunos = alunos+self.lista[i][1]+'\n'


			self.matricula["text"] = matricula[0:len(matricula)-1]
			self.alunos["text"] = alunos[0:len(alunos)-1]

			self.botaovoltar = tk.Button(self, text = 'Voltar', fg = 'black',command=lambda: voltar(self, parent))
			self.botaovoltar.place(x=60, y=60)

		def voltar(self, parent):
			
			self.serielabel.destroy()
			self.series.destroy()
			self.turnolabel.destroy()
			self.turnos.destroy()
			self.botaovoltar.destroy()
			self.matricula.destroy()
			self.matriculalabel.destroy()
			self.alunos.destroy()
			self.alunoslabel.destroy()
			self.serie.set(0)
			self.turno.set("a")

			self.series = []
			self.turnos = []

			self.serielabel = tk.Label(self, text="Série:*", font=LARGE1_FONT)
			self.serielabel.place(x=10, y=150)

			self.turnolabel = tk.Label(self, text="Turno:*", font=LARGE1_FONT)
			self.turnolabel.place(x=290, y=150)

			self.todos = tk.Button(self, text = 'Todos os Alunos', fg = 'black', font = SMALL_FONT,command=lambda: parent.show_frame(TodosAlunos))
			self.todos.place(x=50, y=73)



			for i in range(3):

				pos_x = (80+80*i)

				self.series.append(tk.Radiobutton(self, text=i+1, value=i+1,state="active", variable=self.serie, font=LARGE1_FONT))
				self.series[i].place(x=pos_x, y= 150)

			TURNO = [("Manhã",0), ("Tarde",1)]

			for turno, indices in TURNO:
		
				pos_x = (360+120*indices)

				self.turnos.append(tk.Radiobutton(self, text=turno, value=turno,state="active", variable=self.turno, font=LARGE1_FONT))
				self.turnos[indices].place(x=pos_x, y= 150)

			self.botaobuscar = tk.Button(self, text = 'Buscar', fg = 'black', font = SMALL_FONT,command=lambda: buscar(self))
			self.botaobuscar.place(x=250, y=250)


			self.botaovoltar = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: voltarinicial(self, parent))
			self.botaovoltar.place(x=350, y=250)

			self.legendalabel = tk.Label(self, text="(*) Campos obrigatórios", font=FOOTER_FONT)
			self.legendalabel.place(x=50, y=300)
	

			
			parent.show_frame(PaginaInicial)





class Matricular(tk.Frame):


	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


		parent.minsize(width= 500, height = 500)

		self.serie = tk.IntVar()
		self.serie.set(0)
		self.turno = tk.StringVar()
		self.turno.set("a")

		self.label = tk.Label(self, text = 'Colégio Escolha Certa', fg = 'black', font = TITLE_FONT, height = 3, width = 50)
		self.label.place(x=20, y=0)

		self.label1 = tk.Label(self, text="Realizar Matricula", font=TITLE_FONT, height = 3, width = 50)
		self.label1.place(x=20, y=50)

		self.nomelabel = tk.Label(self, text="Nome do aluno: *", font=SMALL_FONT)
		self.nomelabel.place(x=50, y=110)

		self.nome = tk.Entry(self, width=40, font=SMALL_FONT)
		self.nome.place(x=180, y=110)	

		self.nascimentolabel = tk.Label(self, text="Data de Nascimento: *", font=SMALL_FONT)
		self.nascimentolabel.place(x=50,y=140)
	
		self.nascimento = tk.Entry(self, width=20, font=SMALL_FONT)
		self.nascimento.insert(0, "DD/MM/AAAA")
		self.nascimento.place(x=220, y=140)

		self.responsavellabel = tk.Label(self, text="Responsável: *", font=SMALL_FONT)
		self.responsavellabel.place(x=50,y=170)
		self.responsavel = tk.Entry(self, width=40, font=SMALL_FONT)
		self.responsavel.place(x=180,y=170)

		self.serielabel = tk.Label(self, text="Série: *", font=SMALL_FONT)
		self.serielabel.place(x=50,y=200)
		
		self.check1 = tk.Radiobutton(self, text="1", value=1,state="active", variable=self.serie, font=SMALL_FONT)
		self.check1.place(x=180,y=200)

		self.check2 = tk.Radiobutton(self, text="2", value=2,state="active", variable=self.serie, font=SMALL_FONT)
		self.check2.place(x= 240,y=200)
		self.check3 = tk.Radiobutton(self, text="3", value=3,state="active", variable=self.serie, font=SMALL_FONT)
		self.check3.place(x=300,y=200)

		self.turnolabel = tk.Label(self, text="Turno: *", font=SMALL_FONT)
		self.turnolabel.place(x=50,y=230)
		self.check4 = tk.Radiobutton(self, text="Manhã", value="Manhã",state="active", variable=self.turno, font=SMALL_FONT)
		self.check4.place(x=180,y=230)
		self.check5 = tk.Radiobutton(self, text="Tarde", value="Tarde",state="active", variable=self.turno, font=SMALL_FONT)
		self.check5.place(x=300,y=230)


		self.botao1 = tk.Button(self, text="Matricular",fg = 'black', font=SMALL_FONT,command=lambda: matricular(self, parent))
		self.botao1.place(x=250,y=260)


		self.botao2 = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: voltar(parent))
		self.botao2.place(x=350, y=260)

		self.legendalabel = tk.Label(self, text="(*) Campos obrigatórios", font=FOOTER_FONT)
		self.legendalabel.place(x=50, y=300)


	

		def matricular(self, controller):

			
			NOME = self.nome.get().upper()
			NASCIMENTO = self.nascimento.get()
			RESPONSAVEL = self.responsavel.get().upper()


			if NOME == "" or NASCIMENTO == "" or RESPONSAVEL == "" or self.serie.get() == 0 or self.turno.get() == "a":
				
				camposvazios()
			
			elif NASCIMENTO == "DD/MM/AAAA":
			
				validarnascimento()

			
			elif len(NASCIMENTO) != 10:
				
				validarnascimento()
			

			else:

				connection = sqlite3.connect('alunos.db')
				c = connection.cursor()
				


				c.execute('CREATE TABLE  IF NOT EXISTS alunos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	nome TEXT, nascimento TEXT, responsavel TEXT, serie TEXT, turno TEXT)')

				c.execute('CREATE TABLE  IF NOT EXISTS boletim (aluno_id INTEGER, boletim_id TEXT NOT NULL PRIMARY KEY, port INTEGER, mat INTEGER, geo INTEGER, hist INTEGER, bio INTEGER, fis INTEGER, qui INTEGER, FOREIGN KEY(aluno_id) REFERENCES alunos(id))')



				c.execute('INSERT INTO alunos (nome, nascimento, responsavel, serie, turno) VALUES(?,?,?,?,?)', (NOME, NASCIMENTO, RESPONSAVEL, self.serie.get(), self.turno.get()))
				c.execute('SELECT id FROM alunos WHERE nome = ?', ([NOME]))
				
				matricula = c.fetchall()
				boletim = []
				for i in range (1,5,1):
					boletim.append(str(matricula[0][0])+str(i))
				for i in range(len(boletim)):
					c.execute('INSERT INTO boletim (aluno_id, boletim_id) VALUES (?,?)', (matricula[0][0], boletim[i]))
					
				

				connection.commit()
				connection.close()


				self.nome.delete(0, len(NOME))
				self.nascimento.delete(0, len(NASCIMENTO))
				self.responsavel.delete(0, len(RESPONSAVEL))
				self.nascimento.insert(0, "DD/MM/AAAA")
				self.serie.set(0)
				self.turno.set("a")

							
				opcao(parent)

		def voltar(parent):
		
			self.nome.delete(0, len(self.nome.get()))
			self.nascimento.delete(0, len(self.nascimento.get()))
			self.responsavel.delete(0, len(self.responsavel.get()))
			self.nascimento.insert(0, "DD/MM/AAAA")
			self.serie.set(0)
			self.turno.set("a")


			parent.show_frame(PaginaInicial)
	


		def camposvazios():
			popup = tk.Tk()
			popup.title("Campos Vazios!")
			label = tk.Label(popup, text="Por favor, antes de matricular o aluno preencha os campos vazios!")
			label.grid(row="1",column="1", columnspan="2")
			B1 =  tk.Button(popup, text="Ok", command=lambda: popup.destroy())
			B1.grid(row="2",column="1", sticky="e")

		def validarnascimento():

			popup = tk.Tk()
			popup.title("Data de nascimento inválida!")
			label = tk.Label(popup, text="Por favor, verifique a data de nascimento antes de continuar!")
			label.grid(row="1",column="1", columnspan="2")
			B1 =  tk.Button(popup, text="Ok", command=lambda: popup.destroy())
			B1.grid(row="2",column="1", sticky="e")

		def opcao(parent):
		
			popup = tk.Tk()
			popup.title("Matrícula realizada!")
			label = tk.Label(popup, text="Deseja realizar outra matricula?", width = 32)
			label.grid(row="1",column="1", columnspan="2")
			B1 =  tk.Button(popup, text="Sim", command=lambda: popup.destroy())
			B1.grid(row="2",column="1", sticky="e")
			B2 = tk.Button(popup, text="Não", command=lambda: fechapopup(popup, parent, PaginaInicial))
			B2.grid(row="2",column="2", sticky="w")




class Buscar(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


		self.label = tk.Label(self, text = 'Colégio Escolha Certa', fg = 'black', font = TITLE_FONT, height = 3, width = 50)
		self.label.place(x=20, y=0)


		self.label1 = tk.Label(self, text="Buscar Aluno", font=TITLE_FONT, height = 3, width = 50)
		self.label1.place(x=20, y=50)


		self.nomelabel = tk.Label(self, text="Nome do aluno:", font=SMALL_FONT)
		self.nomelabel.place(x=50, y=110)


		self.aluno = tk.Entry(self, width=40, font=SMALL_FONT)
		self.aluno.place(x=180, y=110)



		self.botao1 = tk.Button(self, text="Buscar",fg = 'black', font=SMALL_FONT,command=lambda: buscar(self))
		self.botao1.place(x=250,y=150)
		


		self.botao2 = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: voltarinicial(self, parent))
		self.botao2.place(x=350, y=150)

		

		def voltarinicial(self, parent):

			self.aluno.delete(0, len(self.aluno.get()))
			parent.show_frame(PaginaInicial)
		

	
		

		def buscar(self):
			
	
			self.matriculalabel = tk.Label(self, text = "Matrícula", font=LARGE_FONT)
			self.matriculalabel.place(x=50, y=200)		
		



			self.matricula = tk.Label(self, font=SMALL_FONT)
			self.matricula.place(x=70,y=230)
		

			self.alunoslabel = tk.Label(self, text = "Aluno", font=LARGE_FONT)
			self.alunoslabel.place(x=280, y=200)
		
			self.alunos = tk.Label(self, font=SMALL_FONT)
			self.alunos.place(x=180,y=230)
			
			self.serielabel = tk.Label(self, text = "Série", font=LARGE_FONT)
			self.serielabel.place(x=470, y=200)
				
			self.serie = tk.Label(self, font=SMALL_FONT)
			self.serie.place(x=500,y=230)
		
			self.turnolabel = tk.Label(self, text = "Turno", font=LARGE_FONT)
			self.turnolabel.place(x=550, y=200)
		
			self.turno = tk.Label(self, font=SMALL_FONT)
			self.turno.place(x=550,y=230)
		

			connection = sqlite3.connect('alunos.db')
			c = connection.cursor()

			nome = self.aluno.get().upper()

			c.execute('SELECT id,nome,serie,turno FROM alunos WHERE nome LIKE ?', [('%'+nome+'%')])

			self.lista = c.fetchall()			
			self.mat = tk.IntVar()
			self.mat.set(0)

			matricula=""
			alunos=""
			serie= ""
			turno= ""

			self.buttons = []
			
			for i in range(len(self.lista)):

				pos_x=10
				pos_y=230+17*i
		

				
				matricula = matricula+str(self.lista[i][0])+'\n'
				alunos = alunos+self.lista[i][1]+'\n'
		
	
				serie = serie+str(self.lista[i][2])+ '\n'
				turno = turno+self.lista[i][3]+'\n'
		
				self.buttons.append(tk.Radiobutton(self, value=self.lista[i][0],state="active", variable=self.mat))
				self.buttons[i].place(x=pos_x, y=pos_y)



	
			self.boletim = tk.Button(self,text="Inserir Notas", font=SMALL_FONT, command=lambda: editarboletim(self, parent))
			self.boletim.place(x=200, y=pos_y+34)
			
		

			self.inserir = tk.Button(self,text="Boletim", font=SMALL_FONT,command = lambda: visualizar(self))
			self.inserir.place(x=350, y=pos_y+34)
		
		
			self.matricula["text"] = matricula[0:len(matricula)-1]
			self.alunos["text"] = alunos[0:len(alunos)-1]
			self.serie["text"] = serie[0:len(serie)-1]
			self.turno["text"] = turno[0:len(turno)-1]


			
		def camposvazios():

				popup = tk.Tk()
				popup.title("Campos Vazios!")
				label = tk.Label(popup, text="Por favor, selecione um aluno antes de continuar!")
				label.grid(row="1",column="1", columnspan="2")
				B1 =  tk.Button(popup, text="Ok", command=lambda: popup.destroy())
				B1.grid(row="2",column="1", sticky="e")

	

		def editarboletim(self, parent):


			if self.mat.get() == 0:

				camposvazios()
	
			else:

				
				self.label1["text"] = "Inserir Notas"
				self.nomelabel["text"] = "Aluno:"
				self.nomelabel["font"] = LARGE_FONT
				self.aluno.destroy()
				self.botao1.destroy()
				self.botao2.destroy()
				self.matriculalabel.destroy()
				self.alunoslabel.destroy()
				self.serielabel.destroy()
				self.turnolabel.destroy()
				self.matricula.destroy()
				self.alunos.destroy()
				self.serie.destroy()
				self.turno.destroy()
	
				for i in range(len(self.lista)):
					self.buttons[i].destroy()

				self.inserir.destroy()
				self.boletim.destroy()
	

	
				connection = sqlite3.connect('alunos.db')
				c = connection.cursor()

				c.execute('SELECT nome,serie,turno FROM alunos WHERE id = ?', [(self.mat.get())])
	
				aluno = c.fetchall()


				self.aluno = tk.Label(self, fg = 'black', font = LARGE_FONT, text=aluno[0][0])
				self.aluno.place(x=120, y=110)

				self.serielabel = tk.Label(self, text = "Série:", font=LARGE_FONT)
				self.serielabel.place(x=500, y=110)

				self.serie = tk.Label(self, font=LARGE_FONT, text = aluno[0][1])
				self.serie.place(x=570,y=110)

			
				self.turno = tk.Label(self, font=LARGE_FONT, text=aluno[0][2])
				self.turno.place(x=600,y=110)
				

				self.bim = tk.IntVar()
				self.bim.set(0)

				self.bimestrelabel = tk.Label(self, text = "Bimestre:", font=SMALL_FONT)
				self.bimestrelabel.place(x=250, y=140)
	

				self.radio = []

				for i in range(4):
				
					pos_x = (350+i*50)
					
					self.radio.append(tk.Radiobutton(self, value=i+1,state="active", variable=self.bim, text=i+1))
					self.radio[i].place(x=pos_x, y=140)

				
				self.labels = []
				self.entradas = []

				AUXILIAR = [("Português:",0), ("Matemática:",1), ("Geografia:",2), ("História:",3), ("Biologia:",4), ("Física:",5), ("Química:",6)]

				for disciplina, indices in AUXILIAR :
				
					pos_y = (190+indices*20)				
				

					self.labels.append(tk.Label(self, text = disciplina, font=SMALL_FONT))
					self.labels[indices].place(x=300, y=pos_y)
					self.entradas.append(tk.Entry(self, font=SMALL_FONT, width = 5))
					self.entradas[indices].place(x=400, y=pos_y)
			
			
				self.botaoenviar = tk.Button(self,text="Enviar", font=SMALL_FONT,command = lambda: enviarnotas(self))
				self.botaoenviar.place(x=300, y=330)

				self.botaovoltar = tk.Button(self,text="Voltar", font=SMALL_FONT,command = lambda: voltarnotas(self, parent))
				self.botaovoltar.place(x=500, y=330)

		def voltarnotas(self, parent):

			self.mat.set(0)
			self.bim.set(0)

			for i in range(7):

				self.labels[i].destroy()
				self.entradas[i].destroy()

			for i in range(4):
				
				self.radio[i].destroy()


			self.botaovoltar.destroy()
			self.botaoenviar.destroy()
			self.bimestrelabel.destroy()
			self.aluno.destroy()
			self.serielabel.destroy()
			self.serie.destroy()
			self.turno.destroy()
			self.label1.destroy()

			self.label1 = tk.Label(self, text="Buscar Aluno", font=TITLE_FONT, height = 3, width = 50)
			self.label1.place(x=20, y=50)


			self.nomelabel = tk.Label(self, text="Nome do aluno:", font=SMALL_FONT)
			self.nomelabel.place(x=50, y=110)


			self.aluno = tk.Entry(self, width=40, font=SMALL_FONT)
			self.aluno.place(x=180, y=110)



			self.botao1 = tk.Button(self, text="Buscar",fg = 'black', font=SMALL_FONT,command=lambda: buscar(self))
			self.botao1.place(x=250,y=150)



			self.botao2 = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: parent.show_frame(PaginaInicial))
			self.botao2.place(x=350, y=150)




			parent.show_frame(PaginaInicial)



		def enviarnotas(self):

			notas = []

			for i in range(7):
		
				notas.append(float(self.entradas[i].get()))	

			boletim_id = int(str(self.mat.get())+str(self.bim.get()))

			notas.append(boletim_id)
			i = 0
			aux = 0

			if self.bim.get() == 0:
		
				escolhabimestre(self)
		
			else:

				while i <= 6:

					if notas[i] < 0 or notas[i] > 10:
						notainvalida(self)
						aux += 1
						break
					i += 1

				if aux == 0:

					connection = sqlite3.connect('alunos.db')
					c = connection.cursor()

					c.execute('UPDATE boletim SET port = ?,  mat = ?, geo = ?, hist = ?,  bio = ?, fis = ?, qui = ?  WHERE boletim_id = ?', notas)


					connection.commit()
					connection.close()

					notasenviadas(self,parent )




		def escolhabimestre(self):

			popup = tk.Tk()
			popup.title("Bimestre inválido!")
			label = tk.Label(popup, text="Por favor, escolha em qual bimestre você deseja inserir as notas!")
			label.grid(row="1",column="1", columnspan="2")
			B1 =  tk.Button(popup, text="Ok", command=lambda: popup.destroy())
			B1.grid(row="2",column="1", sticky="e")


		def notainvalida(self):

			popup = tk.Tk()
			popup.title("Nota inválida!")
			label = tk.Label(popup, text="Por favor, verifique as notas antes de enviar!")
			label.grid(row="1",column="1", columnspan="2")
			B1 =  tk.Button(popup, text="Ok", command=lambda: popup.destroy())
			B1.grid(row="2",column="1", sticky="e")

		def notasenviadas(self, parent):

			self.popup = tk.Tk()
			self.popup.title("Notas enviadas com sucesso!")
			self.label = tk.Label(self.popup, text="As notas do aluno foram enviadas com sucesso!", width = 40)
			self.label.grid(row="1",column="1", columnspan="2")
			self.B1 =  tk.Button(self.popup, text="OK", command=lambda: fechapopup(self, parent))
			self.B1.grid(row="2",column="1", sticky="e")

		def fechapopup(self, parent):

			self.mat.set(0)
			self.bim.set(0)

			for i in range(7):

				self.labels[i].destroy()
				self.entradas[i].destroy()

			for i in range(4):
				
				self.radio[i].destroy()


			self.botaovoltar.destroy()
			self.botaoenviar.destroy()
			self.bimestrelabel.destroy()
			self.aluno.destroy()
			self.serielabel.destroy()
			self.serie.destroy()
			self.turno.destroy()
			self.label1.destroy()

			self.label1 = tk.Label(self, text="Buscar Aluno", font=TITLE_FONT, height = 3, width = 50)
			self.label1.place(x=20, y=50)


			self.nomelabel = tk.Label(self, text="Nome do aluno:", font=SMALL_FONT)
			self.nomelabel.place(x=50, y=110)


			self.aluno = tk.Entry(self, width=40, font=SMALL_FONT)
			self.aluno.place(x=180, y=110)



			self.botao1 = tk.Button(self, text="Buscar",fg = 'black', font=SMALL_FONT,command=lambda: buscar(self))
			self.botao1.place(x=250,y=150)



			self.botao2 = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: parent.show_frame(PaginaInicial))
			self.botao2.place(x=350, y=150)




			parent.show_frame(PaginaInicial)
			self.popup.destroy()


		def visualizar(self):


			if self.mat.get() == 0:

				camposvazios()
	
			else:

				
				self.label1["text"] = "Boletim"
				self.nomelabel["text"] = "Aluno:"
				self.nomelabel["font"] = LARGE_FONT
				self.aluno.destroy()
				self.botao1.destroy()
				self.botao2.destroy()
				self.matriculalabel.destroy()
				self.alunoslabel.destroy()
				self.serielabel.destroy()
				self.turnolabel.destroy()
				self.matricula.destroy()
				self.alunos.destroy()
				self.serie.destroy()
				self.turno.destroy()

				for i in range(len(self.lista)):
					self.buttons[i].destroy()

				self.inserir.destroy()
				self.boletim.destroy()

				self.notas = []

				connection = sqlite3.connect('alunos.db')
				c = connection.cursor()

				c.execute('SELECT nome,serie,turno FROM alunos WHERE id = ?', [(self.mat.get())])
	
				aluno = c.fetchall()
			
				c.execute('SELECT port,mat,geo,hist, bio, fis, qui FROM boletim WHERE boletim_id = ?', [(int(str(self.mat.get())+"1"))])

				self.notas.append(c.fetchall())
				
				c.execute('SELECT port,mat,geo,hist, bio, fis, qui FROM boletim WHERE boletim_id = ?', [(int(str(self.mat.get())+"2"))])

				self.notas.append(c.fetchall())

				c.execute('SELECT port,mat,geo,hist, bio, fis, qui FROM boletim WHERE boletim_id = ?', [(int(str(self.mat.get())+"3"))])

				self.notas.append(c.fetchall())

				c.execute('SELECT port,mat,geo,hist, bio, fis, qui FROM boletim WHERE boletim_id = ?', [(int(str(self.mat.get())+"4"))])

				self.notas.append(c.fetchall())


				
				
				
				self.aluno = tk.Label(self, fg = 'black', font = LARGE_FONT, text=aluno[0][0])
				self.aluno.place(x=120, y=110)

				self.serielabel = tk.Label(self, text = "Série:", font=LARGE_FONT)
				self.serielabel.place(x=500, y=110)

				self.serie = tk.Label(self, font=LARGE_FONT, text = aluno[0][1])
				self.serie.place(x=570,y=110)

				self.turno = tk.Label(self, font=LARGE_FONT, text=aluno[0][2])
				self.turno.place(x=600,y=110)
				
				self.labels = []
				self.bim = []

				DISCIPLINAS = [("Português:",0), ("Matemática:",1), ("Geografia:",2), ("História:",3), ("Biologia:",4), ("Física:",5), ("Química:",6)]
				BIMESTRES = [("1 Bimestre", 0), ("2 Bimestre", 1), ("3 Bimestre", 2), ("4 Bimestre", 3)]
				

				for disciplina, indices in DISCIPLINAS:
				
					pos_y = (190+indices*20)				
				

					self.labels.append(tk.Label(self, text = disciplina, font=SMALL_FONT))
					self.labels[indices].place(x=100, y=pos_y)

				for bimestre, indices in BIMESTRES:

					pos_x = (200+indices*100)

					self.bim.append(tk.Label(self, text = bimestre, font=SMALL_FONT))
					self.bim[indices].place(x=pos_x, y=150)

	
				self.boletim = [[],[],[],[]]
			
				for i in range(4):
					for j in range(7):
				
						pos_x = (240+i*100)
						pos_y = (190+j*20)

						self.boletim[i].append(tk.Label(self, text = self.notas[i][0][j], font=SMALL_FONT))
						self.boletim[i][j].place(x= pos_x, y= pos_y)


				self.botaovoltar = tk.Button(self, text = 'Voltar', fg = 'black',command=lambda: voltarboletim(self, parent))
				self.botaovoltar.place(x=50, y=50)


		def voltarboletim(self, parent):

			self.mat.set(0)

			for i in range(4):
				for j in range(7):
					self.boletim[i][j].destroy()
		
			
			for i in range(4):
				self.bim[i].destroy()


			for i in range(7):

				self.labels[i].destroy()



			self.botaovoltar.destroy()
			self.aluno.destroy()
			self.serielabel.destroy()
			self.serie.destroy()
			self.turno.destroy()
			self.label1.destroy()

			self.label1 = tk.Label(self, text="Buscar Aluno", font=TITLE_FONT, height = 3, width = 50)
			self.label1.place(x=20, y=50)


			self.nomelabel = tk.Label(self, text="Nome do aluno:", font=SMALL_FONT)
			self.nomelabel.place(x=50, y=110)


			self.aluno = tk.Entry(self, width=40, font=SMALL_FONT)
			self.aluno.place(x=180, y=110)



			self.botao1 = tk.Button(self, text="Buscar",fg = 'black', font=SMALL_FONT,command=lambda: buscar(self))
			self.botao1.place(x=250,y=150)



			self.botao2 = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: parent.show_frame(PaginaInicial))
			self.botao2.place(x=350, y=150)




			parent.show_frame(PaginaInicial)



class TodosAlunos(tk.Frame):


	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


		self.label = tk.Label(self, text = 'Colégio Escolha Certa', fg = 'black', font = TITLE_FONT, height = 3, width = 50)
		self.label.place(x=20, y=0)


		self.label1 = tk.Label(self, text="Alunos", font=TITLE_FONT, height = 3, width = 50)
		self.label1.place(x=20, y=50)

		self.botao1 = tk.Button(self, text = 'Buscar', fg = 'black', font = SMALL_FONT,command=lambda: buscar(self))
		self.botao1.place(x=200, y=350)


		self.botao2 = tk.Button(self, text = 'Voltar', fg = 'black', font = SMALL_FONT,command=lambda: voltar(self, parent))
		self.botao2.place(x=300, y=350)

		self.scrollbar = tk.Scrollbar(self)
		self.listbox = tk.Listbox(self, width=60, yscrollcommand=self.scrollbar.set)

		self.listbox.place(x=50,y=150)
		
		self.scrollbar.place(x=540, y=150, height = 160)





		def buscar(self):
		
			connection = sqlite3.connect('alunos.db')
			c = connection.cursor()


			c.execute('SELECT id,nome,responsavel,serie,turno FROM alunos')
	
			self.lista = c.fetchall()

			for i in range(len(self.lista)):

				self.listbox.insert("end",  str(self.lista[i][0])+"    "+self.lista[i][1]+"    "+self.lista[i][2]+"    "+str(self.lista[i][3])+"    "+self.lista[i][4])

			self.scrollbar.config(command=self.listbox.yview)

			connection.close()

		
		def voltar(self, parent):

			for i in range(len(self.lista)):

				self.listbox.delete(0, "end")
				parent.show_frame(PaginaInicial)



app = SecretariaApp()
app.mainloop()


