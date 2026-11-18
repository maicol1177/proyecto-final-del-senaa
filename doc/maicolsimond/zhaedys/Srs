# Especificación de Requisitos de Software (SRS) – Licores Connect

**Proyecto productivo SENA** · Programa ADSO · Ficha 3532730 · Convenio UAC – SENA No. 05[cite: 1]  
**Equipo:** Didier Rangel, Alfred Castro, Samuel Sequeda, Maicol Simond y Luis Gomez · **Instructor:** Zajedis · **Versión:** 1.0 · **Fecha:** 18 de noviembre de 2026[cite: 1]

---

## 1. Introducción

### 1.1 Propósito
Este documento especifica los requisitos funcionales y no funcionales de **Licores Connect**, un software web de gestión de ventas e inventario para pequeños y medianos comercios de licores en Colombia. Está dirigido al equipo de desarrollo, al instructor evaluador, a los negocios piloto y a cualquier persona que participe en el diseño, las pruebas o el mantenimiento del sistema[cite: 1].

### 1.2 Alcance
Licores Connect es una aplicación web en la nube, ofrecida bajo modelo SaaS (suscripción mensual o anual), que permite a licorerías, estancos, tiendas de barrio, minimercados y emprendedores[cite: 1]:
* Registrar ventas de forma rápida y generar la facturación correspondiente[cite: 1].
* Controlar automáticamente el stock de botellas y bebidas[cite: 1].
* Realizar el cuadre de caja diario[cite: 1].
* Consultar reportes financieros y de inventario en tiempo real[cite: 1].
* Administrar usuarios y permisos del negocio[cite: 1].

*Fuera del alcance de la versión 1.0:* facturación electrónica ante la DIAN, contabilidad completa, nómina, domicilios y tienda en línea para el consumidor final (ver sección 7, supuestos y riesgos)[cite: 1].

### 1.3 Definiciones, acrónimos y abreviaturas

| Término | Definición |
| :--- | :--- |
| **SRS** | Software Requirements Specification (Especificación de Requisitos de Software)[cite: 1] |
| **SaaS** | Software como servicio, accedido por suscripción desde el navegador[cite: 1] |
| **Stock** | Cantidad disponible de cada producto en inventario[cite: 1] |
| **SKU** | Código único que identifica un producto[cite: 1] |
| **Cuadre de caja** | Conciliación entre las ventas registradas y el dinero efectivamente recibido[cite: 1] |
| **Negocio / cliente** | Comercio suscrito a Licores Connect[cite: 1] |
| **Administrador** | Dueño o encargado con control total del negocio dentro del sistema[cite: 1] |
| **Vendedor** | Empleado que registra ventas[cite: 1] |
| **PSE** | Pagos Seguros en Línea[cite: 1] |
| **ADSO** | Análisis y Desarrollo de Software (SENA)[cite: 1] |
| **RF / RNF** | Requisito funcional / Requisito no funcional[cite: 1] |

### 1.4 Referencias
* Documento del proyecto productivo SENA: Planteamiento y delimitación del problema (componente Exploración)[cite: 1].
* Modelo de negocio CANVAS (componente Ideación)[cite: 1].
* IEEE Std 830-1998, práctica recomendada para especificaciones de requisitos de software (usada como guía de estructura)[cite: 1].

### 1.5 Visión general del documento
La sección 2 describe el producto en términos generales; la sección 3 detalla los requisitos funcionales; la sección 4, los no funcionales; la sección 5, las interfaces; la sección 6, los criterios de aceptación; y la sección 7, supuestos, restricciones y riesgos[cite: 1].

---

## 2. Descripción general

### 2.1 Contexto y problema
En Colombia, muchos pequeños y medianos comercios de licores llevan sus ventas e inventarios en libretas, cuadernos u hojas de cálculo básicas. Esto genera desorden administrativo, pérdida de tiempo en el registro diario, errores de facturación y de cuadre de caja, descuadres de inventario y ausencia de reportes en tiempo real para conocer las ganancias reales y decidir mejor[cite: 1].

### 2.2 Perspectiva del producto
Licores Connect es un producto independiente, accesible desde cualquier navegador con conexión a internet, sin instalaciones complicadas. Se integra con pasarelas de pago en línea para el cobro de suscripciones. Su diferenciador es ser intuitivo (sin requerir conocimientos técnicos), económico y especializado en licores y bebidas[cite: 1].

### 2.3 Funciones principales del producto
* Módulo de ventas: registro rápido, facturación y cuadre de caja[cite: 1].
* Módulo de inventario de licores: catálogo, stock automático y alertas[cite: 1].
* Módulo de reportes: ganancias, ventas e inventario en tiempo real[cite: 1].
* Módulo de usuarios: roles, permisos y gestión de cuentas[cite: 1].
* Módulo de suscripción y pagos: planes, cobro y estado de la cuenta[cite: 1].
* Soporte y demostración: acceso a una versión de prueba gratuita[cite: 1].

### 2.4 Clases de usuarios y características

| Usuario | Descripción | Nivel técnico |
| :--- | :--- | :--- |
| **Administrador del negocio** | Dueño o encargado. Configura el negocio, gestiona inventario, usuarios, reportes y suscripción[cite: 1]. | Bajo[cite: 1] |
| **Vendedor / cajero** | Registra ventas y consulta disponibilidad de productos[cite: 1]. | Bajo[cite: 1] |
| **Emprendedor nuevo** | Administrador que empieza su negocio y necesita organizarse desde el primer día[cite: 1]. | Bajo[cite: 1] |
| **Soporte Licores Connect** | Equipo desarrollador que atiende incidencias y administra cuentas de clientes[cite: 1]. | Alto[cite: 1] |

### 2.5 Entorno operativo
* Aplicación web alojada en servidores en la nube (hosting) con dominio propio[cite: 1].
* Compatible con navegadores modernos (Chrome, Edge, Firefox, Safari) en computador, tableta y celular[cite: 1].
* Requiere conexión a internet estable[cite: 1].

### 2.6 Restricciones de diseño e implementación
* Desarrollo por un equipo de 5 estudiantes bajo metodologías ágiles[cite: 1].
* Presupuesto limitado: uso de hosting económico y herramientas de desarrollo web modernas[cite: 1].
* Los precios del servicio deben ser accesibles para pequeños comercios[cite: 1].
* Cumplimiento de la normativa colombiana de protección de datos personales (Ley 1581 de 2012)[cite: 1].

### 2.7 Supuestos y dependencias
* Los negocios cuentan con al menos un dispositivo con internet en el punto de venta[cite: 1].
* Dependencia de proveedores externos de hosting, dominio y pasarelas de pago[cite: 1].
* Disponibilidad de licorerías piloto para validar el software[cite: 1].

---

## 3. Requisitos funcionales

*Prioridad:* Alta (imprescindible para la versión 1.0), Media (importante, puede entrar en un segundo ciclo) y Baja (deseable)[cite: 1].

### 3.1 Autenticación y gestión de usuarios

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-01** | El sistema debe permitir registrar un nuevo negocio con nombre, NIT o documento, correo, teléfono y datos del administrador[cite: 1]. | Alta[cite: 1] |
| **RF-02** | El sistema debe permitir iniciar y cerrar sesión con correo y contraseña[cite: 1]. | Alta[cite: 1] |
| **RF-03** | El sistema debe permitir recuperar la contraseña mediante un enlace enviado al correo[cite: 1]. | Alta[cite: 1] |
| **RF-04** | El administrador debe poder crear, editar, desactivar y eliminar usuarios de su negocio[cite: 1]. | Alta[cite: 1] |
| **RF-05** | El sistema debe manejar roles (Administrador y Vendedor) con permisos diferenciados por módulo[cite: 1]. | Alta[cite: 1] |
| **RF-06** | El sistema debe registrar un historial de acciones relevantes por usuario (quién vendió, modificó stock, anuló una venta)[cite: 1]. | Media[cite: 1] |

### 3.2 Gestión de inventario de licores

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-07** | El sistema debe permitir crear, consultar, editar y desactivar productos con: nombre, categoría (aguardiente, ron, whisky, cerveza, vino, otros), marca, presentación (volumen), código/SKU, precio de compra, precio de venta y stock[cite: 1]. | Alta[cite: 1] |
| **RF-08** | El sistema debe permitir buscar y filtrar productos por nombre, categoría, marca o código[cite: 1]. | Alta[cite: 1] |
| **RF-09** | El sistema debe descontar automáticamente del stock cada producto vendido[cite: 1]. | Alta[cite: 1] |
| **RF-10** | El sistema debe permitir registrar entradas de mercancía (compras a proveedores) que aumenten el stock[cite: 1]. | Alta[cite: 1] |
| **RF-11** | El sistema debe permitir ajustes manuales de inventario con motivo obligatorio (pérdida, rotura, conteo físico)[cite: 1]. | Alta[cite: 1] |
| **RF-12** | El sistema debe definir un stock mínimo por producto y alertar cuando se alcance o se supere hacia abajo[cite: 1]. | Alta[cite: 1] |
| **RF-13** | El sistema debe mostrar el historial de movimientos (kardex) de cada producto[cite: 1]. | Media[cite: 1] |
| **RF-14** | El sistema debe permitir gestionar proveedores (nombre, contacto, productos que surte)[cite: 1]. | Media[cite: 1] |
| **RF-15** | El sistema debe permitir importar el inventario inicial desde un archivo de Excel o CSV para facilitar la migración desde hojas de cálculo[cite: 1]. | Media[cite: 1] |
| **RF-16** | El sistema debe permitir registrar la fecha de vencimiento o lote en productos que lo requieran (cervezas, vinos u otros) y avisar de próximos vencimientos[cite: 1]. | Baja[cite: 1] |

### 3.3 Gestión de ventas y facturación

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-17** | El sistema debe permitir registrar una venta seleccionando productos y cantidades, con cálculo automático de subtotal, descuentos, impuestos y total[cite: 1]. | Alta[cite: 1] |
| **RF-18** | El sistema debe validar que haya stock suficiente antes de confirmar una venta y advertir al usuario en caso contrario[cite: 1]. | Alta[cite: 1] |
| **RF-19** | El sistema debe permitir registrar el método de pago (efectivo, transferencia, Nequi, Daviplata, tarjeta, mixto)[cite: 1]. | Alta[cite: 1] |
| **RF-20** | Para pagos en efectivo, el sistema debe calcular el valor a devolver (cambio)[cite: 1]. | Alta[cite: 1] |
| **RF-21** | El sistema debe generar un comprobante o factura de venta con numeración consecutiva, imprimible o descargable en PDF[cite: 1]. | Alta[cite: 1] |
| **RF-22** | El sistema debe permitir anular una venta (solo Administrador), restituyendo el stock y dejando registro del motivo[cite: 1]. | Alta[cite: 1] |
| **RF-23** | El sistema debe permitir apertura y cierre de caja por turno, con monto inicial y conteo final[cite: 1]. | Alta[cite: 1] |
| **RF-24** | El sistema debe realizar el cuadre de caja automático, mostrando el total esperado frente al valor contado y la diferencia[cite: 1]. | Alta[cite: 1] |
| **RF-25** | El sistema debe permitir registrar gastos y retiros de caja con descripción y monto[cite: 1]. | Media[cite: 1] |
| **RF-26** | El sistema debe permitir registrar clientes frecuentes y ventas fiadas (crédito) con control de saldos pendientes[cite: 1]. | Media[cite: 1] |
| **RF-27** | El sistema debe permitir consultar y buscar el historial de ventas por fecha, vendedor, método de pago o número de factura[cite: 1]. | Alta[cite: 1] |
| **RF-28** | El sistema debe permitir registrar ventas con lector de código de barras[cite: 1]. | Baja[cite: 1] |

### 3.4 Reportes y panel de control

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-29** | El sistema debe mostrar un panel de inicio con ventas del día, ganancia estimada, productos con bajo stock y últimos movimientos[cite: 1]. | Alta[cite: 1] |
| **RF-30** | El sistema debe generar reportes de ventas por día, semana, mes y rango personalizado[cite: 1]. | Alta[cite: 1] |
| **RF-31** | El sistema debe generar un reporte de ganancias (ingresos menos costo de los productos vendidos y gastos registrados)[cite: 1]. | Alta[cite: 1] |
| **RF-32** | El sistema debe generar un reporte de inventario valorizado y de productos con bajo stock[cite: 1]. | Alta[cite: 1] |
| **RF-33** | El sistema debe mostrar los productos más y menos vendidos[cite: 1]. | Media[cite: 1] |
| **RF-34** | El sistema debe permitir ver ventas por vendedor y por método de pago[cite: 1]. | Media[cite: 1] |
| **RF-35** | El sistema debe permitir exportar los reportes a PDF y Excel[cite: 1]. | Media[cite: 1] |
| **RF-36** | Los reportes deben actualizarse en tiempo real conforme se registren ventas y movimientos[cite: 1]. | Alta[cite: 1] |

### 3.5 Suscripción y pagos del servicio

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-37** | El sistema debe ofrecer planes de suscripción mensual y anual con sus características y precios visibles[cite: 1]. | Alta[cite: 1] |
| **RF-38** | El sistema debe permitir pagar la suscripción en línea mediante pasarela de pagos (PSE, tarjeta) y reportar pagos por transferencia digital (Nequi, Daviplata)[cite: 1]. | Alta[cite: 1] |
| **RF-39** | El sistema debe permitir un periodo de prueba o demo gratuita sin tarjeta de crédito[cite: 1]. | Alta[cite: 1] |
| **RF-40** | El sistema debe mostrar el estado de la suscripción (activa, por vencer, vencida) y notificar al administrador antes del vencimiento[cite: 1]. | Alta[cite: 1] |
| **RF-41** | El sistema debe restringir el acceso a las funciones de escritura cuando la suscripción esté vencida, conservando los datos del cliente y permitiendo su consulta o descarga[cite: 1]. | Media[cite: 1] |
| **RF-42** | El sistema debe permitir al equipo de soporte activar, suspender o prorrogar cuentas manualmente (recaudo directo)[cite: 1]. | Media[cite: 1] |
| **RF-43** | El sistema debe enviar recibos de pago de la suscripción por correo electrónico[cite: 1]. | Media[cite: 1] |

### 3.6 Soporte y ayuda

| ID | Requisito | Prioridad |
| :--- | :--- | :--- |
| **RF-44** | El sistema debe incluir una sección de ayuda con guías breves y videos cortos de uso[cite: 1]. | Media. 
