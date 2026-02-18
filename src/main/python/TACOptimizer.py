"""
Optimizador de Código de Tres Direcciones

Implementa varias pasadas de optimización sobre el código intermedio
generado, incluyendo:
  1. Propagación de copias
  2. Plegado de constantes 
  3. Eliminación de código muerto / variables redundantes 

Cada optimización se aplica de forma independiente y secuencial.
El resultado es un TAC más eficiente que produce el mismo resultado.
"""

import re


class TACOptimizer:
    """
    Optimizador de código de tres direcciones.
    
    Recibe el código TAC como string, lo parsea en instrucciones
    individuales, aplica optimizaciones y genera el código optimizado.
    """
    
    def __init__(self, codigo_tac: str):
        """
        Inicializa el optimizador con el código TAC original.
        
        
        codigo_tac: String con el código TAC (líneas separadas por \\n)
        """
        self.lineas_originales = codigo_tac.strip().split('\n')
        self.lineas = list(self.lineas_originales)  # Copia de trabajo
        self.cambios_realizados = []  # Log de optimizaciones aplicadas
    
    # ================================================================
    # PLEGADO DE CONSTANTES
    # ================================================================
    def _constant_folding(self):
        """
        Evalúa en tiempo de compilación las operaciones entre constantes.
        
        Si ambos operandos de una operación aritmética o comparativa son
        literales numéricos, se reemplaza la instrucción por una asignación
        directa del resultado.
        
        Ejemplo:
            t0 = 3 + 5       →   t0 = 8
            t1 = 10 * 2      →   t1 = 20
            t2 = 4 < 10      →   t2 = 1
        """
        nuevas = []
        cambios = 0
        operadores = {'+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!='}
        
        for linea in self.lineas:
            stripped = linea.strip()
            
            # Patrón: var = num op num
            match = re.match(
                r'^(\s*)([\w]+)\s*=\s*(-?\d+)\s*([+\-*/%<>]=?|==|!=)\s*(-?\d+)\s*$',
                linea
            )
            
            if match:
                indent, var, izq_str, op, der_str = match.groups()
                izq = int(izq_str)
                der = int(der_str)
                resultado = None
                
                try:
                    if op == '+':
                        resultado = izq + der
                    elif op == '-':
                        resultado = izq - der
                    elif op == '*':
                        resultado = izq * der
                    elif op == '/' and der != 0:
                        resultado = izq // der  # División entera
                    elif op == '%' and der != 0:
                        resultado = izq % der
                    elif op == '<':
                        resultado = 1 if izq < der else 0
                    elif op == '>':
                        resultado = 1 if izq > der else 0
                    elif op == '<=':
                        resultado = 1 if izq <= der else 0
                    elif op == '>=':
                        resultado = 1 if izq >= der else 0
                    elif op == '==':
                        resultado = 1 if izq == der else 0
                    elif op == '!=':
                        resultado = 1 if izq != der else 0
                except:
                    pass
                
                if resultado is not None:
                    nueva_linea = f"{indent}{var} = {resultado}"
                    nuevas.append(nueva_linea)
                    cambios += 1
                    self.cambios_realizados.append(
                        f"  Constant Folding: '{stripped}' → '{var} = {resultado}'"
                    )
                    continue
            
            nuevas.append(linea)
        
        self.lineas = nuevas
        return cambios
    
    # ================================================================
    # PROPAGACIÓN DE COPIAS
    # ================================================================
    def _copy_propagation(self):
        """
        Cuando se encuentra una asignación simple de la forma:
            t0 = x
        reemplaza todos los usos posteriores de t0 por x directamente,
        siempre que t0 no sea reasignado.
        
        Ejemplo:
            t0 = x              t0 = x
            t1 = t0 + 1    →    t1 = x + 1
            y = t1               y = t1
        
        Solo propaga copias de temporales (tN) hacia identificadores o
        literales para evitar efectos secundarios.
        """
        cambios = 0
        copias = {}  # mapeo: temporal → valor original
        
        # Primera pasada: identificar copias simples
        for linea in self.lineas:
            stripped = linea.strip()
            # Patrón: tN = <identificador_o_literal> (sin operador)
            match = re.match(r'^(\s*)(t\d+)\s*=\s*(\w+)\s*$', linea)
            if match:
                _, temp, valor = match.groups()
                # Solo propagar si el valor NO es otro temporal que podría cambiar
                # o si es un literal/variable simple
                copias[temp] = valor
        
        # Segunda pasada: verificar que los temporales no sean reasignados
        conteo_asig = {}
        for linea in self.lineas:
            stripped = linea.strip()
            match = re.match(r'^(\s*)(t\d+)\s*=', linea)
            if match:
                temp = match.group(2)
                conteo_asig[temp] = conteo_asig.get(temp, 0) + 1
        
        # Solo propagar temporales que se asignan exactamente una vez
        copias_seguras = {k: v for k, v in copias.items() if conteo_asig.get(k, 0) == 1}
        
        # Tercera pasada: reemplazar usos
        if copias_seguras:
            nuevas = []
            for linea in self.lineas:
                nueva_linea = linea
                for temp, valor in copias_seguras.items():
                    # Reemplazar el temporal por su valor en expresiones
                    # Usar word boundary para no reemplazar parcialmente
                    patron = r'\b' + re.escape(temp) + r'\b'
                    # No reemplazar en la línea de definición del temporal
                    stripped = linea.strip()
                    if stripped.startswith(f"{temp} ="):
                        continue
                    nueva = re.sub(patron, valor, nueva_linea)
                    if nueva != nueva_linea:
                        cambios += 1
                        nueva_linea = nueva
                nuevas.append(nueva_linea)
            self.lineas = nuevas
            
            if cambios > 0:
                self.cambios_realizados.append(
                    f"  Copy Propagation: {cambios} usos de temporales reemplazados"
                )
        
        return cambios
    
    # ================================================================
    # ELIMINACIÓN DE CÓDIGO MUERTO 
    # ================================================================
    def _dead_code_elimination(self):
        """
        Elimina instrucciones que definen temporales (tN) que nunca
        son usados en instrucciones posteriores.
        
        Un temporal se considera "muerto" si:
        - Se asigna pero nunca aparece como operando en otra instrucción
        - No es parte de una instrucción de control (if, goto, return, param, call)
        
        Ejemplo:
            t0 = a + b         (eliminada si t0 no se usa)
            t1 = c * d    →    t1 = c * d
            x = t1              x = t1
        """
        cambios = 0
        
        # Identificar todos los temporales definidos y usados
        definidos = {}  # temporal → índice de línea
        usados = set()
        
        # Palabras clave que no deben eliminarse
        no_eliminar = {'if', 'goto', 'return', 'param', 'call', 'FUNC', 'END', 'pop',
                       '#', 'DECLARE'}
        
        for i, linea in enumerate(self.lineas):
            stripped = linea.strip()
            
            # Encontrar definiciones de temporales
            match_def = re.match(r'^\s*(t\d+)\s*=', stripped)
            if match_def:
                definidos[match_def.group(1)] = i
            
            # Encontrar usos de temporales (en el lado DERECHO de asignaciones
            # o en instrucciones de control)
            # Excluir la propia definición
            if '=' in stripped:
                partes = stripped.split('=', 1)
                lado_izq = partes[0].strip()
                lado_der = partes[1].strip() if len(partes) > 1 else ''
                
                # Si el lado izquierdo NO es un temporal, el temporal del
                # lado derecho está siendo usado
                for temp_match in re.finditer(r'\b(t\d+)\b', lado_der):
                    usados.add(temp_match.group(1))
                
                # Si lado izquierdo es una variable real (no temporal),
                # los temporales en lado derecho ya se agregaron
                if not re.match(r'^t\d+$', lado_izq):
                    # Los temporales del lado derecho ya se agregaron arriba
                    pass
                else:
                    # Es un temporal = algo. Los temporales del lado derecho se usan
                    pass
            else:
                # Instrucciones de control: if, goto, return, param
                for temp_match in re.finditer(r'\b(t\d+)\b', stripped):
                    usados.add(temp_match.group(1))
        
        # Eliminar temporales que se definen pero nunca se usan
        indices_eliminar = set()
        for temp, idx in definidos.items():
            if temp not in usados:
                stripped = self.lineas[idx].strip()
                # No eliminar si es parte de instrucción de control
                primera_palabra = stripped.split()[0] if stripped.split() else ''
                if primera_palabra not in no_eliminar and not stripped.endswith(':'):
                    indices_eliminar.add(idx)
                    cambios += 1
                    self.cambios_realizados.append(
                        f"  Dead Code Elimination: eliminada '{stripped}' (temporal no usado)"
                    )
        
        if indices_eliminar:
            self.lineas = [l for i, l in enumerate(self.lineas) if i not in indices_eliminar]
        
        return cambios
    
    # ================================================================
    # ELIMINACIÓN DE ASIGNACIONES REDUNDANTES
    # ================================================================
    def _redundant_assignment_elimination(self):
        """
        Elimina asignaciones redundantes donde una variable se asigna
        a sí misma: x = x
        
        También simplifica patrones como:
            t0 = x + 0   →   t0 = x    (identidad aditiva)
            t0 = x * 1   →   t0 = x    (identidad multiplicativa)
        """
        cambios = 0
        nuevas = []
        
        for linea in self.lineas:
            stripped = linea.strip()
            
            # Patrón: x = x (autoasignación)
            match_self = re.match(r'^(\s*)([\w]+)\s*=\s*([\w]+)\s*$', linea)
            if match_self:
                indent, var, valor = match_self.groups()
                if var == valor:
                    cambios += 1
                    self.cambios_realizados.append(
                        f"  Redundant Assignment: eliminada '{stripped}' (autoasignación)"
                    )
                    continue
            
            # Patrón: var = x + 0 o var = x - 0 (identidad aditiva)
            match_add_zero = re.match(
                r'^(\s*)([\w]+)\s*=\s*([\w]+)\s*[+\-]\s*0\s*$', linea
            )
            if match_add_zero:
                indent, var, operando = match_add_zero.groups()
                nueva_linea = f"{indent}{var} = {operando}"
                nuevas.append(nueva_linea)
                cambios += 1
                self.cambios_realizados.append(
                    f"  Algebraic Simplification: '{stripped}' → '{var} = {operando}'"
                )
                continue
            
            # Patrón: var = x * 1 o var = 1 * x (identidad multiplicativa)
            match_mul_one = re.match(
                r'^(\s*)([\w]+)\s*=\s*([\w]+)\s*\*\s*1\s*$', linea
            )
            if match_mul_one:
                indent, var, operando = match_mul_one.groups()
                nueva_linea = f"{indent}{var} = {operando}"
                nuevas.append(nueva_linea)
                cambios += 1
                self.cambios_realizados.append(
                    f"  Algebraic Simplification: '{stripped}' → '{var} = {operando}'"
                )
                continue
            
            match_one_mul = re.match(
                r'^(\s*)([\w]+)\s*=\s*1\s*\*\s*([\w]+)\s*$', linea
            )
            if match_one_mul:
                indent, var, operando = match_one_mul.groups()
                nueva_linea = f"{indent}{var} = {operando}"
                nuevas.append(nueva_linea)
                cambios += 1
                self.cambios_realizados.append(
                    f"  Algebraic Simplification: '{stripped}' → '{var} = {operando}'"
                )
                continue
            
            # Patrón: var = x * 0 o var = 0 * x → var = 0
            match_mul_zero = re.match(
                r'^(\s*)([\w]+)\s*=\s*([\w]+)\s*\*\s*0\s*$', linea
            )
            if match_mul_zero:
                indent, var, _ = match_mul_zero.groups()
                nueva_linea = f"{indent}{var} = 0"
                nuevas.append(nueva_linea)
                cambios += 1
                self.cambios_realizados.append(
                    f"  Algebraic Simplification: '{stripped}' → '{var} = 0'"
                )
                continue
            
            match_zero_mul = re.match(
                r'^(\s*)([\w]+)\s*=\s*0\s*\*\s*([\w]+)\s*$', linea
            )
            if match_zero_mul:
                indent, var, _ = match_zero_mul.groups()
                nueva_linea = f"{indent}{var} = 0"
                nuevas.append(nueva_linea)
                cambios += 1
                self.cambios_realizados.append(
                    f"  Algebraic Simplification: '{stripped}' → '{var} = 0'"
                )
                continue
            
            nuevas.append(linea)
        
        self.lineas = nuevas
        return cambios
    
    # ================================================================
    # ORQUESTADOR DE OPTIMIZACIONES
    # ================================================================
    def optimizar(self):
        """
        Ejecuta todas las pasadas de optimización en orden.
        Repite hasta que no haya más cambios (punto fijo).
        
        Returns:
            String con el código TAC optimizado
        """
        iteracion = 0
        max_iteraciones = 10  # Evitar bucle infinito
        
        while iteracion < max_iteraciones:
            cambios_totales = 0
            iteracion += 1
            
            # 1. Plegado de constantes
            cambios_totales += self._constant_folding()
            
            # 2. Propagación de copias
            cambios_totales += self._copy_propagation()
            
            # 3. Eliminación de asignaciones redundantes
            cambios_totales += self._redundant_assignment_elimination()
            
            # 4. Eliminación de código muerto
            cambios_totales += self._dead_code_elimination()
            
            # Si no hubo cambios, hemos alcanzado el punto fijo
            if cambios_totales == 0:
                break
        
        return '\n'.join(self.lineas)
    
    def obtener_reporte(self):
        """
        Genera un reporte de las optimizaciones realizadas.
        
        Returns:
            String con el detalle de cada optimización aplicada
        """
        if not self.cambios_realizados:
            return "  No se aplicaron optimizaciones."
        
        reporte = f"  Total de optimizaciones: {len(self.cambios_realizados)}\n"
        for cambio in self.cambios_realizados:
            reporte += f"  {cambio}\n"
        return reporte
    
    def obtener_comparacion(self, codigo_original: str):
        """
        Genera una comparación lado a lado entre el código original
        y el optimizado.
        
        Args:
            codigo_original: El código TAC antes de optimizar
            
        Returns:
            String con la comparación formateada
        """
        lineas_orig = codigo_original.strip().split('\n')
        lineas_opt = self.lineas
        
        resultado = ""
        resultado += f"  Líneas originales:  {len(lineas_orig)}\n"
        resultado += f"  Líneas optimizadas: {len(lineas_opt)}\n"
        resultado += f"  Líneas eliminadas:  {len(lineas_orig) - len(lineas_opt)}\n"
        
        # Calcular porcentaje de reducción
        if len(lineas_orig) > 0:
            reduccion = ((len(lineas_orig) - len(lineas_opt)) / len(lineas_orig)) * 100
            resultado += f"  Reducción:          {reduccion:.1f}%\n"
        
        return resultado
