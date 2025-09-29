# Tema: Tratamiento Seguro de la Información y Vulnerabilidades en Sistemas Informáticos

## Índice
1. [Introducción a la Seguridad de la Información](#1-introducción-a-la-seguridad-de-la-información)
2. [Seguridad Física vs Seguridad Lógica](#2-seguridad-física-vs-seguridad-lógica)
3. [Clasificación de Vulnerabilidades](#3-clasificación-de-vulnerabilidades)
4. [Ingeniería Social y Fraudes Informáticos](#4-ingeniería-social-y-fraudes-informáticos)
5. [Políticas de Contraseñas](#5-políticas-de-contraseñas)
6. [Sistemas Biométricos](#6-sistemas-biométricos)
7. [Técnicas Criptográficas](#7-técnicas-criptográficas)
8. [Protección Perimetral](#8-protección-perimetral)
9. [Análisis Forense](#9-análisis-forense)
10. [Casos Prácticos](#10-casos-prácticos)

---

## 1. Introducción a la Seguridad de la Información

### 1.1 La Tríada CIA de la Seguridad

La seguridad de la información se fundamenta en tres pilares básicos conocidos como la **tríada CIA**:

#### **Confidencialidad (Confidentiality)**
- **Definición**: Garantizar que la información solo sea accesible por personas autorizadas
- **Importancia**: Protege datos sensibles como información personal, secretos comerciales, datos financieros
- **Ejemplos de amenazas**: Espionaje industrial, robo de identidad, acceso no autorizado
- **Medidas**: Cifrado, control de acceso, clasificación de información

#### **Integridad (Integrity)**
- **Definición**: Asegurar que la información no ha sido alterada de forma no autorizada
- **Importancia**: Mantiene la veracidad y exactitud de los datos
- **Ejemplos de amenazas**: Modificación maliciosa de bases de datos, alteración de registros contables
- **Medidas**: Checksums, firmas digitales, control de versiones

#### **Disponibilidad (Availability)**
- **Definición**: Garantizar que la información esté accesible cuando sea necesaria
- **Importancia**: Asegura la continuidad del negocio y la operatividad de los sistemas
- **Ejemplos de amenazas**: Ataques DDoS, fallos de hardware, desastres naturales
- **Medidas**: Redundancia, copias de seguridad, sistemas de alta disponibilidad

### 1.2 Valor de la Información
- **Activo estratégico**: La información es uno de los activos más valiosos de las organizaciones
- **Coste de la pérdida**: Las brechas de seguridad pueden costar millones en multas, pérdida de reputación y recuperación
- **Marco legal**: RGPD, LOPD-GDD establecen obligaciones legales de protección

---

## 2. Seguridad Física vs Seguridad Lógica

### 2.1 Seguridad Física

#### **Definición**
Medidas para proteger los componentes físicos de los sistemas informáticos y el entorno donde operan.

#### **Componentes principales:**
- **Control de acceso físico**
  - Sistemas de tarjetas de identificación
  - Cerraduras biométricas
  - Personal de seguridad
  - Cámaras de vigilancia

- **Protección del hardware**
  - Salas de servidores climatizadas
  - Sistemas de alimentación ininterrumpida (SAI/UPS)
  - Sistemas contra incendios
  - Blindaje electromagnético

- **Gestión ambiental**
  - Control de temperatura y humedad
  - Detección de humo y agua
  - Sistemas de ventilación

#### **Amenazas físicas típicas:**
- Robo de equipos
- Acceso no autorizado a instalaciones
- Sabotaje
- Desastres naturales
- Cortes de suministro eléctrico

### 2.2 Seguridad Lógica

#### **Definición**
Medidas para proteger los datos, software y recursos lógicos del sistema informático.

#### **Componentes principales:**
- **Autenticación y autorización**
  - Sistemas de login
  - Control de privilegios
  - Gestión de identidades

- **Protección del software**
  - Antivirus y antimalware
  - Firewalls
  - Sistemas de detección de intrusiones (IDS/IPS)

- **Protección de datos**
  - Cifrado de datos
  - Copias de seguridad
  - Clasificación de información

#### **Amenazas lógicas típicas:**
- Malware (virus, gusanos, troyanos)
- Ataques de red
- Acceso no autorizado a sistemas
- Ingeniería social

### 2.3 Comparativa

| Aspecto | Seguridad Física | Seguridad Lógica |
|---------|------------------|------------------|
| **Objetivo** | Proteger hardware y instalaciones | Proteger datos y software |
| **Medidas** | Barreras físicas, vigilancia | Software de seguridad, cifrado |
| **Coste inicial** | Alto (infraestructura) | Medio (licencias software) |
| **Mantenimiento** | Bajo | Alto (actualizaciones constantes) |
| **Impacto de fallo** | Total (pérdida de acceso) | Variable (según el sistema) |

---

## 3. Clasificación de Vulnerabilidades

### 3.1 Definición de Vulnerabilidad
Una vulnerabilidad es una debilidad en un sistema que puede ser explotada para comprometer la seguridad.

### 3.2 Clasificación por Tipología

#### **3.2.1 Vulnerabilidades de Software**
- **Errores de programación**
  - Buffer overflow
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Cross-Site Request Forgery (CSRF)

- **Configuraciones inseguras**
  - Contraseñas por defecto
  - Servicios innecesarios activos
  - Permisos excesivos

- **Falta de actualizaciones**
  - Sistemas sin parches
  - Software obsoleto
  - Bibliotecas desactualizadas

#### **3.2.2 Vulnerabilidades de Hardware**
- **Fallas de diseño**
  - Spectre y Meltdown (procesadores)
  - Vulnerabilidades en firmware

- **Componentes físicos**
  - Puertos USB sin protección
  - Interfaces de depuración expuestas

#### **3.2.3 Vulnerabilidades de Red**
- **Protocolos inseguros**
  - HTTP vs HTTPS
  - Telnet vs SSH
  - FTP vs SFTP

- **Configuración de red**
  - Segmentación inadecuada
  - Reglas de firewall permisivas

#### **3.2.4 Vulnerabilidades Humanas**
- **Falta de formación**
- **Ingeniería social**
- **Errores operacionales**
- **Insider threats (amenazas internas)**

### 3.3 Clasificación por Origen

#### **3.3.1 Origen Interno**
- **Personal de la organización**
  - Empleados descontentos
  - Acceso privilegiado mal gestionado
  - Errores humanos

- **Procesos internos deficientes**
  - Falta de políticas de seguridad
  - Procedimientos inadecuados

#### **3.3.2 Origen Externo**
- **Atacantes externos**
  - Hackers
  - Grupos organizados (APT)
  - Competencia

- **Factores externos**
  - Proveedores de servicios
  - Socios comerciales

### 3.4 Sistemas de Clasificación

#### **CVSS (Common Vulnerability Scoring System)**
- **Puntuación**: 0.0 - 10.0
- **Categorías**:
  - Bajo: 0.1-3.9
  - Medio: 4.0-6.9
  - Alto: 7.0-8.9
  - Crítico: 9.0-10.0

#### **CWE (Common Weakness Enumeration)**
- Catálogo estandardizado de debilidades de software
- Más de 800 tipos de vulnerabilidades catalogadas

---

## 4. Ingeniería Social y Fraudes Informáticos

### 4.1 Definición de Ingeniería Social
La ingeniería social es el arte de manipular personas para que divulguen información confidencial o realicen acciones que comprometan la seguridad.

### 4.2 Técnicas Principales

#### **4.2.1 Phishing**
- **Descripción**: Suplantación de identidad para obtener credenciales
- **Variantes**:
  - Email phishing
  - Spear phishing (dirigido)
  - Whaling (dirigido a ejecutivos)
  - Smishing (SMS)
  - Vishing (llamadas telefónicas)

#### **4.2.2 Pretexting**
- **Descripción**: Crear un escenario falso para obtener información
- **Ejemplos**:
  - Hacerse pasar por soporte técnico
  - Fingir ser un nuevo empleado
  - Simular una emergencia

#### **4.2.3 Baiting**
- **Descripción**: Ofrecer algo atractivo para comprometer la seguridad
- **Ejemplos**:
  - USB con malware dejado en el parking
  - Descargas gratuitas infectadas
  - Ofertas demasiado buenas para ser verdad

#### **4.2.4 Tailgating/Piggybacking**
- **Descripción**: Seguir a personas autorizadas para acceder a áreas restringidas
- **Técnicas**:
  - Llevar cajas pesadas para que abran la puerta
  - Fingir ser un repartidor
  - Aprovecharse de la cortesía

### 4.3 Impacto en Fraudes Informáticos

#### **Estadísticas relevantes:**
- 95% de los ataques exitosos involucran ingeniería social
- El phishing representa el 36% de las brechas de datos
- Coste promedio: $4.65 millones por brecha

#### **Casos de uso en fraudes:**
- **Fraude CEO**: Suplantación de ejecutivos para transferencias
- **Fraude de proveedores**: Cambio de datos bancarios
- **Robo de identidad**: Obtención de datos personales

### 4.4 Medidas de Prevención

#### **Técnicas organizacionales:**
- Formación y concienciación regular
- Políticas de verificación de identidad
- Simulacros de phishing
- Procedimientos de escalado

#### **Medidas técnicas:**
- Filtros de email
- Autenticación multifactor
- Sistemas de detección de anomalías
- Verificación de dominios (SPF, DKIM, DMARC)

---

## 5. Políticas de Contraseñas

### 5.1 Importancia de las Políticas de Contraseñas

Las contraseñas siguen siendo el mecanismo de autenticación más utilizado, por lo que establecer políticas robustas es fundamental para la seguridad.

### 5.2 Características de Contraseñas Seguras

#### **5.2.1 Longitud**
- **Mínimo recomendado**: 12 caracteres
- **Ideal**: 15 o más caracteres
- **Principio**: La longitud es más importante que la complejidad

#### **5.2.2 Complejidad**
- **Variedad de caracteres**:
  - Letras mayúsculas y minúsculas
  - Números
  - Símbolos especiales
- **Evitar patrones predecibles**
- **No usar información personal**

#### **5.2.3 Unicidad**
- Una contraseña única por servicio/sistema
- No reutilizar contraseñas anteriores
- No derivar contraseñas de otras existentes

### 5.3 Elementos de una Política de Contraseñas

#### **5.3.1 Requisitos técnicos**
```
Ejemplo de política:
- Longitud mínima: 12 caracteres
- Al menos 3 de los 4 tipos de caracteres
- No contener el nombre de usuario
- No contener información personal
- Diferir en al menos 4 caracteres de las últimas 12 contraseñas
```

#### **5.3.2 Gestión del ciclo de vida**
- **Cambio periódico**: Cada 90-180 días para cuentas críticas
- **Cambio inmediato**: En caso de compromiso sospechado
- **Bloqueo por intentos**: Después de 5-10 intentos fallidos
- **Recuperación segura**: Mediante canales alternativos verificados

#### **5.3.3 Almacenamiento seguro**
- **Hash con salt**: bcrypt, scrypt, Argon2
- **Nunca en texto plano**
- **Protección de bases de datos de contraseñas**

### 5.4 Alternativas y Mejoras

#### **5.4.1 Gestores de contraseñas**
- **Ventajas**:
  - Generación de contraseñas únicas y complejas
  - Almacenamiento cifrado
  - Autocompletado seguro
- **Ejemplos**: Bitwarden, KeePass, LastPass

#### **5.4.2 Autenticación multifactor (MFA)**
- **Factores**:
  - Algo que sabes (contraseña)
  - Algo que tienes (token, móvil)
  - Algo que eres (biometría)
- **Implementaciones**: SMS, aplicaciones (Google Authenticator, Authy), llaves físicas (YubiKey)

#### **5.4.3 Passphrases**
- **Concepto**: Frases fáciles de recordar pero difíciles de adivinar
- **Ejemplo**: "Mi gato Negro come 3 ratones Diarios!"
- **Ventajas**: Más largas y memorizables que contraseñas complejas

---

## 6. Sistemas Biométricos

### 6.1 Definición y Principios

Los sistemas biométricos utilizan características físicas o conductuales únicas de las personas para la identificación y autenticación.

### 6.2 Tipos de Biometría

#### **6.2.1 Biometría Física**
- **Huellas dactilares**
  - Más utilizada y económica
  - Falsos positivos: ~0.01%
  - Falsos negativos: ~2%

- **Reconocimiento facial**
  - Crecimiento rápido en adopción
  - Problemas con gemelos y cambios de apariencia
  - Cuestiones de privacidad

- **Iris y retina**
  - Muy alta precisión
  - Costoso de implementar
  - Intrusivo para algunos usuarios

- **Geometría de la mano**
  - Menos preciso pero más aceptado
  - Útil en entornos industriales

- **ADN**
  - Máxima precisión
  - Lento y costoso
  - Solo para casos especiales

#### **6.2.2 Biometría Conductual**
- **Reconocimiento de voz**
  - Natural para los usuarios
  - Afectado por enfermedades y ruido

- **Dinámica de escritura**
  - Patrón de pulsaciones en teclado
  - Útil para autenticación continua

- **Dinámica de firma**
  - Familiar para los usuarios
  - Variable con el tiempo

- **Patrón de caminar**
  - No intrusivo
  - Menos preciso

### 6.3 Ventajas de los Sistemas Biométricos

#### **6.3.1 Seguridad**
- **No transferibles**: No se pueden prestar o compartir
- **Únicos**: Cada persona tiene características distintas
- **Siempre presentes**: No se pueden olvidar como las contraseñas
- **Difíciles de falsificar**: Aunque no imposible

#### **6.3.2 Conveniencia**
- **Sin memorización**: No hay que recordar contraseñas
- **Rápidos**: Autenticación en segundos
- **Sin pérdida**: No se pueden perder como las tarjetas

#### **6.3.3 Auditabilidad**
- **Trazabilidad**: Registro claro de accesos
- **No repudio**: Difícil negar la identidad
- **Integración**: Fácil combinación con otros sistemas

### 6.4 Limitaciones y Desafíos

#### **6.4.1 Técnicas**
- **Falsos positivos/negativos**: Nunca 100% precisos
- **Cambios temporales**: Heridas, enfermedades
- **Calidad de sensores**: Afecta la precisión
- **Condiciones ambientales**: Luz, ruido, humedad

#### **6.4.2 Privacidad y legales**
- **Datos sensibles**: Información biométrica muy personal
- **RGPD**: Considerados datos de categoría especial
- **Permanencia**: No se pueden "cambiar" como contraseñas
- **Consentimiento**: Necesario consentimiento explícito

#### **6.4.3 Costes**
- **Implementación inicial**: Hardware especializado
- **Mantenimiento**: Limpieza y calibración de sensores
- **Escalabilidad**: Crecimiento del sistema

### 6.5 Mejores Prácticas

#### **Implementación segura:**
- Cifrado de plantillas biométricas
- Almacenamiento distribuido
- Auditoría de accesos
- Protección contra ataques de replay

#### **Consideraciones legales:**
- Política de privacidad clara
- Consentimiento informado
- Derecho de retirada
- Minimización de datos

---

## 7. Técnicas Criptográficas

### 7.1 Fundamentos de la Criptografía

#### **Definición**
La criptografía es la ciencia de proteger la información mediante la transformación de datos legibles en datos codificados.

#### **Objetivos principales:**
- **Confidencialidad**: Solo el destinatario puede leer el mensaje
- **Integridad**: Detectar modificaciones no autorizadas
- **Autenticación**: Verificar la identidad del emisor
- **No repudio**: Evitar que el emisor niegue haber enviado el mensaje

### 7.2 Tipos de Criptografía

#### **7.2.1 Criptografía Simétrica**
- **Principio**: La misma clave para cifrar y descifrar
- **Ventajas**:
  - Muy rápida
  - Eficiente para grandes volúmenes de datos
- **Desventajas**:
  - Problema de distribución de claves
  - No proporciona no repudio

##### **Algoritmos principales:**
- **AES (Advanced Encryption Standard)**
  - Estándar actual
  - Claves de 128, 192 o 256 bits
  - Muy seguro y eficiente

- **DES/3DES**
  - Obsoletos (DES) o en desuso (3DES)
  - Mencionados solo por contexto histórico

##### **Modos de operación:**
- **ECB**: Simple pero inseguro
- **CBC**: Más seguro, requiere IV
- **GCM**: Proporciona cifrado y autenticación

#### **7.2.2 Criptografía Asimétrica**
- **Principio**: Par de claves (pública y privada)
- **Ventajas**:
  - Soluciona el problema de distribución de claves
  - Proporciona no repudio
  - Permite firmas digitales
- **Desventajas**:
  - Más lenta que la simétrica
  - Complejidad computacional alta

##### **Algoritmos principales:**
- **RSA**
  - Más utilizado históricamente
  - Claves de 2048 bits mínimo
  - Basado en factorización de números primos

- **ECC (Elliptic Curve Cryptography)**
  - Más eficiente que RSA
  - Claves más pequeñas para la misma seguridad
  - Ideal para dispositivos móviles

##### **Casos de uso:**
- Intercambio de claves simétricas
- Firmas digitales
- Autenticación de identidad

#### **7.2.3 Funciones Hash Criptográficas**
- **Principio**: Función unidireccional que produce un resumen fijo
- **Propiedades**:
  - Determinista
  - Avalanche effect
  - Irreversible
  - Resistente a colisiones

##### **Algoritmos principales:**
- **SHA-256**: Estándar actual seguro
- **SHA-3**: Alternativa más reciente
- **MD5/SHA-1**: Obsoletos e inseguros

##### **Usos:**
- Verificación de integridad
- Almacenamiento de contraseñas
- Proof of work (blockchain)

### 7.3 Aplicaciones en Almacenamiento

#### **7.3.1 Cifrado de Disco Completo**
- **BitLocker** (Windows)
- **FileVault** (macOS)
- **LUKS** (Linux)
- **Ventajas**: Protección completa en caso de robo
- **Consideraciones**: Gestión de claves de recuperación

#### **7.3.2 Cifrado a Nivel de Archivo**
- **EFS** (Encrypted File System - Windows)
- **Herramientas**: 7-Zip, AxCrypt, VeraCrypt
- **Ventajas**: Granularidad en la protección
- **Uso**: Archivos específicos sensibles

#### **7.3.3 Cifrado en Base de Datos**
- **TDE (Transparent Data Encryption)**
- **Cifrado a nivel de campo**
- **Consideraciones**: Impacto en rendimiento vs seguridad

### 7.4 Aplicaciones en Transmisión

#### **7.4.1 Protocolos Seguros**
- **HTTPS**: HTTP sobre TLS/SSL
- **SFTP**: FTP seguro sobre SSH
- **SMTPS/POP3S/IMAPS**: Email seguro
- **VPN**: Túneles cifrados

#### **7.4.2 TLS/SSL**
- **Versiones actuales**: TLS 1.2 y 1.3
- **Proceso de handshake**:
  1. Negociación de algoritmos
  2. Intercambio de certificados
  3. Verificación de identidad
  4. Establecimiento de claves de sesión

#### **7.4.3 Certificados Digitales**
- **PKI (Public Key Infrastructure)**
- **Autoridades de Certificación (CA)**
- **Cadena de confianza**
- **Tipos**: DV, OV, EV

### 7.5 Gestión de Claves

#### **Principios fundamentales:**
- **Generación segura**: Entropía suficiente
- **Distribución segura**: Canales protegidos
- **Almacenamiento seguro**: HSMs, smart cards
- **Rotación regular**: Cambio periódico de claves
- **Destrucción segura**: Eliminación apropiada

#### **Tecnologías:**
- **HSM (Hardware Security Module)**
- **KMS (Key Management Service)**
- **Smart cards y tokens**

---

## 8. Protección Perimetral

### 8.1 Concepto de Perímetro de Seguridad

El perímetro de seguridad es el conjunto de controles que establecen una barrera entre la red interna (confiable) y las redes externas (no confiables).

### 8.2 Componentes de la Protección Perimetral

#### **8.2.1 Firewalls**
##### **Tipos:**
- **Firewall de paquetes**
  - Filtra basándose en IPs, puertos y protocolos
  - Rápido pero limitado
  - Ejemplo: iptables

- **Firewall de estado**
  - Rastrea el estado de las conexiones
  - Más inteligente que el filtrado de paquetes
  - Ejemplo: pfSense

- **Firewall de aplicación (WAF)**
  - Inspección del contenido de aplicación
  - Protege aplicaciones web específicas
  - Ejemplo: ModSecurity

- **Next Generation Firewall (NGFW)**
  - Combinación de funcionalidades
  - Inspección profunda de paquetes
  - Control de aplicaciones
  - Ejemplo: FortiGate, Palo Alto

##### **Configuración básica:**
```
Reglas típicas de firewall:
- Deny ALL por defecto
- Allow HTTP/HTTPS saliente
- Allow DNS saliente
- Allow SSH desde IPs específicas
- Allow servicios internos específicos
- Log de intentos denegados
```

#### **8.2.2 Sistemas de Detección y Prevención de Intrusiones**

##### **IDS (Intrusion Detection System)**
- **Función**: Detecta y alerta sobre actividades sospechosas
- **Tipos**:
  - NIDS (Network-based): Analiza tráfico de red
  - HIDS (Host-based): Monitoriza sistemas específicos
- **Métodos de detección**:
  - Basado en firmas: Patrones conocidos
  - Basado en anomalías: Desviaciones del comportamiento normal
- **Ejemplos**: Snort, Suricata

##### **IPS (Intrusion Prevention System)**
- **Función**: Detecta y bloquea automáticamente amenazas
- **Ventajas**: Respuesta inmediata
- **Riesgos**: Posibles falsos positivos que bloqueen tráfico legítimo
- **Implementación**: En línea con el tráfico

#### **8.2.3 Proxy y Gateways**

##### **Proxy Server**
- **Forward Proxy**:
  - Actúa en nombre del cliente
  - Filtra contenido saliente
  - Cache de contenido
  - Control de acceso a sitios web

- **Reverse Proxy**:
  - Actúa en nombre del servidor
  - Balanceo de carga
  - Terminación SSL
  - Protección del servidor web

##### **Email Gateway**
- **Filtrado de spam**
- **Detección de malware**
- **Data Loss Prevention (DLP)**
- **Cifrado de emails**

#### **8.2.4 VPN (Virtual Private Network)**
- **Site-to-Site VPN**: Conecta redes remotas
- **Remote Access VPN**: Acceso de usuarios remotos
- **Protocolos**:
  - **IPSec**: Estándar para VPNs empresariales
  - **OpenVPN**: Flexible y open source
  - **WireGuard**: Moderno y eficiente

### 8.3 Arquitecturas de Seguridad Perimetral

#### **8.3.1 Red Plana (No recomendada)**
- Todos los sistemas en la misma red
- Sin segmentación
- Alto riesgo de propagación de amenazas

#### **8.3.2 DMZ (Zona Desmilitarizada)**
```
Internet → Firewall → DMZ → Firewall → LAN Interna
```
- **DMZ**: Zona intermedia para servicios públicos
- **Servicios típicos en DMZ**: Web servers, mail servers, DNS público
- **Ventaja**: Aislamiento de servicios públicos

#### **8.3.3 Defensa en Profundidad**
```
Internet → WAF → Firewall → IPS → DMZ → Firewall → Segmentación interna
```
- Múltiples capas de seguridad
- Si una capa falla, otras proporcionan protección
- Principio de "never trust, always verify"

#### **8.3.4 Zero Trust Architecture**
- **Principio**: No confiar en nada automáticamente
- **Verificación continua** de usuarios y dispositivos
- **Microsegmentación** de la red
- **Monitorización constante** de actividades

### 8.4 Consideraciones Especiales para Redes Públicas

#### **8.4.1 Amenazas específicas**
- **Man-in-the-Middle**: Interceptación de comunicaciones
- **Evil Twin**: Puntos de acceso WiFi falsos
- **Packet Sniffing**: Captura de tráfico no cifrado
- **DDoS**: Ataques de denegación de servicio

#### **8.4.2 Medidas de protección**
- **Cifrado end-to-end**: Toda la comunicación cifrada
- **VPN obligatoria**: Para acceso remoto
- **Autenticación fuerte**: MFA para todos los accesos
- **Monitorización 24/7**: SOC (Security Operations Center)

### 8.5 Plan Integral de Protección Perimetral

#### **8.5.1 Evaluación de riesgos**
1. **Identificación de activos**: Qué necesita protección
2. **Análisis de amenazas**: Qué puede atacar
3. **Evaluación de vulnerabilidades**: Puntos débiles
4. **Cálculo de riesgo**: Impacto × Probabilidad

#### **8.5.2 Diseño de arquitectura**
1. **Segmentación de red**: Dividir en zonas de confianza
2. **Puntos de control**: Dónde implementar controles
3. **Redundancia**: Evitar puntos únicos de fallo
4. **Escalabilidad**: Capacidad de crecimiento

#### **8.5.3 Implementación por fases**
1. **Fase 1**: Controles básicos (firewall, antivirus)
2. **Fase 2**: Detección avanzada (IDS/IPS, SIEM)
3. **Fase 3**: Respuesta automatizada (SOAR)
4. **Fase 4**: Inteligencia de amenazas (Threat Intelligence)

#### **8.5.4 Mantenimiento continuo**
- **Actualizaciones regulares**: Firmware, firmas, reglas
- **Monitorización continua**: Alertas y dashboards
- **Pruebas periódicas**: Pentesting, vulnerability assessment
- **Formación del personal**: Concienciación y actualización técnica

---

## 9. Análisis Forense

### 9.1 Definición y Objetivos

#### **Análisis Forense Digital**
Proceso sistemático de identificación, preservación, análisis y presentación de evidencias digitales de manera que sean admisibles legalmente.

#### **Objetivos principales:**
- **Identificar** qué ocurrió durante el incidente
- **Determinar** cómo se produjo el ataque
- **Establecer** quién fue el responsable
- **Cuantificar** el daño causado
- **Prevenir** futuros incidentes similares

### 9.2 Fases del Análisis Forense

#### **9.2.1 Fase 1: Preparación**
##### **Establecimiento del equipo de respuesta**
- **CERT (Computer Emergency Response Team)**
- **Roles definidos**: Líder, analistas, legal, comunicaciones
- **Herramientas preparadas**: Software forense, hardware especializado
- **Procedimientos documentados**: Playbooks de respuesta

##### **Preparación técnica**
- **Kits de respuesta**: Dispositivos de captura, cables, adaptadores
- **Software forense**: EnCase, FTK, SIFT, Autopsy
- **Documentación legal**: Formularios de cadena de custodia
- **Contactos**: Fuerzas del orden, asesores legales, proveedores

#### **9.2.2 Fase 2: Identificación y Detección**
##### **Detección del incidente**
- **Fuentes de detección**:
  - Sistemas de monitorización (SIEM)
  - Alertas automáticas (IDS/IPS)
  - Reportes de usuarios
  - Revisiones de seguridad rutinarias

##### **Clasificación inicial**
- **Tipo de incidente**: Malware, intrusión, fraude, sabotaje
- **Severidad**: Crítico, alto, medio, bajo
- **Alcance**: Sistemas afectados, datos comprometidos
- **Urgencia**: Tiempo de respuesta requerido

##### **Primeras acciones**
```
Checklist de respuesta inmediata:
□ Documentar hora y fecha de detección
□ Identificar sistemas afectados
□ Evaluar si el ataque está en curso
□ Determinar si es necesario aislar sistemas
□ Notificar al equipo de respuesta
□ Preservar logs críticos
□ Comenzar documentación detallada
```

#### **9.2.3 Fase 3: Preservación y Recolección**
##### **Principios fundamentales**
- **Integridad**: La evidencia no debe alterarse
- **Autenticidad**: Debe ser genuina y verificable
- **Completitud**: Toda la evidencia relevante debe recolectarse
- **Cadena de custodia**: Registro detallado de quién, cuándo y dónde

##### **Orden de volatilidad (RFC 3227)**
1. **Registros CPU, caché**
2. **Contenido de memoria RAM**
3. **Estado de conexiones de red**
4. **Procesos en ejecución**
5. **Datos en discos duros**
6. **Logs del sistema**
7. **Configuración física**
8. **Documentación**

##### **Técnicas de preservación**
- **Imágenes forenses**: Copia bit a bit de discos
- **Memory dumps**: Volcado completo de memoria RAM
- **Network capture**: Captura de tráfico de red
- **Log preservation**: Copia de logs antes de rotación

##### **Herramientas de adquisición**
- **dd**: Comando Linux para imágenes de disco
- **FTK Imager**: Herramienta gratuita de AccessData
- **MSAB XRY**: Para dispositivos móviles
- **Volatility**: Para análisis de memoria

#### **9.2.4 Fase 4: Análisis e Investigación**
##### **Análisis de timeline**
- **Reconstrucción cronológica** de eventos
- **Correlación** de evidencias de múltiples fuentes
- **Identificación** de patrones y anomalías

##### **Análisis de artefactos**
- **Sistema de archivos**:
  - Archivos eliminados
  - Timestamps (MAC times)
  - Metadata de archivos

- **Registro del sistema (Windows)**:
  - Claves de inicio automático
  - Historial de programas instalados
  - Actividad de red

- **Logs de aplicación**:
  - Web server logs
  - Database logs
  - Email logs

- **Memoria RAM**:
  - Procesos activos
  - Conexiones de red
  - Claves de cifrado

##### **Análisis de malware**
- **Análisis estático**: Sin ejecutar el malware
- **Análisis dinámico**: Ejecutar en ambiente controlado
- **Ingeniería inversa**: Entender funcionamiento interno
- **Indicators of Compromise (IOCs)**: Hashes, IPs, dominios

#### **9.2.5 Fase 5: Documentación y Reporte**
##### **Documentación técnica**
- **Procedimientos seguidos**: Pasos detallados realizados
- **Herramientas utilizadas**: Versiones y configuraciones
- **Evidencias encontradas**: Con referencias y hashes
- **Análisis realizado**: Métodos y conclusiones

##### **Reporte ejecutivo**
- **Resumen del incidente**: Qué pasó, cuándo, cómo
- **Impacto del negocio**: Sistemas afectados, datos comprometidos
- **Causas raíz**: Vulnerabilidades explotadas
- **Recomendaciones**: Medidas para prevenir recurrencia

##### **Consideraciones legales**
- **Admisibilidad**: Evidencia que puede usarse en juicio
- **Cadena de custodia**: Documentación completa
- **Integridad**: Hashes y firmas digitales
- **Expertise**: Cualificación del analista forense

### 9.3 Herramientas de Análisis Forense

#### **9.3.1 Suites comerciales**
- **EnCase Forensic**: Estándar de la industria
- **FTK (Forensic Toolkit)**: Análisis completo
- **X-Ways Forensics**: Eficiente y potente
- **Cellebrite**: Especializado en móviles

#### **9.3.2 Herramientas open source**
- **Autopsy**: Suite completa gratuita
- **SIFT Workstation**: Distribución Linux especializada
- **Volatility**: Análisis de memoria
- **Wireshark**: Análisis de tráfico de red

#### **9.3.3 Herramientas por categoría**
```
Adquisición de evidencias:
- dd, dcfldd, dc3dd
- FTK Imager
- Guymager

Análisis de disco:
- Sleuth Kit
- PhotoRec
- Foremost

Análisis de red:
- Wireshark
- tcpdump
- NetworkMiner

Análisis de memoria:
- Volatility
- Rekall
- WinDbg
```

### 9.4 Tipos Específicos de Análisis

#### **9.4.1 Análisis de Incidentes de Red**
- **Captura de tráfico**: Durante y después del incidente
- **Análisis de logs**: Firewalls, routers, servidores
- **Identificación de lateral movement**: Movimiento interno del atacante
- **Exfiltración de datos**: Detección de transferencias sospechosas

#### **9.4.2 Análisis de Malware**
- **Identificación**: Tipo de malware (virus, troyano, ransomware)
- **Funcionalidades**: Qué hace el malware
- **Comunicaciones C&C**: Servidores de comando y control
- **Persistencia**: Cómo mantiene presencia en el sistema

#### **9.4.3 Análisis de Fraude Interno**
- **Accesos anómalos**: Horarios, ubicaciones inusuales
- **Transferencias de datos**: Copias a dispositivos externos
- **Comunicaciones**: Emails, mensajes sospechosos
- **Escalada de privilegios**: Cambios en permisos

### 9.5 Aspectos Legales y Normativos

#### **9.5.1 Marco legal español**
- **Código Penal**: Delitos informáticos
- **Ley de Enjuiciamiento Criminal**: Procedimientos de investigación
- **RGPD**: Protección de datos durante la investigación
- **Ley de Servicios de la Sociedad de la Información**: Responsabilidades

#### **9.5.2 Principios de admisibilidad**
- **Legalidad**: Evidencia obtenida legalmente
- **Autenticidad**: Demostrar que es genuina
- **Integridad**: No ha sido alterada
- **Relevancia**: Relacionada con el caso

#### **9.5.3 Buenas prácticas legales**
- **Consentimiento**: Para análisis de sistemas de empleados
- **Notificación**: A autoridades cuando sea requerido
- **Retención**: Políticas de conservación de evidencias
- **Destrucción segura**: Cuando ya no sea necesaria

---

## 10. Casos Prácticos

### 10.1 Caso Práctico 1: Phishing Dirigido (Spear Phishing)

#### **Escenario**
Una empresa de 500 empleados recibe múltiples reportes de usuarios que han recibido emails sospechosos aparentemente del CEO pidiendo transferencias urgentes.

#### **Análisis del caso**
```
Indicadores iniciales:
- Emails desde dominio similar: company-ceo.com vs company.com
- Presión temporal: "Urgente", "Confidencial"
- Solicitud inusual: Transferencia a cuenta desconocida
- Bypass de procedimientos: Sin autorización habitual
```

#### **Respuesta recomendada**
1. **Inmediata**:
   - Alertar a todos los usuarios
   - Bloquear el dominio malicioso
   - Verificar si hay transferencias realizadas

2. **Investigación**:
   - Analizar headers del email
   - Identificar empleados objetivo
   - Revisar logs de email gateway

3. **Prevención futura**:
   - Implementar DMARC
   - Formación en reconocimiento de phishing
   - Procedimientos de verificación para transferencias

#### **Lecciones aprendidas**
- La ingeniería social explota la confianza y urgencia
- Los controles técnicos deben complementarse con formación
- Los procedimientos de verificación son críticos

### 10.2 Caso Práctico 2: Ransomware Corporativo

#### **Escenario**
Una empresa manufacturera descubre que sus sistemas de producción están cifrados y aparece un mensaje exigiendo pago en Bitcoin.

#### **Análisis forense necesario**
```
Evidencias a recolectar:
1. Memoria RAM de sistemas afectados
2. Logs de Windows Event
3. Logs de antivirus y EDR
4. Tráfico de red capturado
5. Imágenes de disco de sistemas críticos
```

#### **Fases del análisis**
1. **Contención**:
   - Aislar sistemas infectados
   - Identificar vector de entrada
   - Evaluar propagación

2. **Erradicación**:
   - Identificar y eliminar malware
   - Aplicar parches a vulnerabilidades
   - Cambiar credenciales comprometidas

3. **Recuperación**:
   - Restaurar desde backups
   - Validar integridad de datos
   - Monitorizar reinfección

#### **Timeline de ataque típico**
```
T-30 días: Email phishing recibido
T-29 días: Usuario ejecuta adjunto malicioso
T-15 días: Establecimiento de persistencia
T-7 días: Reconnaissance interno
T-3 días: Escalada de privilegios
T-1 día: Movimiento lateral
T-0: Despliegue de ransomware
```

### 10.3 Caso Práctico 3: Fuga de Datos Interna

#### **Escenario**
Se detecta que un empleado de RRHH ha accedido a expedientes de todos los empleados fuera de su horario laboral y ha copiado archivos a un USB.

#### **Evidencias digitales**
```
Fuentes de evidencia:
- Logs de acceso a aplicaciones
- Logs de Windows (USB insertion)
- CCTV del área de trabajo
- Análisis del dispositivo USB
- Email y comunicaciones del empleado
```

#### **Proceso de investigación**
1. **Preservación inmediata**:
   - Imaging del ordenador del empleado
   - Conservar logs antes de rotación
   - Asegurar dispositivos USB

2. **Análisis de actividad**:
   - Reconstruir acciones del usuario
   - Identificar archivos accedidos/copiados
   - Analizar patrones de comportamiento

3. **Evaluación de impacto**:
   - Qué datos fueron comprometidos
   - Posible uso malintencionado
   - Obligaciones de notificación (RGPD)

### 10.4 Laboratorio Virtual: Herramientas Forenses

#### **Ejercicio 1: Análisis básico con Autopsy**
```
Objetivos:
1. Cargar imagen forense de disco
2. Identificar archivos eliminados recientemente
3. Extraer metadatos de imágenes
4. Generar reporte básico
```

#### **Ejercicio 2: Análisis de memoria con Volatility**
```
Comandos básicos:
volatility -f memory.dmp --profile=Win10x64 pslist
volatility -f memory.dmp --profile=Win10x64 netscan
volatility -f memory.dmp --profile=Win10x64 malfind
```

#### **Ejercicio 3: Análisis de red con Wireshark**
```
Filtros útiles:
- http.request.method == "POST"
- dns.qry.name contains "malware"
- tcp.flags.reset == 1
```

---

## 11. Evaluación y Autoevaluación

### 11.1 Preguntas de Repaso por Criterios

#### **Criterio a) Tríada CIA**
1. ¿Cuáles son los tres pilares fundamentales de la seguridad de la información?
2. ¿Qué amenazas específicas afectan a cada pilar de la tríada CIA?
3. ¿Cómo se interrelacionan confidencialidad, integridad y disponibilidad?

#### **Criterio b) Seguridad física vs lógica**
1. ¿Cuáles son las principales diferencias entre seguridad física y lógica?
2. ¿Qué tipos de amenazas afectan específicamente a cada tipo de seguridad?
3. ¿Cómo se complementan ambos tipos de seguridad?

#### **Criterio c) Clasificación de vulnerabilidades**
1. ¿Cómo se clasifican las vulnerabilidades según su tipología?
2. ¿Qué diferencia hay entre vulnerabilidades de origen interno y externo?
3. ¿Qué es el sistema CVSS y cómo funciona?

#### **Criterio d) Ingeniería social**
1. ¿Cuáles son las principales técnicas de ingeniería social?
2. ¿Por qué es tan efectiva la ingeniería social en los fraudes informáticos?
3. ¿Qué medidas se pueden tomar para prevenir ataques de ingeniería social?

#### **Criterio e) Políticas de contraseñas**
1. ¿Qué elementos debe incluir una política de contraseñas robusta?
2. ¿Cuáles son las alternativas modernas a las contraseñas tradicionales?
3. ¿Cómo se debe gestionar el ciclo de vida de las contraseñas?

#### **Criterio f) Sistemas biométricos**
1. ¿Cuáles son las principales ventajas de los sistemas biométricos?
2. ¿Qué limitaciones y desafíos presentan?
3. ¿Qué consideraciones legales hay que tener en cuenta?

#### **Criterio g) Técnicas criptográficas**
1. ¿Cuáles son las diferencias entre criptografía simétrica y asimétrica?
2. ¿Cómo se aplican las técnicas criptográficas en el almacenamiento?
3. ¿Qué protocolos seguros se utilizan para la transmisión?

#### **Criterio h) Protección perimetral**
1. ¿Qué componentes incluye un plan integral de protección perimetral?
2. ¿Cuáles son las arquitecturas de seguridad perimetral más comunes?
3. ¿Qué consideraciones especiales hay para sistemas en redes públicas?

#### **Criterio i) Análisis forense**
1. ¿Cuáles son las fases del análisis forense digital?
2. ¿Qué principios se deben seguir en la preservación de evidencias?
3. ¿Qué herramientas se utilizan en cada fase del análisis?

### 11.2 Casos de Estudio para Evaluación

#### **Caso 1: Evaluación integral**
Una empresa de desarrollo de software ha sufrido una brecha de seguridad. Como especialista en ciberseguridad, debes:
1. Identificar las vulnerabilidades que pudieron ser explotadas
2. Proponer mejoras en las políticas de seguridad
3. Diseñar un plan de respuesta a incidentes
4. Recomendar medidas de protección perimetral

#### **Caso 2: Análisis técnico**
Se ha detectado actividad sospechosa en una red corporativa:
1. Describe el proceso de análisis forense a seguir
2. Identifica las herramientas necesarias para la investigación
3. Explica cómo preservar las evidencias digitales
4. Propone medidas para prevenir futuros incidentes

---

## 12. Recursos Adicionales

### 12.1 Marcos de Referencia y Estándares

#### **Marcos de ciberseguridad**
- **NIST Cybersecurity Framework**: Marco integral de gestión de riesgos
- **ISO 27001**: Estándar internacional de gestión de seguridad
- **COBIT**: Marco de gobierno y gestión de TI
- **ENS**: Esquema Nacional de Seguridad (España)

#### **Metodologías de análisis de riesgos**
- **MAGERIT**: Metodología española de análisis de riesgos
- **OCTAVE**: Metodología Carnegie Mellon
- **FAIR**: Factor Analysis of Information Risk

### 12.2 Herramientas y Software

#### **Distribuciones especializadas**
- **Kali Linux**: Distribución para pentesting
- **SIFT Workstation**: Para análisis forense
- **Security Onion**: Para monitorización de seguridad
- **Parrot Security OS**: Alternativa a Kali Linux

#### **Plataformas de aprendizaje**
- **TryHackMe**: Plataforma gamificada de ciberseguridad
- **Hack The Box**: Laboratorios de pentesting
- **OverTheWire**: Wargames de seguridad
- **PicoCTF**: Competiciones de CTF para estudiantes

### 12.3 Certificaciones Profesionales

#### **Certificaciones básicas**
- **CompTIA Security+**: Fundamentos de ciberseguridad
- **CompTIA CySA+**: Analista de ciberseguridad
- **SANS GIAC**: Diferentes especialidades

#### **Certificaciones avanzadas**
- **CISSP**: Certified Information Systems Security Professional
- **CISM**: Certified Information Security Manager
- **CEH**: Certified Ethical Hacker
- **GCIH**: GIAC Certified Incident Handler

### 12.4 Fuentes de Información Actualizada

#### **Organizaciones de referencia**
- **INCIBE**: Instituto Nacional de Ciberseguridad (España)
- **CCN-CERT**: Centro Criptológico Nacional
- **ENISA**: Agencia Europea de Ciberseguridad
- **NIST**: National Institute of Standards and Technology

#### **Feeds de amenazas**
- **MITRE ATT&CK**: Framework de tácticas y técnicas de atacantes
- **CVE**: Common Vulnerabilities and Exposures
- **US-CERT**: Alertas de seguridad del gobierno estadounidense
- **Threat Intelligence Platforms**: AlienVault OTX, VirusTotal Intelligence

#### **Blogs y comunidades técnicas**
- **Krebs on Security**: Investigación de cibercrimen
- **Schneier on Security**: Análisis de Bruce Schneier
- **SANS Internet Storm Center**: Análisis diario de amenazas
- **Reddit r/netsec**: Comunidad de profesionales de seguridad

---

## Conclusiones

Este tema ha cubierto de manera integral todos los aspectos fundamentales del tratamiento seguro de la información y las vulnerabilidades en sistemas informáticos. Los puntos clave incluyen:

1. **La importancia crítica** de proteger la confidencialidad, integridad y disponibilidad de la información
2. **La complementariedad** entre seguridad física y lógica
3. **La necesidad** de un enfoque sistemático para identificar y clasificar vulnerabilidades
4. **El papel crucial** del factor humano y la ingeniería social en los ataques
5. **La evolución** hacia sistemas de autenticación más robustos
6. **La aplicación práctica** de la criptografía en el mundo real
7. **La importancia** de una arquitectura de seguridad perimetral bien diseñada
8. **La necesidad** de procedimientos forenses rigurosos para la respuesta a incidentes

La ciberseguridad es un campo en constante evolución que requiere actualización continua de conocimientos y adaptación a nuevas amenazas. Los profesionales deben mantener una visión integral que combine aspectos técnicos, organizacionales y legales para proteger eficazmente los activos digitales de las organizaciones.