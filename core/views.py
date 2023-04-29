from django.shortcuts import render, redirect
from .models import Questao

# Create your views here.
def home(request):
    questoes=Questao.objects.all() #Dentro da variável questao tem todas as questoes que estao no banco de dados
    return render(request,"index.html",{"questoes":questoes})

def salvar(request):
    vtitulo=request.POST.get("titulo")
    vpergunta=request.POST.get("pergunta")
    vopcao1=request.POST.get("opcao1")
    vopcao2=request.POST.get("opcap2")
    vopcao3=request.POST.get("opcao3")
    vopcao4=request.POST.get("opcao4")
    vcorreta=request.POST.get("correta")
    vmsg_correta=request.POST.get("msg_correta")
    vmsg_errada=request.POST.get("msg_errada")
    vmsg_neutra=request.POST.get("msg_neutra")
    Questao.objects.create(titulo=vtitulo) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(pergunta=vpergunta) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(opcao1=vopcao1) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(opcao2=vopcao2) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(opcao3=vopcao3) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(opcao4=vopcao4) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(correta=vcorreta) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(msg_correta=vmsg_correta) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(msg_errada=vmsg_errada) #passa a variavel vtitulo para o atributo titulo
    Questao.objects.create(msg_neutra=vmsg_neutra) #passa a variavel vtitulo para o atributo titulo
    
    questoes=Questao.objects.all()
    return render(request,"index.html",{"questoes":questoes})

def editar(request, id):
    questao = Questao.objects.get(id=id)
    return render(request,"update.html",{"questao":questao})

def update(request,id):
    vtitulo=request.POST.get("titulo")
    vpergunta=request.POST.get("pergunta")
    vopcao1=request.POST.get("opcao1")
    vopcao2=request.POST.get("opcap2")
    vopcao3=request.POST.get("opcao3")
    vopcao4=request.POST.get("opcao4")
    vcorreta=request.POST.get("correta")
    vmsg_correta=request.POST.get("msg_correta")
    vmsg_errada=request.POST.get("msg_errada")
    vmsg_neutra=request.POST.get("msg_neutra")

    questao = Questao.objects.get(id=id)
    questao.titulo = vtitulo
    questao.pergunta = vpergunta
    questao.opcao1 = vopcao1
    questao.opcao2 = vopcao2
    questao.opcao3 = vopcao3
    questao.opcao4 = vopcao4
    questao.correta = vcorreta
    questao.msg_correta = vmsg_correta
    questao.msg_errada = vmsg_errada
    questao.msg_neutra = vmsg_neutra
    questao.save()
    return redirect(home)

def delete(request, id):
    questao = Questao.objects.get(id=id)
    questao.delete()
    return redirect(home)

