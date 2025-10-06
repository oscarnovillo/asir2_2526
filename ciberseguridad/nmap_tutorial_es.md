# Tutorial Completo de Nmap
## Guía Práctica de Escaneo de Redes y Análisis de Seguridad

---

## Tabla de Contenidos

1. [Introducción a Nmap](#introducción-a-nmap)
2. [Instalación](#instalación)
3. [Conceptos Básicos](#conceptos-básicos)
4. [Tipos de Escaneo](#tipos-de-escaneo)
5. [Técnicas de Evasión de IDS/IPS](#técnicas-de-evasión-de-idsips)
6. [Nmap Scripting Engine (NSE)](#nmap-scripting-engine-nse)
7. [Detección de Vulnerabilidades](#detección-de-vulnerabilidades)
8. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## Introducción a Nmap

**Nmap** (Network Mapper) es una herramienta de código abierto para exploración de redes y auditoría de seguridad. Fue diseñada para escanear rápidamente grandes redes, aunque funciona muy bien contra hosts individuales.

### ¿Para qué se utiliza Nmap?

- Descubrir hosts en una red
- Identificar puertos abiertos
- Detectar servicios y versiones
- Identificar sistemas operativos
- Detectar vulnerabilidades
- Auditorías de seguridad

### Características principales

- Flexible y potente
- Multiplataforma (Linux, Windows, macOS)
- Soporta múltiples técnicas de escaneo
- Incluye un motor de scripts (NSE)
- Puede evadir firewalls e IDS

---

## Instalación

### Linux (Debian/Ubuntu)
```bash
sudo apt-get update
sudo apt-get install nmap
```

### Linux (RedHat/CentOS)
```bash
sudo yum install nmap
```

### macOS
```bash
brew install nmap
```

### Windows
Descargar el instalador desde: https://nmap.org/download.html

### Verificar instalación
```bash
nmap --version
```

---

## Conceptos Básicos

### Sintaxis general
```bash
nmap [Tipo de Escaneo] [Opciones] [objetivo]
```

### Escaneo básico
```bash
# Escanear un solo host
nmap 192.168.1.1

# Escanear múltiples hosts
nmap 192.168.1.1 192.168.1.2

# Escanear un rango
nmap 192.168.1.1-50

# Escanear una subred completa
nmap 192.168.1.0/24

# Escanear desde un archivo
nmap -iL targets.txt
```

### Especificar puertos
```bash
# Puerto específico
nmap -p 80 192.168.1.1

# Múltiples puertos
nmap -p 80,443,3306 192.168.1.1

# Rango de puertos
nmap -p 1-1000 192.168.1.1

# Todos los puertos
nmap -p- 192.168.1.1

# Puertos más comunes (top 1000)
nmap --top-ports 1000 192.168.1.1
```

### Opciones de salida
```bash
# Salida normal
nmap 192.168.1.1 -oN salida.txt

# Salida XML
nmap 192.168.1.1 -oX salida.xml

# Salida en formato "grepable"
nmap 192.168.1.1 -oG salida.grep

# Todas las salidas a la vez
nmap 192.168.1.1 -oA resultados
```

---

## Tipos de Escaneo

### 1. Escaneo TCP Connect (-sT)

El escaneo más básico. Completa el three-way handshake de TCP.

```bash
nmap -sT 192.168.1.1
```

**Características:**
- No requiere privilegios de root
- Más detectable por IDS
- Más lento que otros métodos
- Muy confiable

**Cómo funciona:**
1. Envía SYN al puerto objetivo
2. Si recibe SYN/ACK → puerto abierto
3. Completa con ACK
4. Cierra la conexión con RST

---

### 2. Escaneo SYN (-sS)

También conocido como "half-open scan" o "stealth scan".

```bash
sudo nmap -sS 192.168.1.1
```

**Características:**
- Requiere privilegios de root
- Más rápido que TCP Connect
- Menos detectable
- Método por defecto con privilegios

**Cómo funciona:**
1. Envía SYN
2. Si recibe SYN/ACK → envía RST (no completa conexión)
3. Puerto abierto confirmado sin establecer conexión completa

---

### 3. Escaneo UDP (-sU)

Escanea puertos UDP (DNS, SNMP, DHCP).

```bash
sudo nmap -sU 192.168.1.1
```

**Características:**
- Muy lento
- Menos confiable que TCP
- Importante para servicios UDP
- Puede combinarse con TCP: `-sU -sS`

**Puertos UDP comunes:**
- 53 (DNS)
- 161/162 (SNMP)
- 67/68 (DHCP)
- 123 (NTP)

---

### 4. Escaneo NULL (-sN)

Envía paquetes sin flags activados.

```bash
sudo nmap -sN 192.168.1.1
```

**Resultado esperado:**
- Sin respuesta → puerto abierto/filtrado
- RST → puerto cerrado

---

### 5. Escaneo FIN (-sF)

Envía paquetes con el flag FIN activado.

```bash
sudo nmap -sF 192.168.1.1
```

**Ventaja:** Puede evadir algunos firewalls no-stateful.

---

### 6. Escaneo XMAS (-sX)

Envía paquetes con flags FIN, PSH y URG activados.

```bash
sudo nmap -sX 192.168.1.1
```

**Nombre:** Los flags "iluminan" como un árbol de Navidad.

---

### 7. Escaneo ACK (-sA)

Usado para mapear reglas de firewall.

```bash
sudo nmap -sA 192.168.1.1
```

**Propósito:** Determinar si un puerto está filtrado o no.

---

### 8. Escaneo de Ventana (-sW)

Similar al escaneo ACK pero examina el tamaño de ventana TCP.

```bash
sudo nmap -sW 192.168.1.1
```

---

## Detección de Servicios y OS

### Detección de versiones (-sV)

Identifica servicios y versiones exactas.

```bash
nmap -sV 192.168.1.1
```

**Niveles de intensidad:**
```bash
# Intensidad ligera (rápida, menos precisa)
nmap -sV --version-intensity 0 192.168.1.1

# Intensidad agresiva (lenta, más precisa)
nmap -sV --version-intensity 9 192.168.1.1
```

---

### Detección de Sistema Operativo (-O)

Identifica el sistema operativo del objetivo.

```bash
sudo nmap -O 192.168.1.1
```

**Opciones adicionales:**
```bash
# Intento agresivo
sudo nmap -O --osscan-guess 192.168.1.1

# Limitar intentos
sudo nmap -O --max-os-tries 1 192.168.1.1
```

---

### Escaneo Agresivo (-A)

Combina detección de OS, versiones, scripts y traceroute.

```bash
sudo nmap -A 192.168.1.1
```

**Equivale a:** `-O -sV -sC --traceroute`

---

## Técnicas de Evasión de IDS/IPS

Los sistemas de detección/prevención de intrusiones (IDS/IPS) pueden detectar escaneos de Nmap. Estas técnicas ayudan a evadir la detección.

### 1. Fragmentación de Paquetes (-f)

Divide los paquetes en fragmentos pequeños.

```bash
sudo nmap -f 192.168.1.1
```

**Fragmentación personalizada:**
```bash
# MTU específico (debe ser múltiplo de 8)
sudo nmap --mtu 16 192.168.1.1
```

---

### 2. Señuelos (Decoy) (-D)

Hace parecer que el escaneo proviene de múltiples fuentes.

```bash
# IPs específicas como señuelos
sudo nmap -D 10.0.0.1,10.0.0.2,ME 192.168.1.1

# Señuelos aleatorios
sudo nmap -D RND:10 192.168.1.1
```

**ME** = tu IP real
**RND:10** = 10 IPs aleatorias

---

### 3. Spoofing de Dirección MAC (--spoof-mac)

Falsifica la dirección MAC de origen.

```bash
# MAC aleatoria
sudo nmap --spoof-mac 0 192.168.1.1

# MAC específica
sudo nmap --spoof-mac 00:11:22:33:44:55 192.168.1.1

# MAC de un fabricante específico
sudo nmap --spoof-mac Apple 192.168.1.1
```

---

### 4. Spoofing de IP de Origen (-S)

Falsifica la dirección IP de origen.

```bash
sudo nmap -S 10.0.0.5 192.168.1.1 -e eth0 -Pn
```

**Nota:** Requiere especificar la interfaz (-e) y deshabilitar ping (-Pn).

---

### 5. Control de Velocidad (Timing)

Ajusta la velocidad del escaneo para ser más sigiloso.

```bash
# T0: Paranoico (más lento, más sigiloso)
nmap -T0 192.168.1.1

# T1: Sigiloso
nmap -T1 192.168.1.1

# T2: Educado
nmap -T2 192.168.1.1

# T3: Normal (por defecto)
nmap -T3 192.168.1.1

# T4: Agresivo
nmap -T4 192.168.1.1

# T5: Loco (muy rápido)
nmap -T5 192.168.1.1
```

---

### 6. Retardos Personalizados

```bash
# Retardo entre sondas
nmap --scan-delay 1s 192.168.1.1

# Retardo máximo
nmap --max-scan-delay 2s 192.168.1.1

# Limitar tasa de paquetes
nmap --max-rate 10 192.168.1.1
```

---

### 7. Puerto de Origen Específico (-g / --source-port)

Usa un puerto de origen específico (algunos firewalls confían en ciertos puertos).

```bash
# Puerto 53 (DNS) - a menudo permitido
sudo nmap -g 53 192.168.1.1

# Puerto 80 (HTTP)
sudo nmap --source-port 80 192.168.1.1
```

---

### 8. Randomización de Objetivos (--randomize-hosts)

Escanea objetivos en orden aleatorio.

```bash
nmap --randomize-hosts 192.168.1.0/24
```

---

### 9. Datos Aleatorios (--data-length)

Añade datos aleatorios a los paquetes enviados.

```bash
nmap --data-length 25 192.168.1.1
```

---

### 10. Evasión con Proxies

```bash
# A través de proxy SOCKS4
nmap --proxies socks4://proxy:1080 192.168.1.1

# Cadena de proxies
nmap --proxies http://proxy1:8080,socks4://proxy2:1080 192.168.1.1
```

---

## Nmap Scripting Engine (NSE)

NSE permite a Nmap ejecutar scripts para tareas avanzadas: detección de vulnerabilidades, explotación, descubrimiento avanzado, etc.

### Categorías de Scripts

- **auth:** Scripts de autenticación
- **broadcast:** Descubrimiento por broadcast
- **brute:** Ataques de fuerza bruta
- **default:** Scripts por defecto (-sC)
- **discovery:** Descubrimiento de información
- **dos:** Detección de vulnerabilidades DoS
- **exploit:** Intentos de explotación
- **external:** Scripts que usan recursos externos
- **fuzzer:** Scripts de fuzzing
- **intrusive:** Scripts intrusivos
- **malware:** Detección de malware
- **safe:** Scripts seguros
- **version:** Detección de versiones
- **vuln:** Detección de vulnerabilidades

---

### Ejecutar Scripts

```bash
# Script específico
nmap --script=http-title 192.168.1.1

# Múltiples scripts
nmap --script=http-title,http-headers 192.168.1.1

# Categoría completa
nmap --script=vuln 192.168.1.1

# Múltiples categorías
nmap --script=default,safe 192.168.1.1

# Todos excepto intrusivos
nmap --script="not intrusive" 192.168.1.1

# Combinación con AND
nmap --script="http-* and not http-brute" 192.168.1.1
```

---

### Scripts Útiles por Servicio

#### HTTP/HTTPS (Puerto 80/443)
```bash
# Información del servidor web
nmap --script=http-headers 192.168.1.1 -p 80

# Métodos HTTP permitidos
nmap --script=http-methods 192.168.1.1 -p 80

# Enumeración de directorios
nmap --script=http-enum 192.168.1.1 -p 80

# Detección de WAF
nmap --script=http-waf-detect 192.168.1.1 -p 80

# Shellshock
nmap --script=http-shellshock 192.168.1.1 -p 80

# SQL injection
nmap --script=http-sql-injection 192.168.1.1 -p 80
```

#### SMB (Puerto 445)
```bash
# Información del sistema
nmap --script=smb-os-discovery 192.168.1.1

# Enumeración de shares
nmap --script=smb-enum-shares 192.168.1.1

# Enumeración de usuarios
nmap --script=smb-enum-users 192.168.1.1

# Vulnerabilidades SMB
nmap --script=smb-vuln-* 192.168.1.1

# EternalBlue
nmap --script=smb-vuln-ms17-010 192.168.1.1
```

#### SSH (Puerto 22)
```bash
# Algoritmos y versión
nmap --script=ssh2-enum-algos 192.168.1.1 -p 22

# Fuerza bruta
nmap --script=ssh-brute 192.168.1.1 -p 22

# Hostkey
nmap --script=ssh-hostkey 192.168.1.1 -p 22
```

#### FTP (Puerto 21)
```bash
# Login anónimo
nmap --script=ftp-anon 192.168.1.1 -p 21

# Fuerza bruta
nmap --script=ftp-brute 192.168.1.1 -p 21

# Vulnerabilidades FTP
nmap --script=ftp-vuln-* 192.168.1.1 -p 21
```

#### MySQL (Puerto 3306)
```bash
# Información
nmap --script=mysql-info 192.168.1.1 -p 3306

# Enumeración de bases de datos
nmap --script=mysql-databases 192.168.1.1 -p 3306

# Usuarios
nmap --script=mysql-users 192.168.1.1 -p 3306

# Fuerza bruta
nmap --script=mysql-brute 192.168.1.1 -p 3306
```

#### DNS (Puerto 53)
```bash
# Transferencia de zona
nmap --script=dns-zone-transfer 192.168.1.1 -p 53

# Fuerza bruta de subdominios
nmap --script=dns-brute 192.168.1.1
```

---

### Actualizar Base de Datos de Scripts

```bash
sudo nmap --script-updatedb
```

---

### Obtener Ayuda de un Script

```bash
nmap --script-help=http-title
```

---

## Detección de Vulnerabilidades

### Escaneo Completo de Vulnerabilidades

```bash
# Ejecutar todos los scripts de vulnerabilidades
sudo nmap -sV --script=vuln 192.168.1.1
```

---

### Vulnerabilidades Comunes

#### Heartbleed (OpenSSL)
```bash
nmap --script=ssl-heartbleed 192.168.1.1 -p 443
```

#### Shellshock (Bash)
```bash
nmap --script=http-shellshock 192.168.1.1 -p 80
```

#### EternalBlue (MS17-010)
```bash
nmap --script=smb-vuln-ms17-010 192.168.1.1
```

#### Poodle (SSLv3)
```bash
nmap --script=ssl-poodle 192.168.1.1 -p 443
```

#### MS08-067 (Windows)
```bash
nmap --script=smb-vuln-ms08-067 192.168.1.1
```

---

### Scripts de Seguridad SSL/TLS

```bash
# Certificado SSL
nmap --script=ssl-cert 192.168.1.1 -p 443

# Enumeración de cifrados
nmap --script=ssl-enum-ciphers 192.168.1.1 -p 443

# Fecha de caducidad
nmap --script=ssl-cert --script-args=vulns 192.168.1.1 -p 443

# Vulnerabilidades SSL/TLS
nmap --script=ssl-* 192.168.1.1 -p 443
```

---

### Fuerza Bruta

```bash
# HTTP
nmap --script=http-brute --script-args userdb=users.txt,passdb=pass.txt 192.168.1.1

# SSH
nmap --script=ssh-brute --script-args userdb=users.txt,passdb=pass.txt 192.168.1.1 -p 22

# FTP
nmap --script=ftp-brute --script-args userdb=users.txt,passdb=pass.txt 192.168.1.1 -p 21

# SMB
nmap --script=smb-brute 192.168.1.1
```

---

## Ejercicios Prácticos

### Ejercicio 1: Escaneo Básico de Red Local

**Objetivo:** Descubrir hosts activos en tu red local.

```bash
# 1. Descubrir tu red
ip addr show
# o en Windows: ipconfig

# 2. Realizar ping scan
nmap -sn 192.168.1.0/24

# 3. Guardar resultados
nmap -sn 192.168.1.0/24 -oN hosts_activos.txt
```

**Preguntas:**
- ¿Cuántos hosts encontraste?
- ¿Reconoces todos los dispositivos?

---

### Ejercicio 2: Identificación de Puertos y Servicios

**Objetivo:** Escanear tu propio equipo o un servidor de prueba.

```bash
# 1. Escaneo básico de puertos
nmap localhost

# 2. Escaneo de todos los puertos
nmap -p- localhost

# 3. Detección de versiones
nmap -sV localhost

# 4. Escaneo completo
nmap -A localhost -oN mi_equipo.txt
```

**Preguntas:**
- ¿Qué puertos están abiertos?
- ¿Qué servicios están corriendo?
- ¿Reconoces todos los servicios?

---

### Ejercicio 3: Comparación de Técnicas de Escaneo

**Objetivo:** Comparar diferentes tipos de escaneo.

**IMPORTANTE:** Usa solo en entornos de prueba o con permiso explícito.

```bash
# 1. TCP Connect
time nmap -sT -p 1-100 [IP_OBJETIVO]

# 2. SYN Scan
time sudo nmap -sS -p 1-100 [IP_OBJETIVO]

# 3. NULL Scan
time sudo nmap -sN -p 1-100 [IP_OBJETIVO]

# 4. XMAS Scan
time sudo nmap -sX -p 1-100 [IP_OBJETIVO]
```

**Compara:**
- Velocidad de cada método
- Puertos detectados
- Resultados diferentes

---

### Ejercicio 4: Técnicas de Evasión

**Objetivo:** Practicar técnicas sigilosas.

```bash
# 1. Escaneo normal (línea base)
sudo nmap -sS [IP_OBJETIVO] -oN normal.txt

# 2. Escaneo con fragmentación
sudo nmap -sS -f [IP_OBJETIVO] -oN fragmentado.txt

# 3. Escaneo con señuelos
sudo nmap -sS -D RND:5 [IP_OBJETIVO] -oN señuelos.txt

# 4. Escaneo sigiloso lento
sudo nmap -sS -T1 --scan-delay 1s [IP_OBJETIVO] -oN sigiloso.txt

# 5. Combinación de técnicas
sudo nmap -sS -f -T2 -D RND:3 --data-length 25 [IP_OBJETIVO] -oN combinado.txt
```

**Analiza:**
- ¿Algún método fue detectado por IDS?
- ¿Diferencias en tiempo de ejecución?

---

### Ejercicio 5: Uso de NSE para Enumeración

**Objetivo:** Usar scripts NSE para obtener información detallada.

```bash
# 1. Listar scripts disponibles para HTTP
ls /usr/share/nmap/scripts/ | grep http

# 2. Obtener información de un servidor web
nmap --script=http-title,http-headers,http-methods 192.168.1.1 -p 80

# 3. Enumeración de directorios
nmap --script=http-enum 192.168.1.1 -p 80

# 4. Información SMB
nmap --script=smb-os-discovery,smb-enum-shares 192.168.1.1

# 5. Guardar resultados
nmap --script=http-* 192.168.1.1 -p 80 -oN web_enum.txt
```

---

### Ejercicio 6: Detección de Vulnerabilidades

**Objetivo:** Identificar vulnerabilidades conocidas.

**Entorno de prueba recomendado:** Metasploitable o máquinas virtuales de HackTheBox/TryHackMe

```bash
# 1. Escaneo básico de vulnerabilidades
nmap --script=vuln [IP_OBJETIVO] -oN vulnerabilidades.txt

# 2. Vulnerabilidades específicas de SMB
nmap --script=smb-vuln-* [IP_OBJETIVO]

# 3. Vulnerabilidades SSL
nmap --script=ssl-* [IP_OBJETIVO] -p 443

# 4. Vulnerabilidades HTTP
nmap --script=http-vuln-* [IP_OBJETIVO] -p 80

# 5. Escaneo completo con detección de vulnerabilidades
sudo nmap -sV -sC --script=vuln [IP_OBJETIVO] -oA auditoria_completa
```

**Documenta:**
- Vulnerabilidades encontradas
- Nivel de severidad
- Posibles soluciones

---

### Ejercicio 7: Auditoría Completa de Red

**Objetivo:** Realizar una auditoría de seguridad completa.

```bash
# Script completo de auditoría
#!/bin/bash

TARGET="192.168.1.0/24"
OUTDIR="auditoria_$(date +%Y%m%d_%H%M%S)"

mkdir -p $OUTDIR

echo "[*] Iniciando auditoría de seguridad..."

# 1. Descubrimiento de hosts
echo "[*] Descubriendo hosts activos..."
nmap -sn $TARGET -oA $OUTDIR/01_host_discovery

# 2. Escaneo de puertos rápido
echo "[*] Escaneo rápido de puertos..."
nmap -sS -T4 --top-ports 1000 $TARGET -oA $OUTDIR/02_port_scan

# 3. Detección de servicios y OS
echo "[*] Detección de servicios y OS..."
nmap -sV -O $TARGET -oA $OUTDIR/03_service_detection

# 4. Scripts por defecto
echo "[*] Ejecutando scripts NSE por defecto..."
nmap -sC $TARGET -oA $OUTDIR/04_default_scripts

# 5. Detección de vulnerabilidades
echo "[*] Escaneando vulnerabilidades..."
nmap --script=vuln $TARGET -oA $OUTDIR/05_vulnerabilities

# 6. Escaneo UDP de puertos comunes
echo "[*] Escaneo UDP..."
sudo nmap -sU --top-ports 20 $TARGET -oA $OUTDIR/06_udp_scan

echo "[*] Auditoría completada. Resultados en: $OUTDIR"
```

---

### Ejercicio 8: Interpretación de Resultados

**Tarea:** Analiza el siguiente output y responde las preguntas.

```
Starting Nmap 7.94 ( https://nmap.org )
Nmap scan report for 192.168.1.100
Host is up (0.0012s latency).

PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
80/tcp   open  http        Apache httpd 2.4.18
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
3306/tcp open  mysql       MySQL 5.5.47-0ubuntu0.14.04.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.43 seconds
```

**Preguntas:**
1. ¿Qué sistema operativo crees que corre el objetivo?
2. ¿Qué servicios potencialmente vulnerables identificas?
3. ¿Qué scripts NSE ejecutarías para más información?
4. ¿Qué puertos representan mayor riesgo?
5. ¿Qué pasos de endurecimiento recomendarías?

**Respuestas sugeridas:**
1. Ubuntu (basado en OpenSSH y versiones de servicio)
2. vsftpd 2.3.4 (backdoor conocido), versiones antiguas de SMB, MySQL expuesto
3. `--script=ftp-vuln-*`, `--script=smb-vuln-*`, `--script=mysql-vuln-*`
4. Puerto 21 (vsftpd 2.3.4), 139/445 (SMB antiguo), 3306 (MySQL expuesto)
5. Actualizar servicios, cerrar puertos innecesarios, firewall, deshabilitar FTP anónimo

---

### Ejercicio 9: Laboratorio Seguro

**Configurar tu propio entorno de pruebas:**

1. **Instalar VirtualBox/VMware**
2. **Descargar máquinas vulnerables:**
   - Metasploitable 2
   - DVWA (Damn Vulnerable Web Application)
   - WebGoat

3. **Configurar red aislada:**
   - Usa red NAT o Host-only
   - No expongas a Internet

4. **Practicar sin consecuencias:**
```bash
# Escaneo agresivo seguro
nmap -A -T5 -p- [IP_METASPLOITABLE]

# Todos los scripts de vulnerabilidades
nmap --script=vuln [IP_METASPLOITABLE]

# Fuerza bruta (en laboratorio)
nmap --script=ssh-brute [IP_METASPLOITABLE]
```

---

### Ejercicio 10: Caso Práctico - Reporte de Auditoría

**Escenario:** Has sido contratado para auditar la seguridad de una pequeña empresa.

**Pasos:**

1. **Reconocimiento:**
```bash
nmap -sn 192.168.100.0/24 -oA reconocimiento
```

2. **Escaneo de puertos:**
```bash
nmap -sS -p- 192.168.100.0/24 -oA escaneo_puertos
```

3. **Identificación de servicios:**
```bash
nmap -sV -sC 192.168.100.0/24 -oA servicios
```

4. **Búsqueda de vulnerabilidades:**
```bash
nmap --script=vuln 192.168.100.0/24 -oA vulnerabilidades
```

5. **Elaborar reporte con:**
   - Resumen ejecutivo
   - Hosts descubiertos
   - Servicios identificados
   - Vulnerabilidades encontradas
   - Nivel de riesgo (Crítico/Alto/Medio/Bajo)
   - Recomendaciones específicas
   - Conclusiones

---

## Consejos Finales y Mejores Prácticas

### Aspectos Legales
- **NUNCA** escanees redes o sistemas sin autorización explícita
- Obtén permiso por escrito antes de auditorías
- Conoce las leyes de tu jurisdicción
- Las pruebas no autorizadas son ilegales

### Mejores Prácticas

#### Antes del Escaneo
- Obtén autorización por escrito
- Define el alcance claramente
- Documenta todos los pasos
- Notifica al personal correspondiente
- Prepara un plan de contingencia

#### Durante el Escaneo
- Comienza con escaneos no intrusivos
- Aumenta gradualmente la agresividad
- Monitorea el impacto en la red
- Mantén comunicación con el cliente
- Documenta todo en tiempo real

#### Después del Escaneo
- Analiza todos los resultados
- Verifica falsos positivos
- Prioriza hallazgos por riesgo
- Crea un reporte profesional
- Ofrece recomendaciones específicas

---

### Comandos Útiles Combinados

```bash
# Escaneo completo y exhaustivo
sudo nmap -sS -sV -O -A -T4 -p- --script=default,vuln 192.168.1.1 -oA auditoria_completa

# Escaneo rápido de red completa
nmap -sn --min-rate 5000 192.168.1.0/24

# Escaneo sigiloso y completo
sudo nmap -sS -T2 -f -D RND:5 --data-length 25 -p- 192.168.1.1 -oA sigiloso

# Escaneo de servicios web
nmap -p 80,443,8080,8443 --script=http-* 192.168.1.0/24

# Escaneo completo de vulnerabilidades
nmap -sV --script="vuln and safe" -p- 192.168.1.1 -oA vuln_scan

# Descubrimiento rápido + puertos comunes
nmap -sn 192.168.1.0/24 && nmap -sV --top-ports 100 192.168.1.0/24

# Escaneo de base de datos
nmap -p 1433,3306,5432,27017 --script=*-info,*-enum 192.168.1.0/24
```

---

### Interpretación de Estados de Puerto

| Estado | Significado |
|--------|-------------|
| **open** | Puerto aceptando conexiones activamente |
| **closed** | Puerto accesible pero sin aplicación escuchando |
| **filtered** | Firewall/filtro bloqueando el acceso |
| **unfiltered** | Puerto accesible pero estado indeterminado |
| **open\|filtered** | Nmap no puede determinar si está abierto o filtrado |
| **closed\|filtered** | Nmap no puede determinar si está cerrado o filtrado |

---

### Optimización de Rendimiento

```bash
# Escaneo muy rápido (puede perder información)
nmap -T5 --min-rate 10000 --max-retries 1 192.168.1.1

# Paralelización
nmap --min-parallelism 100 192.168.1.0/24

# Timeout reducido
nmap --host-timeout 5m 192.168.1.0/24

# Skip DNS resolution (más rápido)
nmap -n 192.168.1.0/24

# No hacer ping (asume que está activo)
nmap -Pn 192.168.1.1
```

---

### Troubleshooting Común

#### Problema: "You requested a scan type which requires root privileges"
**Solución:** Usar `sudo` antes del comando o ejecutar como root

#### Problema: "No route to host" o "Host seems down"
**Solución:** 
```bash
# Intentar con -Pn (sin ping)
nmap -Pn 192.168.1.1

# Verificar conectividad
ping 192.168.1.1
```

#### Problema: Escaneo muy lento
**Solución:**
```bash
# Aumentar timing
nmap -T4 192.168.1.1

# Reducir número de puertos
nmap --top-ports 100 192.168.1.1

# Desactivar resolución DNS
nmap -n 192.168.1.1
```

#### Problema: Resultados inconsistentes
**Solución:**
```bash
# Aumentar reintentos
nmap --max-retries 3 192.168.1.1

# Timing más conservador
nmap -T2 192.168.1.1
```

---

## Glosario de Términos

**Three-way handshake:** Proceso de establecimiento de conexión TCP (SYN → SYN/ACK → ACK)

**IDS (Intrusion Detection System):** Sistema de detección de intrusiones

**IPS (Intrusion Prevention System):** Sistema de prevención de intrusiones

**Firewall:** Sistema que filtra tráfico de red basado en reglas

**Port:** Punto de conexión lógico para comunicaciones de red

**Service:** Aplicación que escucha en un puerto específico

**Banner:** Información que un servicio revela sobre sí mismo

**Fingerprinting:** Técnica para identificar sistemas/servicios

**Stealth scan:** Escaneo diseñado para evitar detección

**False positive:** Resultado incorrecto que indica vulnerabilidad inexistente

**False negative:** Fallo en detectar una vulnerabilidad real

**NSE:** Nmap Scripting Engine

**CVE:** Common Vulnerabilities and Exposures (identificador de vulnerabilidad)

**CVSS:** Common Vulnerability Scoring System (0-10)

**Exploit:** Código que aprovecha una vulnerabilidad

**Payload:** Código malicioso ejecutado tras una explotación

**Zero-day:** Vulnerabilidad desconocida públicamente

**Patch:** Actualización que corrige una vulnerabilidad

---

## Recursos Adicionales

### Documentación Oficial
- **Sitio web oficial:** https://nmap.org
- **Documentación:** https://nmap.org/book/
- **Referencia NSE:** https://nmap.org/nsedoc/

### Libros Recomendados
- "Nmap Network Scanning" by Gordon "Fyodor" Lyon (creador de Nmap)
- "Network Security Assessment" by Chris McNab
- "The Hacker Playbook 3" by Peter Kim

### Plataformas de Práctica Legal
- **HackTheBox:** https://hackthebox.com
- **TryHackMe:** https://tryhackme.com
- **VulnHub:** https://vulnhub.com
- **PentesterLab:** https://pentesterlab.com

### Máquinas Virtuales de Práctica
- Metasploitable 2 y 3
- DVWA (Damn Vulnerable Web App)
- WebGoat
- OWASP Juice Shop
- Vulhub

### Comunidades
- **Reddit:** r/netsec, r/AskNetsec
- **Discord:** Servidores de ciberseguridad
- **Twitter:** Sigue a @nmap

### Scripts NSE Personalizados
- **GitHub:** Busca "nmap scripts" para scripts comunitarios
- **Nmap NSE Library:** Scripts adicionales de la comunidad

---

## Cheat Sheet Rápida

```bash
# DESCUBRIMIENTO DE HOSTS
nmap -sn 192.168.1.0/24                    # Ping scan
nmap -sL 192.168.1.0/24                    # Lista sin escanear

# ESCANEO DE PUERTOS
nmap 192.168.1.1                           # Escaneo básico
nmap -p 80,443 192.168.1.1                 # Puertos específicos
nmap -p- 192.168.1.1                       # Todos los puertos
nmap --top-ports 1000 192.168.1.1          # Top 1000 puertos

# TIPOS DE ESCANEO
nmap -sT 192.168.1.1                       # TCP Connect
sudo nmap -sS 192.168.1.1                  # SYN (stealth)
sudo nmap -sU 192.168.1.1                  # UDP
sudo nmap -sN 192.168.1.1                  # NULL
sudo nmap -sF 192.168.1.1                  # FIN
sudo nmap -sX 192.168.1.1                  # XMAS

# DETECCIÓN
nmap -sV 192.168.1.1                       # Versiones
sudo nmap -O 192.168.1.1                   # OS Detection
nmap -A 192.168.1.1                        # Agresivo (todo)

# TIMING
nmap -T0 192.168.1.1                       # Paranoico
nmap -T1 192.168.1.1                       # Sigiloso
nmap -T2 192.168.1.1                       # Educado
nmap -T3 192.168.1.1                       # Normal
nmap -T4 192.168.1.1                       # Agresivo
nmap -T5 192.168.1.1                       # Loco

# EVASIÓN
sudo nmap -f 192.168.1.1                   # Fragmentación
sudo nmap -D RND:10 192.168.1.1            # Decoys
sudo nmap --spoof-mac 0 192.168.1.1        # Spoof MAC
sudo nmap -g 53 192.168.1.1                # Puerto origen
nmap --data-length 25 192.168.1.1          # Datos aleatorios

# NSE SCRIPTS
nmap -sC 192.168.1.1                       # Scripts default
nmap --script=vuln 192.168.1.1             # Vulnerabilidades
nmap --script=http-* 192.168.1.1           # Scripts HTTP
nmap --script=smb-vuln-* 192.168.1.1       # Vulns SMB

# SALIDA
nmap 192.168.1.1 -oN salida.txt            # Normal
nmap 192.168.1.1 -oX salida.xml            # XML
nmap 192.168.1.1 -oG salida.grep           # Grepable
nmap 192.168.1.1 -oA resultados            # Todos

# COMBINACIONES ÚTILES
sudo nmap -sS -sV -O -p- 192.168.1.1       # Completo
nmap -A -T4 192.168.1.1                    # Rápido y completo
sudo nmap -sS -sV --script=vuln 192.168.1.1  # Detección vulns
nmap -Pn -n 192.168.1.1                    # Sin ping ni DNS
```

---

## Ejercicios de Evaluación

### Test de Conocimientos

**1. ¿Cuál es la diferencia entre -sS y -sT?**
   - a) -sS es más rápido
   - b) -sS no completa el handshake TCP
   - c) -sS requiere privilegios root
   - d) Todas las anteriores ✓

**2. ¿Qué flag hace un escaneo XMAS?**
   - a) -sN
   - b) -sF
   - c) -sX ✓
   - d) -sA

**3. ¿Cuál es el timing más sigiloso?**
   - a) T0 ✓
   - b) T1
   - c) T2
   - d) T3

**4. ¿Qué opción escanea todos los puertos?**
   - a) -p *
   - b) -p all
   - c) -p- ✓
   - d) -p 1-65535 ✓

**5. ¿Qué hace el flag -Pn?**
   - a) Escaneo ping
   - b) Salta el descubrimiento de host ✓
   - c) Paralleliza el escaneo
   - d) Ninguna de las anteriores

**6. ¿Qué categoría NSE es para vulnerabilidades?**
   - a) exploit
   - b) vuln ✓
   - c) safe
   - d) intrusive

**7. ¿Qué puerto usa SSH por defecto?**
   - a) 21
   - b) 22 ✓
   - c) 23
   - d) 25

**8. ¿Qué significa un puerto "filtered"?**
   - a) Está abierto
   - b) Está cerrado
   - c) Bloqueado por firewall ✓
   - d) No existe

**9. ¿Qué hace -D RND:10?**
   - a) Decoys aleatorios ✓
   - b) Delay de 10 segundos
   - c) 10 reintentos
   - d) DNS lookup

**10. ¿Cuál requiere privilegios root?**
   - a) -sS ✓
   - b) -sU ✓
   - c) -O ✓
   - d) -sV

---

## Laboratorios Avanzados

### Lab 1: Red Corporativa Simulada

**Escenario:** Escanear una red corporativa con múltiples segmentos.

```bash
# Topología
# 192.168.10.0/24 - DMZ (servidores públicos)
# 192.168.20.0/24 - Interna (estaciones de trabajo)
# 192.168.30.0/24 - Servidores (bases de datos)

# Fase 1: Descubrimiento
nmap -sn 192.168.10.0/24 192.168.20.0/24 192.168.30.0/24 -oA descubrimiento

# Fase 2: Escaneo de servicios externos (DMZ)
nmap -sV -p 80,443,21,22,25 192.168.10.0/24 -oA dmz_servicios

# Fase 3: Escaneo interno completo
sudo nmap -sS -sV -O --top-ports 1000 192.168.20.0/24 -oA interna

# Fase 4: Servidores críticos
sudo nmap -sS -sV -p- --script=vuln 192.168.30.0/24 -oA servidores_criticos

# Fase 5: Análisis y reporte
# Genera un reporte con hallazgos, riesgos y recomendaciones
```

---

### Lab 2: Simulación de Ataque APT

**Escenario:** Simular un ataque dirigido evitando detección.

```bash
# Fase 1: Reconocimiento pasivo (sin tocar objetivo)
# (Usar OSINT, no Nmap)

# Fase 2: Escaneo sigiloso inicial
sudo nmap -sS -T1 --max-rate 1 -p 80,443 [OBJETIVO]

# Fase 3: Esperar 24 horas

# Fase 4: Escaneo más agresivo pero con evasión
sudo nmap -sS -T2 -f -D RND:5 --data-length 25 \
  --scan-delay 5s --max-retries 1 -p- [OBJETIVO]

# Fase 5: Fingerprinting de servicios
sudo nmap -sV --version-intensity 2 -p [PUERTOS_ABIERTOS] [OBJETIVO]

# Fase 6: Enumeration específica
nmap --script=safe -p [PUERTOS_ABIERTOS] [OBJETIVO]

# Fase 7: Búsqueda de vulnerabilidades
nmap --script="vuln and not dos" -p [PUERTOS_ABIERTOS] [OBJETIVO]
```

---

### Lab 3: Auditoría de Infraestructura Cloud

**Escenario:** Auditar instancias en AWS/Azure/GCP.

```bash
# Consideraciones especiales para cloud:
# - Rangos IP públicas del proveedor
# - Rate limiting estricto
# - Monitoreo avanzado

# Escaneo adaptado para cloud
nmap -sS -T2 --max-rate 50 \
  --max-retries 1 \
  --host-timeout 3m \
  -p 22,80,443,3389,3306,5432,27017 \
  [RANGO_IP_CLOUD] -oA cloud_audit

# Verificar configuraciones de seguridad
nmap --script=ssh-auth-methods,ssl-cert,http-security-headers \
  [IP_INSTANCIA]
```

---

## Proyecto Final: Mini Pentest

**Objetivo:** Realizar un mini penetration test completo.

### Fases del Proyecto

#### 1. Preparación
- Definir alcance
- Obtener autorización escrita
- Preparar herramientas
- Documentar todo

#### 2. Reconocimiento
```bash
# Host discovery
nmap -sn [RED_OBJETIVO] -oA 01_discovery

# Identificar objetivos de valor
nmap -sV --top-ports 100 [HOSTS_ACTIVOS] -oA 02_prioritization
```

#### 3. Escaneo
```bash
# Escaneo completo de puertos
sudo nmap -sS -p- [OBJETIVOS] -oA 03_full_scan

# Detección de servicios y OS
sudo nmap -sV -O [OBJETIVOS] -oA 04_service_os_detection
```

#### 4. Enumeración
```bash
# Scripts de enumeración
nmap -sC [OBJETIVOS] -oA 05_enumeration

# Enumeración específica por servicio
nmap --script=http-enum,smb-enum-shares,ssh-auth-methods \
  [OBJETIVOS] -oA 06_detailed_enum
```

#### 5. Identificación de Vulnerabilidades
```bash
# Escaneo de vulnerabilidades
nmap --script=vuln [OBJETIVOS] -oA 07_vulnerabilities
```

#### 6. Análisis y Reporting
Crea un reporte profesional con:

**Resumen Ejecutivo**
- Objetivos de la auditoría
- Metodología utilizada
- Hallazgos principales
- Nivel de riesgo general

**Hallazgos Técnicos**
- Hosts descubiertos
- Puertos y servicios identificados
- Vulnerabilidades encontradas (por severidad)
- Evidencias (capturas de pantalla, logs)

**Recomendaciones**
- Corto plazo (críticas)
- Mediano plazo (altas)
- Largo plazo (medias/bajas)
- Mejores prácticas

**Anexos**
- Logs completos
- Comandos ejecutados
- Referencias (CVE, CWE, etc.)

---

## Conclusión

Has completado el tutorial completo de Nmap. Ahora tienes conocimientos sobre:

✅ Fundamentos de Nmap y escaneo de redes
✅ Múltiples tipos de escaneo y cuándo usarlos
✅ Técnicas de evasión de IDS/IPS
✅ Uso del Nmap Scripting Engine
✅ Detección de vulnerabilidades
✅ Mejores prácticas y consideraciones legales

### Próximos Pasos

1. **Practica regularmente** en entornos seguros
2. **Mantente actualizado** con nuevas técnicas
3. **Aprende otras herramientas** complementarias:
   - Masscan (escaneo ultra-rápido)
   - Netcat
   - Wireshark
   - Metasploit
   - Burp Suite

4. **Considera certificaciones:**
   - CEH (Certified Ethical Hacker)
   - OSCP (Offensive Security Certified Professional)
   - GPEN (GIAC Penetration Tester)

5. **Contribuye a la comunidad:**
   - Escribe scripts NSE
   - Comparte hallazgos
   - Ayuda a otros a aprender

---

## Recordatorio Final

⚠️ **ADVERTENCIA LEGAL:** El uso de Nmap sin autorización explícita es ILEGAL y puede resultar en acciones legales. Usa estas técnicas únicamente en:
- Tu propia red/equipos
- Entornos de laboratorio
- Con permiso escrito del propietario
- En plataformas legales de práctica

**La ciberseguridad ética es crucial. Usa tus conocimientos para proteger, no para dañar.**

---

**Autor:** Tutorial de Nmap - Guía Completa 2025
**Versión:** 1.0
**Última actualización:** Septiembre 2025

¡Feliz escaneo y hacking ético! 🛡️🔍