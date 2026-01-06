#  EJEMPLO EXPLICADO: Generación de Código de Tres Direcciones

## Código Fuente Original

```c
int x;
int y;
int z;

x = 5;
y = 10;
z = x + y * 2;

while (x < 100) {
    x = x + 1;
}

if (z > 20) {
    z = z - 5;
} else {
    z = z + 10;
}
```

---

## Código de Tres Direcciones Generado

```
# === INICIO DEL PROGRAMA ===
DECLARE x
DECLARE y
DECLARE z
x = 5
y = 10
t0 = y * 2              ← temporal para y * 2
t1 = x + t0             ← temporal para x + (y * 2)
z = t1                  ← asignación final a z

L0:                     ← inicio del bucle while
  t2 = x < 100          ← evaluar condición
  if not t2 goto L1     ← si es falsa, salir del while
  t3 = x + 1            ← calcular x + 1
  x = t3                ← asignar nuevo valor a x
  goto L0               ← volver al inicio del while
L1:                     ← fin del while

t4 = z > 20             ← evaluar condición del if
if not t4 goto L2       ← si es falsa, ir al else
  t5 = z - 5            ← bloque del if
  z = t5
  goto L3               ← saltar después del else
L2:                     ← inicio del else
  t6 = z + 10           ← bloque del else
  z = t6
L3:                     ← fin del if-else

# === FIN DEL PROGRAMA ===
```

---

## 📝 Análisis Detallado

### 1. Declaraciones (líneas 1-3)
```
DECLARE x
DECLARE y
DECLARE z
```
**Explicación**: Reserva espacio para las 3 variables enteras.

---

### 2. Asignaciones Simples (líneas 4-5)
```
x = 5
y = 10
```
**Explicación**: Asignación directa de valores constantes.

---

### 3. Expresión Compleja (línea 6-8)
**Código fuente:**
```c
z = x + y * 2;
```

**TAC generado:**
```
t0 = y * 2    // Paso 1: Multiplicación (mayor precedencia)
t1 = x + t0   // Paso 2: Suma
z = t1        // Paso 3: Asignación final
```

**Explicación**: La expresión se descompone respetando la precedencia de operadores:
1. Primero se calcula `y * 2` (multiplicación tiene prioridad)
2. Resultado se guarda en temporal `t0`
3. Luego se suma `x + t0`
4. Resultado se guarda en `t1`
5. Finalmente `z` recibe el valor de `t1`

---

### 4. Bucle While (líneas 9-13)
**Código fuente:**
```c
while (x < 100) {
    x = x + 1;
}
```

**TAC generado:**
```
L0:                    // Etiqueta de inicio del bucle
  t2 = x < 100         // Evaluar la condición
  if not t2 goto L1    // Si condición es FALSA, salir del bucle
  t3 = x + 1           // Cuerpo del while: calcular x + 1
  x = t3               // Asignar el nuevo valor
  goto L0              // Volver al inicio del bucle
L1:                    // Etiqueta de salida del bucle
```

**Flujo de ejecución:**
```
     ┌─────────┐
     │   L0    │ ← Inicio del bucle
     └────┬────┘
          │
          ▼
    ┌──────────────┐
    │ t2 = x < 100 │ Evaluar condición
    └──────┬───────┘
           │
      ┌────┴────┐
      │         │
     t2?       no → L1 (salir)
      │
     sí
      │
      ▼
  ┌─────────┐
  │ x = x+1 │ Cuerpo del bucle
  └────┬────┘
       │
       ▼
   goto L0  ← Repetir
```

---

### 5. Condicional If-Else (líneas 14-20)
**Código fuente:**
```c
if (z > 20) {
    z = z - 5;
} else {
    z = z + 10;
}
```

**TAC generado:**
```
t4 = z > 20           // Evaluar condición
if not t4 goto L2     // Si FALSA, ir al else (L2)
  t5 = z - 5          // Bloque IF: ejecutado si condición es VERDADERA
  z = t5
  goto L3             // Saltar el else
L2:                   // Inicio del ELSE
  t6 = z + 10         // Bloque ELSE: ejecutado si condición es FALSA
  z = t6
L3:                   // Fin del if-else
```

**Flujo de ejecución:**
```
        ┌──────────┐
        │t4 = z>20 │
        └─────┬────┘
              │
         ┌────┴────┐
        t4?        no → L2 (else)
         │              │
        sí              ▼
         │         ┌─────────┐
         ▼         │ z=z+10  │
    ┌────────┐     └────┬────┘
    │ z=z-5  │          │
    └────┬───┘          │
         │              │
         ▼              │
      goto L3           │
         │              │
         └──────┬───────┘
                ▼
               L3
```

---

## 🔑 Conceptos Clave

### Variables Temporales
- **Nombre**: `t0`, `t1`, `t2`, `t3`, ...
- **Propósito**: Almacenar resultados intermedios
- **Generación**: Automática por el compilador
- **Vida útil**: Solo necesaria durante el cálculo

### Etiquetas
- **Nombre**: `L0`, `L1`, `L2`, `L3`, ...
- **Propósito**: Marcar puntos de destino para saltos
- **Usos**:
  - Inicio de bucles
  - Fin de bucles
  - Bloques else
  - Fin de condicionales

### Tipos de Instrucciones TAC

1. **Asignación Simple**: `x = 5`
2. **Operación Binaria**: `t0 = a + b`
3. **Salto Condicional**: `if condicion goto L`
4. **Salto Incondicional**: `goto L`
5. **Etiquetas**: `L0:`
6. **Declaración**: `DECLARE var`

---

## 💡 Ventajas de TAC

### 1. Simplicidad
Cada instrucción hace UNA sola cosa, es fácil de entender y traducir.

### 2. Optimización
Es más fácil optimizar código simple:
```
# Antes de optimizar:
t0 = 5
t1 = 3
t2 = t0 + t1
x = t2

# Después de optimizar:
x = 8            # ¡Calculado en tiempo de compilación!
```

### 3. Independencia de Máquina
TAC no depende de:
- Cantidad de registros del procesador
- Conjunto de instrucciones específico
- Arquitectura (32/64 bits)

### 4. Base para Código Máquina
Traducir TAC a ensamblador es directo:
```
TAC:              ARM Assembly:
t0 = x + y    →   LDR R0, [x]
                  LDR R1, [y]
                  ADD R2, R0, R1
                  STR R2, [t0]
```

---

## 🎓 Ejercicios para Practicar

### Ejercicio 1: Expresión Compleja
Convierte manualmente a TAC:
```c
resultado = (a + b) * (c - d) / e;
```

<details>
<summary>Ver solución</summary>

```
t0 = a + b
t1 = c - d
t2 = t0 * t1
t3 = t2 / e
resultado = t3
```
</details>

### Ejercicio 2: Bucle For
```c
for (int i = 0; i < 10; i = i + 1) {
    suma = suma + i;
}
```

<details>
<summary>Ver solución</summary>

```
i = 0
L0:
  t0 = i < 10
  if not t0 goto L1
  t1 = suma + i
  suma = t1
  t2 = i + 1
  i = t2
  goto L0
L1:
```
</details>

### Ejercicio 3: If-Else If-Else
```c
if (x > 10) {
    y = 1;
} else if (x > 5) {
    y = 2;
} else {
    y = 3;
}
```

<details>
<summary>Ver solución</summary>

```
t0 = x > 10
if not t0 goto L0
y = 1
goto L2
L0:
  t1 = x > 5
  if not t1 goto L1
  y = 2
  goto L2
L1:
  y = 3
L2:
```
</details>

---

## 📚 Siguientes Pasos

1. **Optimización**: Eliminar temporales innecesarios
2. **Asignación de registros**: Mapear temporales a registros reales
3. **Generación de código máquina**: Convertir TAC a ensamblador
4. **Análisis de flujo**: Detectar código muerto o inalcanzable

---

## 🔗 Recursos Adicionales

- **Dragon Book** (Compilers: Principles, Techniques, and Tools) - Capítulo 6
- **Engineering a Compiler** - Cooper & Torczon - Capítulo 5
- **Modern Compiler Implementation** - Appel - Capítulo 7

---

¡Felicidades! 🎉 Ahora entiendes cómo funciona la generación de código intermedio con Three Address Code.
