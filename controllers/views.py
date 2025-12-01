from flask import render_template, request, redirect, url_for
from models.modelo import db, Tarefa
from werkzeug.utils import secure_filename
import os

def init_app(app):

    @app.route("/")
    def index():
        busca = request.args.get("busca", "")
        categoria = request.args.get("categoria", "")
        ordem = request.args.get("ordem", "")

        tarefas = Tarefa.query

        if busca:
            tarefas = tarefas.filter(Tarefa.titulo.ilike(f"%{busca}%"))

        if categoria:
            tarefas = tarefas.filter_by(categoria=categoria)

        if ordem == "alf":
            tarefas = tarefas.order_by(Tarefa.titulo.asc())
        else:
            tarefas = tarefas.order_by(Tarefa.data_criacao.desc())

        tarefas = tarefas.all()
        return render_template("index.html", tarefas=tarefas)

    @app.route("/adicionar", methods=["GET", "POST"])
    def adicionar():
        if request.method == "POST":
            titulo = request.form["titulo"]
            descricao = request.form.get("descricao", "")
            categoria = request.form.get("categoria", "")
            imagem = None

            if "imagem" in request.files:
                file = request.files["imagem"]

                if file.filename != "":
                    filename = secure_filename(file.filename)

                    ext = filename.rsplit('.', 1)[1].lower()
                    if ext not in ["png", "jpg", "jpeg"]:
                        return """
                        <script>
                            alert('Formato de imagem inválido! Apenas PNG, JPG e JPEG são permitidos.');
                            window.location.href = '/adicionar';
                        </script>
                        """

                    filepath = os.path.join(app.root_path, "static/img", filename)
                    file.save(filepath)
                    imagem = filename

            nova = Tarefa(
                titulo=titulo,
                descricao=descricao,
                categoria=categoria,
                imagem=imagem
            )

            db.session.add(nova)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("adicionar.html")

    @app.route("/editar/<int:id>", methods=["GET", "POST"])
    def editar(id):
        tarefa = Tarefa.query.get_or_404(id)

        if request.method == "POST":
            tarefa.titulo = request.form["titulo"]
            tarefa.descricao = request.form["descricao"]
            tarefa.categoria = request.form["categoria"]

            db.session.commit()
            return redirect(url_for("index"))

        return render_template("editar.html", tarefa=tarefa)


    @app.route("/concluir/<int:id>", methods=["POST"])
    def concluir(id):
        tarefa = Tarefa.query.get_or_404(id)
        tarefa.concluida = not tarefa.concluida
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/deletar/<int:id>", methods=["POST"])
    def deletar(id):
        tarefa = Tarefa.query.get_or_404(id)
        db.session.delete(tarefa)
        db.session.commit()
        return redirect(url_for("index"))
