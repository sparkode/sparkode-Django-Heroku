from django.template import loader
import json
import random
from django.shortcuts import render
from django.db.models import Q
from django.http  import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pnl.models import Usuario, Aprendizaje, Temas, SubTemas, Ejercicio, TemaUsuario, EjercicioR, Tecnologico
from django.views import View
#from braces.views import JSONResponseMixin, LoginRequiredMixin
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail

# Create your views here.

def recuperarContra(request):
    if 'member_id' in request.session:
        return HttpResponseRedirect('/principal/')
    if request.method == 'POST':
        errores = []
        if not request.POST.get('NUsuario',''):
            errores.append('Introduce tu nombre de usuario')
        if not request.POST.get('Email',''):
            errores.append('Introduce tu email')
        if not errores:
            try:
                recuperar = Usuario.objects.get(NombreUsuario = request.POST['NUsuario'])
                usuario = getattr(recuperar,'NombreUsuario')
                correo = getattr(recuperar, 'Email')
                if (usuario == request.POST['NUsuario'] and correo == request.POST['Email']):
                    contra = getattr(recuperar, 'Password')
                    send_mail(
                        'Recuperar Contraseña',
                        'Su contraseña es: '+contra,
                        'sparkodeteam@gmail.com',
                        [correo],
                        fail_silently=False,
                    )
                    errores.append('Revise su correo para obtener su contraseña')
                    return render(request,'recuperar.html',{'errores':errores})
                else:
                    errores.append('El usuario no existe')
                    return render(request,'recuperar.html',{'errores':errores})
            except Usuario.DoesNotExist:
                errores.append('Los datos no son correctos')            
                return render(request,'recuperar.html',{'errores':errores})
    return render(request,'recuperar.html')
#vista de acerca de 
def acercade(request):
    #aquí validamos que exista una sesión para que el usuario pueda entrar a la página principal
  
          
            return render(request,'acercade.html',{'color':'tema-uno','color2':'j1'})



def principal(request):
    #aquí validamos que exista una sesión para que el usuario pueda entrar a la página principal
    if 'member_id' in request.session:
        errores = []
        try: 
            nusuario = Usuario.objects.get(id = request.session['member_id'])
            usu = getattr(nusuario,'NombreUsuario')
           
            Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
            return render(request,'principal.html',{'nusuario':usu})
        except Aprendizaje.DoesNotExist:
            errores.append('Debe completar este cuestionario primero')
            return render(request,'TestAprendizaje.html',{'errores':errores}) 

    return HttpResponseRedirect('/login/')
#vista para cerrar sesión
def logOut(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/principal/')

#vista del temario
def temario(request):
    #aquí validamos que exista una sesión para que el usuario pueda entrar a la página principal
    if 'member_id' in request.session:
        errores = []
        try: 
            nusuario = Usuario.objects.get(id = request.session['member_id'])
            usu = getattr(nusuario,'NombreUsuario')
            #???
            Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
            return render(request,'Temas/Temario.html',{'color':'tema-uno','color2':'j1','nusuario':usu})
        except Aprendizaje.DoesNotExist:
           
            return render(request,'TestAprendizaje.html',{'errores':errores}) 

    return HttpResponseRedirect('/login/')

#vista para logear un usuario
def login(request):
    #lista para almacenar posibles errores
    errores = []
    if 'member_id' in request.session:
        return HttpResponseRedirect('/principal/')
    if request.method == 'POST':
        if not request.POST.get('usuario',''):
            errores.append('Introduce tu nombre de usuario')
        if not request.POST.get('password',''):
            errores.append('Introduce tu contraseña')
        if not errores:
            try:
                #obtenemos los datos del usuario desde la BD
                validar = Usuario.objects.get(NombreUsuario = request.POST['usuario'])
            except Usuario.DoesNotExist:
                errores.append('¡El nombre de usuario no existe!')
            else:
                if validar.Password == request.POST['password']:
                    #request.session es un diccionario de datos, en el cual llenamos con información del usuario
                    request.session['member_id'] = validar.id
                    request.session['member_Nivel'] = validar.Nivel
                    request.session['member_Progreso'] = validar.Progreso
                    if validar.Nivel == 0 and validar.Progreso == 0:
                        #si el nivel del usuario y su progreso es 0, se le mandará al test de aprendizaje para saber 
                        #cómo aprende mejor las cosas
                        return HttpResponseRedirect('/TestAprendizaje/')
                        #si el usuario ya tiene un avance, se le manda a la página principal
                    return HttpResponseRedirect('/principal/')
                errores.append('La contraseña no es correcta')
    #si el usuario intenta ir al login, se valida si la sesión está activa, si es así, se le manda a la página principal

    return render(request,'login.html',{'errores':errores})

#vista para procesar el registro de un usuario
def registro(request):
    #lista para almacenar los errores
    errores=[]
    #aquí se debe colocar la condición para que si una sesión está activa, se impida el acceso al registro
    #el formulario envía los datos mediante POST
    if request.method == 'POST':
        #vamos a validar que el formulario esté completo, a pesar que ya se limitó el formulario en html, se verifica de nuevo
        if not request.POST.get('Nombre',''):
            errores.append('Por favor introduce tu nombre')
        if not request.POST.get('ApellidoP',''):
            errores.append('Por favor introduce tu apellido paterno')    
        if not request.POST.get('ApellidoM',''):
            errores.append('Por favor introduce tu apellido Materno')
        if not request.POST.get('Year',''):
            errores.append('Por favor introduce tu año de nacimiento')
        if not request.POST.get('NUsuario',''):
            errores.append('Por favor introduce tu nombre de usuario')
        if not request.POST.get('Password',''):
            errores.append('Por favor introduce tu contraseña')
        if not request.POST.get('Password2',''):
            errores.append('Por favor introduce tu contraseña 2 veces')
        if not request.POST.get('Email',''):
            errores.append('Por favor introduce tu email')
        if not request.POST.get('Clave',''):
            errores.append('Por favor introduce la clave de tu tecnológico')
        if not errores:
            if request.POST['Password'] == request.POST['Password2']:
                #ahora tenemos que verificar que no exista el Usuario que se va a registrar en la BD
                try:
                    Usuario.objects.get(NombreUsuario=request.POST['NUsuario'])
                except Usuario.DoesNotExist:
                    #aunque el usuario no exista, se debe tener cuidado que el correo tampoco se repita con algún otro
                    try:
                        Usuario.objects.get(Email = request.POST['Email'])
                    except Usuario.DoesNotExist:
                        #concateno para que se guarde la fecha de nacimiento de forma correcta
                        Fecha_Nacimiento = request.POST['Year']
                        #tuve que poner objects porque objec no jala xdxd
                        try:
                            idTec = Tecnologico.objects.get(ClavePlantel = request.POST['Clave'])
                        except Tecnologico.DoesNotExist:
                            errores.append('La clave de tu Tecnológico no está registrada, acude con tus profesores')
                            return render(request,'registro.html',{'errores':errores})                          
                        send_mail(
                            'Mensaje de Bienvenida',
                            'Bienvenido a Sparkode: Usuario: '+request.POST['NUsuario']+' Contrseña: '+request.POST['Password'],
                            'sparkodeteam@gmail.com',
                            [request.POST['Email']],
                            fail_silently=False,
                            )
                        errores.append('Hemos envíado un correo de validación, si no lo encuentra, puede cambiar su correo en su perfil')
                        
                        insert= Usuario(NombreUsuario=request.POST['NUsuario'],Nombre=request.POST['Nombre'],ApellidoPaterno=request.POST['ApellidoP'], ApellidoMaterno=request.POST['ApellidoM'],Password=request.POST['Password'],Email=request.POST['Email'],FechaNacimiento=Fecha_Nacimiento,Nivel=0, Progreso=0,IdTecnologico=idTec)
                        #Guardar en la BD
                        insert.save()
                        #retornar al login
                        return render(request,'registro.html',{'errores':errores})
                    #ahora retrocediendo, si el email existe, almacena otro mensaje de error y así con el usuario
                    else:
                        errores.append('El Email ya existe')
                else:
                    errores.append('El usuario ya existe')
            if request.POST['Password'] != request.POST['Password2']:
                errores.append('Las contraseñas no coinciden')
#nos redirecciona al formulario de registro y devolvemos los errores
    return render(request,'registro.html',{'errores':errores})

def TestAprendizaje (request):
    errores = []
    if 'member_id' in request.session:
        if request.session['member_Progreso'] > 0:
            return HttpResponseRedirect('/principal/')
        
        if request.method == 'POST':
            contador = 1       
            while contador < 19:                
                cont = str(contador)
                if not request.POST.get('p'+cont, False):
                    errores.append('Por favor contesta la pregunta: '+ cont)
                    return render(request,'TestAprendizaje.html',{'errores':errores}) 
                contador = contador + 1                     
                
            #comprobar que los campos estén completos
            #obtener los valores del formulario del test, organizados por Pregunta auditiva, visual y kinestésica
            Pa=int(request.POST['p2'])+int(request.POST['p5'])+int(request.POST['p12'])+int(request.POST['p14'])+int(request.POST['p15'])+int(request.POST['p17'])
            Pv=int(request.POST['p1'])+int(request.POST['p3'])+int(request.POST['p6'])+int(request.POST['p9'])+int(request.POST['p10'])+int(request.POST['p11'])
            Pk=int(request.POST['p4'])+int(request.POST['p7'])+int(request.POST['p8'])+int(request.POST['p13'])+int(request.POST['p16'])+int(request.POST['p18'])
            Pt= Pa+Pv+Pk
            #porcentaje de cada tipo de aprendizaje
            EvAu = round((Pa/Pt)*100)
            EvVi = round((Pv/Pt)*100)
            EvKi = round((Pk/Pt)*100)   

            #asignar la cantidad de ejercicios a mostrar al usuario         
            if EvAu > EvVi and EvAu > EvKi:
                CantidadAudi = 3
                CantidadVis = 1 
                CantidadKin = 1   
            if EvVi > EvAu and EvVi > EvKi:
                CantidadVis = 3
                CantidadAudi = 1
                CantidadKin = 1
            if EvKi > EvAu and EvKi > EvVi:
                CantidadKin = 3
                CantidadAudi = 1
                CantidadVis = 1
                #si las respuestas son todas iguales
            else:
                CantidadKin = 2
                CantidadAudi = 1
                CantidadVis = 2              
            #guardar la información obtenida
            try:
                Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
            except Aprendizaje.DoesNotExist:
                insert= Aprendizaje(Visual=EvVi,Auditivo=EvAu,Kinestesico=EvKi, CantidadVisuales = CantidadVis, CantidadAuditivos = CantidadAudi,CantidadKinestesicos = CantidadKin ,IdUsuario_id=request.session['member_id'])
                insert.save()
                #modificar el nivel y progreso del usuario
                Usuario.objects.filter(id=request.session['member_id']).update(Progreso=1)
                Usuario.objects.filter(id=request.session['member_id']).update(Nivel=1)
                #actualizar el diccionario de la sesión
                request.session['member_Nivel'] = 1
                request.session['member_Progreso'] = 1 

                dato = Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
                return render(request, 'Resultados.html',{'dato':dato})
            else:
                return HttpResponse("Consulta con el Administrador")               
                #si hay algun problema, vuelve al test
        return render(request,'TestAprendizaje.html',{'errores':errores})        
        #si no hay una sesion retorna al login
    return HttpResponseRedirect('/login/')

def tema(request, tema, subtema, pagina):
    #al retroceder después de cerrar sesión, la página carga, pero al recargar, si dirige correctamente
    #esto no pasa al iniciar sesión, y cerrar desde la página principal

    if 'member_id' in request.session:
        try:
            if tema == 1:
                color = "tema-uno"
                color2 ="j1"
            if tema == 2:
                color = "tema-dos"
                color2 ="j2"
            if tema == 3:
                color = "tema-tres"
                color2 ="j3"
            if tema == 4:
                color = "tema-cuatro"
                color2 ="j4"
            if tema == 5:
                color = "tema-cinco"
                color2 ="j5"
            evaluacion = ['E1', 'E2', 'E3', 'E4', 'E5']
            datos = Usuario.objects.get(id = request.session['member_id'])            
            nivel = getattr(datos, 'Nivel')
            nusuario = getattr(datos,'NombreUsuario') 
            # por si el usuario se encuentra en evaluación, que lo mande al tema sin actualizar los niveles ni progreso
            if nivel in evaluacion:
                ###para revisar lo del tema = E1
                return render(request, 'Temas/%d-%d-%d.html'%(int(tema), int(subtema), int(pagina)),{'nusuario':nusuario, 'color':color, 'color2':color2})
            nivel = int(nivel)
            progreso = int(getattr(datos, 'Progreso'))
#si el usuario se pasa a otra parte del temario de mayor nivel, que se almacene su ultima conexión, pues se queda atascado en las evaluaciones

            if tema > nivel:
                Usuario.objects.filter(id=request.session['member_id']).update(Nivel=tema)
                Usuario.objects.filter(id=request.session['member_id']).update(Progreso=1)   
            if subtema > progreso and tema >= nivel:
                Usuario.objects.filter(id=request.session['member_id']).update(Progreso=subtema)                
            return render(request, 'Temas/%d-%d-%d.html'%(int(tema), int(subtema), int(pagina)),{'nusuario':nusuario, 'color':color, 'color2':color2})
        except Usuario.DoesNotExist:
            return HttpResponseRedirect('/principal/')        
    return HttpResponseRedirect('/principal/')

#vista para los ejemplos
def EjercicioEj(request, clave, subtema, tipo, numero):
    if 'member_id' in request.session:
        if clave == "EJ1":
            color = "tema-uno"
            color2 ="j1"
        if clave == "EJ2":
            color = "tema-dos"
            color2 ="j2"
        if clave == "EJ3":
            color = "tema-tres"
            color2 ="j3"            
        if clave == "EJ4":
            color = "tema-cuatro"
            color2 ="j4"
        if clave == "EJ5":
            color = "tema-cinco"
            color2 ="j5"
        nusuario = Usuario.objects.get(id = request.session['member_id'])
        usu = getattr(nusuario,'NombreUsuario')            
        return render(request,'Ejercicios/%s-%d-%s-%d.html'%(clave, int(subtema), tipo, int(numero)),{'nusuario': usu,'color':color, 'color2':color2})
    return HttpResponseRedirect('/principal/')    

def Ejercicios(request, clave):
    if 'member_id' in request.session:
        if clave == "E1":
            color = "tema-uno"
            color2 ="j1"
            tema = 1
        if clave == "E2":
            color = "tema-dos"
            color2 ="j2"
            tema = 2
        if clave == "E3":
            color = "tema-tres"
            color2 ="j3"            
            tema = 3
        if clave == "E4":
            color = "tema-cuatro"
            color2 ="j4"
            tema = 4
        if clave == "E5":
            color = "tema-cinco"
            color2 ="j5"
            tema = 5
        Usuario.objects.filter(id=request.session['member_id']).update(Nivel=clave) 
        try:
            Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
            try:
                Ejercicio.objects.filter(IdUsuario_id = request.session['member_id'])
                #obtener la cantidad de ejercicios que debe hacer el usuario
                nusuario = Usuario.objects.get(id = request.session['member_id'])
                usu = getattr(nusuario,'NombreUsuario')

                aprendi = Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
                visuales = getattr(aprendi, 'CantidadVisuales')
                auditivos = getattr(aprendi, 'CantidadAuditivos')
                kinestesicos = getattr(aprendi, 'CantidadKinestesicos')

                cantidad_resueltos_V = Ejercicio.objects.filter(Tipo = "V", IdTem = tema, IdUsuario_id = request.session['member_id']).count()
                cantidad_resueltos_A = Ejercicio.objects.filter(Tipo = "A", IdTem = tema, IdUsuario_id = request.session['member_id']).count()
                cantidad_resueltos_K = Ejercicio.objects.filter(Tipo = "K", IdTem = tema, IdUsuario_id = request.session['member_id']).count()
                cantidad_ejercicios = cantidad_resueltos_V + cantidad_resueltos_A + cantidad_resueltos_K
                tipo_ejercicio = "V"

                numero = 1 
                if cantidad_ejercicios < 6:
                    if cantidad_resueltos_V < visuales and cantidad_resueltos_A == 0 and cantidad_resueltos_K == 0:
                        tipo_ejercicio = "V"
                    elif cantidad_resueltos_V == visuales and (cantidad_resueltos_A == 0 or cantidad_resueltos_A < auditivos):
                        tipo_ejercicio = "A"
                    else:
                        tipo_ejercicio = "K"               

                ###############################################
                ###############Falta actualizar los datos de progreso y nivel del usuario en esta parte
                ###############################################
                
                #si ya acabó los ejercicios del tema, que lo mande al siguiente tema
                if cantidad_ejercicios >= 5:
                    if tema == 5:
                       return HttpResponseRedirect('/principal/') 
                    else:    
                        tema = tema + 1
                        siguienteTema = str(tema)
                        Usuario.objects.filter(id=request.session['member_id']).update(Nivel=siguienteTema) 
                        Usuario.objects.filter(id=request.session['member_id']).update(Progreso=1)                      
                        return HttpResponseRedirect('/tema/%d/%d/%d'%(int(tema),int(1),int(1)))
                              
                    nombre_ejercicio = clave +"-"+str(tipo_ejercicio)+"-"+str(numero)   
                while True: 
                    try:
                        if cantidad_ejercicios < 6:
                            if cantidad_resueltos_V < visuales and cantidad_resueltos_A == 0 and cantidad_resueltos_K == 0:
                                tipo_ejercicio = "V"
                            elif cantidad_resueltos_V == visuales and (cantidad_resueltos_A == 0 or cantidad_resueltos_A < auditivos):
                                tipo_ejercicio = "A"
                            else:
                                tipo_ejercicio = "K"              
                        numero = random.randint(1,3)
                        nombre_ejercicio = clave +"-"+str(tipo_ejercicio)+"-"+str(numero)
                        #ver si el ejercicio ya ha sido contestado                        
                        Ejercicio.objects.get(Nombre = nombre_ejercicio, IdTem = tema, IdUsuario_id = request.session['member_id'])
                        #si el ejercicio no se encuentra en los ejercicios contestados, lo manda al ejercicio
                    except Ejercicio.DoesNotExist:
                        #separar a los kinestésicos
                        if tipo_ejercicio != "K":
                            return render(request,'Ejercicios/%s-%s-%d.html'%(clave, tipo_ejercicio, numero),{'nusuario': usu,'color':color, 'color2':color2})
                        else:
                            #numero = random.randint(1,3)
                            while True:
                                try :
                                    numero = random.randint(1,3)
                                    nombre_ejercicio = clave+"-"+str(tipo_ejercicio)+"-"+str(numero)
                                    Ejercicio.objects.get(Nombre = nombre_ejercicio, IdTem = tema, IdUsuario_id = request.session['member_id'])
                                except Ejercicio.DoesNotExist:
                                    return render(request,'Ejercicios/kinestesicos/%s-K-%d.html'%(clave, numero),{'nusuario': usu,'color':color, 'color2':color2}) 
                else:
                    #aquí debe mandar al siguiente tema ###creo se puede quitar
                    return HttpResponseRedirect('/principal/')
            except Ejercicio.DoesNotExist:
                #va a dirigir a un ejercicio visial por defecto
                num = random.randint(1,3)
                return render(request,'Ejercicios/%s-%s-%d.html'%(clave, "V", num),{'color':color, 'color2':color2})                
        except Aprendizaje.DoesNotExist:
            return HttpResponseRedirect('/principal/')  

    return HttpResponseRedirect('/principal/')    

#para evaluar ejercicios kinestésicos
def evaluarK(request, clave, subtema, tipo, numero):
    if 'member_id' in request.session:
        errores = []
        nombre_ejercicio = clave +"-"+str(tipo)+"-"+str(numero)
        nusu = Usuario.objects.get(id = request.session['member_id'])
        usu = getattr(nusu,'NombreUsuario')
        if clave == "E1":
            color = "tema-uno"
            color2 ="j1"
            tema = 1
        if clave == "E2":
            color = "tema-dos"
            color2 ="j2"
            tema = 2
        if clave == "E3":
            color = "tema-tres"
            color2 ="j3"            
            tema = 3
        if clave == "E4":
            color = "tema-cuatro"
            color2 ="j4"
            tema = 4
        if clave == "E5":
            color = "tema-cinco"
            color2 ="j5"
            tema = 5   
        try: 
            Ejercicio.objects.get(Nombre = nombre_ejercicio ,IdUsuario_id = request.session['member_id'])
            errores.append('Continue con el siguiente ejercicio')
            return render(request, 'respuestas.html',{'errores':errores, 'tema':clave,'color':color,'color2':color2,'nusuario':usu})
        except Ejercicio.DoesNotExist:        
        
            if request.method == 'POST':
                if  not request.POST.get('calificacion',''):
                    errores.append('No se puede evaluar: Contesta todas las preguntas por favor')
                    return render(request, 'respuestas.html',{'errores':errores, 'tema':clave,'color':color,'color2':color2,'nusuario':usu})
                else:
                    calificacion = int(request.POST['calificacion'])
                    if calificacion >= 70:
                        ################ hacer una consulta para traer el id del subtema, con ayuda de los parámetros subtema y tema
                        ######## Subtemas.objects.get(IdTem_id = tema, Numero = subtema)
                        try:
                            subT = SubTemas.objects.get(IdTemas_id = tema, Numero = subtema)
                        except SubTemas.DoesNotExist:
                            errores.append('El subtema no existe')
                        Nsubtema = getattr(subT,'Numero')
                        insertar = Ejercicio(Nombre = clave+'-'+tipo+'-'+str(numero), Tipo = tipo,
                        Evaluacion = round(calificacion),  Fecha = datetime.now(), 
                        IdSubtema_id = Nsubtema, IdUsuario_id = request.session['member_id'], IdTem = tema)
                        insertar.save()
                        errores.append('Tu calificación fue de: '+str(calificacion))
                    else:
                        errores.append('No aprobaste el ejercicio, tu calificación fue de: '+str(calificacion))
            return render(request, 'respuestas.html',{'errores':errores, 'tema':clave, 't':tema, 'sub':subtema,'color':color,'color2':color2,'nusuario':usu})
    else:
        return HttpResponseRedirect('/principal/')

#evaluar para los que no son kinestésicos
def evaluar(request, clave, subtema, tipo, numero):
    if 'member_id' in request.session:
        errores = []
        nombre_ejercicio = clave +"-"+str(tipo)+"-"+str(numero) 
        nusu = Usuario.objects.get(id = request.session['member_id'])
        usu = getattr(nusu,'NombreUsuario')
        if clave == "E1":
            color = "tema-uno"
            color2 ="j1"
            tema = 1
        if clave == "E2":
            color = "tema-dos"
            color2 ="j2"
            tema = 2
        if clave == "E3":
            color = "tema-tres"
            color2 ="j3"            
            tema = 3
        if clave == "E4":
            color = "tema-cuatro"
            color2 ="j4"
            tema = 4
        if clave == "E5":
            color = "tema-cinco"
            color2 ="j5"
            tema = 5 
        try: 
            ##necesito el subtema
            Ejercicio.objects.get(Nombre = nombre_ejercicio , IdUsuario_id = request.session['member_id'])
            errores.append('Continue con el siguiente ejercicio')            
                
            return render(request, 'respuestas.html',{'errores':errores, 'tema':clave, 't':tema, 'sub':subtema,'color':color,'color2':color2,'nusuario':usu})
        except Ejercicio.DoesNotExist:            
            if request.method == 'POST':

                respuestas = []
                contador = 1
                
                while True:
                    cont = str(contador)
                    if not request.POST.get('respuesta'+cont,''):
                        break
                    if request.POST['respuesta'+cont]:
                        respuestas.append(request.POST['respuesta'+cont])
                        contador +=1
                    else:
                        break
                tamaño = contador-1
                calificacion = 0

                # por si el usuario no contesta todo
                if tamaño >= 5:
                    cal_por_respuesta = 100 / tamaño

                else:
                    errores.append('No se puede evaluar: Contesta todas las preguntas por favor')
                    return render(request, 'respuestas.html',{'errores':errores, 'tema':clave, 't':tema, 'sub':subtema, 'color':color,'color2':color2,'nusuario':usu})
                    
                cal_por_respuesta = 100 / tamaño
                #sacar la info de los ejercicios resueltos
                try:
                    subT = SubTemas.objects.get(IdTemas_id = tema, Numero = subtema)
                    Nsubtema = getattr(subT,'id')
                    respuestasBD = EjercicioR.objects.get(IdTem_id = tema, IdSub_id = Nsubtema, Tipo = tipo, NEjer = numero)
                    contador = 1
                    for resp in respuestas:
                        cont = str(contador)
                        solucion = getattr(respuestasBD, 'RP'+cont)
                        if solucion == resp:
                            calificacion = calificacion + cal_por_respuesta
                       # else:
                         #   errores.append(request.POST.get('pregunta1'))
                        contador += 1
                
                    if calificacion >= 70:
                        if tamaño < 6:
                            respuestas.append('-')

                        insertar = Ejercicio(Nombre = clave+'-'+tipo+'-'+str(numero), Tipo = tipo,
                        Evaluacion = round(calificacion),  Fecha = datetime.now(), R1 = respuestas[0], R2 = respuestas[1],
                        R3 = respuestas[2], R4 = respuestas[3], R5 = respuestas[4], R6 = respuestas[5],
                        IdSubtema_id = Nsubtema, IdUsuario_id = request.session['member_id'], IdTem = tema)
                        insertar.save()
                        errores.append('Tu calificación fue de: '+str(calificacion))
                    else:
                        errores.append('No aprobaste el ejercicio, tu calificación fue de: '+str(calificacion))

                except EjercicioR.DoesNotExist:
                    errores.append("No se encontró el ejercicio")
            return render(request, 'respuestas.html',{'errores':errores, 'tema':clave, 't':tema, 'sub':subtema,'color':color,'color2':color2,'nusuario':usu})

    else:
        return HttpResponseRedirect('/principal/')

def ultimaConexion(request):
    if 'member_id' in request.session:
        try:
            datos = Usuario.objects.get(id = request.session['member_id'])
            nivel = getattr(datos, 'Nivel')
            progreso = getattr(datos, 'Progreso')
            usu = getattr(datos, 'NombreUsuario')
            evaluacion = ['E1','E2','E3', 'E4', 'E5']
            if nivel == "E1" or nivel == "1":
                color = "tema-uno"
                color2 ="j1"
            if nivel == "E2" or nivel == "2":
                color = "tema-dos"
                color2 ="j2"
            if nivel == "E3" or nivel == "3":
                color = "tema-tres"
                color2 ="j3"            
            if nivel == "E4" or nivel == "4":
                color = "tema-cuatro"
                color2 ="j4"
            if nivel == "E5" or nivel == "5":
                color = "tema-cinco"
                color2 ="j5"            
            if nivel in evaluacion:
                return HttpResponseRedirect('/ejercicio/'+nivel)
            else: 

                return render(request, 'Temas/%s-%s-1.html'%(nivel, progreso),{'color':color,'color2':color2,'nusuario':usu})
        except Usuario.DoesNotExist:
            return HttpResponseRedirect('/principal/')
    else:
        return HttpResponseRedirect('/principal/')

def perfil (request):
    if 'member_id' in request.session:
        try:
            datos = Usuario.objects.get(id = request.session['member_id'])
            nombreU = getattr(datos, 'NombreUsuario')
            fotoP = getattr(datos, 'Foto')
            nombre = getattr(datos, 'Nombre')
            apellidoP = getattr(datos, 'ApellidoPaterno')
            apellidoM = getattr(datos, 'ApellidoMaterno')
            email = getattr(datos, 'Email')
            fechaNac = getattr(datos, 'FechaNacimiento')
            nivel = getattr(datos, 'Nivel')
            progreso = getattr(datos, 'Progreso')
            idTec = getattr(datos, 'IdTecnologico_id')
            datosTec = Tecnologico.objects.get(id = idTec)
            nombreTec = getattr(datosTec, 'Nombre')
            clave = getattr(datosTec,'ClavePlantel')
            #sacar las respuestas de los ejercicios resueltos
            ejercicios = Ejercicio.objects.filter(IdUsuario_id = request.session['member_id'])
            #para saber el estado en que se encuentran los temas, es decir, si ya acabó sus ejercicios de cada tema
            resueltos_T = []
            avance = []
            resueltos_T.append(Ejercicio.objects.filter(IdTem = 1, IdUsuario_id = request.session['member_id']).count())
            resueltos_T.append(Ejercicio.objects.filter(IdTem = 2, IdUsuario_id = request.session['member_id']).count())
            resueltos_T.append(Ejercicio.objects.filter(IdTem = 3, IdUsuario_id = request.session['member_id']).count())
            resueltos_T.append(Ejercicio.objects.filter(IdTem = 4, IdUsuario_id = request.session['member_id']).count())
            resueltos_T.append(Ejercicio.objects.filter(IdTem = 5, IdUsuario_id = request.session['member_id']).count())
            apren = Aprendizaje.objects.get(IdUsuario_id = request.session['member_id'])
            Visual = getattr(apren, 'Visual')
            Auditivo = getattr(apren,'Auditivo')
            Kinestesico = getattr(apren, 'Kinestesico')
            for T in resueltos_T:
                if T > 0:
                    porcentaje = T*100/5
                    if T >= 5:
                        avance.append(str(porcentaje)+'% Tema Completo')
                    else:
                        avance.append(str(porcentaje)+'% Tema Incompleto')
                else:
                    avance.append('Tema Incompleto')


            return render(request,'perfil.html',{'nombreU':nombreU, 'nombre': nombre, 'apellidoP':apellidoP, 'apellidoM':apellidoM,'email':email,'fechaNac':fechaNac, 'tec':nombreTec, 'clave':clave,
            'nivel':nivel,'progreso':progreso, 'ejercicios':ejercicios, 'resueltos_T':resueltos_T, 'avance':avance,'Visual':Visual, 'Auditivo':Auditivo, 'Kinestesico':Kinestesico,'fotoP':fotoP})
        
        except Usuario.DoesNotExist:
            return render(request,'perfil.html',{'nombre':'El usuario no existe'})
    else:
        return HttpResponseRedirect('/principal/')   
#vista para modificar
def fotoPerfil(request):
    if 'member_id' in request.session:
        datos = Usuario.objects.get(id= request.session['member_id'])
        datosTec = Tecnologico.objects.get(id = datos.IdTecnologico_id)
        if request.POST:
            errores = []
            nuevosDatos = Usuario.objects.get(id= request.session['member_id'])
            if request.POST['Nombre']:
                nuevosDatos.Nombre = request.POST['Nombre']
            if request.POST['Password'] and request.POST['PassAct'] and request.POST['Password2']:
                if (request.POST['PassAct'] == nuevosDatos.Password) and (request.POST ['Password2'] == request.POST['Password']):
                    nuevosDatos.Password = request.POST['Password']
                else:
                    errores.append('Las contraseñas ingresadas no coinciden o la contraseña actual no es correcta.')
            if request.POST['ApellidoP']:
                nuevosDatos.ApellidoPaterno = request.POST['ApellidoP']
            if request.POST['ApellidoM']:
                nuevosDatos.ApellidoMaterno = request.POST['ApellidoM']
            if request.POST['NUsuario'] and datos.NombreUsuario != request.POST['NUsuario'] :
                try:
                    Usuario.objects.get(NombreUsuario=request.POST['NUsuario'])
                    errores.append('El nombre de usuario ya existe')
                except Usuario.DoesNotExist:
                    nuevosDatos.NombreUsuario = request.POST['NUsuario']
            if request.POST['Email']:
                nuevosDatos.Email = request.POST['Email']
            if request.POST['Year']:
                nuevosDatos.FechaNacimiento = request.POST['Year']
           
            if request.FILES.get('foto'):
                nuevosDatos.Foto = request.FILES['foto']
           
            

            if not errores:
                nuevosDatos.save()
                return HttpResponseRedirect('/perfil/')
            else:
                return render(request, 'modificar.html', {'datos':datos, 'datosTec':datosTec,'errores':errores})
        else:
            #datos = Usuario.objects.get(id= request.session['member_id'])
            #datosTec = Tecnologico.objects.get(id = datos.IdTecnologico_id)
            return render(request, 'modificar.html', {'datos':datos, 'datosTec':datosTec})
            #retornar los errores
        return HttpResponseRedirect('/perfil/')
    return HttpResponseRedirect('/principal/')