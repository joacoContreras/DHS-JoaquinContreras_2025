# Arquitectura Modular del Compilador

## 📋 Descripción

El listener `Escucha.py` ha sido refactorizado en una arquitectura modular que separa las responsabilidades en módulos independientes y reutilizables.

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────┐
│                    App.py                            │
│              (Aplicación Principal)                  │
└──────────────────┬──────────────────────────────────┘
                   │
         ┌─────────▼─────────┐
         │    Escucha.py     │
         │   (Coordinador)   │
         └─┬──┬──┬──┬────────┘
           │  │  │  │
     ┌─────┘  │  │  └─────┐
     │        │  │        │
┌────▼───┐ ┌──▼──▼───┐ ┌──▼───────────┐
│ Error  │ │Semantic │ │SymbolTable   │
│Manager │ │Validator│ │Manager       │
└────────┘ └─────────┘ └──────────────┘
                       
     ┌──────────────┐
     │    Stats     │
     │  Collector   │
     └──────────────┘
```

## 📦 Módulos

### 1. **ErrorManager.py** - Gestión de Errores
**Responsabilidad:** Centralizar el manejo de todos los errores (sintácticos y semánticos).

**Características:**
- Patrón Singleton para instancia única
- Listas separadas para errores sintácticos y semánticos
- Generación de reportes formateados
- Métodos de consulta de estado

**Uso:**
```python
from ErrorManager import ErrorManager

error_mgr = ErrorManager.getInstance()
error_mgr.reportar_error_semantico(10, "Variable no declarada")
if error_mgr.tiene_errores():
    error_mgr.generar_reporte()
```

### 2. **SemanticValidator.py** - Validaciones Semánticas
**Responsabilidad:** Realizar todas las validaciones semánticas del código.

**Características:**
- Validación de variables declaradas
- Validación de inicialización
- Validación de compatibilidad de tipos
- Inferencia de tipos
- Detección de doble declaración
- Detección de variables no usadas

**Uso:**
```python
from SemanticValidator import SemanticValidator

validator = SemanticValidator(error_manager)
simbolo = validator.validar_variable_declarada("x", 10, tabla_simbolos)
validator.validar_tipo_compatible("int", "double", 10)
```

### 3. **SymbolTableManager.py** - Gestión de Tabla de Símbolos
**Responsabilidad:** Proporcionar una capa de abstracción sobre la tabla de símbolos.

**Características:**
- Agregar/eliminar contextos (scopes)
- Agregar variables y funciones
- Búsqueda de símbolos
- Marcar variables como usadas/inicializadas
- Consultas sobre la tabla

**Uso:**
```python
from SymbolTableManager import SymbolTableManager

sym_mgr = SymbolTableManager()
sym_mgr.agregar_contexto()
sym_mgr.agregar_variable("x", "int", 10, inicializado=True)
simbolo = sym_mgr.buscar_simbolo("x")
sym_mgr.eliminar_contexto()
```

### 4. **StatsCollector.py** - Recolección de Estadísticas
**Responsabilidad:** Recolectar estadísticas del código analizado.

**Características:**
- Contadores para todas las estructuras
- Generación de reportes de estadísticas
- Métodos de consulta
- Resumen en formato dict

**Uso:**
```python
from StatsCollector import StatsCollector

stats = StatsCollector()
stats.incrementar_declaraciones()
stats.incrementar_whiles()
stats.generar_reporte()
print(stats)  # Muestra resumen
```

### 5. **Escucha.py** - Coordinador Principal
**Responsabilidad:** Coordinar entre todos los módulos durante el recorrido del árbol sintáctico.

**Características:**
- Implementa el patrón Listener de ANTLR
- Delega responsabilidades a los módulos especializados
- Mantiene el estado del recorrido (indent, profundidad)
- Código limpio y mantenible

**Uso:**
```python
from Escucha import Escucha

escucha = Escucha()
# Los componentes se inicializan automáticamente:
# - escucha.error_manager
# - escucha.validator
# - escucha.symbol_manager
# - escucha.stats
```

## 🎯 Ventajas de la Arquitectura Modular

### ✅ Separación de Responsabilidades
Cada módulo tiene una única responsabilidad bien definida.

### ✅ Reutilización
Los módulos pueden usarse independientemente en otros proyectos.

### ✅ Testabilidad
Cada módulo puede probarse de forma aislada con pruebas unitarias.

### ✅ Mantenibilidad
Los cambios en una funcionalidad están contenidos en su módulo.

### ✅ Escalabilidad
Fácil agregar nuevas funcionalidades sin modificar código existente.

### ✅ Legibilidad
El código es más claro y autodocumentado.

## 📊 Comparación de Líneas de Código

| Archivo | Antes | Después | Reducción |
|---------|-------|---------|-----------|
| Escucha.py | ~365 líneas | ~236 líneas | -35% |

**Nota:** La funcionalidad se mantuvo completa, pero ahora está mejor organizada.

## 🔄 Flujo de Ejecución

1. **App.py** crea una instancia de `Escucha`
2. **Escucha** inicializa todos sus componentes modulares
3. Durante el recorrido del árbol:
   - **Escucha** detecta eventos (enter/exit de nodos)
   - **Validator** realiza validaciones semánticas
   - **SymbolTableManager** gestiona la tabla de símbolos
   - **ErrorManager** registra errores encontrados
   - **StatsCollector** cuenta estructuras
4. Al finalizar:
   - **Validator** verifica variables no usadas
   - **ErrorManager** genera reporte de errores
   - **StatsCollector** muestra estadísticas

## 🛠️ Extensibilidad

### Agregar nueva validación semántica:
1. Agregar método en `SemanticValidator.py`
2. Llamar desde el método apropiado en `Escucha.py`

### Agregar nueva estadística:
1. Agregar contador y método en `StatsCollector.py`
2. Incrementar desde el método apropiado en `Escucha.py`

### Agregar nuevo tipo de error:
1. Agregar método en `ErrorManager.py`
2. Usar desde `SemanticValidator.py` o `Escucha.py`

## 📝 Ejemplo de Uso Completo

```python
# App.py
from Escucha import Escucha
from ErrorManager import ErrorManager

# Crear escucha
escucha = Escucha()

# Parsear y recorrer árbol
tree = parser.programa()
walker.walk(escucha, tree)

# Verificar resultados
if not escucha.error_manager.tiene_errores():
    print("✓ Compilación exitosa")
    print(escucha.stats)
else:
    print("✗ Se encontraron errores")
    escucha.error_manager.generar_reporte()
```

## 🎓 Principios de Diseño Aplicados

- **Single Responsibility Principle (SRP)**: Cada módulo tiene una sola razón para cambiar
- **Open/Closed Principle (OCP)**: Abierto a extensión, cerrado a modificación
- **Dependency Inversion (DIP)**: Dependencias a través de interfaces/abstracciones
- **Don't Repeat Yourself (DRY)**: Lógica común centralizada
- **Separation of Concerns (SoC)**: Separación clara de responsabilidades

---

**Autor:** Refactorización modular del compilador  
**Fecha:** Enero 2026  
**Versión:** 2.0
