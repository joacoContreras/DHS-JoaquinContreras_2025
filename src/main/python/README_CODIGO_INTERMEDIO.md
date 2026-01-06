# Generación de Código Intermedio - Código de Tres Direcciones (TAC)

##  ¿Qué es el Código de Tres Direcciones?

El **código de tres direcciones** es una representación intermedia en el proceso de compilación que se encuentra entre el código fuente de alto nivel y el código máquina. 

### Características principales:
- **Como máximo 3 operandos** por instrucción (dos fuentes, un destino)
- **Un operador** por instrucción
- Usa **variables temporales** para almacenar resultados intermedios
- Usa **etiquetas** para control de flujo (saltos, bucles, condicionales)

### ¿Por qué es útil?

1. **Simplifica las expresiones complejas**: Divide expresiones en pasos más pequeños
2. **Facilita la optimización**: Es más fácil optimizar instrucciones simples
3. **Independiente de la máquina**: No depende de la arquitectura específica
4. **Base para generar código máquina**: Traducir TAC a ensamblador es más sencillo

---

## 🔄 Ejemplos de Transformación

### Ejemplo 1: Expresión Aritmética Simple
```c
z = x + y * 2;
```

**Código TAC generado:**
```
t0 = y * 2
t1 = x + t0
z = t1
```

**Explicación:**
1. Primero se calcula `y * 2` y se guarda en temporal `t0`
2. Luego se suma `x + t0` y se guarda en `t1`
3. Finalmente se asigna `t1` a `z`

---

### Ejemplo 2: Expresión Compleja
```c
resultado = (a + b) * (c - d);
```

**Código TAC generado:**
```
t0 = a + b
t1 = c - d
t2 = t0 * t1
resultado = t2
```

---

### Ejemplo 3: Bucle While
```c
while (x < 10) {
    x = x + 1;
}
```

**Código TAC generado:**
```
L0:
  t0 = x < 10
  if not t0 goto L1
  t1 = x + 1
  x = t1
  goto L0
L1:
```

**Explicación:**
- `L0` es la etiqueta de inicio del bucle
- Se evalúa la condición `x < 10`
- Si es falsa (`if not t0`), salta a `L1` (fin del bucle)
- Si es verdadera, ejecuta el cuerpo
- `goto L0` regresa al inicio del bucle
- `L1` marca el fin del bucle

---

### Ejemplo 4: Condicional If-Else
```c
if (a > b) {
    max = a;
} else {
    max = b;
}
```

**Código TAC generado:**
```
t0 = a > b
if not t0 goto L0
max = a
goto L1
L0:
  max = b
L1:
```

**Explicación:**
- Se evalúa la condición `a > b`
- Si es falsa, salta a `L0` (else)
- Si es verdadera, ejecuta `max = a` y salta a `L1` (fin)
- En `L0` se ejecuta el else
- `L1` es el punto de continuación

---

### Ejemplo 5: Bucle For
```c
for (int i = 0; i < 5; i = i + 1) {
    suma = suma + i;
}
```

**Código TAC generado:**
```
DECLARE i
i = 0
L0:
  t0 = i < 5
  if not t0 goto L1
  t1 = suma + i
  suma = t1
  t2 = i + 1
  i = t2
  goto L0
L1:
```

---

##  Componentes del Generador

### 1. Variables Temporales
- Se generan automáticamente con nombres `t0, t1, t2, ...`
- Almacenan resultados intermedios
- Generadas por `nuevo_temporal()`

### 2. Etiquetas
- Se generan con nombres `L0, L1, L2, ...`
- Marcan puntos en el código para saltos
- Usadas en bucles y condicionales
- Generadas por `nueva_etiqueta()`

### 3. Instrucciones TAC

#### Asignación Simple
```
x = y
```

#### Operación Binaria
```
t0 = x + y
t1 = a * b
t2 = c / d
```

#### Saltos Condicionales
```
if condicion goto Letiqueta
if not condicion goto Letiqueta
```

#### Saltos Incondicionales
```
goto Letiqueta
```

---

##  Cómo Usar el Generador

### En tu código Python:

```python
from IntermediateCodeGenerator import IntermediateCodeGenerator

# Después de parsear
tree = parser.programa()

# Crear el generador
generador = IntermediateCodeGenerator()

# Visitar el árbol
generador.visit(tree)

# Obtener el código generado
codigo_tac = generador.obtener_codigo()
print(codigo_tac)
```

### Ejecutar con un archivo:

```bash
python src/main/python/App.py input/ejemplo_tac.txt
```

---

## Estructura del Generador

```
IntermediateCodeGenerator
│
├── Atributos
│   ├── codigo[]           # Lista de instrucciones generadas
│   ├── temp_counter       # Contador de temporales
│   └── label_counter      # Contador de etiquetas
│
├── Métodos Auxiliares
│   ├── nuevo_temporal()   # Genera t0, t1, t2, ...
│   ├── nueva_etiqueta()   # Genera L0, L1, L2, ...
│   ├── emitir()           # Agrega instrucción al código
│   └── obtener_codigo()   # Retorna todo el código
│
└── Visitadores (por tipo de nodo)
    ├── visitExpresion()   # Expresiones
    ├── visitAsignacion()  # x = y
    ├── visitIwhile()      # Bucles while
    ├── visitIfor()        # Bucles for
    ├── visitIif()         # Condicionales
    └── visitCond()        # Condiciones
```

---

## 🧪 Pruebas

### Probar con diferentes archivos:

1. **Expresiones simples:**
   ```bash
   python src/main/python/App.py input/test_simple.txt
   ```

2. **Bucles:**
   ```bash
   python src/main/python/App.py input/for.txt
   ```

3. **Programa completo:**
   ```bash
   python src/main/python/App.py input/programa.txt
   ```

4. **Ejemplo de TAC:**
   ```bash
   python src/main/python/App.py input/ejemplo_tac.txt
   ```

---

## 🔍 Orden de Precedencia

El generador respeta la precedencia de operadores:

1. **Paréntesis** `( )`
2. **Multiplicación, División, Módulo** `* / %`
3. **Suma, Resta** `+ -`
4. **Comparaciones** `< > <= >= == !=`

---

## Conceptos Importantes

### ¿Por qué usar temporales?
Los temporales permiten descomponer expresiones complejas:
- Facilitan la evaluación paso a paso
- Permiten reutilizar subexpresiones
- Simplifican la generación de código máquina

### ¿Por qué usar etiquetas?
Las etiquetas permiten implementar control de flujo:
- Marcan destinos de saltos
- Implementan bucles
- Implementan condicionales

### Optimizaciones futuras
- **Eliminación de código muerto**: Quitar código inalcanzable
- **Propagación de constantes**: Calcular valores en tiempo de compilación
- **Reducción de temporales**: Reutilizar temporales cuando sea posible
- **Eliminación de saltos redundantes**: Optimizar etiquetas

---

## 📖 Referencias

- **Dragon Book**: "Compilers: Principles, Techniques, and Tools" - Capítulo 6
- **Tiger Book**: "Modern Compiler Implementation" - Capítulo 7
- **Engineering a Compiler**: Cooper & Torczon - Capítulo 5

---

##  Checklist de Aprendizaje

- [ ] Entiendo qué es el código de tres direcciones
- [ ] Puedo convertir manualmente una expresión a TAC
- [ ] Entiendo cómo funcionan las variables temporales
- [ ] Entiendo el uso de etiquetas en control de flujo
- [ ] Puedo leer y entender el TAC generado
- [ ] Puedo extender el generador para nuevas construcciones

---

## 🚀 Próximos Pasos

1. **Generar código ensamblador**: Traducir TAC a instrucciones de máquina
2. **Optimización de código**: Mejorar el TAC generado
3. **Análisis de flujo de datos**: Para optimizaciones avanzadas
4. **Asignación de registros**: Mapear temporales a registros reales

