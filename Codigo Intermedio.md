# Codigo Intermedio

Lenguaje independiente del lenguaje de programacion utilizado y de la arquitectura de computadora a utilizar

Codigo de tres direcciones:
    x = y <op> z

    X = variable donde asigno la operacion entre 2 variables mas
    
similar a assembler:
        
    mov ax, bx
    add ax, bx, cx


Tiene que tener si o si:

    x = y <op> z (operaciones)
    x = y (asignacion)
    jmp x (saltos)
    label x  (etiquetas)
    ifnjmp x <op> y, z (si es falso, salta)
    push x
    pop x

Necesito:
* Un generador de nombres de variables temporales
* Un generador de nombre de etiquetas

--------------------
x = 0
x = 2 + y

x = 3 * y + ( 5 * z ) / 2

t0 = 3 * y
t1 = 5 * z
t2 = t1 / 2
t3 = t0 + t2
x = t3

--------------------
if (x > 0)
    y = z * 2
else 
    y = z / 2


t0 = x > 0
ifnjmp t0, l0
t1 = z * 2
y = t1
jmp l1
label l0
t2 = z / 2
y = t2
label l1

--------------------
for (i = 0; i < x; i = i + 1)
    y = z * x;
    

i = 0
label l0
t0 = i < X
ifnjmp t0, l1
t1 = z * X
y = t1
t2 = i + 1
i = t2
jmp l0
label l1

--------------------
int f (int a, int b){
    return a + b;
}
<...>
    x = f(o, p)
<...>

label l0
pop t0
pop b
pop a
t1 = a + b
push t1
jmp t0
<...>
push o
push p
push l1
jmp l0
label l1
pop x